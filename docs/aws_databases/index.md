# Index

* Amazon RDS
* Amazon Aurora
* ElastiCache

## RDS Read Deplicas and Multi-AZ

* RDS Read Replicas:
    * Used to increase read performance
    * Asynchronous replication
    * Can be promoted to standalone database instance
    * Can be created in different regions for disaster recovery
    * Up to 15 Read Replicas
    * Whithin AZ, Cross AZ or Cross Region
    * Replication is ASYNC, so reads are eventually consistent
    * Replicas can be promoted to their own DB
    * Applications must update the connection string to leverage read replicas

## Read replicas - Use Cases

* Scale out beyond the capacity constraints of a single DB instance for read-heavy database workloads
* Support read-only applications and business intelligence tools
* Perform data migrations with minimal downtime
* Disaster recovery by replicating data to a different region
* Offload read traffic from the primary database to improve performance
* Use read replicas to serve read traffic while the primary database handles write operations, improving overall application performance and scalability.

## RDS Read Replicas - Network Cost

* Data transfer between the primary database and read replicas is subject to standard AWS data transfer charges.
* Free: Same Region/ Different AZ
* Charged: Cross Region

## RDS Multi AZ (Disaster Recovery)

* It happens thanks a One DNS name in front of the database layer for automatic failover
* RDS Multi-AZ:
    * Provides high availability and failover support for DB instances
    * Synchronous replication to a standby instance in a different AZ
    * Automatic failover in case of primary instance failure
    * Standby instance is not accessible for read or write operations
    * Designed for disaster recovery and high availability, not for read scaling

## RDS - From Single AZ to Multi AZ

* Zero downtime operation
* RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone (AZ)
* Process:
    * A snapshot is taken
    * A new DB is restored from the snapshot in a new AZ
    * Synchronization is established between the two databases