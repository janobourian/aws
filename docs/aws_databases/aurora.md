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
* Backup and Re overy
* Isolation and security
* Industry compliance
* Push-button scaling
* Automated Patching with Zero Downtime
* Advanced Moonitoring
* Routine Maintenance
* Backtrack: restore data at any point of time without using backups