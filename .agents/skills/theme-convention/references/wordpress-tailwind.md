---
source: https://underscoretw.com/docs/wordpress-tailwind/
---

Extras

# On Tailwind and WordPress

Understand how WordPress and Tailwind work together

## CSS in WordPress

A typical WordPress site loads CSS from three sources:

- WordPress itself
- Active plugins
- The active theme

That CSS can target either the site’s front end or the administration area.

**Tailwind is excellent at creating the CSS provided by the active theme targeting the site’s front end.**

## Can plugins use Tailwind?

Plugins absolutely can use Tailwind, but not without deviating from a more standard Tailwind configuration and adding sometimes significant levels of complexity.

While an active theme gets the highest level of priority in terms of dictating front-end CSS, a plugin needs to work in conjunction with the active theme’s styles. This generally means disabling Tailwind’s Preflight, wrapping all of the generated CSS in a selector specific to the plugin, prefixing all utility classes with a string specific to the plugin, or some combination of the above.

## Why can’t themes use Tailwind in the administration area (outside the editor)?

To the extent that a theme provides custom CSS for WordPress’s administration area, Tailwind is unlikely to work as expected without taking similar steps to the ones required for plugins.

Themes will be better served by embracing the administration area’s included CSS and by mirroring the HTML structure of existing administration pages. (And if you find yourself needing administration area styles outside the editor, you could be in plugin territory: It may be worth transitioning that functionality into a dedicated plugin.)

## What about the block editor?

WordPress themes can opt in to provide block editor styles using `add_theme_support( 'editor-styles' )` and can then point to an appropriate CSS file using the `add_editor_style` function.

_tw takes care of this, and automatically creates a separate CSS file compatible with the block editor.

If you want to use Tailwind and WordPress together without using _tw, please be aware that the block editor’s requirements for this file may not be compatible with the front-end CSS you’ve written for your site, and will vary significantly if you’re using Tailwind in conjunction with Tailwind Typography. However, with an appropriate build process, it’s possible to create front-end and editor styles from the same source files supporting both use cases. By using _tw, you’ll be able to avoid the work of setting up this build process yourself.

## What about full-site editing?

WordPress’s full-site editing functionality remains very much in flux, but right now the way global styles are translated from `theme.json` into front-end CSS does not work well when paired with Tailwind CSS.

My current expectation is that hybrid themes using a `theme.json` file to integrate with the block editor, but not supporting all features of full-site-editing, will continue to be the best path forward for Tailwind-based WordPress themes. This is the approach that _tw currently uses.

## Can I add arbitrary Tailwind classes in the block editor?

When you add Tailwind classes directly to your theme and generate a CSS file using Tailwind&#8217;s build process, only the classes included in your theme will be added to your CSS file. This means that if you add new classes not found in your theme to blocks in the block editor, the corresponding styles will not appear in your CSS file because Tailwind did not know to include them when it built the CSS.

If your project requires you to add classes within the block editor without them appearing within class attributes in your theme, two options to consider are:

- [Safelisting classes](https://tailwindcss.com/docs/content-configuration#safelisting-classes) in your Tailwind configuration file (assuming you know in advance what the classes will be)
- Using [Twind&#8217;s shim module](https://twind.dev/handbook/the-shim.html) to translate Tailwind utility classes into CSS using JavaScript