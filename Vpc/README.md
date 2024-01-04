# VPC and Networking using AWS

# General Information

[Slides and Extra Information](https://digitalcloud.training/aws-networking-masterclass-course-downloads/)

# Previous configuration to start to work with the project

We have the "Services Quotas" as a service to measure the quantity of instances or something like that in our available services (and so on, but I'm gonna check it with our AWS manager)

# Billing preferences

- Alert preferences: 
    * Billing and cost Management > Billing preferences > Alert preferences
- Simple notification service: 
    * Amazon SNS > Topics > Create topic 
    * (Inside the last topic) Subscriptions > Insert information
- CloudWatch:
    * CloudWatch > Alarms > Create alarms

# EC2 ssh key-pair.

SSH key-pair is by Region. 

To generate Key pair
- EC2 > Network & Security > Key Pairs > Create key pair

Putty and putty gen steps
- Download putty and puttygen
- open puttygen and load our .pem credentials

Create EC2 instance
- EC2 > Instances > Launch instances

Connect EC2 using putty
- Open putty.exe
- Configure HostName (or IP address)
- Connection > SSH > Auth > Credentials (file the .ppk file) > Open
- login as: ec2-user

# Buy a public domain and configure DNS

- Using the respective DNS provider
- DNS -> Amazon Route 53 -> Instance, CloudFront, LoadBalancer
- Amazon Route 53 > Hosted zones > Create hosted zone > 

# Simple automation to track unattended AWS usage

- Describe EC2 instances, Describe Get EBS Volumes, Describe EIPs. <- Lambda -> Simple Email Service -> User Inbox
- EventBridge for triggers 
- AWS Cloud Formation 

# AWS VPC & Networking Fundamentals

## Overview (The Big Picture)

Communication: User -> Internet -> Region -> Internet Gateway -> VPC -> Main Route Table -> Local Router -> Availability Zones -> Public Subnet -> EC2 Instance

### The common case

![Alt text](img/image.png)

### Using EC2 Instances

![Alt text](img/image-2.png)

### Using a database

![Alt text](img/image-3.png)

### Using a database replication

![Alt text](img/image-4.png)

### Communicated out of the application

![Alt text](img/image-5.png)

### Regional services (Don't use NAT Gateway in those cases)

#### VPC Endpoint (gateway)

![Alt text](img/image-6.png)

#### VPC Endpoint (interface) + Private Link

![Alt text](img/image-7.png)

#### Service VPC

![Alt text](img/image-8.png)

### Peering connection

![Alt text](img/image-9.png)

### Transit Gateway

![Alt text](img/image-10.png)

### On Premises

![Alt text](img/image-11.png)

### Direct connect

![Alt text](img/image-12.png)

### Client VPN

![Alt text](img/image-13.png)

