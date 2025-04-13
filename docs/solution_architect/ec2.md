# Elastic Compute Cloud (EC2)

## EC2 Fundamentals

* A good first step is to create a budget on billing console
* EC2 is infrastructure as a services
* Some capabilities:
    * Renting virtual machines (EC2)
    * Storing data on virtual drives (EBS-EFS)
    * Distributing load across machines (ELB)
    * Scaling the services using an auto-scaling group (ASG)
* Configuration options:
    * Operating system
    * Compute power an cores
    * Random Access Memory
    * Storage space
        * Always review delete on terminate
    * Network card
    * Firewall rules
    * Bootstrap script
        * Installing updates
        * Installing software
        * Downloading common files
* Instance types example:
    * micro 1vCPU 
    * xlarge 4vCPU
    * 4xlarge 16vCPU
    * 8xlarge 32vCPU
    * 16xlarge 64vCPU

Bootstrap example 

```bash
#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello world from $(hostname -f)</h1>" > /var/www/html/index.html
```

* Command to connect locally:
    * `chmod 400 ".pem"`
    * `ssh -i ".pem" ec2-user@*.compute-1.amazonaws.com`

### EC2 instance types

* Naming convention:
    * m5.2xlarge
        * m: instance class
        * 5: generation
        * 2xlarge: size within the instance class

* Types
    * General purpose
        * Great for a diversity of workloads
    * Compute optimized
        * Great for compute-intensitive tasks
            * Batch processing workloads
            * Media transcoding
            * High performance web servers
            * Scientific modeling and machine learning
            * Dedicated gaming servers
    * Memory optimized
        * Fast performance for workloads that process large data sets in memory
            * High performance relational/non-relational databases
            * Distributed web scale cache stores
            * In-memory databases optimized for BI
            * Applications performing real-time processing of big unstructured data
    * Accelerated computing
    * Storage Optimized
        * Great for storage-intensive tasks that require high, sequential read and write access to large data sets on local storage
            * High frequency Online Transaction Processing systems (OLTP)
            * Relational and NoSQL databases
            * Cache for in-memory databases (for example, Redis)
            * Data Warehousing applications
            * Distributed file systems
    * HPC optimized

* Security groups:
    * They control how traffic is allowed into or out of oue EC2 Instances
    * Only contain allow rules
    * Can reference by IP or by Security Group
    * Is like a firewall
    * Locked down to a region/VPC combination
    * Problems:
        * Time out: maybe is a security group issue
        * Connection refused: maybe it is an application error or it is not launched
    * Traffic:
        * All inbound traffic is blocked by default
        * All outbound traffic is allowed by default
    * Referencing other security Groups:
        * EC2 instances with the same security group can change information
    * They structure is:
        * Type
            * FTP: 21
            * SSH: 22
            * SFTP: 22
            * HTTP: 80
            * HTTPS: 443
            * RDP: 3389 (Remote Desktop Protocol)
        * Protocol
        * Port Range
        * Source
        * Description

## EC2 Solution Architect Associate Level

## EC2 Instance Storage