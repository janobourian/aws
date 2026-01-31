# Networking - VPC

This document provides an overview of Virtual Private Cloud (VPC) networking concepts and best practices for designing and implementing VPCs in AWS. 

## VPC Components 

* Internet Gateway: One by VPC, it allows to connect with the internet. 
* Transit Gateway: A way to avoid vpc peering hell, all conections in one place.
* VPC Peering Connections: Connect two vpc using a peering.
* VPN
* DX
* Route Table: The rules that a Subnet o VPC componet follows to communicate with others. 
* NACL: Stateless, do it have permission to start a communication?
* VPN Gateway
* VPC Endpoint
* VPC Flow Logs
* Direct Connect Connection
* Customer Gateway
* DX Location
* NAT Gateway: It has regional option, allow to connect private subnet with other resources. 
* NAT Instances: Like NAT Gateway but this is a EC2 Instance
* Bastion Host: Check the private resources using an EC2 instance in a public subnet.
* Security groups: Stateful, to check the permissions between components.

## CIDR - IPv4

* Classless Inter-Domain Routing - a method for allocating IP addresses
* Used in Security Groups rules and AWS networking in general
* Base IP
    * Represents an IP contained in the range:
        * XX.XX.XX.XX
* Subnet Mask
    * Defines how many bits can change in the IP
    * Represented as /XX: /0, /24, /32
    * Example (take 256.256.256.256 and take the value):
        * /8 -> 255.0.0.0
        * /9 -> 255.32.0.0
        * /16 -> 255.255.0.0
        * /21 -> 255.255.248.0
        * /22 -> 255.255.252.0
        * /23 -> 255.255.254.0
        * /24 -> 255.255.255.0
        * /32 -> 255.255.255.255
* Public vs Private IP (IPv4)
    * Private IP:
        * 10.0.0.0 - 10.255.255.255 (10.0.0.0/8)
        * 172.16.0.0 - 172.31.255.255 (172.12.0.0/12)
        * 192.168.0.0 - 192.168.255.255 (192.168.0.0/16)
    * Public IP:
        * The rest of IPs
* Examples:
    * 192.168.0.0/30 => 2^2 = 4. 192.168.0.0 - 192.168.0.3 => 255.255.255.251
    * 192.168.0.0/28 => 2^4 = 16. 192.168.0.0 - 192.168.0.15 => 255.255.255.240
    * 192.168.0.0/20 => 2^12 = 4096. 192.168.0.0 - 192.168.16.0 => 255.255.240.0
    * 172.16.0.0/12 => 2^20 = 1,048,576. 172.16.0.0 - 172.31.255.255 => 255.240.0.0

## Public vs Private IP (IPv4)

* The Internet Assigned Numbers Authoriry (IANA) established certain blocks of IPv4 for the use of private (LAN) and public (Internet) addresses
* Private IP:
    * 10.0.0.0/8 --> 10.255.255.255
    * 172.16.0.0/12 --> 172.31.255.255
    * /12 -> 255.240.0.0 -> 172.16.0.0 - 172.31.255.255 (sum all and substract one)
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
    * You can not choose a subnet /27 (32 IP addresses, 32 - 5 = 27 < 29)
    * You can choose /26 (64 IP addresses, 64 -  5 = 59 > 29)

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

![alt text](image-2.png)

## Bastion Host

* We can use a Bastion Host to SSH into our private EC2 instance
* A Bastion Host is a special purpose instance that sits in a public subnet
* It is used to securely connect to instances in a private subnet
* The Bastion Host must have a security group that allows SSH access from the internet
* The private instance must have a security group that allows SSH access from the Bastion Host security

![alt text](image-3.png)

## NAT Instance

* Network Address Translation
* Used to allow instances in a private subnet to access the internet
* It is an EC2 instance configured to forward traffic to the internet
* It must be launched in a public subnet with a security group that allows inbound traffic from the internet
* Must disable EC2 setting: Source/destination Check
* Route Tables must be configured to route traffic from private subnets to the NAT Instance
* Exist a preconfigured AMIs
* Comments:
    * Pre-configured Amazon Linux AMI is available
    * Not Highly available/resilient setup out of the box
        * You need to create an ASG in multi-AZ + resilient user-data script
    * Internet traffic bandwith depends on EC2 instance type
    * You must manage Security Groups and rules

![alt text](image-4.png)

![alt text](image-5.png)

## NAT Gateway

* AWS-managed NAT, higher bandwidth, high availability, no administration
* Pay per hour for usage and bandwith
* Must be created in a public subnet
* Must be associated with an Elastic IP
* Route Tables must be configured to route traffic from private subnets to the NAT Gateway
* Requires an IGW (Private Subnet => NATGW => IGW)
* 5 Gbps on bandwith with automatic scaling up to 100 Gbps
* Highly available within an AZ
* No Security Groups to manage / required
* Recommended over NAT Instances for most use cases
* There is no cross-AZ failover needed because if an AZ goes down it does not need NAT

