# RDS + Aurora + ElastiCache

## RDS: Relational Database Service

It is a managed DB service for DB use SQL as a query language:

* PostgreSQL
* MySQL
* MariaDB
* Oracle
* Microsoft SQL Server
* IBM DB2
* Aurora (AWS Propietary database)

Benefits:

* RDS is a managed service
* Automated provisioning, OS patching
* Read replicas for improved read performance
* Multi AZ setup for DR (Disaster Recovery)
* But you can not SSH into yout instances
* You can use EBS

Storage Auto Scaling:

* Helps you increase storage on your RDS DB instance dynamically
* Avoid manually scaling your database storage
* You have to set Maximum Storage Threshold
* Useful for applications with unpredictable workloads
* Automatically modify storage if:
  * Free storage is less tan 10% of allocated storage
  * Low-storage lasts at least 5 minutes
  * 6 hours have passed since last modification

## Read Replicas vs Multi AZ

### Read replicas

* Up to 15 Read Replicas
* Within AZ, cross AZ or Cross Region
* Replication is ASYNC, so read are eventually consistent
* Used to scale out read-heavy database workloads
* Can be promoted to become a standalone database instance
* Applications must update the connection string to leverage read replicas
* In the same region you do not pay fee for data goes from one

### Multi AZ (Disaster Recovery)

* SYNC replication from Master DB
* One DNS name - automatic failover
* Increase availability
* Failover in case of loss of AZ, loss of network, instance or storage failure
* No manual intervention in apps
* Not used for scaling
* The read replicas can be setup as Multi AZ Disaster Recovery

### RDS - From Single-AZ to Multi-AZ

* Zero downtime operation
* Just click on "modify" for the database
