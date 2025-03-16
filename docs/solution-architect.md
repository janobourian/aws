# Solution Architect SAA-C03

## Getting Started with AWS

* AWS Cloud History
    * 2004 With SQS
    * Relaunch with SQS, S3, and EC2

* Use cases:
    * Enterprise IT, Backup and Storage, Big Data Analytics
    * Website hosting, Mobile and Social apps
    * Gaming

* AWS Global Insfrastructure
    * AWS Regions
        * A cluster of data centers
    * AWS Availability Zones
    * AWS Data Centers
    * AWS Edge Locations / Points of presence
        * Delivery services with ultra low latency

* How can I choose an AWS Region?
    * Compliance
    * Latency / Proximity
    * Service Availability
    * Price

* AWS Global Services:
    * Identity and Access Manager (IAM)
    * Route53
    * ClouFront
    * AWS WAF

* Check the Global Infrastructure
    * https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/



## Identity and Access Management and AWS CLI

* Basic concepts
    * Root account
    * Users
    * Groups
    * Roles
    * IAM: Permissions
        * Users or Groups can be assigned JSON documents called policies
        * These policies define the permissions of the users
        * least privilege principle
        * VIS - SEPARC
            * VIS
                * Version
                * Id
                * Statement
            * SEPARC
                * Sid
                * Effect
                * Principal
                * Action 
                * Resource
                * Condition

## Identity and Access Management (IAM) - Advanced