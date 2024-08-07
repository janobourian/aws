# Servicios de Cómputo en AWS

## Servicios de informática

* Amazon EC2
* Amazon EC2 Auto Scaling
* Amazon Elastic Container Registry (Amazon ECR)
* Amazon Elastic Container Service (Amazon ECS)
* Amazon Elastic Kubernetes Service (Amazon EKS)
* VMware Cloud en AWS
* AWS Elastic Beanstalk
* AWS Lambda
* Amazon Lightsail
* AWS Batch
* AWS Fargate
* AWS Outposts
* AWS Serverless Application Repository

* Opciones para el cómputo:
    * Instancias de servidor virtual en la nube
    * Servicio de gestión de contenedores para correr Docker en un cluster de EC2
    * Cómputo sin servidor para la ejecución de código sin estado en respuesta a disparadores

* Categorías:
    * EC2 / Máquinas virtuales
    * Lambda / Sin servidor
    * ECR / ECS / EKS / AWS Fargate 
    * AWS Elastic Beanstalk

## Amazon Elastic Compute Cloud EC2

AMI: Amazon Machine Images

* Virtualización de host en EC2:
    * Servidor host
    * Hipervisor
    * Invitado 1, 2, 3, ..., n

* Linux | Windows | Mac

## Proceso de lanzamiento

1. Etiquetas:
    * Nombres e identificadores
2. AMI:
    * Puedes crear una AMI basado en el estado de una EC2 (Capture as a new AMI)
    * La AMI se puede compartir en otra región
    * Las AMIs son regionales
3. Tipo de instancia
    * Consideraciones:
        * ¿Cómo vamos a usar la instancia EC2 que crearemos?
            * RAM
            * CPU
            * Almacenamiento
            * Rendimiento de red
    * Categorías: https://aws.amazon.com/es/ec2/instance-types/
        * Uso general: a1, m4, m5, t2, t3
        * Optimizadas para informática (procesamiento): c4, c5
        * Optimizadas para memoria: r4, r5, x1, z1
        * Optimizadas para almacenamiento: d2, h1, i3
        * Informática acelerada: f1, g4, g4, p2, p3
    * Nomenclatura:
        * t3.Large: t es la familia, 3 es la generación, Large es el tamaño
4. Par de claves:
    * For Windows the key pair generates the password to access rpd
    * For Linux the key pair is used to connect via SSH
5. Configuración de red
    * Definir VPC y Subnet
    * ¿Será pública o privada?
6. Grupo de seguridad
7. Opciones de almacenamiento
8. Perfil de Instancia IAM
9. Datos de usuario:
    * Script que se ejecuta al lanzar la instancia
    * Sólo se ejecuta al lanzar la instancia, si se apaga ya no.
    * Se lanza como usuario root

* Conexión mediante SSH:
    * cd /var/log
    * sudo car *.log

## Opciones de compra Amazon EC2

* Instancias bajo demanda
* Saving Plans
* Instancias reservadas
* Instancias de spot
* Dedicated Hosts
* Instancias dedicadas
* Reservas de capacidad

* Servicios:
    * Amazon EC2 auto scaling
    * EC2 Fleet
    * Amazon Elastic Container Service (Amazon ECS)
    * Amazon Elastic Kubernetes Service (Amazon EKS)
    * AWS Thinkbox
    * Amazon EMR
    * AWS CloudFormation
    * AWS Batch

