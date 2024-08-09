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

## Elastic Container Service

* Lab:
    * Create Clúster in ECS
    * Create Task Definition
    * Create Service inside our Clúster:
        * Servicio: webapp
        * Tarea: Algo en específico
    * Para borrar:
        * Eliminar Tarea
        * Eliminar Servicio
        * Eliminar Clúster

## Amazon Elastic BeanStalk

Sólo cargar el código y la configuración se desplega por si sola.

PaaS

* Web App 3-tier:
    * ELB + Auto Scaling Group + Database
    * ELB + ASG + EC2 + RDS

* Models:
    * Instancia única
    * ELB + ASG
    * Sólo ASG

* Lab:
    * Create application
    * Inside application, create a new environment:
        * Crear un nuevo perfil de instancia (Role):
            * AWSElasticBeanstalkMulticontainerDocker
            * AWSElasticBeanstalkWebTier
            * AWSElasticBeanstalkWorkerTier
        