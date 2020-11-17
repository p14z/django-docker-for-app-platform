django-docker-for-app-platform
==============================

This is a Django 2.2 based project using Docker for deployment on DigitalOcean App Platform

Deploying the App
-----------------

* Fork this repository
* Create a new App in DigitalOcean (https://cloud.digitalocean.com/apps/new)
* When prompted about environment variables:

  * Set a ``SECRET_KEY``
  * You can set ``ALLOWED_HOSTS`` to ``${APP_DOMAIN}`` to set the allowed hosts to the default domain provided by DigitalOcean
  * If you want to add a database, you can set ``DATABASE_URL`` as described `here <https://github.com/jacobian/dj-database-url>`_. By default SQLite is used, but the data is lost everytime the application is re-deployed
  * All other environment variables are optional, you can find the list in the ``settings.py`` file

* There is no need to set a Run Command
* The default HTTP Port for the project is already ``8080``

**Note:**
Static and Media files are served using Gunicorn, this is not recommended for production.
