django-docker-for-app-platform
==============================

This is a Django 2.2 based project using Docker for deployment on DigitalOcean App Platform

Deploying the App
-----------------

* Fork this repository
* Create a new App in DigitalOcean (https://cloud.digitalocean.com/apps/new)
* When prompted about environment variables:

  * Set a ``SECRET_KEY`` environment variable
  * You can set ``ALLOWED_HOSTS`` to ``${APP_DOMAIN}`` to set the allowed_hosts setting to the default domain provided by DigitalOcean
  * All other enviroment variables are optional, you can find the list in the ``Dockerfile``

* There is no need to set a Run Command
* The default HTTP Port for the project is already ``8080``
* If you want to add a database, you must update `settings.py`. By default SQLite is used, but the data is lost everytime the application is re-deployed
