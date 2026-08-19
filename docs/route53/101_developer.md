# This is a section for Route53 from Developer Associated Perspective

## DNS

* Domain Name System: Translates the human friendly hostnames into the machine IP addresses
* DNS is the backbone of the internet
* <https://www.subdomain.domain.com>
* Terminology:
  * Domain register: Amazon Route53, GoDaddy
  * DNS Records: A, AAAA, CNAME, NS,...
  * Zone File: contains DNS records
  * Name Server: resolves DNS queries
  * Top Level Domain: .com, .mx, .com.mx
  * Second Level Domain: amazon.com, google.com
* How DNS Works:
  * Web Browser
  * Local DNS Server
  * Root DNS Server (.com)
  * Local DNS Server
  * TLD DNS Server
  * Local DNS Server
  * SLD DNS Server (Managed by Domain Registar)
  * Local DNS Server
  * Local DNS Cache TTL

## Route53

* Amazon Route53 is a highly available and scalable cloud DNS web service
* It is designed to give developers and businesses an extremely reliable and cost effective way to route end user requests to Internet applications by translating human readable names into the IP addresses
* It is also used to route users to infrastructure outside of AWS
* It is a global service that can be used to manage DNS records for domains registered with any domain register
* It provides a simple web interface and APIs to manage DNS records and configure routing policies
* It also provides health checking and failover capabilities to ensure high availability of applications
* It supports various routing policies such as simple, weighted, latency-based, failover, and geolocation routing
* It also supports DNSSEC for domain name security and protection against DNS spoofing attacks
* It is a pay-as-you-go service with no upfront costs or minimum fees, and you only pay for the resources you use
* It also provides integration with other AWS services such as Elastic Load Balancing, Amazon S3, and Amazon CloudFront for seamless routing of traffic to these services
* It also provides a feature called Route53 Resolver for hybrid cloud DNS resolution, allowing you to resolve DNS queries between your on-premises network and your VPCs in AWS
* It also provides a feature called Route53 Traffic Flow for advanced traffic management and routing based on various criteria such as latency, geography, and endpoint health
* It also provides a feature called Route53 Health Checks for monitoring the health of your resources and automatically routing traffic away from unhealthy resources
* It also provides a feature called Route53 Domain Registration for registering and managing domain names directly through AWS
* It also provides a feature called Route53 Application Recovery Controller for automatic recovery of applications in case of failure
* Each record contains:
  * Domain/Subdomain
  * Record Type
  * Value
  * Routing Policy
  * TTL
* DNS record types
  * A - maps a hostname to IPv4
  * AAAA - maps a hostname to IPv6
  * CNAME - maps a hostname to another hostname
  * NS - Name servers for the Hosted Zone

## Hosted Zones

* A container for records that define how to route traffic to a domain and its subdomains
* There are two types of hosted zones:
  * Public Hosted Zone: used to route traffic on the internet
  * Private Hosted Zone: used to route traffic within a VPC
