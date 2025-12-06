# Networking - VPC

This document provides an overview of Virtual Private Cloud (VPC) networking concepts and best practices for designing and implementing VPCs in AWS. 

## CIDR - IPv4

* Classless Inter-Domain Routing - a method for allocating IP addresses
* Used in Security Groups rules and AWS networking in general
* Base IP
    * Represents an IP contained in the range:
        * XX.XX.XX.XX
* Subnet Mask
    * Defines how many bits can change in the IP
    * Represented as /XX: /0, /24, /32
    * Example:
        * /8 -> 255.0.0.0
        * /16 -> 255.255.0.0
        * /24 -> 255.255.255.0
        * /32 -> 255.255.255.255
* Public vs Private IP (IPv4)
    * Private IP:
        * 10.0.0.0 - 10.255.255.255 (10.0.0.0/8)
        * 172.16.0.0 - 172.31.255.255 (172.12.0.0/12)
        * 192.168.0.0 - 192.168.255.255 (192.168.0.0/16)
    * Public IP:
        * The rest of IPs

## Public vs Private IP (IPv4)

* The Internet Assigned Numbers Authoriry (IANA) established certain blocks of IPv4 for the use of private (LAN) and public (Internet) addresses
* Private IP:
    * 10.0.0.0/8 --> 10.255.255.255
    * 172.16.0.0/12 --> 172.31.255.255
    * 196.168.0.0/16 --> 196.168.255.255
* Public IP:
    The rest of the IPs
* All new AWS accounts have a a default VPC
* EC2 are launched into the default VPC with public access
* You can create your own VPCs with custom CIDR blocks
* 5 AWS VPC per region (soft-limit)
* Each VPC can have up to 200 subnets (soft-limit)
* Each subnet must reside entirely within one AZ
* Subnets can be public or private
* VPC min size: /28 -> 16 IPs
* VPC max size: /16 -> 65536 IPs
* AWS reserves 5 IPs per subnet:
    * 10.0.0.0 -> Network address
    * 10.0.0.1 -> VPC Router
    * 10.0.0.2 -> DNS Server
    * 10.0.0.3 -> Future use
    * 10.0.0.255 -> Broadcast address

* Exam tip: if you nee 29 IP addresses for EC2 instances:
    * You can not choose a subnet /27 (32 IP addresses, 32 -5 = 27 < 29)
    * You can choose /26 (64 IP addresses, 64 -5 = 59 > 29)

## Internet Gateway (IGW)

* Allows resources in a VPC connect to the internet
* It scales horizontally and is highly available and redundant
* Must be created separatly from a VPC
* One VPC can only be attached to one IGW and viceversa
* Internet Gateways on their own do not allow internet access
* Route tables must also be edited
    * You should check the subnets route tables
    * You should add the Internet Gateway to the Subnet Route Table
* Subnets can manage the auto assign IPv4 operations

## Bastion Host

* We can use a Bastion Host to SSH into our private EC2 instance
* A Bastion Host is a special purpose instance that sits in a public subnet
* It is used to securely connect to instances in a private subnet
* The Bastion Host must have a security group that allows SSH access from the internet
* The private instance must have a security group that allows SSH access from the Bastion Host security

## NAT Instance

* Network Address Translation
* Used to allow instances in a private subnet to access the internet
* It is an EC2 instance configured to forward traffic to the internet
* It must be launched in a public subnet with a security group that allows inbound traffic from the internet
* Must disable EC2 setting: Source/destination Check
* Route Tables must be configured to route traffic from private subnets to the NAT Instance
* Comments:
    * Pre-configured Amazon Linux AMI is available
    * Not Highly available/resilient setup out of the box
        * You need to create an ASG in multi-AZ + resilient user-data script
    * Internet traffic bandwith depends on EC2 instance type
    * You must manage Security Groups and rules

## NAT Gateway