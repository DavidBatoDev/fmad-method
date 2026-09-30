/**
 * Shared i18n locale configuration.
 *
 * Single source of truth for locale definitions used by:
 *   - docs-site/astro.config.mjs  (Starlight i18n)
 *   - docs-site/src/pages/404.astro (client-side locale redirect)
 *
 * The site is English-only: the root locale uses Starlight's 'root' key
 * convention (no URL prefix). A translated locale would get a URL prefix
 * matching its key.
 */

export const locales = {
  root: {
    label: 'English',
    lang: 'en',
  },
};

/**
 * Non-root locale keys (the URL prefixes for translated content).
 * @type {string[]}
 */
export const translatedLocales = Object.keys(locales).filter((k) => k !== 'root');
