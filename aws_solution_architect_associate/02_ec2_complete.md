# Elastic Compute Cloud (EC2) complete

## Create a Budget

* First, as a root user, you should allow the permission to `IAM user and role access to Billing information`
    * root account > Account > Billing and Payments
* To create budget
    * Billing and Cost Managment > Budget 

## About EC2

* Elastic Compute Cloud (IaaS):
    * Renting virtual machines (EC2)
    * Storing data on virtual drives (EBS)
    * Distributing load across machines (ELB)
    * Scaling the services using an auto-scaling groups (ASG)

* Operating System:
    * Linux
    * Windows
    * MacOS

* How much:
    * CPU
    * RAM
    * Storage:
        * EBS and EFS
        * EC2 Instance Store
    * Network Card: Public IP
    * Securty rules: security group

* Bootstraping is possible:
    * That scripts is only run once at the instance first start
    * Automate boot tasks using scripts as root user
    * Task such as:
        * Installing updates
        * Installing software
        * Downloading common files from the internet
        * Anything you can think of

## Hands On

* Bootstrap

```bash
#!/bin/bash
# Use this for your user data (script from to to bottom)
# install httpd (Linuz 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1> Hello from $(hostname -f)</h1>" > /var/www/html/index.html
```

* Size:
    * small -> 0.5gb
    * medium -> 1gb
    * large -> 2gb
    * xlarge -> 4gb
    * 2xlarge -> 8gb

* Name convention:
    * m5.2xlarge
        * m: instance class
        * 5: generation
        * 2xlarge: size

* Key points
    * CPU
    * Memory
    * Networking

* EC2 instance types:
    * General purpose:
        * The common EC2 instance
    * Compute optimized:
        * Batch processing workloads
        * Media transcoding
        * Scientific modeling and machine learning
        * Dedicated gaming services
    * Memory optimized:
        * Large datasets in memory
        * RDB
        * BI 
    * Accelerate optimized
        * Graphics
        * Floating point number
    * Storage optimized
        * OLTP: OnLine Transaction Processing
            * OLAP: OnLine Analytics Processing
        * Datawarehouse
        * Relational and NoSQL Data bases
    * HPC

* To have a reference about the instances cost: https://instances.vantage.sh

* Security:
    * Security groups
        * Are like a firewall
        * Only allow rules based on IP adresses and other security group
        * Access to ports
        * Control inbound and outbound rules
        * Locked down to a region/VPC combination
        * Errors
            * Time out is a security group issue
            * Connection refuse is a deploy error
        * To reference another security groups is a good way to link EC2 instances or services

* Classic ports:
    * 21 FTP -> File Transfer Protocol
    * 22 SSH -> Secure Shell
    * 22 SFTP
    * 80 HTTP -> Hyper Text Transfer Protocol
    * 433 HTPS
    * 3389 RDP -> Remote Deskto Protocol
    
* Connect using SSH:
    * chmod 400 *.pem
    * ssh -i "*.pem" ec2-user@.us-west-2.compute.amazonaws.com

* Roles on EC2 instance:
    * Do not use ACCESS KEYS into EC2 instances
    * Roles help us to communicate AWS services

* Types 
    * Pay-as-you-go
    * 1 year
    * 3 years
    * You can buy or sell them in the Reserved Instance Marketplace

* Instance purchasing options:
    * On demand:
        * Pay-as-you-go
        * Linux and windows - billing per second, but after first minute
        * Other OS - billing per hour
        * No upfront
    * Reserved Instances
        * You reserve a specific instance attributes
            * Instance Type, Region, Tenancy and OS
        * Convertible reserved instances
            * Change the instance type, instance family, OS, scope, and Tenancy
    * Saving Plans
        * Commitment to an amount of usage
        * Locked for specific instance family and Region
        * Beyond the reservation you will pay as On-demand
        * Flexible across:
            * Instance Size
            * OS
            * Tenancy
    * Spot Instances
        * Can lose instances
    * Dedicated host
        * A complete physical server for you
        * Purchasing Options:
            * On-demand
            * Resever
            * BYOL: Bring Your Own License
        * BYOL - Bring Your Own License
    * Dedicated Instance
        * Hardware for you
    * Capacity reservation:
        * Reserve by AZ for any duration

* AWS Charges for IPv4 addresses

* Spot instances and Spot Fleet
    * Two minutes grace period
    * Define a max spot price
    * Spot Block*
    * Request type: one-time | persistent
    * Finish them: Cancel request > Terminate
    * Spot fleets = Spot Instances + On-Demand Instances
        * lowestPrice
        * diversified
        * capacityOptimized
        * priceCapacityOptimized

