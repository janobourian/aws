# Servicios de Base de Datos, Migración y Contenedores

## Bases de Datos Relacionales y No relacionales

* Relacionales:
    * SQL is the best fit for them
    * PostgreSQL, MySQL, SQL Server, Oracle, MAriaDB
* NoSQL:
    * Esquemas flexibles
    * Escalabilidad: diseñado para escalar mediante clústeres
    * JSON: Javascript Object Notation is a common format
    * MongoDB, Cassandra, Redis, Memcached

### SQL

* Amazon Aurora
* Amazon RDS

### NoSQL

* Amazon DocumentDB
* Amazon ElasticCache
* Amazon KeySpaces

## Amazon RDS

* Relational Database Service
* PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, Aurora

* Key points:
    * Réplicas
    * Configuración Multi AZ para DR (Disaster Recovery)
    * Respaldado por EBS
    * No puedes conectarte mediante SSH a tus instancias

## Amazon Aurora

* Patentada por AWS
* PostgreSQL y MySQL son compatibles con Aurora
* De 10GB hasta 128TB
* Cuesta un 20% más que RDS, pero es más eficiente
* No en el nivel gratuito

* Aurora Serverless:
    * Pago por segundo
    * Casos de uso:
        * Cargas de trabajo poco frecuentes, intermitentes o impredecibles

* Read Replicas:
    * Puede crear hasta 15 réplicas
    * Sólo se escriben en la instancia principal
* Multi AZ:
    * Los datos sólo se van a leer y escribir en la principal
    * Sólo como conmutación de error
* Multi Region:
    * Recuperación ante desastres 
    * Rendimiento local 
    * Costo de replicación

### Laboratorio

## ElasticCache

* Administra Redis o Memcached
* Almacena en memoria la información para aliviar la carga a la base de datos
* Discount: https://pages.awscloud.com/GLOBAL-ln-GC-Traincert-Associate-Certification-Challenge-Registration-2024.html

## Amazon DynamoDB

* NoSQL
* No admite combinación de consultas
* Se escalan horizontalmente

* Amazon DynamoDB:
    * High availability
    * IAM for security
    * Permite el uso de programación basada en eventos con DynamoDB Streams
    * Clases de tabla de acceso estándar y poco frecuente (IA)
    * Components:
        * Tables
        * Primary Key al momento de la creación
        * Items (filas)
            * Maximum Size: 400kb
        * Data types:
            * Escalares: String, Number, Binary, Boolean, Null
            * Documentos: List, Map
            * Conjuntos: String set, Number set, Binary set
    * Primary keys: 
        * HASH
    * Partition Key + Sort Key:
        * HASH + RANGE
    * Amazon DynamoDB en Big Data:

* DynamoDB read/write capacity:
    * Provisioned Mode:
        * Pago por unidades de capacidad de lectura y escritura aprovisionadas
    * On-Demand Mode:
        * Pago por lo que usas
    * Se puede cambiar el modo cada 24 horas. 

* Modo de capacidad R/W - Provisionado:
    * Read Capacity Units (RCU)
        * ConsistentRead: True
        * Eventually Consistent Read -> 2 RCU por segundo de hasta 4KB
        * Strongly Consistent Read -> 1 RCU por segundo de hasta 4KB
    * Write Capacity Units (WCU)
        * Representa una escritura por segundo para un elemento de hasta 1KB
        * Se redonde hacia arriba

* Particiones Internas:
    * Maximum of (# of partitions by capacity, # of partitions by size)

* DynamoDB Throttling:
    * Si superamos las RCU o WCU aprovisionadas
    * Razones:
        * Hot Keys
        * Hot partitions
        * Items muy grandes

* DynamoDB using SDK:
    * PutItem
    * UpdateItem
    * ConditionalWrites
    * GetItem:
        * ProjectionExpression se puede especificar para recuperar solo ciertos atributos
    * DeleteItem
    * DeleteTable

* DynamoDB - Query:
    * KeyConditionExpression:
        * Partition Key (=)
        * Sort Key (another expressions)
    * FilterExpression:
        * Atributos que no son clave
    * Se devuelve:
        * El número de ítems en Limit
        * Hasta 1 MB
        * Se puede paginar
    * Scan (usualmente en consola)

* DynamoDB - Operaciones por lote:
    * BatchWriteItem
    * BatchGetItem
    * Casos de uso:
        * Escrituras muy frecuentes

* PartiQL:
    * Ejecución de consultas en varias tablas de DynamoDB
    * Se puede ejecutar desde:
        * AWS Management Console
        * NoSQL Workbench for DynamoDB
        * DynamoDB APIs
        * AWS CLI
        * AWS SDK

* Indexes:
    * Local Secondary Index (LSI)
    * Global Secondary Index (GSI)

* DynamoDB Accelerator (DAX):
    * Caché en memoria totalmente administrada
    * No requiere la modificación de la lógica de la aplicación
    * 5 minutos for TTL
    * Hasta 10 nodos en el clúster
    * Mínimo 3 nodos para producción (recomendación)

* DynamoDB Streams:
    * Flujo ordenado de modificaciones a nivel de elemento
    * Retención de datos durante un máximo de 24 horas
    * Casos de uso:
        * Reaccionar a los cambios en tiempo real
        * Analítica
        * Insertar en OpenSearch Service
        * Implementación de las réplicas entre regiones
        * Los registros no se llenan de manera retroactiva
    * DynamoDB Stream and AWS Lambda
    * Puede trabajar como Trigger

* DynamoDB TTL
    * Elimina automáticamente items después de una marca de tiempo de caducidad
    * Se debe agregar un valor numérico en la tabla con el nombre TTL

* DynamoDB Objetos grandes:
    * Guarda la metadata solamente

* Seguridad
    * VPC Endpoints disponibles para acceder a DynamoDB sin usar internet
    * Acceso totalmente controlado por IAM
    * Cifrado en reposo mediante KMS
    * Cifrado en tránsito mediante SSL/TLS
    * Copia de seguridad y restauración disponible
    * Global Tables:
        * Multiregión
        * Active-Active
    * Amazon Database Migration Service se puede utilizar para migrar DynamoDB de Mongo, Oracle, MySQL, S3

## Amazon DocumentDB

* Para almacén de documentos similar a MongoDB

## Amazon MemoryDB for Redis

* Base de datos en memoria para Redis
* Casos de uso:
    * Aplicaciones Web y móviles
    * Juegos en línea
    * Transmisión de medios

## Amazon Keyspaces (Apache Cassandra)

* Serverless
* Es básicamente un Apache Cassandra
* Apache Cassandra:
    * Base de datos distribuida NoSQL de código abierto
* CQL: Cassandra Query Language

## Amazon Neptune

* Base de datos de grafos
* Ejemplo: Red Social

## Amazon TimeStream

* Para series de tiempo 
* Compatibilidad con SQL
* Funciones integradas de análisis de series de temporales