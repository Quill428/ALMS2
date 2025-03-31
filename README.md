README File for JustMooreSalt website

Background
This was a challenging project as I had to attempt this website twice. This website is the result of my second attempt at my Django website. My first attempt at the website had too many issues, and after a long battle to try fixing the website, I decided it would be easier to start again. My thinking on this was that the most significant issue was based on how I initially set up the app and settings within the app. These seem to be causing multiple issues that were too many to fix, so I decided to restart the project from the beginning.

About the website
This website is the JustMooreSalt site, a recipe app that allows people to view and add recipes to the app so they have a collection of the JustMooreSalt recipes and the user's own recipes, all in one place. This is also a program to test Django's website development capabilities.

This site has a built-in user account that allows users to create their own account and later sign in as that account. There is a recipe page that holds all the recipes, as well as a ‘create post’ button that allows users to add their own recipes to the site with their description, image, name, ingredients, and directions. Users can also choose which category and sub-category the recipes most connect with, such as holiday or breakfast recipes.   

The website has a navigation bar at the top of the page that holds most of the links to the rest of the site. This navigation bar is static and shared across all of the site pages. There is also a footer that is also static on all of the site pages, and this holds all of the social media links and information about the website.

Help documentation
Pip: Pip is a required Dependency as it is a command-line tool that can help install, manage and update any Python packages from the Python index, including other dependencies. Without Pip, you can’t install Django as it is. Pip is usually already installed, but there may need to be an update at some stage. Use Pip Install to upgrade, update, or check the Pip version. You will then be prompted to update if needed. 

Django: Django is the main Dependency that you need. Without the Django framework, the website will not work. This framework sets up how the code runs and connects the different parts of the code. Django is also helpful in creating its administration area. The command for this is Pip Install Django.

Pillow: Pillow is the Django add-on that allows images to be added into the code. Once added to the code, these need to be able to run, so you enter the command Pip Install Pillow.

While downloading this Pillow code, be sure to download the most recent version on the most recent branch to hold all of the images and code pages. After you install Pillow, you must migrate the code with Python manage.py makemigrations followed by Python manage.py migrate. These will ensure that all the migrations on the site and in each app are working correctly.
