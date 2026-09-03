---
source: https://underscoretw.com/docs/deployment/
---

Deployment

# Move to production

Share your new WordPress theme with the world

## Building for production

Before deployment, you’ll want to create a production build:

`npm run prod`This ensures all unneeded CSS declarations have been removed and also minifies the resulting `style.css` file.

## Deployment via zip archive

To package your theme as a zip archive, you can use the `bundle` command:

`npm run bundle`This command will first execute `npm run prod` and then create a zip archive from your `theme` folder, in a file named after your theme slug.

The resulting theme archive can be uploaded directly to a WordPress site. Since WordPress 5.5, uploading a theme that has already been installed will result in an option to overwrite the existing theme, providing a viable path for quick deployments.

If you have copied your development theme from your local development environment to your production server as part of your initial deployment, you will notice that uploading the zip file created by the `bundle` script doesn&#8217;t overwrite the development version. In this case, you can activate the newly uploaded version and then delete the development version from your production server.

## Other deployment options

When deploying via other means, you&#8217;ll need to keep three things in mind:

- You should always run `npm run prod` before deploying
- Generated files (like `style.css` and `script.min.js`) aren&#8217;t committed to git by default
- Only the `./theme` folder should be deployed to production

If you’d like to deploy from the command line, [Deployer](https://deployer.org/) and [Capistrano](https://capistranorb.com/) are both great solutions for the command-line deployment of WordPress themes. SpinupWP also has a detailed look at [Deploying WordPress using the Command Line](https://spinupwp.com/wordpress-deployment-workflow-command-line/) showing several different techniques.

[GitHub Actions](https://github.com/features/actions) and [Envoyer](https://envoyer.io/) are excellent options as well.