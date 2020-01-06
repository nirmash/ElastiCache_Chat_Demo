# Overview
This repo contains a demo for using Redis (in a Docker container or on ElastiCache) as a backend for a realtime chat application. 

**Warning:** The application and instructions were developed and tested on a Mac client and an EC2 Amazon Linux server.

# How it works
The demo is a single page web application ([SPA](https://en.wikipedia.org/wiki/Single-page_application)). It creates a Redis list that stores messages and user names. The name of the list is used by the demo as a session id. The demo includes a REST API that sets the active session id.

The demo is implemented in [Python Flask](https://www.fullstackpython.com/flask.html) (backend) and Javascript on a client HTML page. The demo runs in a Docker container to make dependencies easier to manage.

# How to use it
Once installed, change the user name in the `User name` field (it defaults to "default user") and type a message in the text box below, the message will appear above the input box, similar to other realtime chat apps. Other users browsing to the demo web address will be able to see all messages in the session and add to it. 

![Screenshot](https://github.com/nirmash/ElastiCache_DbCache_Demo/blob/master/images/chat-screenshot.jpg?raw=true)

# Install
This demo can run on a local environment that uses Docker or on EC2 with ElastiCache for Redis. 
## Prerequisites 
The application dependencies are valid for both local environments or on EC2:
* [Docker](https://docs.docker.com/v17.09/engine/installation/)
* [docker-compose](https://docs.docker.com/compose/install/)
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

**Note:** `yum` is the package manager used on EC2 Amazon Linux instances.

## Application files
Clone the demo repository:
```
$ git clone https://github.com/nirmash/ElastiCache_Chat_Demo.git
```
## Environment variables
Set the environment variables required to run the demo.

**Note:** The demo uses environment variables to store application secrets.
### AWS
```
export REDIS_MASTER_HOST=your_redis_master_node_endpoint
export REDIS_MASTER_PORT=your_redis_master_port (typically 6379)
export FLASK_ENV=development
export PYTHONPATH=/code
```
### Locally 
```
export REDIS_MASTER_HOST=chat_redis_1
export REDIS_MASTER_PORT=6379
export FLASK_ENV=development
export PYTHONPATH=/code
```

# Build
Browse to the `docker-compose.yaml` file location and load the application Docker container:
```
$ cd ElastiCache_Chat_Demo/chat
$ ./init_service.sh
```
After the build process is done, the Docker containers status will appear (see below):

```
     Name                   Command               State                 Ports               
--------------------------------------------------------------------------------------------
chat_redis_1     docker-entrypoint.sh redis ...   Up      0.0.0.0:63791->6379/tcp, 63791/tcp
chat_service_1   /bin/sh -c /code/run-server.sh   Up      10000/tcp, 0.0.0.0:80->80/tcp     
```
Note that the application will load 2 containers, the chat_service_1 contains the application code while the chat_redis_1 container can be used instead of ElastiCache to run the demo locally.

# Run the demo
**Locally:** Browse to http://localhost.

**On AWS:** Browse to the endpoint of the EC2 server you created earlier.