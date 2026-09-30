// @ts-check
import { fileURLToPath } from 'node:url';

import { unified } from '@astrojs/markdown-remark';
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';
import fmadDiagrams from './src/integrations/diagrams.js';
import rehypeInlineDiagrams from './src/rehype-inline-diagrams.js';
import rehypeMarkdownLinks from './src/rehype-markdown-links.js';
import rehypeBasePaths from './src/rehype-base-paths.js';
import { getSiteUrl } from './src/lib/site-url.mjs';
import { locales } from './src/lib/locales.mjs';

const siteUrl = getSiteUrl();
const urlParts = new URL(siteUrl);
// Normalize basePath: ensure trailing slash so links can use `${BASE_URL}path`
const basePath = urlParts.pathname === '/' ? '/' : urlParts.pathname.endsWith('/') ? urlParts.pathname : urlParts.pathname + '/';

export default defineConfig({
  compressHTML: true,
  site: `${urlParts.origin}${basePath}`,
  base: basePath,
  outDir: '../build/site',
  redirects: {
    '/how-to/install-fmad': `${basePath}start/install-fmad/`,
    '/how-to/non-interactive-installation': `${basePath}start/install-fmad/`,
    '/tutorials/getting-started': `${basePath}start/build-your-first-change/`,
    '/how-to/get-answers-about-fmad': `${basePath}start/get-answers-about-fmad/`,
    '/how-to/quick-fixes': `${basePath}build/build-a-change/`,
    '/explanation/build': `${basePath}build/build-a-change/`,
    '/explanation/checkpoint-preview': `${basePath}build/walk-through-a-change/`,
    '/build/review-a-completed-change': `${basePath}build/walk-through-a-change/`,
    '/build/checkpoint-a-change': `${basePath}build/walk-through-a-change/`,
    '/explanation/adversarial-review': `${basePath}build/review-a-change/`,
    '/reference/testing': `${basePath}build/test-completed-work/`,
    '/reference/build-auto': `${basePath}build/autonomous-development-loops/`,
    '/reference/workflow-map': `${basePath}plan/choose-a-planning-path/`,
    '/reference/agents': `${basePath}reference/skills-and-agents/`,
    '/reference/commands': `${basePath}reference/skills-and-agents/`,
    '/reference/core-tools': `${basePath}reference/skills-and-agents/`,
    '/explanation/advanced-elicitation': `${basePath}reference/skills-and-agents/`,
    '/how-to/choose-a-development-path': `${basePath}plan/choose-a-planning-path/`,
    '/explanation/analysis-phase': `${basePath}plan/explore-and-validate-an-idea/`,
    '/explanation/brainstorming': `${basePath}plan/explore-and-validate-an-idea/`,
    '/explanation/forge-idea': `${basePath}plan/explore-and-validate-an-idea/`,
    '/how-to/pressure-test-an-idea': `${basePath}plan/explore-and-validate-an-idea/`,
    '/explanation/deep-recon': `${basePath}plan/research-a-decision/`,
    '/explanation/why-solutioning-matters': `${basePath}plan/design-ux-and-architecture/`,
    '/explanation/preventing-agent-conflicts': `${basePath}plan/design-ux-and-architecture/`,
    '/explanation/sprint-planning': `${basePath}plan/break-work-into-stories-and-track-it/`,
    '/explanation/retrospective': `${basePath}build/finish-an-epic/`,
    '/how-to/established-projects': `${basePath}existing-codebases/start-in-an-existing-codebase/`,
    '/explanation/established-projects-faq': `${basePath}existing-codebases/start-in-an-existing-codebase/`,
    '/how-to/project-context': `${basePath}existing-codebases/set-and-maintain-project-context/`,
    '/explanation/project-context': `${basePath}existing-codebases/set-and-maintain-project-context/`,
    '/explanation/project-context-theory': `${basePath}existing-codebases/theory-of-project-context/`,
    '/tutorials/getting-deeper': `${basePath}existing-codebases/getting-deeper/`,
    '/how-to/customize-fmad': `${basePath}customize/customize-fmad/`,
    '/explanation/named-agents': `${basePath}customize/customize-fmad/`,
    '/how-to/expand-fmad-for-your-org': `${basePath}customize/adopt-fmad-across-a-team/`,
    '/how-to/install-custom-modules': `${basePath}customize/add-modules/`,
    '/reference/modules': `${basePath}customize/add-modules/`,
    '/how-to/use-web-bundles': `${basePath}customize/use-web-bundles/`,
    '/explanation/web-bundles': `${basePath}customize/use-web-bundles/`,
    '/explanation/party-mode': `${basePath}customize/run-multi-agent-discussions/`,
  },

  // Disable aggressive caching in dev mode
  vite: {
    optimizeDeps: {
      force: true, // Always re-bundle dependencies
    },
    server: {
      watch: {
        usePolling: false, // Set to true if file changes aren't detected
      },
    },
  },

  markdown: {
    processor: unified({
      rehypePlugins: [
        // Hand-authored diagrams are inlined so custom.css can theme them; this
        // runs before rehypeBasePaths, which would otherwise rewrite the src of
        // an <img> that is about to be replaced.
        [rehypeInlineDiagrams, { root: fileURLToPath(new URL('.', import.meta.url)), locales }],
        [rehypeMarkdownLinks, { base: basePath }],
        [rehypeBasePaths, { base: basePath }],
      ],
    }),
  },

  integrations: [
    // must come before the pages that embed diagrams are rendered
    fmadDiagrams(),
    // Exclude custom 404 pages (all locales) from the sitemap — they are
    // treated as normal content docs by Starlight even with disable404Route.
    sitemap({
      filter: (page) => !/\/404(\/|$)/.test(new URL(page).pathname),
    }),
    starlight({
      title: 'Foundry Method',

      // i18n: locale config from shared module (docs-site/src/lib/locales.mjs)
      defaultLocale: 'root',
      locales,

      // The FMAD tile: the same mark the header carries. The SVG is what modern
      // browsers pick up; the .ico and the apple-touch-icon are rendered from
      // the same drawing, for the ones that ignore `image/svg+xml` and for iOS
      // home screens. Starlight prefixes `favicon` with the base path itself;
      // the two custom `head` links need it spelled out, because the site is
      // served from a subpath on GitHub Pages.
      favicon: '/favicon.svg',
      head: [
        {
          tag: 'link',
          attrs: { rel: 'icon', href: `${basePath}favicon.ico`, sizes: '32x32' },
        },
        {
          tag: 'link',
          attrs: { rel: 'apple-touch-icon', href: `${basePath}apple-touch-icon.png`, sizes: '180x180' },
        },
      ],

      // Social links
      social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/DavidBatoDev/fmad-method' }],

      // Show last updated timestamps
      lastUpdated: true,

      // Custom CSS
      customCss: ['./src/styles/custom.css'],

      // Sidebar configuration
      sidebar: [
        {
          label: 'Start',
          collapsed: false,
          items: [
            {
              label: 'Welcome',
              slug: 'index',
            },
            {
              label: 'Install FMAD',
              slug: 'start/install-fmad',
            },
            {
              label: 'Build Your First Change',
              slug: 'start/build-your-first-change',
            },
            {
              label: 'Get Answers About FMAD',
              slug: 'start/get-answers-about-fmad',
            },
          ],
        },
        {
          label: 'Build',
          collapsed: false,
          items: [
            {
              label: 'Build a Change',
              slug: 'build/build-a-change',
            },
            {
              label: 'Review a Change',
              slug: 'build/review-a-change',
            },
            {
              label: 'Walk Through a Change',
              slug: 'build/walk-through-a-change',
            },
            {
              label: 'Test Completed Work',
              slug: 'build/test-completed-work',
            },
            {
              label: 'Finish an Epic',
              slug: 'build/finish-an-epic',
            },
            {
              label: 'Autonomous Development Loops',
              slug: 'build/autonomous-development-loops',
            },
          ],
        },
        {
          label: 'Plan Larger Work',
          collapsed: true,
          items: [
            {
              label: 'Choose a Planning Path',
              slug: 'plan/choose-a-planning-path',
            },
            {
              label: 'Plan Inside an Organization',
              slug: 'plan/plan-inside-an-organization',
            },
            {
              label: 'Explore and Validate an Idea',
              slug: 'plan/explore-and-validate-an-idea',
            },
            {
              label: 'Research a Decision',
              slug: 'plan/research-a-decision',
            },
            {
              label: 'Define Requirements and a Specification',
              slug: 'plan/define-requirements-and-a-specification',
            },
            {
              label: 'Design UX and Architecture',
              slug: 'plan/design-ux-and-architecture',
            },
            {
              label: 'Break Work into Stories and Track It',
              slug: 'plan/break-work-into-stories-and-track-it',
            },
            {
              label: 'Set Up the Ticket Tree',
              slug: 'plan/set-up-the-ticket-tree',
            },
          ],
        },
        {
          label: 'Existing Codebases',
          collapsed: true,
          items: [
            {
              label: 'Start in an Existing Codebase',
              slug: 'existing-codebases/start-in-an-existing-codebase',
            },
            {
              label: 'Set and Maintain Project Context',
              slug: 'existing-codebases/set-and-maintain-project-context',
            },
            {
              label: 'Getting Deeper',
              slug: 'existing-codebases/getting-deeper',
            },
            {
              label: 'The Theory of Project Context',
              slug: 'existing-codebases/theory-of-project-context',
            },
          ],
        },
        {
          label: 'Customize and Extend',
          collapsed: true,
          items: [
            {
              label: 'Customize FMAD',
              slug: 'customize/customize-fmad',
            },
            {
              label: 'Adopt FMAD Across a Team',
              slug: 'customize/adopt-fmad-across-a-team',
            },
            {
              label: 'Add Modules',
              slug: 'customize/add-modules',
            },
            {
              label: 'Use Web Bundles',
              slug: 'customize/use-web-bundles',
            },
            {
              label: 'Run Multi-Agent Discussions',
              slug: 'customize/run-multi-agent-discussions',
            },
          ],
        },
        {
          label: 'Reference',
          collapsed: true,
          items: [{ autogenerate: { directory: 'reference' } }],
        },
      ],

      // Credits in footer
      credits: false,

      // Pagination
      pagination: false,

      // Use our docs/404.md instead of Starlight's built-in 404
      disable404Route: true,

      // Custom components
      components: {
        Header: './src/components/Header.astro',
        MobileMenuFooter: './src/components/MobileMenuFooter.astro',
        Sidebar: './src/components/Sidebar.astro',
        SiteTitle: './src/components/SiteTitle.astro',
        PageTitle: './src/components/PageTitle.astro',
        TwoColumnContent: './src/components/TwoColumnContent.astro',
      },

      // Table of contents
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
    }),
  ],
});
