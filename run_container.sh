#!/bin/bash

if [ "$(docker ps -a -q -f name=proactive_web)" ]; then
    # The container already exists, start and attach to container
    docker start proactive_web
    docker attach proactive_web
else
    # The container is not running, start a new one
    docker run -it --name proactive_web -p 8000:8000 -v ./ProactiveWeb:/root proactive_web:latest /bin/bash
fi
