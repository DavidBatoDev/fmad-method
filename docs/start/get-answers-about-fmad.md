---
title: 'Get Answers About FMAD'
description: Use an LLM to quickly answer your own FMAD questions
---

Use FMAD's built-in help, source docs, or the community to get answers — from quickest to most thorough.

## 1. Ask FMAD

The fastest way to get answers. The `fmad` skill is available directly in your AI session and handles over 80% of questions — it reads your active initiative, sees which `<type>-<slug>/` documents are already written, and tells you what to do next.

```
fmad I have a SaaS idea and know all the features. Where do I start?
fmad What are my options for UX design?
fmad I'm stuck on the PRD workflow
```

:::tip
You can also use `/fmad` or `$fmad` depending on your platform, but just `fmad` should work everywhere. The same skill runs `fmad setup` and `fmad status`, and switches the active initiative.
:::

## 2. Go Deeper with Source

The `fmad` skill draws on your installed configuration. For questions about FMAD's internals, history, or architecture — or if you're researching FMAD before installing — point your AI at the source directly.

Clone or open the [FMAD-METHOD repo](https://github.com/DavidBatoDev/fmad-method) and ask your AI about it. Any agent-capable tool (Claude Code, Cursor, Windsurf, etc.) can read the source and answer questions directly.

:::note[Example]
**Q:** "Tell me the fastest way to build something with FMAD"

**A:** Run `fmad-build`. Give it direct intent, an issue, a spec, or a planned story; it uses the available context and chooses the clarification, planning, implementation, and review depth needed.
:::

**Tips for better answers:**

- **Be specific** — "What does step 3 of the PRD workflow do?" beats "How does PRD work?"
- **Verify surprising claims** — LLMs occasionally get things wrong. Check the source file or ask in [GitHub Discussions](https://github.com/DavidBatoDev/fmad-method/discussions).

### Not using an agent? Use the docs site

If your AI can't read local files (ChatGPT, Claude.ai, etc.), open [the FMAD docs site](https://davidbatodev.github.io/fmad-method/).

## 3. Ask Someone

If neither the `fmad` skill nor the source answered your question, you now have a much better question to ask.

| Channel            | Use For                                |
| ------------------ | -------------------------------------- |
| GitHub Discussions | Questions, ideas, and feature requests |
| GitHub Issues      | Bug reports                            |

**GitHub Discussions:** [github.com/DavidBatoDev/fmad-method/discussions](https://github.com/DavidBatoDev/fmad-method/discussions)

**GitHub Issues:** [github.com/DavidBatoDev/fmad-method/issues](https://github.com/DavidBatoDev/fmad-method/issues)

_You!_  
&emsp;&emsp;_Stuck_  
&emsp;&emsp;&emsp;&emsp;_in the queue—_  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_waiting_  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_for who?_

_The source_  
&emsp;&emsp;_is there,_  
&emsp;&emsp;&emsp;&emsp;_plain to see!_

_Point_  
&emsp;&emsp;_your machine._  
&emsp;&emsp;&emsp;&emsp;_Set it free._

_It reads._  
&emsp;&emsp;_It speaks._  
&emsp;&emsp;&emsp;&emsp;_Ask away—_

_Why wait_  
&emsp;&emsp;_for tomorrow_  
&emsp;&emsp;&emsp;&emsp;_when you have_  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_today?_

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_—Claude_
