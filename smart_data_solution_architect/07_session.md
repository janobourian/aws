# Servicios de Base de Datos

## Bases de datos

* Relacionales (SQL)
    * Permite JOINS
* No relaciones (NoSQL)
    * Esquemas flexibles
    * Examples:
        * key - value
        * document
        * graphs
        * memory
        * search databases
    * JSON is a common format

* Managed Databases:
    * SQL:
        * Amazon Aurora
        * Amazon RDS
    * NoSQL:
        * Amazon DocumentDB
        * Amazon ElastiCache
        * Amazon KeySpace

## Relational Database Service (RDS)

* Motores:
    * PostgreSQL
    * MySQL
    * MariaDB
    * Oracle
    * Microsoft SQL Server
    * Aurora

* Features:
    * Multi AZ para DR (Desaster Recovery)
    * Horizontal and vertical scaling
    * Automatic scaling
        * You need to set up the maximum of storage to scale dynamically
        * Free low 10%
    * EBS storage to backup
    * No connection using SSH

* Common architecture:
    * Elastic Loab Balancer -> EC2 Instances -> RDS

* Read Replicas:
    * 15 réplicas
    * AZ, Cross AZ, Cross Regions
    * Réplica Asíncrona
    * Casos de uso:
        * Read Replica to read operations (SELECT)
    * Cost:
        * Free in same region
        * Cost for tranfer information Cross Region
    
* RDS Multi AZ (Desaster recovery):
    * Sync replication
    * Same DNS
    * Automatic failover

* RDS: One AZ to Multi AZ
    * Create snapshot 
    * Create replica

* Custom RDS:
    * Oracle and Microsoft SQL Server
    * Acceder al sistema operativo
    * SSH connection

## Aurora

* Compatible with:
    * PostgreSQL (3x)
    * MySQL (5x)
    
* Features
    * Increase in 10GB to 128TB
    * It costes 20% more
    * Not available in free tier 
    * Six copies in three AZ
    * Almacenamiento se divide en 100 volúmenes
        * Replicación
        * Autoreparación
        * Autoexpansión
    * Two endpoints
        * Write endpoint
        * Read endpoint
    * Good features:
        * Conmutación automática por error
        * Copia de seguridad y recuperación
        * Aislamiento y seguridad
        * Cumplimiento con la industria

* Custom endpoints:
    * Custom CPU for each instance
    * Writer endpoint
    * Reader endpoint
    * Analytical Queries

* Aurora Serverless
    * Proxy Fleet
    * Cargas de trabajo poco frecuentes, intermitentes o impredecibles

* Global Aurora:
    * Aurora Cross Region
    * Primary Region for read and write
    * Until five regions for read

* Aurora Machine Learning:
    * Prediction based on ML using SQL
    * Services:
        * Amazon SageMaker
        * Amazon Comprehend
    * Use cases:
        * Fraude detection
        * Ads
        * Sentiment Analysis
        * Product recomendations

* Copias de seguridad en RDS
    * Copia diaria
    * Retenión 1 a 35 días
    * Instantáneas manuales

* Restauración usando S3
* Clonación a partir de un clúster existente
* Amazon RDS Proxy:
    * Permite que las aplicaciones agrupen y compartan las conexiones de base de datos establecidas con la base de datos
    * Serverless

## Lab

## Amazon ElastiCache

* Implica cambios en el código de la aplicación
* Redis o MemCached
* Reduce la carga de RDS
* Debe tener una estrategia de invalidación para asegurarse de que solo se usan los datos más recientes. 
* Se van generando los datos según el dato que se traiga
* Casos de uso:
    * Clasificación de juegos

## Amazon DynamoDB

* NoSQL
* Millones de filas, millones de solicitudes, 100Tb de almacenamiento
* Tablas de acceso estándar and IA

* Tablas:
    * Primary Key:
        * Partition Key
        * Partition Key + Sort Key
    * Tamaño máximo de un elemento es de 400KB
    * Datos:
        * Escalares: cadena, número, binario, booleano, nulo
        * Documentos: lista, mapa
        * Conjuntos: cadenas, números, binarios

* Modos de capacidad
    * Aprovisionado
        * Número de RCU, WCU
    * On demand
        * Cargas de trabajo impredecibles

* DynamoDB Accelerator (DAX):
    * Caché en memoria totalmente administrada
    * Son cachés
    * No requiere modificación de lógica
    * 5 minutos de TTL

* DynamoDB Streams
    * Casos de uso
        * Reaccionar a los cambios en tiempo real
        * Análisis de uso en tiempo real
        * Invocar AWS Lambda en los cambios realizados en la tabla de DynamoDB
    * DynamoDB Streams
        * Retención de 24 horas
        * Lambda and EC2 (With KCL Adapter)
    * Amazon Kinesis Streams
        * Un año de retención
        * Kinesis Data Firehose