* Shared responsability model for EC2:
    * AWS
        * Infrastructure
        * Isolation
        * Replacing faulty hardware
        * Compliance validation
    * EC2
        * Security groups rules
        * Operating-system patches and updates
        * Software and utilities installed
        * IAM 
        * Data security on your instance

## EC2 for solution Architect

* Type of IPs:
    * IPv4
    * IPv6

* Public IP -> Internet Gateway -> Private IP (inside private network)

* Public:
    * To be identified on the internet
* Private
    * In a local network
    * They need to use NAT Gateway + Internet Gateway to connect to the internet
* Elastic IP
    * Is to have a fixed public IP on EC2
    * Five for account

## Placement Groups

* Control over how the EC2 instances placement
* Strategies:
    * Cluster: Cluster instances into a low-latency group in a Single AZ
        * 10 Gps of bandwith
        * Big data jobs
        * App that needs low latency
    * Partition: spreads instances across many different partitions within an AZ. Scale to 100s of EC2 instances per group
        * Up to seven partitions by AZ
        * Multiple AZ
        * Each partition has a rack 
        * Use cases: Cassandra, Hadoop, Kafka
    * Spread: Spreads instances across underlying hardware (max 7 instances per group per AZ) - critical applications
        * Multiple AZ
        * Different hardware
        * Isolated the failure

## Elastic Network Interface

* Logical component in a VPC that represents a Virtual Network Card
* It can have a primary private IPv4 and one or more secondary IPv4
* One Elastic IP per private IPv4
* One public IPv4
* One or more security gruop
* Limited by AZ
* It is used for availability
* It help us in a failover
* Custom ENI does not go when the instance are deleted

## Hibernate

* Options
    * Stop
    * Terminate (EBS root volumen will be destoyed)
    * Hibernate:
        * RAM state is preserved
        * The instance boot is much faster
        * The root EBS volume must be encrypted
        * RAM size must be less than 150 GB
        * Root Volume must be EBS, encrypted, not instance store and large
        * Not suported for bare metal instances
        * Not be hibernated more than 60 days
        * Use cases:
            * Long-running processing
            * Saving the RAM state
            * Service take too long

# EC2 Instance Storage

* EBS Volume (Elastic Block Store),
    * network drive
    * to persist data and 
    * can be attached to multiple EC2 instances and 
    * be limited by AZ and 
    * is a network drive to more performance and
    * you need to create a copy to move to another AZ and
    * you can manage the behavior on delete or termination

* EBS Snapshot
    * Make a backup
    * Is not necessary to detach volume
    * Can copy EBS in several AZ
    * EBS Snapshots Features
        * EBS Snapshot Archive
        * Recycle Bin for EBS Snapshots
        * Fast Snapshot Restore
    * You can attach your EBS to other EBS

* EBS Volume Types:
    * gp2/gp3, general purpose SSD
        * Cost effective storage, low-latency
    * io1/io2
        * Critical business applications
        * database workloads
    * st1
        * Hard Disk Drives
        * Can not be a boot volume
    * sc1
        * COLD HDD
        * Hard Disk Drives
        * Can not be a boot volume

* EBS Multi-attach
    * Only io1/io2
    * Attach the same EBS volume to multiple EC2 instances in the same AZ
    * Use case: 
        * Higher Application Availability
        * Concurrent write operations
        * Up to 16 EC2 Instances at time

* EBS Encryption
    * It uses KMS

* AMI (Amazon Machine Image)
    * EC2 instance customization
    * For specific region
    * Launch
        * Public AMI
        * Your own AMI
        * An AWS Marketplace AMI
    * Process
        * Start an EC2 instance and customize it
        * Stop the instance
        * Build an AMI - this will also create EBS snapshot
        * Launch instances from other AMIs

* EC2 Instance Store
    * High performance
    * Hardware disk
    * Ephemeral storage
    * Use cases:
        * buffer
        * cache
        * scratch data
        * Temporary content

* EFS (Elastic File System)
    * Mounting 100s of instances accross AZ
    * multi-AZ
    * Expensive
    * Pay per use
    * Compatible with Linux
    * Security using security group
    * Performances:
        * EFS Scale
        * Performance Mode
            * General Purpose
            * MAX I/O
        * Throughput mode
            * Bursting
            * Provisioned
            * Elastic
    * Storage clases:
        * Standard
        * Infrequent Access
        * Archive
    * You can implemente lifecycle policies
    * Availability and durability
        * Standard
        * One zone
