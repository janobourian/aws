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

* CRR: Cross-Region Replication (by region), cobro por transferencia
* SRR: Same-Region Replication (by AZ)
* Sólo se replican objetos nuevos
* S3 Batch Replication: Puede replicar objetos existentes
* No hay "encadenamiento" de replicación
* Replicación unidireccional

### Amazon S3 - Clases de almacenamiento

* Amazon S3 Standard - General Purpose
* Amazon S3 Standard - Infrequent Access (IA)
* Amazon S3 One Zone - Infrequent Access 
* Amazon S3 Glacier Instant Retrieval
* Amazon S3 Glacier Flexible Retrieval
* Amazon S3 Glacier Deep Archive
* Amazon S3 Intelligent Tiering

### Amazon S3 - Lifecycle Rules

### Amazon S3 and Event Bridge

### Cifrado Amazon S3

### Amazon S3 - Access Point

## Amazon Elastick Block Store (EBS)

## Amazon Elastic File System (EFS)