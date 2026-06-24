# Amazon FSx

Launch 3rd party high-performance file systems on AWS

## Amazon FSx for Windows File Server

* It is a fully managed Windows file system share drive
* Supports SMB protocol and Windows NTFS
* Microsoft Active Directory integration, ACLs, user quotas
* Can be mounted on Linux EC2 instances
* Can be accessed from your on-premises infrastructure
* Can be configured to be Multi-AZ
* Data is backed-up to S3

## Amazon FSx for Lustre

* Lustre = Linux + Cluster
* Machine Learning and High Performance Computing (HPC)
* FSx Lustre: 
    * Scratch File System
        * Temporary storage
        * Data is not replicated
    * Persistent File System
        * Long-term storage
        * Data is replicated within same AZ

## Amazon FSx for NetApp ONTAP

* Managed NetApp ONTAP on AWS

## Amazon FSx for OpenZFS

* Up to 1'000,000 IOPS with < 0.5ms latency
* Snapshots compression and low-cost
* Point-in-time instantaneous cloning (helpful for testing new workloads)