# Scalability and High Availability

* Scalability: 
    * Vertical
        * Increase the size of the instance
    * Horizontal = elasticity
        * Increase the number of instances

* High Availability:
    * The goal is to survive a data center loss
    * It can be passive
        * Multi AZ
    * It can be Active
        * Horizontal Scalability

## Elastic Load Balancing (ELB)

* Load Balances are servers that forward traffic to multiple servers downstream
* Expose a single point of access to your application
* Do regular health checks to your instances
* Provide SSL termination
* Types of load balancer:
    * Classic Load Balancer (CLB)
    * Application Load Balancer (ALB)
    * Network Load Balancer (NLB)
    * Gateway Load Balancer (GWLB)
* Security:
    * Users > HTTP/HTTPS > Loac Balancer > HTTP Restricted to Load Balancer > EC2

### Application Load Balancing (ALB)

* It is in the 7th layer
* Support HTTP/2, HTTP, HTTPS and Websockets
* Routing tables to different target groups:
    * Based on path in URL (example.com/users and example.com/posts)
    * Based on hostname in URL (one.example.com and other.example.com)
    * Based on Query String (example.com/users?id=123&order=false)
* Is great fit for micro services and container based application
* Target Group:
    * EC2 Instances
    * ECS Tasks
    * Lambda functions
    * IP Addresses (Private IP routing)
* The ALB do not see the IP of the client directly
* You need to use X-Forwarded-Port and X-Forwarded-Proto

* Hands on:
    * Create instances
    * Create Aplication Load Balancer
    * Create Target groups
    * Create and edit security groups
    * Launch ALB
    
```bash
#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from @janobourian in $(hostname -f)</h1>" > /var/www/html/index.html
```

### Network Load Balancing (NLB)

### Gateway Load Balancing (GWLB)