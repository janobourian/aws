# Another ways to deploy

## Container and Docker

* From Docker Hub
* From Amazon Elastic Container Register (Amazon ECR)

Docker Daemon is something like Hypervisor

* Services:
    * Amazon Elastic Container Registry (Amazon ECR)
    * Amazon Elastic Kubernetes Service (Amazon EKS)
    * Amazon Elastic Container Service (Amazon ECS)
    * AWS Fargate

WorkShop: https://ecsworkshop.com/

## Amazon Elastic BeanStalk

PaaS

* Web App 3-tier:
    * ELB + Auto Scaling Group + Database
    * ELB + ASG + EC2 + RDS

* Models:
    * Instancia única
    * ELB + ASG
    * Sólo ASG