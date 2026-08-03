# AWS Storage

* S3 < EBS < EFS

## EBS | Elastic Block Storage

* It usually works with EC2 instances
* Data is organized in blocks
* Must be attached to EC2
* Use cases:
    * Low latency access to data
    * Boot/Data volumes for EC2
    * Relations and NoSQL Database storage
    * Data Warehouse ETL
    * SAP ERP, Oracle ERP, Microsoft Share Point, MySQL, MongoDB

## S3 | Simple Storage Service

* Share to the internet
* Bucket or container
* Object storage - Flat structure
* API access to data (HTTP/HTTPS)
* Metadata driven (Attributes, Policy)
* Use cases:
    * Unlimited space
    * Media and enternainment
    * Log files
    * Backups and archives
    * Content Management
    * Version Control System

## EFS | Elastic File System

* Between multiple instances
* Shared file system - Hierarchical structure
* Comes with serving File System
* Should be mounted on EC2 or on-premises services
* Use cases:
    * Shared access to files
    * Web Serving
    * Big Data and Analytics
    * Users Home Directory
    * Content Management
    * Container Storage