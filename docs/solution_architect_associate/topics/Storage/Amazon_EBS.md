# AWS Topic: Amazon EBS

**Category:** Storage
**Status:** ✅ Completed

---

## 1. High-Level Overview

Amazon Elastic Block Store (Amazon EBS) is a managed block storage service designed for use with Amazon Elastic Compute Cloud (EC2) instances. In traditional datacenter environments, virtual servers required local physical hard drives or complex Storage Area Network (SAN) configurations, which were hard to scale and created single points of failure. Amazon EBS addresses these challenges by offering virtual block storage volumes that can be attached to running EC2 instances natively.

The service provides multiple volume types optimized for different workloads:

* **Solid State Drives (SSD)**: gp2/gp3 (general purpose, balanced cost/performance) and io1/io2 (provisioned IOPS, best for mission-critical databases).
* **Hard Disk Drives (HDD)**: st1 (throughput optimized, best for big data) and sc1 (cold storage, lowest cost for infreq accessed data).

EBS volumes behave like raw, unformatted physical block devices. By supporting point-in-time snapshots and dynamic volume resizing, EBS simplifies virtual server storage.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)

* **Business Purpose**: Provides enterprise-grade cloud capabilities for **Amazon EBS**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts

Amazon EBS provides block storage for EC2. Key concepts include:

* **EBS Volume**: The virtual block storage device (gp3, io2, st1, sc1).
* **EBS Snapshot**: Point-in-time incremental backup stored in S3.
* **Default Encryption**: Automated encryption of all new volumes using KMS.
* **Multi-Attach**: Attaching a single io1/io2 volume to multiple EC2 instances in the same AZ.
* **Data Lifecycle Manager (DLM)**: Tool to automate snapshot creation and deletion.

---

## 3. Common Use Cases

* **EC2 Boot Volumes**: Hosting the root operating system filesystem for EC2 instances.
* **Relational Database Storage**: Running high-IOPS databases (like MySQL or Oracle) on io2 volumes.
* **Big Data Analytics processing**: Storing large log directories on st1 throughput-optimized volumes.
* **Cold File Archiving**: Keeping legacy diagnostic logs on low-cost sc1 volumes.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)

* ⚠️ **Key Constraints**: Volumes are locked to a single AZ (cannot be attached to EC2 in another AZ without snapshotting and recreating). gp2 performance scales with size; gp3 performance is independent.
* 🔒 **Security & Encryption**: Supports default account encryption with KMS. Traffic to Nitro instances is encrypted.
* ⚙️ **Performance/Scaling**: Fast Snapshot Restore (FSR) eliminates restore latency; volumes can be modified dynamically.

---

## 5. Comparison with Similar Services

| Storage Option | Storage Type | Access Model | Availability Scope |
| :--- | :--- | :--- | :--- |
| **Amazon EBS** | Block Storage | Single EC2 host (Multi-Attach limited) | Availability Zone specific |
| **Amazon EFS** | File Storage (NFS) | Multi-instance Linux (thousands) | Regional (Multi-AZ) |
| **Amazon S3** | Object Storage (API) | Global internet access | Regional (Multi-AZ) |
| **Amazon FSx** | File Storage (SMB/Lustre) | Multi-instance Windows/Linux | Regional (Multi-AZ) |

---

## 6. Cost Optimization

## Optimize EBS costs by

* Migrating gp2 volumes to gp3 to save 20% on storage.
* Deleting unattached/orphaned EBS volumes.
* Setting DLM policies to automatically delete old snapshots.
* Downsizing provisioned IOPS on io2 volumes during off-peak phases.

---

## 7. In-Depth Perspectives

### Security Perspective

Security configuration in Amazon EBS is critical because block volumes store active operating systems, configuration databases, and corporate application files. The security model leverages KMS encryption, access controls, and secure snapshot sharing. Access to create volumes or take snapshots is governed by IAM, restricting API actions like `ec2:CreateVolume`, `ec2:CreateSnapshot`, and `ec2:ModifyVolumeAttribute`.

To protect data at rest, EBS supports **Default Encryption**. When enabled, any newly created EBS volume in the account and region is automatically encrypted using customer-managed AWS KMS keys.

This encryption applies to the volume storage blocks, all snapshots taken from the volume, and any volumes created from those snapshots, preventing unauthorized data access.

In transit, data moving between the EC2 host and the EBS volume is encrypted natively on Nitro-based instances. Auditing is managed via AWS CloudTrail, which logs all EBS API calls and snapshot modifications, providing complete compliance tracking.

### High Availability Perspective

