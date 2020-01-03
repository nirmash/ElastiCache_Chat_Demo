#!/bin/sh
docker-compose stop
docker-compose pull
docker-compose up --build -d
docker-compose ps