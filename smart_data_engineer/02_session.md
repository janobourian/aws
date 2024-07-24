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

- Seguridad física del centro de datos
- Seguridad EC2:
    * hypervisor
    * Sistema operativo Host
    * Firewall con estado: Tráfico entrante se deniega, tráfico de salida se permite, configuración mediante grupos de seguridad
- Seguridad de la red
- Administración de configuración
- Construido para "Disponibilidad Continua":
    * Servicios escalables y tolerantes a fallos
    * Todas las AZ están siempre disponibles
    * Conectividad robusta a internet
- Administración de discos
- Desmantelamiento de dispositivos de almacenamiento

## Acceder a aws

* Consola
* CLI
* SDK

## IAM

- AAA con AWS:
    * Authenticate: IAM Access
    * Authorize: IAM POlicies
    * Audit: CloudTrail

* Los usuarios pueden o no pertenecer a un grupo.
* Los usuarios pueden pertenecer a muchos grupos.
* Los grupos sólo contienen usuarios, no otros grupos. 

- IAM:
    * Users
    * Groups
    * Policies
    * Roles
    * Credenciales de seguridad temporales:
        * Acceso a servicios específicos
        * Acceso a consola y/o APIs

### Policy

* Principio de mínimos privilegios
* SEPARC. 
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

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Deny",
			"Action": "iam:ListUsers",
			"Resource": "*"
		}
	]
}
```

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sns:publish"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3Policy",
            "Effect": "Allow",
            "Action": [
                "S3:DeleteObject",
                "S3:GetBucketLocation",
                "S3:GetObject*"
            ],
            "Resource": [
                "arn:aws:s3:::janobourian-demo-*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:username": "janobourian"
                }
            }
        }
    ]
}
```

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowListActions",
            "Effect": "Allow",
            "Action": [
                "iam:ListUsers",
                "iam:ListVirtualMFADevices"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowUserToCreateVirtualMFADevice",
            "Effect": "Allow",
            "Action": [
                "iam:CreateVirtualMFADevice"
            ],
            "Resource": "arn:aws:iam::*:mfa/*"
        },
        {
            "Sid": "AllowUserToManageTheirOwnMFA",
            "Effect": "Allow",
            "Action": [
                "iam:EnableMFADevice",
                "iam:ListMFADevices",
                "iam:ResyncMFADevice"
            ],
            "Resource": "arn:aws:iam::*:user/${aws:username}"
        },
        {
            "Sid": "AllowUserToDeactivateTheirOwnMFAOnlyWhenUsingMFA",
            "Effect": "Allow",
            "Action": [
                "iam:DeactivateMFADevice"
            ],
            "Resource": [
                "arn:aws:iam::*:user/${aws:username}"
            ],
            "Condition": {
                "Bool": {
                    "aws:MultiFactorAuthPresent": "true"
                }
            }
        },
        {
            "Sid": "BlockMostAccessUnlessSignedInWithMFA",
            "Effect": "Deny",
            "NotAction": [
                "iam:CreateVirtualMFADevice",
                "iam:EnableMFADevice",
                "iam:ListMFADevices",
                "iam:ListUsers",
                "iam:ListVirtualMFADevices",
                "iam:ResyncMFADevice"
            ],
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:MultiFactorAuthPresent": "false"
                }
            }
        }
    ]
}
```

* IAM Credentials Report (account-level)
* IAM Access Advisor (user-level)

CLI: https://aws.amazon.com/es/cli/
Documentation: https://awscli.amazonaws.com/v2/documentation/api/latest/index.html

```bash
aws --version
aws configure
aws iam list-users
aws quicksight list-dashboards --aws-account-id <Account_id>
```

### Roles

Una instancia de EC2 tenga que ejecutar acciones en otro servicio. 
No insertar access keys dentro de la instancia: use roles.
Los roles pueden ser usados por usuarios. 

Roles comunes:
* Roles de instancia EC2
* Roles de la función Lambda
* Funciones para CloudFormation
    
## Support plans

* AWS Basic:
    * Servicio al cliente
    * Trusted Advisor
    * AWS Personal Health Dashboard
* Developer:
    * Acceso por correo electrónico en horario comercial a los asociados de soporte en la nube
    * Casos ilimitados / 1 contacto primario
    * Gravedad del caso:
        * Orientación general < 24 horas hábiles
        * Sistema deteriorado < 12 horas hábiles
* Business
    * Para cargas de trabajo en producción
    * Trusted advisor + acceso a la API
    * Acceso por teléfono, correo electrónico y chat 24/7 
    * Casos ilimitados / contactos ilimitados
    * Acceso a la gestión de eventos de infraestructura por una tarifa adicional
    * Gravedad del caso: 
        * Orientación general < 24 horas hábiles
        * Sistema deteriorado < 12 horas hábiles
        * Sistema en producción deteriorado < 4 horas
        * Sistema en producción inactivo < 1 hora
* Enterprise On-Ramp:
    * Para cargar críticas en producción o para el negocio
    * Acceso a grupo de gestores técnicos de cuenta (TAM)
    * Equipo de soporte de conserjería (para conocer las mejores prácticas de facturación y cuentas)
    * Gestión de eventos de infraestructura, revisión de operaciones y buena arquitectura
    * Gravedad del caso:
        * Sistema en producción deteriorado < 4 horas
        * Sistema de producción inactivo < 1 hora
        * Sistema crítico para el negocio < 30 minutos
* Enterprise:
    * Diseñado para usarse si tiene cargas de trabajo críticas
    * Plan de AWS Business
    * Acceso a un Gestor Técnico de Cuentas (TAM) designado
    * Gestión de eventos de infraestructura, revisión de operaciones y buena arquitectura
    * Gravedad del caso:
        * Sistema en producción deteriorado < 4 horas
        * Sistema de producción inactivo < 1 hora
        * Sistema crítico para el negocio < 15 minutos