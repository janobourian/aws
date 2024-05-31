# AWS Cloud Practitioner

https://explore.skillbuilder.aws/learn/mycourses

## Index

- [Introducción a Amazon Web Services](#section1)
- [Cómputo en la nube](#section2)
- [Infraestructura Y Fiabilidad Global](#section3)
- [Redes](#section4)
- [Almacenamiento y bases de datos](#section5)
- [Seguridad](#section6)
- [Supervisión y Análisis](#section7)
- [Precios y soportes](#section8)

<div id="section1"> </div>

## Introducción a Amazon Web Services

Servicios:
- Cómputo
- Almacenamiento
- Seguridad de red
- Blockchain
- Machine learning
- Inteligencia artificial

El modelo Cliente-Servidor es el modelo base. Amazon Elastic Compute Cloud (EC2)

Conceptos clave:
- Se paga por lo que se usa.

### Cómputo en la nube

La entrega bajo demanda de recursos de TI a través de internet con precios de pago por uso. 

Diferenciar el Transporte pesado indiferenciado de TI.

Modelos de implementación:
- Basada en la nube (pública)
- Basada en las instalaciones (privada)
- Híbrida

Beneficios del cómputo en la nube:
- Cambiar gastos iniciales por gastos variables.
- Dejar de gastar dinero en la ejecución y el mantenimiento de centros de datos
- Deje de hacer conjeturas sobre la capacidad
- Obtener beneficios de las grandes economías de escala
- Aumentar la velocidad y la agilidad
- Convertirse en una empresa global en minutos

Well-Architected Framework
- Operational excellence: Mejora continua de procesos.
- Security: Protect data and information.
- Reliability: Recovery and adapting.
- Performance efficiency: Select the correct services based on requirements.
- Cost optimization: Scaling without overspending
- Sustainability: Reduce the environment impact.

<div id="section2"> </div>

## Cómputo en la nube

Amazon Elastic Compute Cloud (IaaS)

* Tipos de instancias
* Opciones de facturación
* Amazon EC2 Auto Scaling
* Elastic Load Balancing
* Amazon SNS and Amazon SQS

Tenencia múltiple, el hypervisor coordina y AWS administra.

Configuraciones:
* SO:
    * Windows
    * Linux
* Aplicaciones empresariales internas
* Aplicaciones web
* Bases de datos
* Software de terceros

Escalado vertical
Escalado Horizontal
Controlar aspectos de red de EC2

### Tipo de instancias EC2

Capacidades de cómputo, memoria, redes y almacenamiento.

* De uso general:
    * Recursos equilibrados
    * Cargas de trabajo diversas
    * Servidores Web
    * Repositorios de código
* Optimizada para cómputo:
    * Altos niveles de cómputo
    * Servidores de juego
    * Cómputo de alto rendimiento (HPC)
    * Modelado científico
* Optimizadas para memoria
    * Tareas de alto uso de memoria
* Cómputo acelerado
    * Cálculos de números en coma flotante
    * Procesamiento gráfico
    * Coincidencias de patrones de datos
    * Utilizar aceleradores de software
* Optimizadas para almacenamiento
    * Alto rendimiento para datos almacenados localmente

### Precios de instancias EC2

* Bajo demanda
* Savings Plans: 
    * Compromiso de uso constante en 1 o 3 años. 
    * Ahorros de hasta 72%.
    * Compromiso de gasto por hora a una familia de instancias 
* Instancia reservadas: Uso predecible. Hasta 75%
    * Standard: Indicas la familia y el tamaño, la plataforma, la tenencia y la región de la instancia.
    * Convertibles: Zonas de disponibilidad diferentes
* Instancias tipo spot: Cómputo adicional con hasta 90%. Carga de trabajo por lotes. 
* Servidores dedicados: No son compartidos. 

### Escalado de Amazon EC2

Servicio: Amazon EC2 Autoscaling:
* Escalado dinámico: responde a la demanda cambiante
* Escalado predictivo: programa automáticamente el número correcto de instancias de Amazon EC2 en función de la demanda prevista
* Escalado Horizontal
* Escalado Vertical

Grupo de Autoscaling:
* Mínimo
* Capacidad deseada
* Capacidad máxima

### Arquitecturas desacopladas
* Elastic Load Balancing
* Simple Queu Service
* Simple Notification Service

### Elastic Load Balancing

* Servicio administrado
* Es regional
* Balanceo de carga

### Amazon SQS and Amazon SNS

* SQS: Servicios de colas:
    * Enviar, almacenar y recibir mensajes entre componentes de software a cualquier volumen
    * Carga: datos en un mensaje
* SNS: Servicios de mensajes
    * Enviar mensajes entre servicios
    * Enviar mensajes a usuarios finales mediante email, sms o notificaciones push
    * Pub/Sub: Modelo publicación subscripción
    * Enviar mensaje a tema que a su vez envía mensaje a usuarios de ese tema

### Servicios de cómputo adicionales


* Amazon Elastic Container Service (ECS)
* Amazon Elastic Kubernetes Service (EKS)
* Serverless:
    * AWS Lambda
    * AWS Fargate (For ECS and EKS)

<div id="section3"> </div>

## Infraestructura global y fiabilidad

* Alta disponibilidad
* Infraestructura global

### Regiones de AWS

* Factores empresariales de elección:
    * Cumplimiento
    * Proximidad
    * Disponibilidad de servicios
    * Precios

### Zonas de disponibilidad

* AZ es un único centro de datos o un grupo de centros de datos
* Cada región cuenta con varias zonas de disponibilidad
* Siempre ejecuta dos zonas de disponibilidad en una región. 
* Servicios regionales se ejecutan en zonas de disponibilidad: ELB

### Ubicaciones perimetrales

* Almacenar datos en caché
* CDN: Amazon Cloud Front utiliza ubicaciones de borde
* DNS: Amazon Route53
* AWS Outposts: AWS instala una mini región dentro de su propio centro de datos.

Key points: 
* Regiones son áreas aisladas geográficamente
* Las regiones contienen zonas de disponibilidad
* Las zonas de disponibilidad dan persistencia
* Ubicaciones de borde ejecutan Amazon Cloud Front

### Aprovisionar recursos

* API: En AWS todo es una llamada a API. 
    * Consola
    * CLI
    * SDK
    * AWS Cloud Formation
    * AWS CDK
    * Otras herramientas
* AWS Elastic Beanstalk
    * Facilita el manejo de EC2
    * Ajuste de capacidad
    * Balanceo de carga
    * Escalado automático
    * Supervisión del estado de las aplicaciones
* AWS Cloud Formation
    * Infraestructura como código IaaC


<div id="section4"> </div>

## Redes

* Amazon Virtual Private Cloud (VPC)
* Subred pública y subred privada

### VPC

* Virtual Private Cloud (VPC)
    * subredes
        * públicas
        * privadas
    * Puerta de enlace de Internet 
        * Elastic Load Balancer (own security group)
        * Autoscaling Group
        * EC2 Instances (own security group)
        * Database (own security group)
    * Puerta de enlace privada virtual
    * AWS Direct Connect

### Listas de control de acceso o Access Control List (ACL)

Inside VPC.
IGW (Internet Gateway)
ACL de red (subred): 
* verifica permisos de entrada o salida
* permite entrada y salida por default
* en un ACL personalizado se deniega todo y se debe ser explícito de quién sí y quién no
* no cuenta con estado
Grupo de seguridad (security group):
* no permite tráfico de entrada pero sí de salida
* cuenta con estado

### Redes globales 

* Route 53 (DNS): 
    * Enrutamiento basado en latencia
    * DNS de geolocalización
    * Enrutamiento de geoproximidad
    * Weighted Round Robin
* Amazon Cloudfront (CDN) Content Delivery Network:

<div id="section5"> </div>

## Almacenamiento y bases de datos

### Almacenes de instancias y Amazon Elastic Block Store (Amazon EBS)

* Almacenamiento a nivel de bloques
* Volúmenes de almacén de instancias (Adyacentes a las instancias de EC2)
* Amazon Elastic Block Store (Amazon EBS): 
    * Se crea un disco virtual no relacionado al host
    * Características:
        * Tamaño
        * Tipo 
        * Configuración
    * Instantáneas:
        * Copias de respaldo progresivas

### Amazon Simple Storage Service

Almacena y recupera una cantidad ilimitada de datos.

* Amazon S3: 
    * Se almacenan datos como objetos
    * Almacenar objetos en buckets
    * Cargue un objeto con un tamaño máximo de 5TB
    * Versiones de objeto
    * Políticas para mover objetos entre las clases de almacenamiento

* Clases de almacenamiento:
    * Amazon S3 Standard: 99.999999999% de durabilidad
    * Alojamiento de sitios web estáticos 
    * Amazon S3 Standard-Infrequent Access (S3-Standard IA):
        * Datos con menos frecuencia pero acceso rápido
    * S3 One Zone (Acceso poco frecuente) S3 One Zone-IA:
        * Sólo una zona de disponibilidad
    * S3 Intelligent Tiering:
        * Amazon supervisa los patrones de acceso a los objetos
        * Trabaja entre Standard y Standard-IA
    * S3 Glacier Instant Retrieval
    * Amazon S3 Glacier Flexible Retriever:
        * Datos para auditoria
        * Se puede implementar un bloqueo de almacenamiento
        * Escribir una vez, leer muchas veces (WORM)
        * Se recupera en minutos u horas
    * S3 Glacier Deep Archive
        * Se recuperan entre 12 y 48 horas
    * S3 Outposts

* Almacenamiento por bloques: Sólo se cambia una porción de bits
* Almacenamiento por objetos: Se actualiza todo el objeto cada vez que se cambia

### Amazon Elastic File System (Amazon EFS)

* Almacenamiento de archivos
* Varias instancias pueden acceder al mismo tiempo
* Se escala automáticamente
* Sistema de archivos Linux
* Recurso regional

### Amazon Relational Database Service (Amazon RDS)

* Sistema de administración de bases de datos relacionales (RDBMS)
* Bases de datos:
    * MySQL
    * PostgreSQL
    * Oracle
    * Microsoft SQL Server
* Transportar y cambiar migraciones

* Amazon RDS:
    * Parches
    * Backups
    * Redundancia

* Amazon Aurora:
    * MySQL
    * PostgreSQL
    * 1/10 del costo de las bases de datos comerciales
    * Replicación de datos 
    * Hasta 15 réplicas de lectura
    * Respaldo continuo en Amazon S3

### Amazon DynamoDB

* Base de datos serverless
* Organización:
    * Tablas -> Datos -> Elementos -> Aributos
* NoSQL Database

* Amazon RDS para relaciones complejas
* Amazon DynamoDB para tablas únicas

### Amazon Redshift

* Big Data
* Datos históricos en lugar de Datos operativos 
* Almacén de datos

### Amazon Database Migration Service (Amazon DMS)

* Base de datos fuente y destino no deben ser del mismo tipo
* Desarrollo y prueba de migraciones de bases de datos
* Consolidación de bases de datos
* Replicación continua de bases de datos

### Servicios de bases de datos adicionales

* Amazon DocumentDB
* Amazon Neptune 
* Amazon Quantum Ledger Database (Amazon QLDB)
* Amazon Managed Blockchain
* Amazon ElastiCache
* Acelerador de Amazon DynamoDB

<div id="section6"> </div>

## Seguridad

### Modelo de responsabilidad compartida de AWS

* Modelo de responsabilidad compartida AWS:
    * AWS: Responsable de la seguridad de la nube
    * Cliente: Responsable de la seguridad en la nube

* Cliente:
    * Datos del cliente
    * Plataforma, aplicaciones e Identity and Access Management (IAM)
    * Sistemas operativos y configuración de red y firewall
    * Cifrado de datos del lado del cliente, cifrado de datos del lado del servidor y protección de tráfico de redes

* AWS:
    * Capa Física:
        * Red
        * Hipervisor
    * Hardware:
        * región, zona de disponibilidad y ubicación perimetral
    * Software:
        * cómputo, almacenamiento, base de datos y redes

### Permisos y accesos del usuario

User root: The owner of the aws account, is not recommendable use this user for any action
AWS IAM: AWS Identity and Access Management
Principio del menor privilegio

User:
Policy:
Groups:
Roles:

### AWS Organizations

* Concentra varias cuentas en una ubicación central
* Administración centralizada de todas las cuentas de AWS
* Facturación unificada
* Descuento por volumen
* Agrupaciones jerárquicas de cuentas
* OU: Organizative Unity
* Control de acceso a las acciones de API y servicios de AWS
* Service Control Policy: Políticas de control de servicios

### Cumplimiento

* RGPD: Reglamento General de Protección de Datos
* HIPAA: Ley de portabilidad y responsabilidad de los seguros médicos
* AWS Artifact: Acceso a los informes de cumplimiento

## DDOS Denegación de Servicio distribuido

* Inundación UDP: Grupos de seguridad
* Ataques de Nivel HTTP: 
* Ataque Slowloris: Elastic Load Balancing
* AWS Shield and AWS WAF
* AWS Shield Advance

## Servicios de Seguridad adicionales

* Cifrado: Proteger mensaje o datos para que sólo accedan las partes interesadas
    * Cifrado en reposo:
        * DynamoDB: AWS Key Management Service (AWS KMS)
    * Cifrado en tránsito
        * Amazon Redshift communicating with SQL

* AWS Key Management Service (AWS KMS)
* Amazon Inspector: Ejecución de seguridad automatizada en la infraestructura
* Amazon Guard Duty: Flujos continuos de metadatos de Amazon Cloudtrail and VPC

<div id="section7"> </div>

## Supervisión y análisis

Supervisión: observación de sistemas, recopilación de métricas y uso de datos para tomar decisiones. In

### Amazon Cloudwatch

* Supervisar infraestructura y aplicaciones en tiempo real
* Métrica: variable vinculada a los recursos
* Alarma de Cloudwatch
* Reduzca el MTTR y mejore el TCO

### AWS Cloud Trail

* Auditoria de APIS

### AWS Trusted Advisor

* Optimización de costos
* Rendimiento
* Seguridad
* Tolerancia a fallas
* Límites de servicios

<div id="section8"> </div>

## Precios y soporte

### Nivel gratuito de AWS

* Siempre gratis
* 12 meses gratis
* Pruebas

Servicios en nivel gratuito:

- Amazon Sagemaker
- Amazon Comprehend Medical
- Amazon DynamoDB
- Amazon Cognito

### Conceptos de precios de AWS

AWS Pricing calculator

* Pago por uso
* Pague menos al reservar
* Pague menos por descuentos de acuerdo al volumen


Amazon S3:
* Almacenamiento:
    * tamaño de los objetos
    * tipo de almacenamiento
    * tiempo de almacenamiento
* Solicitudes y obtenciones de datos
* Transferencia de datos
* Administración y replicación

<div id="section9"> </div>

## Migración e innovación

<div id="section10"> </div>

## El traspaso a la nube

<div id="section11"> </div>

## Conceptos básicos de AWS Certified Cloud Practitioner

