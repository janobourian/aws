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
