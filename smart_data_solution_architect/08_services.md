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

## VPC Security

* NACL
    * ALLOW and DENY
    * Sin estado
    * Sólo IPs
    * Input and Output allow by defect
* Security Groups
    * ALLOW
    * IPs and Security Groups
    * With Estado
    * AWS Verified Access
* VPC Flow Logs
    * Information about IP traffic
    * The data could forward to S3, CloudWatch Logs, and Kinesis Data Firehose

* Labs:
    - Create a VPC
    - Create a new subnet
    - Edit Route tables to add the new subnets
    - Launch EC2 instance

## Conectivity options

* VPC Peering
* AWS Transit Gateway
* VPC Endpoint
    * Interface
    * Gateway
        * S3
        * DynamoDB
* VPC Flow Logs

## On-premises

* Site-to-site VPN
    * Public internet
        * AWS side:
            * Virtual Private Gateway
        * Customer side:
            * Customer Gateway
    * AWS VPN CloudHub
* Direct Connect (DX)
    * Conexión física
        * Conexiones dedicadas
        * Conexiones alojadas
    * For backup we can use a site-to-site VPN
* AWS Private Link
    * Exponer un servicio a miles de VPC

## AWS Network Firewall

* Protección a nivel de VPC
    * De capa tres a siete
    * Filtrado de tráfico

## Route53

* DNS Service
* Hosted Zone
* Routing:
    * Simple
    * Weightleng (ponderado)
    * Latency
    * Conmutación por error
    * State (conmutación por error)
    * Geolozalization
    * Geoproximity
    * IP Routing
    * Multi-value
* Health Checker

## CloudFront

## AWS Global Accelerator