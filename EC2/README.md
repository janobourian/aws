# Amazon EC2 Basics

EC2: Elastic Compute Cloud and is Infrastructure as a Service.

## Launching an EC2 Running Linux

Terminology:
* Renting virtual machines (EC2)
* Storing data on virtual drives (EBS)
* Distributing load across machines (ELB)
* Scaling the services using an auto-scaling group (ASG)

Launching EC2 Instance:
* Launch an instance
    * Name and tags
    * Application and OS Images
    * Instances type
    * Key pair
    * Network settings
        * Create VPC
        * Create Subnet
    * Configure storage
    * Advanced details

## Access our Instance Via the Web and Adding new SG Rules

First you need to remove the "s" in "https" url and you need to modify the security group.

## SSH into EC2 Instance

```bash
ssh -i "*.pem" ec2-user@Public-IPv4-DNS
```

## Security group

## Public vs Private IP

## EC2 User Data - Overview

## EC2 Pricing