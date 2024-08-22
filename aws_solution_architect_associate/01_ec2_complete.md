# EC2 complete

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
    * IP
    * Securty rules: security group

* Bootstraping is possible:
    * Automate boot tasks using scripts as root user

* EC2 instance types:
    * General purpose:
        * The common Ec2 instance
    * Compute optimized:
        * Batch processing workloads
        * Media transcoding
        * Scientific modeling and machine learning
        * Dedicated gaming services
    * Memory optimized:
        * Large datasets in memory
        * RDB
        * BI 
    * Accelera0te optimized
        * Graphics
        * Floating point number
    * Storage optimized
        * OLTP
        * Datawarehouse
    * HPC

* Security:
    * Security groups
        * Access to ports
        * Control inbound and outbound rules
        * Locked down to a region/VPC combination

* Classic ports:
    * 21 FTP
    * 22 SSH
    * 22 SFTP
    * 80 HTTP
    * 433 HTPS
    * 3389 RDP
    
* Connect using SSH:
    * ssh -i "*.pem" ec2-user@.us-west-2.compute.amazonaws.com

* Instance purchasing options:
    * On demand:
        * Pay-as-you-go
    * Reserved Instances
        * Convertible reserved instances
    * Saving Plans
        * Commitment to an amount of usage
        * Locked for specific instance family
    * Spot Instances
        * Can lse instances
    * Dedicated Instance
        * Hardware for you
    * Dedicated host
        * A complete physical server for you
    * Capacity reservation:
        * Reserve by AZ for any duration

* Spot instances and Spot Fleet
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