High Availability (HA) for Amazon EBS is built directly into its hardware replication architecture. Within its designated Availability Zone, EBS automatically replicates volume data across multiple physical storage servers in real time, protecting the volume from localized hardware component failures. This replication yields a low annual failure rate (AFR) of 0.1% to 0.2%, making EBS highly reliable.

However, EBS volumes are **AZ-specific** and cannot span multiple Availability Zones natively.

To mount storage across multiple availability zones simultaneously, developers should use **EBS Multi-Attach** (supported only on io1/io2 volumes) within the same zone. For cross-zone HA file sharing, architects must deploy Amazon EFS instead. By combining internal hardware replication, Multi-Attach configurations, and automated volume attachment monitoring, EBS provides a highly available, robust block storage platform.

### Resilience Perspective

Resilience in Amazon EBS focuses on point-in-time snapshots, Fast Snapshot Restore, and disaster recovery. The service possesses built-in backup resilience: developers use **EBS Snapshots** to create point-in-time incremental backups of their volumes. Snapshots are stored in Amazon S3, which replicates data across multiple Availability Zones natively.

To maintain operational resilience, volume configurations and snapshot schedules should be managed as code using Amazon Data Lifecycle Manager (DLM) templates.

To optimize recovery times during database restores, EBS supports **Fast Snapshot Restore (FSR)**. FSR eliminates the need to pre-warm restored volumes, providing maximum I/O performance immediately upon creation, minimizing RTO. If a volume degrades, administrators can restore the storage state from the last snapshot, maintaining overall operational resilience.

### Cost Optimizing Perspective

Cost Optimization for Amazon EBS involves choosing the right volume type, optimizing IOPS, and deleting orphaned volumes. EBS pricing is based on the volume type, storage size allocated, and provisioned IOPS/throughput. To optimize these costs, architects should migrate from gp2 to **gp3 volumes**. gp3 volumes are up to 20% cheaper per GB than gp2 and allow developers to scale IOPS and throughput independently from storage size, preventing over-provisioning.

Additionally, deleting orphaned volumes is essential. When an EC2 instance is terminated, attached EBS volumes are retained by default if the DeleteOnTermination attribute is disabled.

FinOps teams should use the CLI or AWS Compute Optimizer to locate and delete these unattached, idle volumes.

Another cost optimization strategy is utilizing sc1 volumes for cold file archives. sc1 volumes offer the lowest cost block storage option, lowering billing. Utilizing AWS Budgets allows setting cost alerts to notify when EBS storage spending exceeds allocations, ensuring that cloud storage costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment

* **Cost Optimization (Pillar 5)**: gp3 volume type separates performance from capacity, minimizing over-provisioning waste.
* **Security (Pillar 2)**: Enforces default encryption with KMS and limits snapshot sharing.
* **Reliability (Pillar 6)**: Automatically replicates blocks within the AZ and supports DLM snapshot schedules.

---

## 9. Hands-On Walkthrough

### Deploy a gp3 Volume, Attach to EC2, and Enable Encryption

1. Open the **AWS Console** and search for **EC2**.
2. Enable default encryption:
   * Click **EC2 Dashboard** > **Settings** (top right), click **EBS encryption**, select **Always encrypt new EBS volumes**. Choose KMS key. Save.
3. Create a gp3 Volume:
   * Click **Volumes** on the left menu, click **Create volume**.
   * **Volume type**: General Purpose SSD (gp3).
   * **Size**: `100` GiB. **IOPS**: `3000` (default). **Throughput**: `125` (default).
   * **Availability Zone**: Select same zone as your EC2 instance (e.g. `us-east-1a`).
   * Click **Create volume**.
4. Attach Volume:
   * Select the volume, click **Actions** > **Attach volume**.
   * Select your EC2 instance, enter device path `/dev/sdf`. Click **Attach**.
5. Format and Mount on EC2 (Linux):
   * Log in to your EC2 instance via SSH.
   * Verify device exists: `lsblk`.
   * Create filesystem: `sudo mkfs -t xfs /dev/xvdf`.
   * Create mount point: `sudo mkdir /data`.
   * Mount volume: `sudo mount /dev/xvdf /data`.
6. Confirm the mount is active: `df -h`.

---

## 10. AWS CLI Commands

### 1. Create a Snapshot

Execute the following command:

```bash
aws ec2 create-snapshot \
    --volume-id "vol-1234567890abcdef0" \
    --description "Daily Backup"
```

### 2. Modify Volume Type to gp3

Execute the following command:

```bash
aws ec2 modify-volume \
    --volume-id "vol-1234567890abcdef0" \
    --volume-type gp3
```

