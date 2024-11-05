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

