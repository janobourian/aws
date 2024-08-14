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

## API Gateway

* Admite:
    * API Restful
    * API WebSocket
    * Seguridad:
        * Autenticación de usuarios
        * Limitación de API
        * Claves API
        * Monitoreo

* Integracion:
    * Lambda
    * HTTP / Load Balancer
    * AWS Service / AWS Step Functions

* Tipos de conexión:
    * Edge-Optimized
    * Regional
    * Private: Sólo dentro de la VPC

* Seguridad:
    * Autenticación:
        * Roles de IAM
        * Cognito
        * Authorizer (Personalizado)
    * Seguridad HTTPS de nombres de dominio personalizados a través de la integración con AWS Certificate Manager (ACM):
        * Para Edge el certificado debe estar en us-east-1
        * Regional: el certificado debe estar en la región de API Gateway
        * Debe configurarse el registro de CNAME o A-alias en Route53

## AWS Batch

* Procesamiento por lotes 
* Los trabajos por lotes se definen como imágenes de Docker y se ejecutan en ECS

## Amazon Lightsail

* Servidores virtuales
* Precios bajos y predecibles
* Casos de uso:
    * Aplicaciones web sencillas
    * Sitios web
    * Entorno de desarrollo/prueba
* Tiene alta disponibilidad pero no escalamiento automático, integraciones limitadas de AWS.

## AWS CloudFormation

* Infraestructura como código.
* Estrategia de ahorro: en Dev, puede automatizar la eliminación de plantillas a las 5 pm y recrearlas a las 8 am

## Servicios de desarrollador

* AWS CodeCommit
* AWS CodeBuild:
    * Creación de código en la nube
* AWS CodeDeploy:
    * Implementar nuestra aplicación automáticamente
* AWS CodePipeline:
    * Orquesta los diferentes pasos para que el código se envíe automáticamente a producción
* AWS CodeArtifact:
    * Gestiona los paquetes y dependencias de software
    * Funciona con npm, Yarn, Pip y NuGet
* AWS CodeStar: 
    * UI unificada para gestionar fácilmente las actividades de desarrollo de software en un solo lugar
* AWS Cloud9:
    * IDE en la nube para escribir, ejecutar y depurar código
* AWS Cloud Development Kit (CDK):
    * Infraestructura como código
    * Compila el código en una plantilla de CloudFormation (JSON/YAML)