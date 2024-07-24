# Características de Cloud Computing

Client-Server model

Servidores:
* Compute: CPU
* Memory: RAM
* Storage: Data
* Databases
* Networks

## Cinco características del Cloud Computing

* Auto servicios bajo demanda
* Amplio acceso a la red
* Multitenancy and grouping resources
* Rápida elasticidad y escalabilidad:
    * Escalabilidad vertical <-->: Crece el número de recursos
    * Escalabilidad horizontal: Crece la capacidad
* Servicio medido

## Six advantages of cloud computing

* CaPEX por OpPEx
* Economías de escalas
* Go global in minutes
* Stop guessing capacity
* Dejar de gastar en servidores
* Velocidad y agilidad

## Problemas que resuelve la nube

* Flexibilidad: Cambie los recursos cuando sea necesario
* Rentabilidad: Pague sobre la marcha, por lo que utilice
* Escalabilidad: Escalabilidad vertical y horizontal
* Elasticidad: Capacidad de escalar cuando quiera
* Alta disponibilidad y tolerancia al fallo:
* Agilidad: Desarrolle, pruebe y lance rápidamente aplicaciones de software

# Introducción a AWS

Ofrece más de 200 servicios

Beneficios:
* Bajo costo
* Elasticidad y agilidad
* Abierto y flexible
* Seguro
* Alcance Global

# Alcance global de AWS

Infrastructure: https://infrastructure.aws/

Latency: https://aws-latency-test.com/

AWS Services by Region: https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/

AWS Pricing Calculator: https://calculator.aws/#/

Composición:
* Regiones 33
* Zonas de disponibilidad de 3 a 6
* Data centers 1 o más data centers
* Edge locations / Points of presence

Zonas locales: conectadas a una región pero sólo para algunos servicios y capacidades

¿Cómo elegir una Región de AWS?
- Cumplimiento
- Proximidad
- Servicios disponibles
- Precios

Servicios globales:
* IAM
* Route53
* CloudFront
* WAF

Servicios regionales:
* Amazon EC2 (IaaS)
* Elastic BeanStalk (PaaS)
* Lambda
* Rekognition (SaaS)

## Responsabilidad compartida

* AWS es responsable de la seguridad DE la nube:
    * Regions
    * Availability Zones
    * Edge Locations
    * Compute
    * Storage
    * Databases
    * Networking
* Los clientes son responsables de la seguridad y cumplimiento EN la nube:
    * Client-side Data Encryption
    * Network Traffic Protection
    * Operating system
    * Network
    * Firewall
    * Platform
    * Applications
    * Identity and Access Management

Seguridad física del centro de datos
Seguridad EC2:
    * hypervisor
    * Sistema operativo Host
    * Firewall con estado: Tráfico entrante se deniega, tráfico de salida se permite, configuración mediante grupos de seguridad
Seguridad de la red
Administración de configuración
Construido para "Disponibilidad Continua":
    * Servicios escalables y tolerantes a fallos
    * Todas las AZ están siempre disponibles
    * Conectividad robusta a internet
Administración de discos
Desmantelamiento de dispositivos de almacenamiento

## Acceder a aws

* Consola
* CLI
* SDK

## IAM

AAA con AWS:
    * Authenticate: IAM Access
    * Authorize: IAM POlicies
    * Audit: CloudTrail

IAM:
    * Users
    * Groups
    * Policies
    * Roles
    * Credenciales de seguridad temporales:
        * Acceso a servicios específicos
        * Acceso a consola y/o APIs

### Policy

* Principio de mínimos privilegios
* Structure:
    * Version
    * Id (optional)
    * Statement:
        * Sid (optional): 
        * Effect: DENY or ALLOW
        * Principal: Account, role o user for this policy
        * Action: Lista de acciones de la política
        * Resource: Lista de recursos
        * Condition (optional): condiciones para cuando esta política esté vigente