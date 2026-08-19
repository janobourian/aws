# Containers on AWS: ECS, Fargate, ECR and EKS

## Docker Introduction

Containers are lightweight, portable units that package an application and its dependencies together. Docker is a popular platform for creating, deploying, and managing containers. It allows developers to build applications in isolated environments, ensuring consistency across different stages of development and production.

* Docker is a software development platform to deploy apps
* Apps are packaged in containers that can be run on any OS
* Containers are isolated from each other and the host system
* Containers share the OS kernel, making them lightweight and fast
* Docker images are read-only templates used to create containers
* Docker Hub is a public registry for sharing Docker images
* Getting Started with Docker:
  * Dockerfile
  * Build
  * Docker image
  * Push/Pull
  * Docker Repository
  * Run
  * Docker Container
* Docker Containers Management on AWS:
  * Amazon Elastic Container Service (Amazon ECS)
    * Amazon's own container platform
  * Amazon Elastic Kubernetes Service (Amazon EKS)
    * Amazon's managed Kubernetes (open source)
  * AWS Fargate
    * Amazon's own Serverless container platform
    * Works with ECS and with EKS
  * Amazon ECR
    * Store container images

## AWS Container Services Overview

AWS offers several services to run and manage containers:

* **Amazon ECS (Elastic Container Service)**: A fully managed container orchestration service that supports Docker containers. It allows you to run and scale containerized applications easily.
* **AWS Fargate**: A serverless compute engine for containers that works with both Amazon ECS and Amazon EKS. It allows you to run containers without managing the underlying infrastructure.
* **Amazon EKS (Elastic Kubernetes Service)**: A managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install and operate your own Kubernetes control plane or nodes.
* **Amazon ECR (Elastic Container Registry)**: A fully managed Docker container registry that makes it easy to store, manage, and deploy Docker container images.

## Amazon ECS

ECS = Elastic Container Service

### EC2 Launch Type

* Launch Docker containers on AWS = Launch ECS Tasks on ECS Clusters
* You must provision and maintain the infrastructure
* Each EC2 Instance must run the ECS Agent to register in the ECS Cluster
* AWS takes care of starting/stopping containers

### Fargate Launch Type

* You do not provision the infrastructure
* It is a serverless
* You just create task definitions
* AWS just runs ECS tasks fro you based on the CPU/RAM you need
* To scale, just increase the number of tasks. Simple - no more EC2 instances

### Amazon ECS - IAM Roles for ECS

* EC2 Instance Profile (EC2 Launch type only)
  * Used by the ECS agente
  * Makes API Call to ECS service to verify the status
  * Send container logs to CloudWathc Logs
  * Pull Docker image from ECR
  * Reference sensitiv data in Secrets Manager or SSM Parameter Store

* ECS Task Role:
  * Allows each task to have specific role
  * Use different roles for the different ECS Services you run
  * Task Role is defined in the task definition

### Amazon ECS - Load Balancer Integrations

* Application Load Balancer
* Network Load Balancer
* Classic Load Balancer (No advanced features - No Fargate)

### Amazon ECS - Data Volumes (EFS)

* Amazon EFS (Elastic File System) is a fully managed NFS file system
* Can be mounted on multiple ECS tasks simultaneously
* Useful for sharing data between containers
* Supported only on Fargate platform version 1.4.0 and later
* Supported by EC2 and Fargate launch types
* Amazon S3 can not be mounted as a file system

### Hands-on

* Create the Cluster
  * AWS Fargate
  * Amazon EC2 Instances
  * Amaxon Anyware
* Assign VPC data
* Auto-Scaling Group will be created
* Capacity providers:
  * Fargate
  * Fargate_Spot
  * ASG

* Create the service:
  * Launch Task (Active Docker Containers)
* Launch the service

### ECS Service Auto Scaling

* Automatically increase/decrease the desired number of ECS tasks
* Amazon ECS Auto Scaling uses AWS Application Auto Scaling
  * ECS Service Average CPU utilization
  * ECS Service Average Memory Utilization - Scale on RAM
  * ALB Request Count Per Target - metric coming from the ALB
* Target tracking - scale based on target value for specific CloudWatch metric
* Step scaling - scale based on specified CloudWatch Alarm
* Scheduling Scaling - scale based on a specified date/time
* ECS Service Auto Scaling is different to EC2 Auto Scaling
* Fargate Auto Scaling is much easier to setup because it is serverless

#### EC2 Launch Type - Auto Scaling EC2 Instances

* Accommodate ECS Service Scaling by adding underlying EC2 Instances
* Auto Scaling Group Scaling
  * Scale your ASG based on CPU Utilization
  * Add EC2 instances over time
* ECS Cluster Capacity Provider
  * Used to automatically provision and scale the infrastructure for your ECS Tasks
  * Capacity Provider paired with an Auto Scaling Group
  * Add EC2 Instances when you are missing capacity

* Patterns:
  * ECS Scaling - Service CPU Usage
  * ECS tasks invoked by Event Bridge
  * ECS tasks invoked by Event Bridge Schedule
  * ECS tasks invoked by SQS messages
  * ECS - Intercept Stopped Tasks using EventBridge

## Amazon ECR

* ECR = Elastic Container Registry
* Store and manage Docker images on AWS
* Private and Public repository
* Integrated with Amazon ECS, EKS, and Fargate
* Supports image scanning for vulnerabilities
* Supports image lifecycle policies to manage image retention
* Securely store images using AWS IAM for access control

## Amazon EKS

* Amazon EKS = Amazon Elastic Kubernetes Service
* It is a way to launch managed Kubernetes clusters on AWS
* Fully managed Kubernetes control plane
* Node Types:
  * Managed Node Groups
  * Self-Managed Nodes
  * AWS Fargate
* Data Volumes:
  * Amazon EBS
  * Amazon EFS
  * Amazon FSx for Lustre
  * Amazon FSx for NetApp ONTAP

## AWS App Runner

* Fully managed service that makes it easy to deploy web applications and APIs at scales
* No infrastructure experience required
* Start with your source code or container image
* Automatic scaling, highly available, load balancer, encryption
* VPC access support
* Connect to databasem cache, and message queue services
* Use cases
  * web apps
  * APIs
  * microservices
  * rapid production deployments

## AWS App2Container

* Command-line tool for modernizing .NET and Java applications into containerized applications
* Lift-and-shift your apps running in on-premises bare metal, virtual machines, or in any Cloud to AWS
* Generate CloudFormation templates
* Register generated Docker containers to ECR
* Deploy to ECS, EKS, or App Runner
* Supports pre-built CI/CD pipelines
