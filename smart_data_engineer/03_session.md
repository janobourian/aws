# Almacenamiento 

## Amazon Simple Storage Service (S3)

* Use cases:
    * Copia de seguridad y almacenamiento
    * Recuperación ante desastres
    * Archivo
    * Almacenamiento en la nube híbrida
    * Alojamiento de aplicaciones
    * Alojamiento de medios
    * Lago de datos y análisis de big data
    * Entrega de software
    * Sitio web estático

### Amazon S3 - Buckets

- Objetos (archivos) en "buckets"
- Nombre único global, en todas las regiones y en todas las cuentas
- S3 parece un servicio global, los buckets se definen a nivel de región
- Key (Path): prefix + object_name
- Tamaño máximo de un objeto es 5 TB
- Si cargas más de 5Gb debes usar "multi-part upload"
- Presigned url: It has a token

### Amazon S3 - Seguridad

* Basado en el usuario: 
    * IAM Policies
* Basado en recursos:
    * Bucket Policies: SEPARC, Sid, Effect, Principal, Action, Resource, Condition
    * Object Access Control List (ACL)
    * Bucket Access Control List (ACL)

* Acceso público: Usar la política de bucket
* Acceso a los usuarios a S3: IAM policy
* Acceso a instancias EC2: IAM Roles
* Acceso Cross-Account: Bucket Policy

