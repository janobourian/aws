# Aurora

* Aurora is a propietary technology from AWS
* Compatible with MySQL and Postgres
* Aurora is AWS cloud optimized and claims 5x performance improvement over MySQL on RDS, over 3x the performance of Postgres on RDS
* Aurora storage automatically grows in increments of 10GB up to 256TB
* Aurora can have up to 15 replicas and the replication process is faster than MySQL (sub 10ms replica lag)
* Aurora replicas can be promoted to standalone databases
* Failover in Aurora is instantaneous. It is HA native.
* Aurora costs more than RDS (20% more), but is more efficient

## Aurora High Availability and Read Scaling

* Six copies of your data across 3 AZ
* One Aurora Instance takes writes (master)
* Up to 15 Aurora Replicas take reads (replicas)
* Automated failover for master in less than 30 seconds
* Support for Cross Region Replication

## Aurora DB Cluster

* In the top of it we have the Writer Endpoint and the Reader Endpoint
* In the bottom of it we have the Shared storage volume Auto Expanding from 10GB to 256TB

## Feature of Aurora

* Automatic fail-over
* Backup and Recovery
* Isolation and security
* Industry compliance
* Push-button scaling
* Automated Patching with Zero Downtime
* Advanced Moonitoring
* Routine Maintenance
* Backtrack: restore data at any point of time without using backups

## Aurora Replicas - Auto Scaling

* Aurora Replicas can be automatically added and removed based on the load of your cluster
* You can set up a target Aurora Replicas CPU utilization percentage, and Aurora will automatically add

## Aurora - Custom Endpoints

* Aurora allows you to create custom endpoints to direct traffic to specific instances in your cluster

## Aurora Serverless

* Aurora Serverless is an on-demand, auto-scaling configuration for Aurora
* It automatically starts up, shuts down, and scales capacity up or down based on your application's
* It is ideal for infrequent, intermittent, or unpredictable workloads
* It can be used for development, testing, and production workloads
* No capacity planning needed, pay per second, can be more cost effective.

## Global Aurora

* Global Aurora is a multi-master, multi-region configuration for Aurora

* Aurora Cross Region Read Replicas:
    * Useful for disaster recovery
    * Simple to put in place
* Aurora Global Database (recommended):
    * 1 primary region (read/write)
    * Up to 10 secondary regions (read only), replication lag is less than 1 second
    * Fast local reads with low latency in each region
    * Disaster recovery with fast local recovery time (typically less than 1 minute)
    * Up to 16 Read Replicas per secondary region

## Machine Learning

* You can apply ML services like SageMaker and Comprenhend to use your Database information

## Babelfish for Aurora PostgreSQL

* Babelfish for Aurora PostgreSQL is an extension that enables Aurora PostgreSQL to understand the SQL Server wire protocol and T-SQL language