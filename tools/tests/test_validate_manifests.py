import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = REPO_ROOT / "tools" / "validate_manifests.py"

SOURCE = "github:DavidBatoDev/fmad-method/skills"

METHOD_RECORD = (
    "[fmod]\n"
    'code = "method"\n'
    'version = "{version}"\n'
    f'update_source = "{SOURCE}"\n'
    'skills = ["fmad-build", "fmad-spec"]\n'
    'required_skills = ["fmad"]\n'
    "\n"
    "[[fmod.knowledge]]\n"
    'path = "delivery-help.md"\n'
    'skills = ["fmad-build"]\n'
)

CORE_TOOLS_RECORD = (
    "[fmod]\n"
    'code = "core-tools"\n'
    'version = "{version}"\n'
    f'update_source = "{SOURCE}"\n'
    'skills = ["fmad", "fmad-flow"]\n'
)

SKILL = f'[skill]\nfmod = "{{fmod}}"\nsource = "{SOURCE}"\n'

ROSTER = (
    "[[members]]\n"
    'code = "fmad-build"\n'
    'skill = "fmad-build"\n'
    'name = "Cinder"\n'
    "\n"
    "[[members]]\n"
    'code = "guest"\n'
    'name = "Guest"\n'
    "\n"
    "[[groups]]\n"
    'id = "team"\n'
    'members = ["fmad-build", "guest"]\n'
)

MEMBERS = {"fmod-method": ("fmad-build", "fmad-spec"), "fmod-core-tools": ("fmad", "fmad-flow")}


def load_module(name: str, path: Path):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


vm = load_module("validate_manifests", VALIDATOR)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_tree(root: Path, version: str = "6.11.0-next") -> None:
    skills = root / "skills"
    write(skills / "fmod-method" / "fmod.toml", METHOD_RECORD.format(version=version))
    write(skills / "fmod-method" / "help" / "help.md", "# help\n")
    write(skills / "fmod-method" / "delivery-help.md", "# delivery\n")
    write(skills / "fmod-method" / "roster.toml", ROSTER)
    write(skills / "fmod-core-tools" / "fmod.toml", CORE_TOOLS_RECORD.format(version=version))
    write(skills / "fmod-core-tools" / "help" / "help.md", "# help\n")
    for fmod, members in MEMBERS.items():
        write(skills / fmod / "SKILL.md", "# record\n")
        for skill in members:
            write(skills / skill / "fmod.toml", SKILL.format(fmod=fmod))
            write(skills / skill / "SKILL.md", "# skill\n")


class ValidatorCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name).resolve()
        self.skills = self.root / "skills"
        make_tree(self.root)

    def problems(self) -> str:
        return "\n".join(vm.check_repo(self.root).problems)

    def method_record(self, old: str, new: str) -> None:
        path = self.skills / "fmod-method" / "fmod.toml"
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        write(path, text.replace(old, new))


