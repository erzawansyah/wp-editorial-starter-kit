---
source: https://underscoretw.com/docs/custom-blocks/
---

Extras

# Managing Styles for Custom Blocks

Learn strategies for using Tailwind in theme-specific custom blocks

If you&#8217;re creating custom blocks for your project and you want a single Tailwind build process capturing both your WordPress theme&#8217;s utility classes and the utility classes for your custom blocks, you have a number of options:

- In your custom block repository, use dynamic blocks and add a filter to the dynamic block&#8217;s HTML markup. Then use that filter to put the block&#8217;s markup in your theme repository with `add_filter`.
- Put your block plugin or plugins inside your theme repository.
- Manually safelist the utility classes required by your block by adding them in a comment or elsewhere in your theme repository.

My preference would be to move the block&#8217;s markup to your theme via a filter. If that isn&#8217;t possible, there are some potential downsides to the other approaches:

## Putting your block plugin inside your theme repository

Imagining that you add a `plugin` folder alongside the `theme` folder in your theme repository, you would need to create a [symbolic link](https://en.wikipedia.org/wiki/Symbolic_link) to add the plugin to WordPress during local development, and you would need to create a separate build process for the plugin.

## Manually safelisting the required utility classes

This means any changes to the block&#8217;s utility classes need to be made in two places as you maintain both the safelist and the class attributes within the block&#8217;s markup.