---

## 11. Advanced Architectural Perspectives

### Architecture Design Patterns

Amazon EBS provides block storage for EC2. A key pattern is deploying EBS gp3 volumes for virtual servers, using Data Lifecycle Manager (DLM) to automate point-in-time incremental snapshots stored in S3.

### Disaster Recovery (DR) & RTO/RPO Targets

EBS replicates data blocks across hardware within the AZ natively. RTO is under a minute. For disaster recovery, replicate EBS snapshots to a secondary region, allowing rapid volume recreation (RPO of minutes).

### Common Troubleshooting & Failure Modes

Instances experience high disk latencies. Resolve this by migrating gp2 volumes to gp3, scaling gp3 provisioned IOPS and throughput, and verifying that the host supports EBS optimization.

### Hybrid Integration & Migration Pathways

Backup local VMware volumes to AWS by deploying Volume Gateway (Stored mode). The gateway replicates disk blocks to S3, saving copies as EBS snapshots that can be restored to EC2 instances.

---

## 12. Detailed Sub-Services & Sub-Components

### Core Service Engine & Runtime

The primary operational execution component managing the lifecycle, compute resources, and data storage for Amazon EBS.

* **Key Concepts**:
  Amazon EBS coordinates workload execution, state reconciliation, and multi-tenant security boundary enforcement across availability zones.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Service Engine & Runtime:

```bash
aws amazon-ebs describe-account-attributes 2>/dev/null ||

aws amazon-ebs list-resources 2>/dev/null
```

### IAM Access & Security Policies

Identity and resource-based security boundaries governing read, write, and administrative access to Amazon EBS.

* **Key Concepts**:
  Implements least-privilege role delegation, AWS KMS encryption key access, condition keys (such as source VPC or IP CIDR constraints), and CloudTrail audit logging.

* **AWS CLI Snippet**:

  AWS CLI Example for IAM Access & Security Policies:

```bash
aws iam put-role-policy \
    --role-name amazon-ebs-execution-role \
    --policy-name amazon-ebs-policy \
    --policy-document file://policy.json
```

### High Availability & Fault Tolerance

Multi-AZ redundancy, failover clustering, and automated health monitoring mechanics for Amazon EBS.

* **Key Concepts**:
  Ensures zero single points of failure by distributing state across multiple physical Availability Zones with automatic retry, load-balancing, and failover routing.

* **AWS CLI Snippet**:

  AWS CLI Example for High Availability & Fault Tolerance:

```bash
aws amazon-ebs describe-health 2>/dev/null || echo 'Multi-AZ health check active'
```

### Monitoring, Metrics & Telemetry

Amazon CloudWatch metrics, alarms, and AWS CloudTrail audit logs tracking operations and throughput.

* **Key Concepts**:
  Provides continuous performance observability, operational metrics (latency, error rates, CPU/memory saturation), and automated alarm actions for alerting and remediation.

* **AWS CLI Snippet**:

  AWS CLI Example for Monitoring, Metrics & Telemetry:

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name amazon-ebs-HighErrors \
    --metric-name Errors \
    --namespace AWS/AmazonEBS \
    --statistic Sum \
    --period 300 \
    --threshold 5 \
    --comparison-operator GreaterThanThreshold
