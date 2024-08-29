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
