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
    - The Docker client is th eprimary way that many Docker users interact with Docker
    - The Docker client communicates with Docker Daemon
- Docker Images:
    - Read-only template with instructions for creating a Docker container
- Docker Containers:
    - Runnable instance of Docker Images. 
- Docker registry or Docker Hub:
    - A docker registry stores Docker images