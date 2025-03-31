second attempt at my django website as my first one came into too many issues and after a while trying to fix it i figured the easiest thing to do was to start again as the issue lying in how i set up the app and settings with in the app causing multiple issues causing me to restart.

this Project is the JustMooreSalt site which is a recipe app that allows people to view and add recipes that are or will be on the app. this is also a program to test out Django's capabilities

In this site there is built in user account that allows users to create their own account and later sign in as that account. There is a recipe page that holds the recipes as well as a create post button that allow the users to create their own Recipes with their own description, image, name, ingredients, and directions with them also able to choose which category and sub category they most connect with

In the site there is a nav bar at the top of the page that holds most of the links to the site and is shared across all of the site as well as a footer which holds all of the social media links and information.

Pip- Pip is a required Dependency as its a command line tool that can help install, manage and update any python packages from the index of python including other dependencies, without it you can’t install Django as it is. This is normally already install but it may need an update use pip install –upgrade yo update it, or check the version with pip version and it will prompt you to update it.l

Django- Django is the main Dependency that you need as without it Django framework won’t work, this frame work sets up the how the code will run and connect to each other because without it there won’t be connections across different parts of the code in the way that is needed for Django, Django is also helpful crating its own admin area. The command for this is pip install Django

Pillow- Pillow is the Django add on that allows images to be added into the code to then be added into the code to run this you need you enter in the command pip install pillow

While downloading this code make sure to download the most recent version of it on the most recent branch, that should hold all of the images and code pages. After its install you’ll need to migrate the code with python manage.py makemigrations followed by python manage.py migrate. This will make sure that all of the migrations on the site and in each app is working
