# Almacenamiento en AWS Parte 02

## AWS S3 - Simple Storage Service

* Almacenado infinito
* Casos de uso: 
    * Copia de seguridad y almacenamiento
    * Recuperación ante desastres
    * Archivo
    * Almacenamiento en la nube híbrida
    * Alojamiento de aplicaciones
    * Alojamiento de medios
    * Lagos de datos y análisis de big data
    * Entrega de Software
    * Sitio web estático

* Buckets:
    * Son directorios que dan la ilusión de archivos
    * Nombre único global en todas las regiones y todas las cuentas
    * Se definen a nivel de región
    * Se almacenan como objetos. Tipos de almacenamientos: Objetos, bloques, archivos. 
    * Máximo tamaño de un archivo es de 5TB
    * Máximo tamaño para subir un archivo es de 5GB
        * Más grande utilizar "Multi-part upload"
    
* Seguridad:
    * Basado en el usuario:
        * Políticas de IAM
            * SEPARC
    * Basado en recursos:
        * Bucket policy
            * SEPARC
        * Bucket Access Control List
        * Object Access Control List
    * Encriptación
    * Para hacerlo público es necesario cambiar la BACL and the bucket policy

* Versionamiento:
    * Se habilita a nivel bucket. 
    * Se recomienda:
        * Protección contra eliminación no deseada
        * Vuelve fácilmente a la versión anterior
        * Los objetos cargados antes de la versión tendrán id null
        * La suspensión del control de versiones no elimina las versiones anteriores

* Replicación
    * Replication
        * CRR: Cross Region Replication
        * SRR: Same Region Replication
    * Crear versionamiento
    * Asíncrona

* Clases de almacenamiento
    * Standard
    * Infrequent access
        * Standard: 
            * Recuperación ante desastres
        * One Zone: 
            * Tiene la menor disponibilidad
            * Almacenamiento de copias de seguridad secundaria 
            * Datos que se pueden volver a generar
    * Intelligent Tiering
        * Utiliza ML:
        * Tipos:
            * Frequent Access tier
            * Infrequent Access tier
            * Archive Instant Access Tier
            * Archive Access Tier
            * Deep Archive Access Tier
    * Glacier
        * Instant retrieval
            * Duración mínima de 90 días
        * Flexible retrieval
            * Duración mínima de 90 días
            * Modos:
                * Expedited: 1 a 5 minutos
                * Standard: 3 a 5 horas
                * Bulk: 5 a 12 horas
        * Deep Archive
            * Duración mínima de 180 días
            * Modos:
                * Standard: 12 horas
                * Bulk: 48 horas

* Life Cycle Rules:
    * Transición
    * Expiración

* Requester Pays Bucket:
    * El solicitante paga

* Eventos
    * SNS
    * SQS
    * Lambda

* Rendimiento:
    * Multipart Upload
    * Transfer Acceleration
    * S3-Byte Range Fetches
    * S3 Select and Glacier Select
    * S3 Batch Operations
    * S3 Storage Lens
        * Metricas
            * Métricas de resumen
            * Métricas de optimización de costos
            * Métricas de protección de datos
            * Métricas de gestión de acceso
            * Métricas de eventos
            * Métricas de rendimiento
            * Métricas de actividad
            * Métricas detalladas del código de acceso

* Cifrados
    * Server-Side Encryption (SSE-S3)
    * Server-Side Encryption with KMS (SSE-KMS)
    * Server-Side Encryption with Customer-Provided Keys (SSE-C)
    * Clien-Side Encryption

* Additional Features:
    * CORS
    * Eliminación MFA
    * Registros de acceso de S3
    * Presigned URLs
    * S3 Glacier VaultLock: Write Once Read Many
    * S3 Object Lock: Write Once Read Many
        * Modos de retención:
            * Cumplimiento: Nadie puede borrarlo
            * Gobernanza: Sólo algunos pueden borrarlo
    * Access Point: Separar por prefijo y brindar políticas
    * Access Point - VPC Origin: Para que sea accesible solo desde dentro de la VPC
        * Modo Gateway (más barato)
        * Modo Interface Endpoint
    * Object Lambda

## Snow Family

* Migración de datos
    * Snowcone: 8 TB - 14 TB, DataSync
    * Snowball Edge: 80 TB
    * SnowMobile: 100 PB

* Computación perimetral:
    * Snowcone
    * Snowball Edge

* AWS OpsHub
    * Software para administrar el dispositivo Snow

SnowBall no se puede enviar directamente a Amazon Glacier

## AWS FSx

* FSx para Windows
* FSx para Lustre: Machine Learning and HCP
* FSx para ONTAP de NetApp
* FSx para OpenZFS

## Almacenamiento Híbrido

* AWS Storage Gateway:
    * Puente entre los datos locales y los datos en la nube
    * Tipos:
        * Amazon S3 File Gateway
        * Amazon FSx File Gateway
        * Volumen Gateway
        * Tape Gateway

## AWS Transfer Family

* Realizar migración de datos por los siguientes protocolos:
    * FTP
    * FTPS
    * SFTP
    
* AWS Transfer for FTP
* AWS Transfer for FTPS
* AWS Transfer for SFTP