# Index

* Amazon RDS
* Amazon Aurora
* ElastiCache
* Amazon MemoryDB for Redis

## RDS and Aurora | Backup and Monitoring

* Automated backups:
  * Daily full backu of the database
  * Transaction logs are backed up every 5 minutes
  * Retention period of up to 35 days (in Aurora can not be disabled)
  * Point-in-time recovery
* Manual DB Snapshots:
  * Manually triggered by the user
  * Retention period until you delete them

* Trick: in a stopped RDS database, you will still pay for storage, If you plan on stopping it for a long time, you should snapshot and restore instead

* Restoring options:
  * You can create a new database based on a backup or a snapshot
  * For RDS you can use S3
  * For Aurora cluster you can use S3

* Aurora Database Cloning:
  * Create a copy of your database in minutes
  * It is a copy of the data, but it shares the same underlying storage
  * You can create a clone for development and testing purposes without incurring additional storage costs

## RDS Security

* RDS provides encryption at rest and in transit:
  * Encryption at rest using AWS Key Management Service (KMS)
  * Encryption in transit using SSL/TLS
  * RDS integrates with AWS Identity and Access Management (IAM) for access control:
    * You can create IAM policies to control who can access your RDS resources and what actions they can perform

## RDS Proxy

* RDS Proxy is a fully managed, highly available database proxy for Amazon RDS
* It helps improve application availability and scalability by managing database connections efficiently
* RDS Proxy supports connection polling, which allows it to reuse database connections and reduce the overhead
* It also provides automatic failover and load balancing for read replicas
