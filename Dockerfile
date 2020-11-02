FROM python:3.7-alpine

# set work directory
WORKDIR /usr/src/app

# install gettext
RUN apk update && apk add gettext

# define arguments and default values
ARG SECRET_KEY
ARG DEBUG="False"
ARG ALLOWED_HOSTS="localhost, 127.0.01"
ARG SITE_ID="1"
ARG STATIC_URL="/static/"
ARG MEDIA_URL="/media/"

# set environment variables
ENV SECRET_KEY=${SECRET_KEY}
ENV DEBUG=${DEBUG}
ENV ALLOWED_HOSTS=${ALLOWED_HOSTS}
ENV SITE_ID=${SITE_ID}
ENV STATIC_URL=${STATIC_URL}
ENV MEDIA_URL=${MEDIA_URL}

# install dependencies
RUN pip install --upgrade pip
ADD requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt --no-cache-dir

# copy entrypoint script
ADD entrypoint.sh /usr/src/app/

# copy project
ADD mysite /usr/src/app/
RUN mkdir -p /user/src/app/log

# expose port
EXPOSE 8080

# run entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
