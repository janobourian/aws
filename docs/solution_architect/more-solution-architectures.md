# More Solution Architectures

## Event Processing

* SQS + Lambda + SNS
* SQS:
  * DLQ
  * SQS FIFO + Lambda
* Fan Out Pattern:
  * SDK + SNS + SQS
* Remember Amazon EventBridge

## Caching strategies

* ElastiCache (Redis/Memcached)
* CloudFront

## Blocking an IP Address in AWS

* Use Network Access Control List
* AWS WAF

## High Performance Computing

* AWS Direct Connect
* Snowball and Snowmobile
* AWS DataSync
* EC2 Instances
* EC2 Placement Groups
* EC2 Enhanced Networking
* Elastic Fabric Adapter
* EBS
* Instance Store
* EFS
* S3

## EC2 Instance High Availability

* ELB
* Elastic IP
* EC2
* Auto-scalig Group
* Multi-AZ
