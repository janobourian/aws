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
    
