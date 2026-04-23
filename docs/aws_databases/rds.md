# RDS

* Relational Database Service:
    * Use SQL as a query language
    * Engines:
        * Postgres
        * MySQL
        * MariaDB
        * Oracle
        * Microsoft SQL Server
        * IBM DB2
        * Aurora
* RDS is a managed service:
    * Automated provisioning
    * OS patching
    * Continuous backups and restores
    * Monitoring dashboards
    * Read replicas
    * Windows for upgrades
    * Scaling capability
    * Storage backed by EBS
    * You can not use SSH into your instances
* RDS Storage Auto Scaling
    * Helps you increase storage on your RDS DB instance dynamically
    * When RDS detects you are running out of free database storage, it scales automatically
    * Avoid manually scaling your database storage
    * You have to set Maximum Storage Threshold (maximum limit for DB storage)
    * Automatically modify storage if:
        * Free storage is less than 10% of allocated storage
        * Low-storage lasts at least 5 minutes
        * 6 hours have passed since last modifications
    * Useful for applications with unpredictable workloads
    * Supports all RDS database engines