To convert our bucket in a public bucket we need to change the `Block public access` and turn off it, also we need to add the next policy in the bucket policy.

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Get Object Access",
			"Principal": "*",
			"Effect": "Allow",
			"Action": [
				"s3:GetObject"
			],
			"Resource": [
				"arn:aws:s3:::janobourian-smartdata/*"
			]
		}
	]
}
```

### Amazon S3 - Versionamiento

It is useful versus non-planed deletes

### Amazon S3 - Replicación (CRR & SRR)

Replicación: https://docs.aws.amazon.com/es_es/AmazonS3/latest/userguide/replication-walkthrough-2.html

* CRR: Cross-Region Replication (by region), cobro por transferencia
* SRR: Same-Region Replication (by AZ)
* Sólo se replican objetos nuevos
* S3 Batch Replication: Puede replicar objetos existentes
* No hay "encadenamiento" de replicación
* Replicación unidireccional

### Amazon S3 - Clases de almacenamiento

* Amazon S3 Standard - General Purpose:
    * Propósito general
* Amazon S3 Standard - Infrequent Access (IA):
    * Menos frecuencias pero acceso rápido
    * Disponibilidad 99.9%
    * Copias de seguridad
* Amazon S3 One Zone - Infrequent Access:
    * Menos frecuencias pero acceso rápido
    * Disponibilidad 99.5%
    * Copias de seguridad secundarias
    * Datos que se puedan recrear
* Amazon S3 Glacier Instant Retrieval:
    * Precio de almacenamiento + coste de recuperación de objetos
    * Recuperación de milisegundos
    * Datos de acceso una vez al trimestre
    * Duración mínima de almacenamiento de 90 días
* Amazon S3 Glacier Flexible Retrieval:
    * Precio de almacenamiento + coste de recuperación de objetos
    * Recuperación:
        * Expedited (1 a 5 minutos)
        * Standard (3 a 5 horas)
        * Bulk (5 a 12 horas)
    * Duración mínima de almacenamiento de 90 días
* Amazon S3 Glacier Deep Archive:
    * Precio de almacenamiento + coste de recuperación de objetos
    * Recuperación:
        * Standard (12 horas)
        * Bulk (48 horas)
    * Duración mínima de almacenamiento de 180 días
* Amazon S3 Intelligent Tiering:
    * Pequeña tarifa de supervisión y estratificación automática
    * Mueve objetos automáticamente entre niveles de acceso en función de uso
    * No hay cargos de recuperación en S3 Intelligent-Tiering
    * Niveles:    
        * Frequent Access tier (automático)
        * Infrequent Access tier (automático) primeros 30 días
        * Archive Instant Access tier (automático) primeros 90 días
        * Archive Access tier (opcional) 90 días a 700+ días
        * Deep Archive Access tier (opcional) 180 a 700+ días

### Amazon S3 - Lifecycle Rules

* Acciones de transición:
    * Configurar objetos para realizar la transición a otra clase de almacenamiento
    * Mover objetos entre clases pasado cierto tiempo
* Acciones de expiración: 
    * Configurar objetos para que caduquen
    * Eliminar versiones antiguas de archivos
    * Eliminar cargas incompletas de Multi-Part upload
    * Se pueden crear reglas para un determinado prefijo
    * Se pueden crear reglas para cierto objetos (Etiquetas)

### Amazon S3 and Event Bridge

* events -> Amazon S3:
    * -> SNS with its SNS Resource (Access) Policy
    * -> SQS with its SQS Resource (Access) Policy
    * -> Lambda with its Lambda Resource Policy

* events -> Amazon S3:
    * -> Amazon EventBridge:
        * -> Over 18 AWS services as destination

* Filtrado avanzado
* Múltiples destinos
* Capacidades EventBridge

* 3,500 PUT/COPY/POST/DELETE por prefijo
* 5,500 GET/HEAD por prefijo

* Multi-Part upload:
    * Archivos > 100mb, obligatorio con > 5gb
* S3 Transfer Acceleration:
    * Edge Location

* S3 Byte-Range Fetches:
    * Paralelizar GET rangos de bytes específicos
    * Mejor resilencia en caso de fallos
    * Se puede utilizar para recuperar solo datos parciales (por ejemplo, el encabezado de un archivo)

* S3 Select & Glacier Select:
    * https://aws.amazon.com/blogs/aws/s3-glacier-select/
    * Filtering using server-side filtering
    * We can retrieve information using SQL

### Cifrado Amazon S3

* Server-side Encryption (SSE):
    * Amazon S3-Managed Keys (SSE-S3):
        * AES-256
        * HTTPS request using "x-amz-server-side-encryption":"AES256"
    * KMS Keys stored in AWS KMS (SSE-KMS):
        * Control de usuarios + uso de claves de auditoría mediante CloudTrail
        * HTTPS request using "x-amz-server-side-encryption":"aws:kms"
        * Tarda en cargar por el llamado a KMS GenerateDataKey
        * Tradar en descargar por el llamado a la API de Decrypt
        * Cuota de KMS por segundo (5500, 10000, 30000)
        * Solicitar aumento de cuota mediante Service Quotas Console
    * Customer-Provided Keys (SSE-C):
        * Amazon S3 NO almacena la clave de cifrado que usted proporciona
        * Se debe utilizar HTTPS
        * La clave de cifrado debe proporcionarse en los encabezados HTTP para cada solicitud HTPP realizada
* Client-side Encryption:
    * Utiliza bibliotecas como Amazon S3 Client-Side Encryption Library
    * Los clientes se encargan del encriptado
    * El cliente descencripta el archivo
    * El cliente gestiona completamente las claves y el ciclo de cifrado

* El cifrado en tránsito también se denomina SSL/TLS
* Amazon S3 expone dos puntos de enlace:
    * HTTP Endpoint - No Encriptado
    * HTTPS Endpoint - Encriptación en tránsito
* Se recomienda HTTPS
* HTTPS es obligatorio para SSE-C
* La mayoría de los clientes usarían el punto de conexión HTTPS de forma predeterminada

We can force encryption with the next condition:

```json
{
    "Version": "2012-10-17",
    "Statment": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket/*",
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "false"
                }
            }
        }
    ]
}
```

Opcionalmente se puede forzar el cifrado mediante una política de bucket y rechazar cualquier llamada a la API PUT de un objeto S3 sin encabezados de cifrado (SSE-KMS o SSE-C)

```json
{
    "Version": "2012-10-17",
    "Statment": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::my-bucket/*",
            "Condition": {
                "StringNotEquals": {
                    "s3:x-amz-server-side-encryption": "aws:kms"
                }
            }
        }
    ]
}
```

```json
{
    "Version": "2012-10-17",
    "Statment": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::my-bucket/*",
            "Condition": {
                "Null": {
                    "s3:x-amz-server-side-encryption-customer-algorithm": "true"
                }
            }
        }
    ]
}
```

### Amazon S3 - Access Point

## Amazon Elastick Block Store (EBS)

## Amazon Elastic File System (EFS)