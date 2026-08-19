# Elastic Compute Cloud (EC2)

* First of all you need to set the billing section for not-root users:
* Activate the budget
* You can buy the next computing resources:
  * CPU
  * Memory
  * Storage
  * Network

## EC2 Fundamentals

* A good first step is to create a budget on billing console
* Elastic Compute Cloud
* EC2 is infrastructure as a services
* Some capabilities:
  * Renting virtual machines (EC2)
  * Storing data on virtual drives (EBS-EFS)
  * Distributing load across machines (ELB)
  * Scaling the services using an auto-scaling group (ASG)
* Configuration options:
  * Operating system (OS)
  * Compute power an cores (CPU)
  * Random Access Memory (RAM)
  * Storage space (EBS or EFS)
    * Always review delete on terminate
  * Network card
  * Firewall rules
    * Security Group
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
## Use this for your user data (script from top to bottom)
## install httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello world from $(hostname -f)</h1>" > /var/www/html/index.html
```

For Amazon Linux 2023

```bash
#!/bin/bash
sudo dnf update -y
sudo dnf install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
echo "<h1>Hello world from $(hostname -f)</h1>" > /var/www/html/index.html
```

* Stop instance
* Start instance
* Hibernate instance
* Terminate instance

* Command to connect locally:
  * `chmod 400 ".pem"`
  * `ssh -i "*.pem" ec2-user@*.compute-1.amazonaws.com`

### EC2 instance types

* Naming convention:
  * m5.2xlarge
    * m: instance class
    * 5: generation
    * 2xlarge: size within the instance class

* Types
  * General purpose
    * Great for a diversity of workloads
    * Good balance between:
      * Compute
      * Memory
      * Networking
  * Compute optimized
    * Great for compute-intensitive tasks
      * Batch processing workloads
      * Media transcoding
      * High performance web servers
      * High performance computing
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
    * Gamming

* If you need to check some instance costs: <https://instances.vantage.sh/>

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

* You can connect with your EC2 instance using EC2 Instance Connect
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

## Optimize EC2 Costs

* Avoid overprovisioning
* Terminate unused instances
* Implement Auto Scaling
* Monitor with Cost Explorer
* Diversify pricing models

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
  * NAT Gateway only accepts outbound traffic and responses from the internet (inbound traffic)
* Elastic IP
  * When you stop and then start an EC2 instance, it can change its public IP
  * If you need to have a fixed public IP for your instance, you need an Elastic IP
  * Five Elastic IP in your account

* Public IP address
  * Public Subnets
  * Lost when the instance is stopped
  * Associated qith a private IP address on the instance
  * Cannot be moved between instances
* Private IP address
  * Retained when the instance is stopped
  * Used in Public and Private subnets
* Elastic IP address
  * Static Public IP address
  * You are charged if not used
  * Associated with a private IP address on the instance
  * Can be moved between instances and Elastic Network Adapters

### EC2 Placement Groups

* How your EC2 instances will be placed acording with your needs
* Strategies
  * Cluster
    * Need for speed
    * The instances are together to reduce the latency
    * Financial applications.
    * All instances are in the same AZ
    * Pros:
      * Great network
    * Cons:
      * If the AZ fails, all instances fails at the same time
    * Use case:
      * Big Data
      * Application that needs extremly low latency
  * Spread
    * Safety First
    * Minimize the risk
    * Every Instance is in different hardware
    * Pros:
      * Can span across AZ
    * Cons:
      * Limited to 7 instances per AZ per placement group
    * Use case:
      * Application that needs to maximize high availability
      * Critical Applications where each must be isolated from failure from each other
  * Partition
    * Isolation at Scale
    * Partition per AZ
    * Each partition is isolated from failure
    * You are using the same AZ but every partitions is in different rack in the same datacenter

### Elastic Network Interfaces

* Logical component in a VPC that represents a virtual network card
* It has the following attributes:
  * Primary IPv4, one or more secondary IPv4
  * One Elastic IP per private IPv4
  * One Public IPv4
  * One or more security groups
  * A Mac address
  * Bound for AZ

### EC2 Hibernate

* Steps
  * Start
  * Stop
  * Terminate
  * Hibernate:
    * RAM state is preserved
    * The instance boot is much faster
    * RAM state is written to a file in the root EBS volume
    * The root EBS volume must be encrypted
    * Instance RAM size must be less than 150GB
    * Not supported for bare metal instances
    * An instance can not be hibernated more than 60 days

## EC2 Instance Storage

### EBS

* You can increase or decrease the memory in EBS

* Elastic Block Store Volume
  * Network drive you can attach to your instances while they run
  * Bound to a specific availability zone
  * Like network USB stick
  * To move a volume across, you first need to snapshot it
  * Have a provisioned capacity
  * Delete on termination (root is deleted by default)

* EBS Snapshots
  * It uses incremental memory
    * 10GB + 2GB = 12GB instead of two copies.
  * Make a backup of your EBS volume at a point in time
  * Can copy snapshots across AZ or Region
  * EBS Snapshot to EBS Snapshot Archive
  * EBS Snapshot to Recycle Bin
  * Fast Snapshot Restore

* IOPS
  * Input Output Per Second
  * Read / Write operations a storage device can perform per second
* Throughput
  * How amount of data can be moved through the devices
* Latency
  * Time delay between request of data and response data

* EBS Volumes
  * General Purpose:
    * gp2/gp3 (SSD)
  * Fast and consistent for crititcal applications:
    * io1/io2 Block Express (SSD)
  * For big data, move fast most access
    * st 1 (HDD)
  * Standard cold, keep the information
    * Archival data, backups
    * sc 1 (HDD)
  * EBS Volumes are characterized in Size, Throughput, IOPS

* Multi Attach:
  * In te same AZ
  * Across multiple EC2
  * Only for io1 and io2
  * Read and write permissions for high-performance volume
  * To manage concurrent write operations
  * Up to 16 EC2 Instances at a time

* Encryption
  * You have nothing to do
  * Data at rest, in flight, snapshots, and all volumes created from the snapshot

### AMI

* Amazon Machine Image
* AMI are a customization of an EC2 Instance
* AMI are built for a specific region and can be copied across regions
* Two ways of creating an AMI
  * AMI from EC2 instance
  * AMI from EBS Snapshot

### EC2 Instance Store

* If you need a high-performance hardware disk, use EC2 Instance Store
* Better I/O performance
* EC2 Instance store lose their storage if the are stopped
* Good for buffer, cache, scratch data, temporary content

### EFS

* Highly available, scalable, expensive (3x gp2), pay per use
* EFS works with EC2 instances in multi-AZ
* Use cases:
  * Content management
  * Web serving
  * Data sharing
  * Wordpress
* Uses NFSv4.1
* Use security Group
* Compatible with Linux, not Windows
* It uses POSIX file system
* EFS scale
* Performance Mode
  * General Purpose
  * Max I/O
  * Throughput Mode
    * Bursting - 1 TB
    * Provisioned
    * Elastic
* Storage Classes
  * Storage Tiers
    * Standard
    * Infrequent Access
    * Archive
  * You can implement Lifecycle policies
* Availability and durability
  * Standard: Multi-AZ
  * One Zone: EFS One Zone-IA

### EFS vs EBS

* EBS
  * one instance
  * Locked by AZ
  * To migrate
    * Take a Snapshot
  * Deletion on terminate should be configured
* EFS
  * Across AZ
  * Multi instance
  * EFS Mount Target
  * Storage Tiers

## High Availability and Scalability: ELB and ASG

* Vertical Scalability
  * scale up - scale down
  * Non distributed Systems such as a database
  * It has a limite
* Horizontal Scalability (= elasticity)
  * scale out - scale in
  * Auto Scaling Group
  * Load Balancer
  * Distributed systems
  * web applications / modern applications
* High Availability
  * Multi AZ
  * Meas running your application in at least 2 data centers
  * The goal is to survive a data center loss
  * Passive: For RDS Multi AZ
  * Actice: For Horizontal scaling

### ELB - Elastic Load Balancer

* Load Balanacers are servers that forward traffic to multiple servers downstream
* Use cases:
  * Spread load across multiple downstream instances
  * Expose a single point of access (DNS) to your application
  * Seamlessly handle failures of downstream instances
  * Do regular health checks to your instances
  * Provide SSL termination for your websites
  * Enforce stickiness with cookies
  * High availability across zones
  * Separate public traffic from private traffic

* Types
  * Classic Load Balancer
  * Application load Balancer
    * HTTP, HTTPS, WebSocket
  * Network Load Balancer
    * TCP, TLS, UDP
  * Gateway Load Balancer
    * GWLB

* Security
  * Load Balancer Security Group
  * Application Security Group (allow traffic only from Load Balancer)

### ASG
