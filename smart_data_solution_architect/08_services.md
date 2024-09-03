# Networking and Delivery Content

## Amazon VPC

* Virtual Private Cloud
* Regional but can work through Availability Zones using VPC CIDR
* Subredes:
    * Private
    * Public
        * Internet Gateway
* Key concepts:
    * Five VPC for region
    * Size:
        * Minimum 16 IPs (/28)
        * Maximum 65536 IPs (/16)
    * Only private ranges
        * 10.0.0.0
        * 172.16.0.0
        * 192.168.0.0
    * Until 200 subnets per VPC
    * AWS reserves 5 public IPs
    * Example: 
        * 10.0.0.0/28
            * 11111111.1111111.11111111.11******
    * Route tables:
        * Es para cada subnet
        * Hasta 50 rutas por route table
        * Dirigen el tráfico a:
            * Internet Gateway
            * NAT Gateway
            * VPN Gateway
            * AWS Transit Gateway
            * AWS Direct Connect

* Internet Gateway:
    * Conectarse a internet utilizando EC2 and Public Subnets
    * One VPC for IG
    * Also, Route Tables should be edited
* NAT Gateway:
    * Conectarse a la public subnet 
    * Using Elastic IP
* Pattern:
    * Internet
    * Internet Gateway
    * Public subnet
        * EC2 Instance
        * NAT Gateway
    * Private subnet:
        * EC2 Instance

* Host Bastion:
    * Permite conectarse a Private EC2 using SSH

* NAT Instance
    * Sólo salida
* NAT Gateway
    * Common case, IG => NATG => Private EC2 Instance
    * High Availability: Create a NATG for each AZ
