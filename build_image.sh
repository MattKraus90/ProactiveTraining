#!/bin/bash

# # unzip images
# apt install unzip
# unzip ProactiveWeb/webapp/static/imgs.zip -d ProactiveWeb/webapp/static

# build container
docker build -t proactive_web .
