FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
ADD requirements.txt /usr/src/app/
RUN apk update && \
    apk add --virtual build-deps build-base python3-dev musl-dev postgresql-dev && \
    apk add gettext && \
    apk add libffi-dev openssl-dev && \
    apk add postgresql-libs && \
    apk add memcached && \
    apk add jpeg-dev zlib-dev libjpeg && \
    apk add libmagic && \
    pip install -r requirements.txt && \
    apk del build-deps

# copy entrypoint script
ADD entrypoint.sh /usr/src/app/

# copy project
ADD mysite /usr/src/app/
RUN mkdir -p /usr/src/app/log

# expose port
EXPOSE 8080

# run entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
