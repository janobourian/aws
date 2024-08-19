# Databases in AWS

* Databases type:
    * RDBMS (OLTP): 
        * RDS
        * Aurora
    * NoSQL:
        * DynamoDB
        * ElastiCache
        * Neptune
        * DocumentDB
        * Keyspaces
    * Object store:
        * S3
        * Glacier
    * Data Warehouse:
        * Redshift (OLAP)
        * Athena
        * EMR
    * Search:
        * OpenSearch
    * Graphs:
        * Amazon Neptune
    * Ledger:
        * Amazon Quantum Ledger Database
    * TimeSeries:
        * Amazon Timestream

* Amazon RDS:
    * Managed:
        * PostgreSQL
        * MySQL
        * Oracle
        * SQL Server
        * DB2
        * MariaDB
    * Provisioned RDS Instance Size and EBS Volume Type and Size
    * Auto-scaling
    * Support:
        * Read replicas
        * Multi AZ
        * Multi Region
    * Security:
        * Iam
        * Security Groups
        * KMS
        * SSL in transit
    * Automated Backup with point in time restore feature (up to 35 days)
    * Manual DB Snapshot
    * Managed and Scheduled maintenance
    * Support for IAM authentication, integration with Secrets Manager
    * RDS Custom for access to and customize the underlying instance (Oracle and SQL Server)

* Amazon Aurora (RDS):
    * Compatible with PostgreSQL and MySQL
    * Storage:
        * Data stored in 6 replicas, accross 3 AZ
        * Compute: CLuster of DB Instance accross Multiple AZ
        * Clúster: Custome endpoints for writer and reader
    * Security as RDS
    * Aurora Serverless
    * Aurora Global
    * Aurora Machine Learning
    * Aurora Database Cloning: New cluster from existing one, faster than restoring a snapchost

* Amazon ElastiCache:
    * Managed Redis / Memchached
    * You need to modify your code
    * The maintainance is similar to RDS

* DynamoDB:
    * NoSQL
    * AWS property technology
    * Capacity modes:
        * provisioned capacity
        * on-demand capacity
    * DAX: for read cache
    * DynamoDB Streams:
        * Integration with Lambda
        * Integration with Kinesis Data Streams
    * Global Table Feature: active-active setup
    * Automated Backups up to 35 days
    * Export to S3 withput using RCU