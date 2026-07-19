# Storage Gateway

* AWS is pushing for "hybrid cloud"
* This service is a bridge between the cloud and on-premises
* AWS Storage Cloud Native Options
    * Block
        * Amazon EBS
        * EC2 Instance Store
    * File
        * Amazon EFS, for Linux (NFS)
        * Amazon FSx, for Windows (SMB)
    * Object
        * Amazon S3
        * Amazon Glacier

## Amazon S3 File Gateway

* NFS or SMB protocol 
* Bucket access using IAM role for each File Gateway
* SMB Protocol ha sintegration with Active Directory for user authentication

## Volume Gateway

* Block storage using iSCSI protocl backed by S3
* Backed by EBS snapshots which can hel restore on-premises volumes!
* Cached volumes or Stored volumes

## Tap Gateway

* Backup of on-premises tape infrastructure to S3 or Glacier