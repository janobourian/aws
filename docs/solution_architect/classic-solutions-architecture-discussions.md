# Classic Solutions Architecture Discussions

## What is The Time

* We do not need a database
* We want to start small and can accept downtime
* We eant to fully scale vertically and horizontally, no downtime
* Starting simple
  * User -> EC2 using t2.micro and Elastic IP Address
  * A lot of users -> EC2 using m5.micro and Elastic IP Address
  * Scale Vertically
  * Scale Horizontally
  * Use 53 for DNS with TTL 1 hour with A Record
  * Use a Load Balancer + Health Checks + Route53 with Alias Record
  * Now add an Auto-Scaling Group
  * Now We implement ELB + Health Checks + Multi AZ
  * Minimum 2 AZ => Let's reserve capacity

## MyClothes.com

* To uy clothes online
* There is a shopping cart
* Our website is having hundreds of users at the same time
* We need to scale, maintain horizontal calability and keep our web application as stateless as possible
* Users should not lose their shopping cart
* Users should have their details in a database
* Starting Simple:
  * Route53 + ELB in Multi-AZ + Auto-Scaling Group
  * add Session Affinity (Stickiness)
  * add User cookies (to store the information in Web Cookies, but they have to less than 4KB)
  * Add session_id in Web Cookies and go to ElastiCache
  * Add RDS Instance for long therm storage
  * Add RDS Read Replicas to have Master and Slaves (Writes - Read)
  * Add ElastiCache Multi-AZ and RDS Multi-AZ

## MyWordPress.com

* Fully scalable WordPress website
* We want that website to access and correctly display picture uploads
* Our user data, and the blog content should be stored in a MySQL database
* Starting Simple:
  * Route53 -> Multi-AZ ELB -> Auto-Scaling Group -> ElastiCache Multi-AZ -> RDS Multi-AZ
  * Add EFS to attach multiple instance in a Region

## Instantiating applications quickly

* We want to deploy a web application quickly
* EC2 Instances:
  * Use a Golden AMI
  * Boostrap using User Data
  * Hybrid
* RDS Databases:
  * Restore from a snapshot
* EBS Volumes:
  * Restore from a snapshot

## Beanstalk

* Elastic Beanstalk is a developer centric view of deploying an application on AWS
* Web Server Tier vs Worker Tier