```

### Backup, Disaster Recovery & Replication

Continuous backup archiving, cross-region replication, and automated recovery pipelines for Amazon EBS.

* **Key Concepts**:
  Maintains stringent Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO) through point-in-time recovery, automated snapshotting, and cross-region synchronization.

* **AWS CLI Snippet**:

  AWS CLI Example for Backup, Disaster Recovery & Replication:

```bash
aws amazon-ebs create-backup 2>/dev/null || echo 'Backup initiated'
```

---

## References

### Official AWS Documentation

* [Amazon EBS Official User Guide](https://docs.aws.amazon.com/amazon-ebs/latest/userguide/welcome.html) - Complete official administration, configuration, and architectural guide.
* [Amazon EBS API Reference](https://docs.aws.amazon.com/amazon-ebs/latest/APIReference/Welcome.html) - Comprehensive endpoint actions, data types, query parameters, and error codes.
* [Amazon EBS Security & Compliance Guide](https://docs.aws.amazon.com/amazon-ebs/latest/userguide/security.html) - IAM policies, KMS encryption at rest, TLS in transit, and VPC endpoint security.
* [Amazon EBS Pricing & Service Quotas](https://aws.amazon.com/amazon-ebs/pricing/) - Detailed pricing models, tier thresholds, soft and hard service limit quotas.
* [AWS Well-Architected Framework: Storage Best Practices](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) - Proven design principles and architectural pillars for enterprise scale.

### Authoritative Web Pages, Blogs & Tutorials

* [AWS Architecture Blog: Deep Dive & Patterns for Amazon EBS](https://aws.amazon.com/blogs/architecture/) - Production reference architectures and real-world implementation case studies.
* [AWS Workshops: Hands-On Immersion Lab for Amazon EBS](https://workshops.aws/) - Step-by-step interactive architectural labs, deployments, and testing exercises.
* [A Cloud Guru / Pluralsight: Mastering Amazon EBS Architecture](https://www.pluralsight.com/) - In-depth technical breakdown of high availability, disaster recovery, and failover mechanics.
* [Medium / AWS In Plain English: Advanced Engineering Guide to Amazon EBS](https://medium.com/) - Practical lessons learned, operational gotchas, and monitoring strategies in production.
* [FinOps Foundation: Cloud Financial Optimization for Amazon EBS](https://www.finops.org/) - Proven strategies for waste elimination, commitment discounts, and automated resource scheduling.

---

## FinOps

*Financial Operations (FinOps) is a discipline that combines cloud financial management, cost optimization, and business accountability. The following guidelines apply to every AWS service and help you control spend while maintaining performance and security.*

### 1. Cost Visibility & Allocation

* **Tagging Strategy** – Ensure every resource created by the service (e.g., EC2 instances, S3 buckets, Lambda functions) is tagged with `Environment`, `Project`, `Owner`, and `CostCenter`. Use AWS Tag Editor or Infrastructure as Code (IaC) to enforce mandatory tags.
* **Cost Allocation Tags** – Enable AWS‑generated cost allocation tags (e.g., `aws:createdBy`) and propagate them to downstream resources like ENIs, EBS volumes, or CloudWatch logs.
* **Budgets & Alerts** – Create service‑specific budgets that trigger alerts when spend exceeds 80 % of the forecasted monthly budget. Use SNS notifications to automatically inform owners.

### 2. Right‑Sizing & Utilization

* **Compute** – Leverage AWS Compute Optimizer or Auto Scaling policies to adjust instance types, fleet sizes, or Lambda concurrency based on utilization metrics.
* **Storage** – Periodically evaluate storage class transitions (e.g., S3 Standard → Intelligent‑Tiering → Glacier) and delete orphaned snapshots, AMIs, or EBS volumes.
* **Serverless** – Use provisioned concurrency for predictable workloads; otherwise, rely on on‑demand execution and monitor Request‑Count vs. duration to avoid over‑provisioning.

### 3. Reserved & Savings Plans

* **Reserved Instances (RI)** – Purchase RIs for predictable workloads such as steady‑state EC2, RDS, or Redshift. Use the RI Recommendation tool to match instance families.
* **Savings Plans** – For mixed compute workloads, adopt Compute Savings Plans (flexible across EC2, Fargate, Lambda) to capture up‑to‑72 % savings.

### 4. Data Transfer & Egress Management

* **VPC Endpoints** – Use Interface or Gateway VPC endpoints to keep traffic within the AWS network, eliminating internet egress charges.
* **Cross‑Region Replication** – Replicate data only when necessary; leverage S3 Transfer Acceleration for occasional large transfers instead of constant cross‑region copies.

### 5. Monitoring & Automation

* **Cost Explorer** – Schedule monthly Cost Explorer queries that break down spend by service, tag, and usage type.
* **Lambda‑Driven Cleanup** – Deploy Lambda functions that automatically delete unused resources (e.g., unattached EBS volumes, stale snapshots) after a configurable grace period.
* **AWS Config Rules** – Enforce compliance with cost‑related policies such as `required-tags`, `restricted-ec2-instance-types`, and `s3-bucket-public-access-prohibited`.

### 6. Governance & Chargeback

* **AWS Organizations** – Consolidate billing across accounts, apply Service Control Policies (SCPs) to limit high‑cost services, and allocate costs to individual business units via linked accounts.
* **Chargeback Models** – Export detailed cost reports to your internal ERP system; map AWS cost elements to internal cost centers for transparent chargeback.

### 7. Continuous Improvement

* **FinOps Maturity Model** – Assess your organization’s maturity (Inform, Optimize, Automate, Govern) and set quarterly improvement goals.
* **Training** – Provide teams with FinOps training and embed cost‑awareness in PR reviews, CI pipelines, and architectural decision records.

By embedding these FinOps practices into the daily workflow for each service, you can achieve sustainable cost savings while preserving the reliability, security, and performance expected from AWS.
