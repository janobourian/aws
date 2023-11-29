# Fargate

## General Information

[Github Repository](https://github.com/stacksimplify/aws-fargate-ecs-masterclass)

## First steps

* ECS Objects:
    - Container Definition.
    - Task Definition:
        - Multiple Container Definition
        - Settings
    - Service:
        - Number of simultaneous instances of a task definition
    - Cluster:
        - Fargate
        - EC2 Linux
        - EC2 Windows
    - Task
        - Instantiation of a task in the last step.

### Create First Fargate Cluster

To get the fast starting we need to put the classic view.

- Container definition
- Task Definition
- Service
- Cluster 

If you increase the number of cluster you will have more ips direction, to avoid this is necessary to use a load balancer.

### Cost of ECS

Shutdown the clusters

## Docker Fundamentals

[Docker fundamentals](https://github.com/stacksimplify/docker-fundamentals)

Advantages to use Docker: 
- Flexible
- Lightweight
- Portable 
- Loosely Coupled 
- Scalable
- Secure

Docker terminology:
- Docker Host
- Docker Daemon: 
    - The Docker daemon listens for Docker API requests and managers Docker objects such as images, containers, networks, and volumes.
- Docker Client:
    - The Docker client is the primary way that many Docker users interact with Docker
    - The Docker client communicates with Docker Daemon
- Docker Images:
    - Read-only template with instructions for creating a Docker container
- Docker Containers:
    - Runnable instance of Docker Images. 
- Docker registry or Docker Hub:
    - A docker registry stores Docker images

### Docker Pull Images

```bash
docker version
docker login
docker logout
docker pull stacksimplify/dockerintro-springboot-helloworld-rest-api:1.0.0-RELEASE
docker images
docker ps
docker ps -a
docker run --name app1 -p 80:8080 -d stacksimplify/dockerintro-springboot-helloworld-rest-api:1.0.0-RELEASE
docker ps -a -q
docker exec -it <container_name> <commands>
docker stop <container_name>
docker rm <container_name>
docker rmi <image_name>
docker tag <your_docker_hub_id>/<container_name>:<version> <your_docker_hub_id>/<new_tag_for_container>:<version>
docker push <your_docker_hub_id>/<container_name>:<version>
```

### Build Docker Images

```bash
docker tag <your_docker_hub_id>/<container_name>:<version> <your_docker_hub_id>/<new_tag_for_container>:<version>
docker push <your_docker_hub_id>/<container_name>:<version>
```

Once you have your Dockerfile the next step is to create your new image, create your container and push it to the Docker Hub. 

```bash
docker build -t janobourian/rabbit:v1 .
docker run -d --name rabbit_starlette -p 8000:8000 --restart=always -it janobourian/rabbit:v1
docker tag janobourian/rabbit:v1 janobourian/rabbit:v1-checked
docker push janobourian/rabbit:v1-checked
``` 

### Essential Docker Commands

```bash
docker ps
docker ps -a
docker stop <container_id>
docker start <container_name>
docker restart <container_id>
docker port <container_id>
docker rm <container_id>
docker rm -f <container_id>
docker pull image <image_name>
docker exec -it <container_name> <commands>
docker rmi <image_id>
docker login
docker logout
docker stats 
docker versions
docker top <container_id>
```

## Understand Clusters, Task Definitions, Tasks and Services