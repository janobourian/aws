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

* You need to configure IAM role

### EC2 Instance Purchasing Options

* On-Demand Instances
    * Linux or Windows - billing per second, after the first minute
    * All other operating systems - billing per hour
* Reserved
    * Reserved Instances
        * You reserve a specific instance attributes:
            * Instance Type
            * Region
            * Tenancy
            * OS
        * You can buy and sell in the Reserved Instance Marketplace
    * Convertible Reserved Instances
        * Can change the EC2:
            * instance type
            * instance family
            * OS
            * scope
            * tenancy
* Saving Plans: commitment to an amount of usage, long workload
    * Commit to a certain type of usage ($10/hour for 1 or 3 years)
    * Locked to a specific instance family and AWS region
    * After your commit start On-Demand pricing
    * Flexible across:
        * Instance size
        * OS
        * Tenancy
* Spot Instances
    * You can lose at any point of time
    * Useful for workloads that are resilient to failure
* Dedicated Hosts
    * A physical server fully dedicated to your use
    * Useful for software that have complicated licensing model (BYOL - Bring Your Own License)
    * Or for companies that have strong regulatory or compliance needs
    * Purchasing Options:
        * On-demand
        * Reserved
* Dedicated Instances
    * Instance run on hardware that is dedicated to you
    * May share hardware with other instances in same account
* Capacity Reservations
    * Reserve On-Demand isntances capacity in a specific AZ for any duration

### IP address charges in AWS

* Public IPv4 created in your account
    * $0.005 per hour (~$3.6 month)
* The trick is to start to migrate to IPv6
* VPC IP Address Manager (VPC IPAM) to manage public IPs

### Spot Instances and Spot Fleet

#### EC2 Spot Instance Request

* Define max spot price and ge the instance while current spot price < max
* Your instance will have two minutes grace period
* Used for batch jobs, data analysis, or workloads that are resilient to failures
* Not great for critical jobs or databases
* Spot block is no longer available
* Spot Request
    * Create request
        * Maximum price
        * Desired number of instances
        * Launch specifications 
        * Request type
        * Valid from
        * Valid until
    * One time
        * It will be terminated after the request
    * Persistent
        * Stop -> Start
        * Interrumpt
        * Cancel (terminate) only in the next status
            * Open
            * Active
            * Disabled

#### EC2 Spot Fleets

* Spot Fleets = set of Spot Instances + (optional) On-Demand Instances
* Strategies to allocate Spot Instances
    * lowestPrice
    * diversified: distributed across all pools
    * capacityOptimized
    * priceCapacityOptimized (recommended): highest capacity available, then select the pool with the lowest price

## EC2 Solution Architect Associate Level

### Private vs Public vs Elastic IP

* IPv4 and IPv6
* Internet Gateway (public)
    * Private Network
* Machines in Private Network can connect to internet using NatGateway
* Elastic IP
    * When you stop and then start an EC2 instance, it can change its public IP
    * If you need to have a fixed public IP for your instance, you need an Elastic IP
    * Five Elastic IP in your account


### EC2 Placement Groups

### Elastic Network Interfaces

### EC2 Hibernate

## EC2 Instance Storage