---
source: https://underscoretw.com/docs/development/
---

Development

# Build something great, faster

Watch for changes, build for production and learn more about how _tw, WordPress and Tailwind work together

## Watching for changes

During development you’ll probably want Tailwind to be watching your theme repository for changes and regenerating your `style.css` file automatically:

`npm run watch`The `watch` command will run continuously in the background, keeping things up-to-date.

## Adding custom CSS

Everything you need to configure Tailwind or to add custom CSS can be found in the `./tailwind` folder.

The file you are most likely to need to modify is `./tailwind/tailwind-theme.css`. This is where you add your design tokens in the form of Tailwind theme variables.

The `./tailwind/tailwind.css` and `./tailwind/tailwind-editor.css` files import everything needed to generate `style.css` and `style-editor.css`, respectively. (You should never edit those generated files directly, as they will be overwritten when new versions are generated.) There are comments throughout the CSS files in the `./tailwind` folder explaining what to put in each file.

## Adding block editor–only CSS

The `./tailwind/tailwind-editor-extra.css` file is processed by Tailwind (so you can use `@apply` and other Tailwind functionality), and its output file is `style-editor-extra.css`, alongside the existing `style.css` and `style-editor.css` files. It is added by default as an editor style in `./theme/functions.php`.

## JavaScript

_tw includes [esbuild](https://esbuild.github.io/) as its JavaScript bundler. For details on how to use it, including an example covering how to install and bundle [Alpine.js](https://alpinejs.dev/), please see the dedicated documentation page on [JavaScript Bundling with esbuild](https://underscoretw.com/docs/esbuild/).

## theme.json

Now with built-in [`theme.json`](https://developer.wordpress.org/block-editor/how-to-guides/themes/theme-json/) support, _tw includes a basic `theme.json` file in its `theme` folder. The color and width values from that file are automatically made available to Tailwind via CSS variables in `./tailwind/tailwind-theme.css`.

This means the top-level colors in `theme.json` can be used in Tailwind (with classes like `bg-primary` or `text-primary`), and the values for `contentSize` and `wideSize` are available for setting `max-width` with either `max-w-content` or `max-w-wide`.

(Still not using the block editor? You can safely ignore the included `theme.json` support entirely! You may want to delete the design tokens referencing WordPress CSS variables, though, as those may not be loaded when using the classic editor.)

## Tailwind Typography

[Tailwind Typography](https://tailwindcss.com/docs/typography-plugin) comes preinstalled with _tw. To learn how to set up the Typography plugin in your generated theme, please see the dedicated documentation page on [using Tailwind Typography](https://underscoretw.com/docs/tailwind-typography/).