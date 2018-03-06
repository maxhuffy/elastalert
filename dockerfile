#!IMAGE ingalls/elastalert

FROM alpine:3.4

# Update APK
RUN apk update && \
    apk upgrade

# Build Essentials
RUN apk add gcc make g++ zlib-dev

# Bash
RUN apk add --update bash

# Python
RUN apk add --no-cache python python-dev libffi-dev openssl openssl-dev && \
    python -m ensurepip && \
    pip install --upgrade pip setuptools

RUN mkdir /elastalert
WORKDIR /elastalert

ENV PYTHONPATH /

# To make sure whatever python outputs is immediately visible through `docker logs`
ENV PYTHONUNBUFFERED 1

COPY ./src /elastalert

RUN pip install -r /elastalert/requirements.txt

CMD ["/usr/bin/python", "/elastalert/elastalert/elastalert.py"]  
