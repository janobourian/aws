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
