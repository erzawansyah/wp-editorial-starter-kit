---
source: https://underscoretw.com/docs/installation/
---

Installation

# Get started with _tw

Generate your custom theme, install it in WordPress and run your first Tailwind builds

## Generate your custom theme

There are two ways to get started with _tw:

- [Using the web-based generator](/), or:
- [Via WP-CLI](https://underscoretw.com/docs/wp-cli/)

Both approaches offer the same options. These ones may not be self-explanatory:

- **Theme Name**: The name of your theme in title case, with or without spaces. If the theme slug and function prefix fields are both left blank, this field will be used to derive values for those fields.
- **Theme Slug**: A custom theme slug if the automatically generated one is not appropriate.
- **Function Prefix**: A custom function prefix if the automatically generated one is inappropriate (or, more often, too long). Please note that WordPress Coding Standards call for function prefixes of at least four characters.

All other fields provide metadata that will appear in the header comment at the beginning of the theme&#8217;s `style.css` file.

## Move your theme into place

After unzipping your generated theme archive, you should move it into the correct folder.

The easiest and quickest way to get started is simply to move your generated theme folder into the `wp-content/themes` folder in your local development environment.

Depending on your requirements, you may want to move your generated theme folder elsewhere in your local environment and then create a symbolic link from the `theme` folder in your generated theme to `wp-content/themes/[theme-slug]`.

Once your theme is in place, you can go ahead and activate it! (Using WordPress Multisite? Don’t forget that your theme must first be enabled via the Network Admin in order to be available for activation on a network site.)

## Install Tailwind

Your first step before installing Tailwind is to [install npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) if you haven’t already. After that, open your terminal of choice, navigate to your generated theme folder and run:

`npm install`With Tailwind now installed, you can then generate your `style.css` file by running:

`npm run dev`This creates a development build of your theme’s stylesheet.

## Install additional tools

Your custom theme also includes tools for linting, code formatting and internationalization. To install them, navigate to your generated theme folder and run:

`composer install`