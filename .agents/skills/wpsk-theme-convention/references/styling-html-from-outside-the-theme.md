---
source: https://underscoretw.com/docs/styling-html-from-outside-the-theme/
---

# Styling HTML from outside the theme

Work with WordPress core, plugins and JavaScript libraries

There are three main approaches to consider when styling HTML from WordPress core, a WordPress plugin or a JavaScript library:

- Use the existing output as-is, attaching CSS to the provided classes and not using utility classes
- When possible, use functions that allow you to add utility classes without rewriting the HTML directly
- Take control of the HTML and use utility classes as usual

The method to use depends on the options available to you and your priorities, and each comes with benefits and drawbacks.

## Using the existing output

One of the main benefits of using Tailwind in a project is the removal of most context switching when styling an HTML component. Nonetheless, there are times when it will prove more straightforward and less work on your part to move your styles into a separate file.

Using WordPress&#8217;s core menus as an example, default output from the [`wp_nav_menu()` function](https://developer.wordpress.org/reference/functions/wp_nav_menu/) looks something like this:

&lt;div class="menu-header-container"&gt;
	&lt;ul id="menu-header" class="menu"&gt;
		&lt;li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1"&gt;
			&lt;a href="https://underscoretw.com/docs/"&gt;Documentation&lt;/a&gt;
		&lt;/li&gt;
		&lt;li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2"&gt;
			&lt;a href="https://underscoretw.com/about/"&gt;About&lt;/a&gt;
		&lt;/li&gt;
		&lt;li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3"&gt;
			&lt;a href="https://underscoretw.com/contact/"&gt;Contact&lt;/a&gt;
		&lt;/li&gt;
	&lt;/ul&gt;
&lt;/div&gt;Code language: HTML, XML (xml)Instead of trying to inject utility classes into this menu, we could add CSS targeting the existing classes, using `@apply` if we want to continue using Tailwind classes:

#menu-header {
	@apply flex justify-between;
}

#menu-header .menu-item {
	@apply text-bold;
}Code language: CSS (css)The above CSS could be added to any appropriate location in the `./tailwind/custom` folder.

## Adding utility classes via function parameters

In some cases, the functions you&#8217;re already using may have options allowing you to add your own classes. Returning to the example above, we could call `wp_nav_menu()` with different arguments:

wp_nav_menu(
	array(
		'container'      =&gt; false,
		'theme_location' =&gt; 'menu-1',
		'menu_id'        =&gt; 'primary-menu',
		'menu_class'     =&gt; 'flex justify-between &#91;&_.menu-item]:text-bold',
	)
);Code language: PHP (php)This provides the same outcome as the approach from the first section, but moves all of the styles to the function call so that you can manage them all in one place. It also does so without any need to modify the structure of the HTML provided by the function.

## Creating your own HTML

You may find that you need to do something more complicated than what a function&#8217;s output allows, or you may want to be able to control the exact HTML output you&#8217;re sending to your visitors. In the specific case of menus, you have a couple of options for creating your own HTML:

- Use the `Walker_Nav_Menu` class
- Use the `wp_get_nav_menu_items()` function

### On walking through your nav(igation)

While extremely powerful, my experience has been that the [`Walker_Nav_Menu` class](https://developer.wordpress.org/reference/classes/walker_nav_menu/) is almost always too cumbersome to be worth using in a custom theme. It nonetheless has its place for deep customization of WordPress menus, and it&#8217;s worth being aware of this approach.

### There has got to be a better way

The [`wp_get_nav_menu_items()` function](https://developer.wordpress.org/reference/functions/wp_get_nav_menu_items/) can more quickly put you in a position to rework the HTML structure of your menus. Returning an array of menu items, this function allows you to iterate through a menu and provide your own HTML as you go.

Because it provides the menu without its hierarchy intact, it&#8217;s best used on simpler menus, or with an understanding that you&#8217;ll need to create your own array with nested submenus before beginning to output your menu.

You&#8217;ll find versions of these approaches will serve you well for both output from WordPress core and for WordPress plugins.

## Notes on JavaScript libraries

JavaScript libraries often come with their own CSS in a separate file. My approach in these cases is generally to drop that CSS file into the `./tailwind/custom/components` folder and to edit it there. Once located in that directory, you can use `@apply` if you so choose, and the CSS will automatically be bundled into the `style.css` file for your theme.

Two items worth noting:

- Be cautious of bloated CSS files with far more styles than you&#8217;ll need for your project
- When possible, choose libraries with fully namespaced CSS

In the former case, editing the CSS file to remove unneeded styles is often worthwhile. In the latter case, keep an eye out for overly broad CSS selectors from third-party libraries that could override your site&#8217;s styles in unexpected ways.