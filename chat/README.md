
# Build
$ docker-compose pull
$ docker-compose up --build -d
$ docker-compose ps

# login to container
docker exec -it chat_service_1 /bin/bash 	
docker exec -it chat_service_1 curl -v http://localhost:80