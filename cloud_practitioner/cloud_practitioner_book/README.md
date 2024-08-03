# Cloud Practitioner Book

## 6 AWS Networking Services - VPCs, Route53, and CloudFront

* Key concepts:
    * CIDR: Classless Interdomain Routing

* Example:
    * VPC: 10.0.0.0/16
    * Subnet-1: 10.0.1.0/24
    * Subnet-2: 10.0.2.0/24

* Complex example (and most real):
    * VPC: 10.0.0.0/16 with its Internet Gateway
    * Availability Zone 1A:
        * Public Subnet 1: 10.0.1.0/24
        * Private Subnet 1: 10.0.2.0/24
    * Availability Zone 1B
        * Public Subnet 2: 10.0.3.0/24
        * Private Subnet 2: 10.0.4.0/24

* EC2:
    * In public subnet it will require a public IP address with a Load Balancer in front of it.
    * If you need a static IP address you need to configure your EC2 instance with a elastic IP address

* Security:
    * Security group:
        * Inbound and outbound rules
        * You can add up to five security groups
        * They are at instance level
        * They can accept itself traffic
        * They are stateless
        * You can allow rules, but can not deny rules
        * You can separate the rules by protocols (HTTP, HTTPS, SSH)