![alt text](image-6.png)

## Security Groups and NACLs

* Security Groups
    * Act as virtual firewalls for EC2 instances
    * Operate at the instance level
    * Stateful: return traffic is automatically allowed, no need to create rules
    * Allow rules only (no deny rules)
    * Can be associated with multiple instances
    * Can have multiple security groups associated with a single instance

* Network Access Control Lists (NACLs):
    * NACLs are stateless
    * Operate at the subnet level
    * Allow and deny rules
    * Can be associated with multiple subnets
    * Each subnet must be associated with a NACL, if none is specified the default NACL
    * Default NACL allows all inbound and outbound traffic

* Stateful in this context: Allowed traffic
* Stateless in this context: Always evaluate the traffic

![alt text](image-7.png)

* NACLs
    * Are like a firewall which control traffic from and to subnets
    * One NACL per subnet, new subnets are ssigned the Default NACL
    * You define NACL Rules
        * #100 ALLOW
        * "*" <- to deny traffic that does not match
    * NACL are a great way of blocking a specific IP address at the subnet level
    * Do not modify the Default NACL, instead create custom NACL

![alt text](image-8.png)

* Ephemeral Ports
    * For any two endpoints to establich a connection, they must use port
    * Cliente connect to a defined port, and expect a response on an ephemeral port
    * Ephemeral ports are temporary ports assigned for the duration of a communication session

![alt text](image-10.png)

![alt text](image-9.png)

![alt text](image-11.png)

* Differences between Security Groups and NACLs:
    * SGs are stateful because they allow the outside communication
    * NACLs are stateless because they review the acess control list in every request
    * SGa at instance leves vs NACLs at subnet level
    * SGs allow only allow rules vs NACLs allow allow and deny rules
    * SGs are associated with multiple instances vs NACLs are associated with multiple subnets
    * Default SG allows all inbound and outbound traffic vs Default NACL allows all inbound and outbound traffic

## VPC Peering

* Networking connection between two VPCs
* Can be within the same AWS account or different AWS accounts
* VPCs can be in different regions (Inter-Region VPC Peering)
* VPC Peering connection is not trantitive
* No single point of failure or bandwidth bottleneck
* Traffic between peered VPCs stays on the global AWS backbone
* You must update route tables in each VPC to enable routing of traffic between them
* You can not have overlapping CIDR blocks between peered VPCs
* There are no bandwidth limitations
* There are no additional hops, low latency connection
* There is no need for a gateway, VPN connection, or separate physical hardware
* Peered VPCs can communicate using private IP addresses
* You can peer VPCs across different AWS accounts

### VPC Peering Hands On

* Create two VPCs with non-overlapping CIDR blocks
* Crete the vpc peering
* Update route tables in both VPCs to enable routing between them
* Test the connectivity between instances in both VPCs using private IP addresses

![alt text](image-12.png)

## VPC Endpoints

* To work with aws services.
* Every AWS service is publicly exposed
* VPC Endpoints allows you to connect to AWS services using a private network.
* Two types of VPC Endpoints:
    * Interface Endpoints: Use AWS PrivateLink to connect to services using ENIs
    * Gateway Endpoints: Use route tables to connect to services like S3 and DynamoDB

### Interface Endpoints (powered by PrivateLink)

* Use AWS PrivateLink to connect to services using ENIs
* Create an elastic network interface (ENI) in your subnet
* Assign private IP addresses from your VPC to the ENI
* Use security groups to control access to the endpoint
* Supports connections to AWS services, third-party services, and your own services
* $ per hour + $ per GB of data processed

### Gateway Endpoints

* Use route tables to connect to services like S3 and DynamoDB
* Create a gateway endpoint for the service 
* Update route tables to direct traffic to the endpoint
* No additional cost for using gateway endpoints
* Supports both S3 and DynamoDB
* Free

Note: Intreface Endpoint for S3 is preferred when you require access from your on premises (Site to Site VPN or Direct Connect), a different VPC or a different region.

## Transit Gateway

* Benefits:
    * Like a Hub of connections
    * Unique service with broadcast properties
    * Increase the throughput using ECMP
* Network transit hub that can connect multiple VPCs and on-premises networks
* Simplifies network architecture by consolidating connections
* Supports inter-region peering
* Scales elastically based on network traffic
* Supports multicast traffic
* Centralized management of network connections
* Supports integration with AWS Direct Connect and VPN connections
* Pay-as-you-go pricing model based on data processed and attachments
* ECMP = Equal-cost multi-path