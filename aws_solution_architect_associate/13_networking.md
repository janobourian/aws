# Virtual Private Cloud (VPC)

## CIDR - IPv4

* CIDR: Classless Inter-Domain Routing 
    * a method for allocating IP addresses
    * Components
        * Base IP
        * Subnet Mask
            * /8 -> 255.0.0.0
            * /16 -> 255.255.0.0
            * /24 -> 255.255.255.0
            * /32 -> 255.255.255.255
            * example:
                * /32 -> 2^(32-32) = 1 -> 192.168.0.0
                * /31 -> 2^(32-31) = 2 -> 192.168.0.0 - 192.168.0.1
                * /30 -> 2^(32-30) = 4
                * /29 -> 2^(32-29) = 8
                * /26 -> 2^(32-26) = 64 -> 192.168.0.0 - 192.168.0.63
                * /24 -> 2^(32-24) = 256 -> 192.168.0.0 - 192.168.0.255
    * example:
        * 192.168.0.0/26 -> 192.168.0.0 - 192.168.0.63
        * 10.1.0.0/16 -> 2^(32-16) = 65536 -> 10.1.0.0 - 10.1.255.255

* Private IPv4
    * 10.0.0.0/8 <- in big networks
    * 172.16.0.0/12 <- AWS default VPC in that range
    * 192.168.0.0/16 <- home networks

* Public IPv4
    * All the rest of the IP addresses on the internet are Public

## VPC Overview

* All new AWS accounts have a default VPC
* VPC
* Subnets
    * Reserved IP for 10.0.0.0/24
        * 10.0.0.0 -> Network Address
        * 10.0.0.1 -> VPC router
        * 10.0.0.2 -> mapping to Amazon-provided DNS
        * 10.0.0.3 -> future use
        * 10.0.0.255 -> Network Broadcast Address
    * Example:
        * If I need 29 IP addresses
            * 2^(32-27) = 2^5 = 32 (but minus 5)
* Internet Gateway
    * Allow resources to connect to the Internet
    * One IGW for a One VPC
* Route Table

## Bastion Host

* When you have an EC2 instance in a private Subnet
* An EC2 instance in a public Subnet can have access to the private instance
* Hands On:
    * Create a EC2 instance in public subnet
    * Create a EC2 instance in private subnet
    * Add the public EC2 ip in the security group for private EC2 instance
    * Connect with the private instance using the public instance and the ssh console

## NAT (Network Address Translation) Instance

* Allows EC2 instances in private subnets to connect to the internet
* Must be launched in a public subnet
* Must disable EC2 settings: Source / destination Check
* Must have Elastic IP attached to it
* Route Tables must be configured to route traffic from private subnets to the NAT Instance
* Hands On:
    * You can use AMI
    * Send the outbound traffic in the private instance to the NAT Instance

## NAT (Network Address Translation) Gateway

* AWS-managed NAT, higher bandwidth, high availability, no administration
* Internet GAteway > NAT Gateway > Private Subnet
* 5Gbps scaling up to 100Gbps
* No security Groups to manage/required
* High availability
    * NAT GW is resilient within a single AZ
    * Must create multiple AZs for fault-tolerance
    * There is no cross-AZ failover needed because if an AZ goes down it does not need NAT
* Hands On:
    * It works similar to NAT Instance

## NACL (Network Access Control List)

* Is stateless
* Request process:
    * Incoming request:
        * NACL Inbound Rules
        * Security Group Inbound rules
        * Security Group Allowed Outbount rules
        * NACL Outbound Rules
    * Outgoing request:
        * Security Group Allowed Outbount rules
        * NACL Outbound Rules
        * NACL Inbound Rules
        * Security Group Inbound rules
* The default NACL allows inbounr/outbound traffic
* It increments 100 by 100
* Ports
    * 21 FTP
    * 22 SSH
    * 22 SFTP
    * 80 HTTP
    * 443 HTTPS
* Ephemeral Port

## VPC Peering

* Privately connect two VPCs using AWS network
* Make them behave as if they were in the same network
* Must not have overlapping CIDRs
* VPC Peering connection is NOT transitive
* You must update route tables in each VPC's to ensure EC2 instances can communicate with each other
* Hands On
    * Create peering connection
    * Accept request 
    * Configure the route table

## VPC Endpoint

## VPC FLow