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

## Lambda

Serverless implies that you do not manage servers anymore.
* EventBridge + Lambda + S3 are a good fit
* You can use SQS, APIGateway, Amazon Kinesis Data Streams, Amazon DynamoDB, SNS, Amazon Kinesis Data Analytics
* Lambda and Redshift
* Lambda and Kinesis
* Disparadores de lambdas:
    * Amazon S3
    * Amazon SNS
    * Amazon Kinesis
    * Amazon DynamoDB
    * Amazon SES
    * Amazon SQS
    * AWS Config
    * AWS IoT 
    * Amazon Lex
    * Amazon CloudWatch
    * AWS Cloudformation
    * Amazon API Gateway
    * Amazon CloudFront
    * Amazon Cognito
    * AWS CodeCommit

* Antipatterns:
    * Long time applications
    * Dynamic web sites
    * Stateless applications

* Lambda lab:
    * Create layer
    * Create two Buckets
    * Create IAM policy and role

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:PutLogEvents",
                "logs:CreateLogGroup",
                "logs:CreateLogStream"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "arn:aws:s3:::janobourian-lambda-lab-01/*",
                "arn:aws:s3:::janobourian-lambda-lab-01",
                "arn:aws:s3:::janobourian-lambda-lab-02/*",
                "arn:aws:s3:::janobourian-lambda-lab-02"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "glue:*"
            ],
            "Resource": "*"
        }
    ]
}
```