class CleanTreeTests(ValidatorCase):
    def test_clean_tree_has_no_problems_and_reports_its_records(self):
        report = vm.check_repo(self.root)
        self.assertEqual(report.problems, ())
        self.assertEqual(
            [path.relative_to(self.root).as_posix() for path in report.records],
            ["skills/fmod-core-tools/fmod.toml", "skills/fmod-method/fmod.toml"],
        )
        self.assertEqual((report.skills, report.documents), (4, 3))

    def test_unknown_keys_and_tables_are_left_alone(self):
        self.method_record('code = "method"\n', 'code = "method"\nfuture_field = ["anything"]\n')
        path = self.skills / "fmod-method" / "fmod.toml"
        write(path, path.read_text(encoding="utf-8") + '\n[builder]\nversion = "9.9.9"\n')
        write(
            self.skills / "fmad-spec" / "fmod.toml",
            SKILL.format(fmod="fmod-method") + "later = true\n\n[extra]\nx = 1\n",
        )
        self.assertEqual(self.problems(), "")

    def test_single_skill_module_is_valid_under_any_folder_name(self):
        write(
            self.skills / "release-notes" / "fmod.toml",
            '[fmod]\ncode = "notes"\nversion = "6.11.0-next"\nupdate_source = "github:acme/notes"\n\n[skill]\n',
        )
        write(self.skills / "release-notes" / "help" / "help.md", "# help\n")
        self.assertEqual(self.problems(), "")

    def test_module_with_no_skills_is_valid(self):
        write(
            self.skills / "fmod-rooms" / "fmod.toml",
            f'[fmod]\ncode = "rooms"\nversion = "6.11.0-next"\nupdate_source = "{SOURCE}"\n',
        )
        write(self.skills / "fmod-rooms" / "help" / "help.md", "# help\n")
        self.assertEqual(self.problems(), "")

    def test_empty_skills_tree_is_a_problem(self):
        empty = self.root / "empty"
        empty.mkdir()
        self.assertIn("no skills/*/fmod.toml found", "\n".join(vm.check_repo(empty).problems))

    def test_main_exit_codes(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = vm.main(["--project-root", str(self.root)])
        self.assertEqual(code, 0, err.getvalue())
        self.assertIn("4 skills, 2 module records, 3 knowledge documents", out.getvalue())
        (self.skills / "fmad-flow" / "fmod.toml").unlink()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = vm.main(["--project-root", str(self.root)])
        self.assertEqual(code, 1)
        self.assertIn("skills/fmad-flow: missing fmod.toml", err.getvalue())


class FileRuleTests(ValidatorCase):
    def test_skill_folder_without_a_fmod_file(self):
        write(self.skills / "fmad-orphan" / "SKILL.md", "# orphan\n")
        self.assertIn("skills/fmad-orphan: missing fmod.toml", self.problems())

    def test_file_the_runtime_parser_rejects(self):
        write(self.skills / "fmad-spec" / "fmod.toml", 'note = "neither table"\n')
        problems = self.problems()
        self.assertIn("skills/fmad-spec/fmod.toml: the runtime parser rejects this file", problems)
        self.assertIn("[fmod] table, a [skill] table, or both", problems)

    def test_record_missing_a_required_key(self):
        self.method_record('version = "6.11.0-next"\n', "")
        problems = self.problems()
        self.assertIn("skills/fmod-method/fmod.toml", problems)
        self.assertIn("'fmod.version'", problems)

    def test_skill_missing_a_required_key(self):
        write(self.skills / "fmad-spec" / "fmod.toml", '[skill]\nfmod = "fmod-method"\n')
        problems = self.problems()
        self.assertIn("skills/fmad-spec/fmod.toml", problems)
        self.assertIn("'skill.source'", problems)

    def test_github_source_with_two_parts_is_accepted(self):
        write(self.skills / "fmad-spec" / "fmod.toml", '[skill]\nfmod = "fmod-method"\nsource = "github:o/r"\n')
        self.assertEqual(self.problems(), "")

    def test_github_source_with_one_part_is_rejected(self):
        write(self.skills / "fmad-spec" / "fmod.toml", '[skill]\nfmod = "fmod-method"\nsource = "github:o"\n')
        self.assertIn("github source must name owner/repo", self.problems())


class RecordRuleTests(ValidatorCase):
    def test_record_folder_not_named_after_its_code(self):
        (self.skills / "fmod-method").rename(self.skills / "fmod-fmad-method")
        for skill in MEMBERS["fmod-method"]:
            write(self.skills / skill / "fmod.toml", SKILL.format(fmod="fmod-fmad-method"))
        self.assertIn(
            "skills/fmod-fmad-method/fmod.toml: a module record folder is named 'fmod-method'", self.problems()
        )

    def test_second_record_for_one_code(self):
        write(
            self.skills / "fmod-zeta" / "fmod.toml",
            f'[fmod]\ncode = "method"\nversion = "6.11.0-next"\nupdate_source = "{SOURCE}"\n\n[skill]\n',
        )
        self.assertIn(
            "skills/fmod-zeta/fmod.toml: module code 'method' is already declared by skills/fmod-method/fmod.toml",
            self.problems(),
        )

    def test_codes_differing_only_by_case(self):
        write(
            self.skills / "upper" / "fmod.toml",
            f'[fmod]\ncode = "Method"\nversion = "6.11.0-next"\nupdate_source = "{SOURCE}"\n\n[skill]\n',
        )
        self.assertIn("module code 'Method' is already declared by", self.problems())

    def test_records_with_different_versions(self):
        self.method_record('version = "6.11.0-next"', 'version = "6.12.0"')
        problems = self.problems()
        self.assertIn("every module record carries one version", problems)
        self.assertIn("fmod-method has '6.12.0'", problems)


class RetiredRuleTests(ValidatorCase):
    def retire(self, record: str, lines: str) -> None:
        write(self.skills / record / "retired.toml", lines)

    def test_retired_names_that_no_longer_ship_are_valid(self):
        self.retire(
            "fmod-method", 'renamed = [{ from = "fmad-old-build", to = "fmad-build" }]\nremoved = ["fmad-gone"]\n'
        )
        self.assertEqual(self.problems(), "")

    def test_a_retired_name_that_still_ships_is_a_problem(self):
        self.retire("fmod-method", 'removed = ["fmad-spec"]\n')
        self.assertIn("retires 'fmad-spec', but skills/fmad-spec still ships", self.problems())

    def test_a_rename_to_a_skill_the_repository_does_not_ship_is_a_problem(self):
        self.retire("fmod-method", 'renamed = [{ from = "fmad-old", to = "fmad-missing" }]\n')
        self.assertIn("renames 'fmad-old' to 'fmad-missing', which this repository does not ship", self.problems())

    def test_a_name_retired_by_two_records_is_a_problem(self):
        self.retire("fmod-method", 'removed = ["fmad-gone"]\n')
        self.retire("fmod-core-tools", 'removed = ["fmad-gone"]\n')
        self.assertIn("retires 'fmad-gone', which skills/fmod-", self.problems())

    def test_two_renames_to_one_skill_are_a_problem(self):
        self.retire(
            "fmod-method",
            'renamed = [{ from = "fmad-a", to = "fmad-build" }, { from = "fmad-b", to = "fmad-build" }]\n',
        )
        self.assertIn("renames more than one skill to 'fmad-build'", self.problems())

    def test_a_retired_file_the_runtime_rejects_is_a_problem(self):
        self.retire("fmod-method", 'removed = ["fmad-gone", "fmad-gone"]\n')
        self.assertIn("skills/fmod-method/retired.toml: the runtime parser rejects this file", self.problems())


class StampRuleTests(ValidatorCase):
    def test_record_the_stamper_cannot_stamp(self):
        self.method_record('version = "6.11.0-next"', "version = '6.11.0-next'")
        self.assertIn(
            "skills/fmod-method/fmod.toml: tools/stamp_release.py cannot stamp this file: expected exactly one "
            "'version = \"...\"' line inside [fmod], found 0",
            self.problems(),
        )

    def test_version_lookalike_inside_a_multi_line_string(self):
        self.method_record('code = "method"\n', 'code = "method"\nnote = """\nversion = "x"\n"""\n')
        self.assertIn("cannot stamp this file", self.problems())

    def test_the_check_writes_nothing(self):
        path = self.skills / "fmod-method" / "fmod.toml"
        before = path.read_bytes()
        self.assertEqual(self.problems(), "")
        self.assertEqual(path.read_bytes(), before)


class MembershipRuleTests(ValidatorCase):
    def test_skill_naming_a_record_the_repo_lacks(self):
        write(self.skills / "fmad-spec" / "fmod.toml", SKILL.format(fmod="fmod-absent"))
        self.assertIn(
            "skills/fmad-spec/fmod.toml: [skill] fmod names 'fmod-absent', which is not a module record",
            self.problems(),
        )

    def test_skill_naming_a_folder_that_is_not_a_record(self):
        write(self.skills / "fmad-spec" / "fmod.toml", SKILL.format(fmod="fmad-build"))
        self.assertIn("[skill] fmod names 'fmad-build', which is not a module record", self.problems())

    def test_skill_its_record_does_not_list(self):
        write(self.skills / "fmad-extra" / "fmod.toml", SKILL.format(fmod="fmod-method"))
        self.assertIn(
            "skills/fmad-extra/fmod.toml: [skill] fmod names 'fmod-method', but skills/fmod-method/fmod.toml "
            "does not list 'fmad-extra'",
            self.problems(),
        )

    def test_listed_skill_the_repo_does_not_ship(self):
        self.method_record('["fmad-build", "fmad-spec"]', '["fmad-build", "fmad-spec", "fmad-typo"]')
        self.assertIn(
            "skills/fmod-method/fmod.toml: lists the skill 'fmad-typo', which this repository does not ship",
            self.problems(),
        )

    def test_listed_skill_that_names_another_record(self):
        write(self.skills / "fmad-spec" / "fmod.toml", SKILL.format(fmod="fmod-core-tools"))
        self.assertIn(
            "skills/fmod-method/fmod.toml: lists the skill 'fmad-spec', but skills/fmad-spec/fmod.toml names "
            "'fmod-core-tools' as its fmod",
            self.problems(),
        )

    def test_listed_folder_that_is_a_record(self):
        self.method_record('["fmad-build", "fmad-spec"]', '["fmad-build", "fmad-spec", "fmod-core-tools"]')
        self.assertIn("lists 'fmod-core-tools', which is a module record", self.problems())

    def test_record_with_skill_table_left_out_of_its_own_list(self):
        write(
            self.skills / "notes" / "fmod.toml",
            f'[fmod]\ncode = "notes"\nversion = "6.11.0-next"\nupdate_source = "{SOURCE}"\nskills = []\n\n[skill]\n',
        )
        self.assertIn("skills/notes/fmod.toml: holds [skill], but its own [fmod] skills list leaves", self.problems())


class RequirementRuleTests(ValidatorCase):
    def add(self, folder: str, line: str) -> None:
        path = self.skills / folder / "fmod.toml"
        write(path, path.read_text(encoding="utf-8") + line)

    def test_plain_names_in_this_repo_are_accepted_in_both_tables(self):
        self.add("fmad-build", 'required_skills = ["fmad"]\nrecommended_skills = ["fmad-spec"]\n')
        self.assertEqual(self.problems(), "")

    def test_required_plain_name_the_repo_lacks(self):
        self.add("fmad-build", 'required_skills = ["fmad-typo"]\n')
        self.assertIn(
            "skills/fmad-build/fmod.toml: skill.required_skills entry 'fmad-typo' names no skill in this repository",
            self.problems(),
        )

    def test_recommended_plain_name_the_repo_lacks(self):
        self.add("fmad-build", 'recommended_skills = ["fmad-typo"]\n')
        self.assertIn("skill.recommended_skills entry 'fmad-typo' names no skill", self.problems())

    def test_record_plain_name_the_repo_lacks(self):
        self.method_record('required_skills = ["fmad"]', 'required_skills = ["fmad-typo"]')
        self.assertIn(
            "skills/fmod-method/fmod.toml: fmod.required_skills entry 'fmad-typo' names no skill", self.problems()
        )

    def test_table_entry_from_another_repo_is_accepted(self):
        self.add(
            "fmad-build", 'required_skills = [{ skill = "elsewhere", version = "1.0.0", source = "github:o/r" }]\n'
        )
        self.assertEqual(self.problems(), "")

    def test_table_entry_without_a_source(self):
        self.add("fmad-build", 'required_skills = [{ skill = "fmad", version = "6.13.0" }]\n')
        self.assertIn("'skill.required_skills[0].source' must be a string", self.problems())

    def test_version_with_build_metadata(self):
        self.add("fmad-build", f'required_skills = [{{ skill = "fmad", version = "6.13.0+x", source = "{SOURCE}" }}]\n')
        problems = self.problems()
        self.assertIn("entry 'fmad' version '6.13.0+x' carries build metadata", problems)
        self.assertIn("'6.13.0'", problems)

    def test_unorderable_version(self):
        self.add("fmad-build", f'required_skills = [{{ skill = "fmad", version = "6.13", source = "{SOURCE}" }}]\n')
        self.assertIn("'skill.required_skills[0].version' must be an orderable version", self.problems())


class PathRuleTests(ValidatorCase):
    def test_help_file_a_fmod_folder_does_not_ship(self):
        (self.skills / "fmod-method" / "help" / "help.md").unlink()
        self.assertIn(
            "skills/fmod-method/help/help.md, which every fmod-* folder holds, the module record does not ship",
            self.problems(),
        )

    def test_help_file_is_optional_outside_a_fmod_folder(self):
        write(
            self.skills / "solo" / "fmod.toml",
            f'[fmod]\ncode = "solo"\nversion = "6.11.0-next"\nupdate_source = "{SOURCE}"\n\n[skill]\n',
        )
        write(self.skills / "solo" / "SKILL.md", "# skill\n")
        self.assertEqual(self.problems(), "")

    def test_help_symlink(self):
        target = self.skills / "fmod-method" / "help" / "help.md"
        target.unlink()
        target.symlink_to(self.skills / "fmod-method" / "delivery-help.md")
        self.assertIn("skills/fmod-method/help/help.md, which every fmod-* folder holds, is a symlink", self.problems())

    def test_topic_file_named_in_help_is_valid(self):
        write(self.skills / "fmod-method" / "help" / "help.md", "# help\n\nSee `help/deep-dive.md`.\n")
        write(self.skills / "fmod-method" / "help" / "deep-dive.md", "# deep dive\n")
        self.assertEqual(self.problems(), "")

    def test_topic_file_help_never_names(self):
        write(self.skills / "fmod-method" / "help" / "orphan.md", "# orphan\n")
        self.assertIn("skills/fmod-method/help/orphan.md is never named in help/help.md", self.problems())

    def test_help_naming_a_topic_file_that_does_not_exist(self):
        write(self.skills / "fmod-method" / "help" / "help.md", "# help\n\nSee `help/gone.md`.\n")
        self.assertIn(
            "skills/fmod-method/help/help.md names skills/fmod-method/help/gone.md, which does not exist",
            self.problems(),
        )

    def test_topic_file_naming_a_topic_that_does_not_exist(self):
        write(self.skills / "fmod-method" / "help" / "help.md", "# help\n\nSee `help/deep-dive.md`.\n")
        write(self.skills / "fmod-method" / "help" / "deep-dive.md", "See `help/gone.md`.\n")
        self.assertIn(
            "skills/fmod-method/help/deep-dive.md names skills/fmod-method/help/gone.md, which does not exist",
            self.problems(),
        )

    def test_knowledge_naming_the_help_file(self):
        self.method_record('path = "delivery-help.md"', 'path = "help/help.md"')
        self.assertIn("knowledge names 'help/help.md', which is always read", self.problems())

    def test_knowledge_file_the_record_does_not_ship(self):
        (self.skills / "fmod-method" / "delivery-help.md").unlink()
        self.assertIn(
            "skills/fmod-method/fmod.toml: knowledge names 'delivery-help.md', which the module record does not ship",
            self.problems(),
        )

    def test_knowledge_url(self):
        self.method_record('path = "delivery-help.md"', 'path = "https://docs.example.com/help.md"')
        self.assertIn("unsafe value", self.problems())

    def test_knowledge_path_leaving_the_folder(self):
        self.method_record('path = "delivery-help.md"', 'path = "../fmad-build/SKILL.md"')
        self.assertIn("unsafe value", self.problems())

    def test_knowledge_directory(self):
        (self.skills / "fmod-method" / "delivery-help.md").unlink()
        (self.skills / "fmod-method" / "delivery-help.md").mkdir()
        self.assertIn("knowledge names 'delivery-help.md', which is not a regular file", self.problems())

    def test_knowledge_symlink(self):
        target = self.skills / "fmod-method" / "delivery-help.md"
        target.unlink()
        target.symlink_to(self.skills / "fmod-method" / "help" / "help.md")
        self.assertIn("knowledge names 'delivery-help.md', which is a symlink", self.problems())

    def test_knowledge_naming_a_skill_outside_the_module(self):
        self.method_record('skills = ["fmad-build"]\n', 'skills = ["fmad-build", "fmad-flow"]\n')
        self.assertIn(
            "knowledge 'delivery-help.md' names 'fmad-flow', which is not a skill of module 'method'",
            self.problems(),
        )

    def test_a_module_without_a_roster_file_is_valid(self):
        (self.skills / "fmod-method" / "roster.toml").unlink()
        self.assertEqual(self.problems(), "")

    def test_roster_symlink(self):
        target = self.skills / "fmod-method" / "roster.toml"
        target.unlink()
        target.symlink_to(self.skills / "fmod-method" / "help" / "help.md")
        self.assertIn("skills/fmod-method/roster.toml is a symlink", self.problems())

    def test_roster_that_is_not_toml(self):
        write(self.skills / "fmod-method" / "roster.toml", "[[members\n")
        self.assertIn("skills/fmod-method/roster.toml: cannot read roster", self.problems())


class RosterContentTests(ValidatorCase):
    def roster(self, old: str, new: str) -> None:
        self.assertIn(old, ROSTER)
        write(self.skills / "fmod-method" / "roster.toml", ROSTER.replace(old, new))

    def test_member_code_defined_twice(self):
        self.roster('code = "guest"', 'code = "fmad-build"')
        self.assertIn("skills/fmod-method/roster.toml: member code 'fmad-build' is defined twice", self.problems())

    def test_group_naming_an_undefined_member(self):
        self.roster('members = ["fmad-build", "guest"]', 'members = ["fmad-build", "nobody"]')
        self.assertIn("group 'team' lists 'nobody', which no member defines", self.problems())

    def test_member_skill_the_repo_does_not_ship(self):
        self.roster('skill = "fmad-build"', 'skill = "fmad-typo"')
        self.assertIn(
            "member 'fmad-build' names skill 'fmad-typo', which this repository does not ship", self.problems()
        )


if __name__ == "__main__":
    unittest.main()
