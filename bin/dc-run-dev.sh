#!/bin/sh

arr=$1
if [[ $arr == "down" ]]
then
    docker-compose down
else
    docker-compose up -d --build
fi
