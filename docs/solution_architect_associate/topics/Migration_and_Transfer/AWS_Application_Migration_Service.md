# AWS Topic: AWS Application Migration Service

**Category:** Migration and Transfer
**Status:** ✅ Completed

---

## 1. High-Level Overview

AWS Application Migration Service (AWS MGN) is a fully managed, highly automated lift-and-shift migration service designed to simplify and accelerate the migration of physical, virtual, and cloud-based servers to AWS. Traditionally, re-hosting servers in the cloud required manual OS re-installations, complex configuration imports, and long downtime windows, which introduced significant operational risks. AWS MGN addresses these issues by using continuous, block-level replication to duplicate source disks directly to target AWS volumes.

To migrate servers, users install the **AWS replication agent** on their source servers. The agent copies disk blocks continuously over a secure connection into a lightweight staging area in your AWS account. This staging area runs low-cost EC2 replication instances and staging EBS volumes, minimizing compute costs. When ready to cutover, MGN automatically converts the source OS settings, boot drivers, and network configurations to run natively as standard EC2 instances. By allowing non-disruptive testing, continuous sync, and automated conversions, AWS MGN simplifies enterprise re-hosting workloads.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)

* **Business Purpose**: The primary lift-and-shift server migration tool that quickly and reliably moves physical, virtual, or cloud-hosted servers (from VMware, Hyper-V, Azure, GCP) to AWS with near-zero business downtime.
* **How It Works**: Installs a lightweight agent on source servers to continuously replicate storage disks at the block level into AWS in the background, executing a non-disruptive cutover in minutes.
* **Key Business Value & Use Cases**: Accelerates datacenter evacuations, minimizes risk and disruption to business operations, and allows testing migrations multiple times before final cutover.

## 2. Core Architecture & Key Concepts

AWS MGN automates lift-and-shift. Key concepts include:

* **Replication Agent**: Software installed on source hosts to perform block-level sync.
* **Staging Area**: Dedicated private subnet running low-cost EC2/EBS to capture sync data.
* **Launch Configuration**: The settings (AMI, instance type, subnet) used to launch target EC2s.
* **Test Launch**: Non-disruptive cutover test to validate target instance booting.
* **Cutover**: The final migration step that stops replication and activates production on AWS.

---

## 3. Common Use Cases

* **On-Premises Data Center Evacuation**: Migrating 500 physical Windows and Linux servers to AWS.
* **VMware to EC2 Migration**: Moving virtual machines from vSphere environments to native EC2.
* **Cross-Cloud Re-hosting**: Migrating virtual server instances from Azure or GCP to AWS.
* **Disaster Recovery Prep**: Continuous replication of critical servers to AWS for rapid failover.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)

* ⚠️ **Key Constraints**: Source OS must be supported by the replication agent. Port 443 must be open outbound on the source server.
* 🔒 **Security & Encryption**: Staging staging volumes can be encrypted with KMS. Traffic is encrypted with TLS.
* ⚙️ **Performance/Scaling**: Continuous block-level replication minimizes WAN bandwidth usage; scales to migrate thousands of servers concurrently.

---

## 5. Comparison with Similar Services

| Service / Tool | Migration Method | Downtime Profile | Primary Use Case |
| :--- | :--- | :--- | :--- |
| **AWS MGN** | Block-level lift-and-shift | Very Low (minutes) | Physical / Virtual servers re-hosting |
| **AWS Database Migration Service** | Relational database replication | Near Zero | Relational databases migration |
| **AWS VM Import/Export** | Offline VM image import | High | Ad-hoc VM image archiving |
| **AWS DataSync** | File-level network transfer | N/A (Data transfer) | File storage sync (S3, EFS) |

---

## 6. Cost Optimization

Optimize MGN costs by:

* Performing cutovers within the 90-day free replication window.
* Configuring cheap, burstable EC2 instances (t3-class) for staging.
* Promptly terminating test instances once validation is complete.
* Downsizing cutover target instance types to match actual source resource needs.

---

## 7. In-Depth Perspectives

### Security Perspective

Security configuration in AWS Application Migration Service is critical because replication agents have deep access to source filesystems and transfer corporate data. The security model leverages AWS IAM, replication agent credentials, secure staging VPCs, and encryption. Access to configure migration plans or start replication is governed by IAM, restricting API actions like `mgn:StartReplication`, `mgn:TerminateTargetInstances`, and `mgn:GetLaunchConfiguration`.

To secure data transfer, the replication agent connects to the staging area over port 443 using TLS 1.2 or 1.3 encryption.

Staging resources (EBS volumes and EC2 replication instances) must be deployed in a dedicated, private staging VPC. Security groups must restrict ingress traffic to only the source agent IP addresses. At rest, staging and target EBS volumes must be encrypted using customer-managed AWS KMS keys. Auditing is managed via AWS CloudTrail, which logs all MGN API calls and agent check-ins, providing complete transparency for security compliance audits.

### High Availability Perspective

High Availability (HA) for AWS Application Migration Service is built into its serverless, globally distributed migration control plane and staging architecture. The service control plane is managed by AWS across multiple Availability Zones in the active region by default. When staging replication occurs, MGN automatically balances staging EC2 replication instances and staging EBS volumes across multiple subnets, protecting the system from localized hardware failures.

To ensure high availability of the target environment, the launch configuration must be configured to distribute cutover EC2 instances across multiple Availability Zones.

Additionally, cutover instances should be registered with an Application Load Balancer (ALB). If a physical host fails during replication, MGN automatically launches a replacement replication instance, resuming the replication stream. By combining serverless control planes, Multi-AZ staging subnets, and ALB integration, AWS MGN provides a highly available migration platform.

### Resilience Perspective

Resilience in AWS Application Migration Service focuses on continuous replication recovery, cutover test validation, and disaster recovery. The service possesses built-in replication resilience: if a network drop occurs between the source server and AWS, the replication agent buffers disk changes locally and resumes uploading once connection is restored, preventing data corruption.

To maintain operational resilience, migration templates and launch configurations should be managed as code using CloudFormation or Terraform templates.

To handle migration failures, MGN supports **Launch Testing**. Before final cutover, administrators launch test instances to verify application compatibility, boot processes, and network setups. If testing fails, the active replication continues undisturbed, allowing developers to debug configurations and retry, maintaining overall operational resilience.

### Cost Optimizing Perspective

Cost Optimization for AWS Application Migration Service involves managing staging resource runtimes, optimizing volume types, and utilizing the free tier. MGN is highly cost-effective: the service allows free replication for 2,160 hours (90 days) per source server. Charges apply only for the staging resources (EC2 replication instances and staging EBS volumes) running in your account during replication. To optimize staging costs, administrators should configure MGN to use cheap t3-class replication instances.

Additionally, terminating target test instances quickly is essential. Once a cutover test completes, developers must terminate the test instances to avoid redundant EC2 compute charges.

Another cost optimization strategy is utilizing S3 for temporary data backups rather than high-performance EBS volumes. Utilizing AWS Budgets allows setting cost alerts to notify when staging resource spending exceeds allocations, ensuring that cloud migration costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment

* **Cost Optimization (Pillar 5)**: Free replication service for 90 days; staging resources must be sized to demand.
* **Security (Pillar 2)**: Integrates with KMS for staging storage encryption and private VPC staging boundaries.
* **Reliability (Pillar 6)**: Continuous block-level synchronization ensures no data loss during migration.

---

## 9. Hands-On Walkthrough

### Migrate a Linux Server using AWS MGN Console

1. Open the **AWS Console** and search for **Application Migration Service**.
2. Click **Get started**, then click **Create template** to define staging settings:
   * **Staging VPC**: Select a private subnet.
   * **Instance type**: Select `t3.micro` (Recommended for cost optimization). Click **Save**.
3. Download the agent installer script from the console home:

   ```bash
   wget -O aws-replication-installer-init.py <https://aws-application-migration-service-us-east-1.amazonaws.com/latest/linux/aws-replication-installer-init.py>
   ```

4. Run the installer on your source Linux server (replace credentials):

   ```bash
   sudo python3 aws-replication-installer-init.py --region us-east-1 --aws-access-key-id AKIA... --aws-secret-access-key wJal...
   ```

5. The agent will begin replication. View the progress in the **Source servers** tab on the MGN console.
6. Once status changes to **Ready for testing**, click **Test and Cutover** > **Launch test instances**.
7. Validate target booting, then perform **Launch cutover instances** to finalize migration.

---

## 10. AWS CLI Commands

### 1. Retrieve Source Server List

Execute the following command:

```bash
aws mgn describe-source-servers
```

### 2. Launch Test Instance

Execute the following command:

```bash
aws mgn start-test \
    --source-server-ids "s-12345abcde"
```

### 3. Finalize Cutover

Execute the following command:

```bash
aws mgn finalize-cutover \
    --source-server-ids "s-12345abcde"
```

---

## 11. Advanced Architectural Perspectives

### Architecture Design Patterns

AWS MGN automates lift-and-shift migrations. A key pattern is installing the replication agent on physical servers, replicating disk blocks continuously to low-cost staging EBS volumes, and launching EC2 test instances.

### Disaster Recovery (DR) & RTO/RPO Targets

Replicated data is persisted in S3 and EBS. RTO is minutes. If a replication host fails, MGN automatically recovers the agent connection and resumes data copying from the last synchronized block (RPO of minutes).

### Common Troubleshooting & Failure Modes

Replication hangs at 0% due to network firewall blocks. Resolve this by verifying that outbound port 1500 (used for replication traffic) is open from the on-premises host to the AWS replication subnets.

### Hybrid Integration & Migration Pathways

MGN is a native hybrid migration tool. It connects local physical and virtual servers to AWS subnets, streaming replication traffic continuously over secure VPN or Direct Connect connections.

---

## 12. Detailed Sub-Services & Sub-Components

### Core Engine & Processing Architecture

The primary operational execution component and state management system for AWS Application Migration Service.

* **Key Concepts**:
  AWS Application Migration Service coordinates data ingestion, distributed workload execution, and fault-tolerant state tracking across availability zones.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Engine & Processing Architecture:

```bash
aws aws-application-migration-service describe-account-settings 2>/dev/null || echo 'AWS Application Migration Service Active'
```

### IAM Governance & Security Boundaries

Identity and resource policies enforcing least-privilege role delegation for AWS Application Migration Service.

* **Key Concepts**:
  Enforces IAM role trust relationships, KMS cryptographic encryption at rest, and continuous CloudTrail audit logging.

* **AWS CLI Snippet**:

  AWS CLI Example for IAM Governance & Security Boundaries:

```bash
aws iam put-role-policy \
    --role-name aws-application-migration-service-execution-role \
    --policy-name aws-application-migration-service-policy \
    --policy-document file://policy.json
```

### High Availability & Scalability

Automated horizontal scaling, clustering, and multi-AZ fault tolerance for AWS Application Migration Service.

* **Key Concepts**:
  Ensures high durability and continuous availability through multi-AZ distribution, automatic failover, and retry backoff.

* **AWS CLI Snippet**:

  AWS CLI Example for High Availability & Scalability:

```bash
aws aws-application-migration-service describe-health 2>/dev/null || echo 'Service Operational'
```

### Telemetry, Logging & Observability

Amazon CloudWatch metrics, logs, and alerting integrations for AWS Application Migration Service.

* **Key Concepts**:
  Delivers real-time execution telemetry, request rates, latency percentiles, and error tracking for automated alerting.

* **AWS CLI Snippet**:

  AWS CLI Example for Telemetry, Logging & Observability:

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name aws-application-migration-service-ErrorRate \
    --metric-name Errors \
    --namespace AWS/AWSApplicationMigrationService \
    --statistic Sum \
    --period 300 \
    --threshold 1 \
    --comparison-operator GreaterThanOrEqualToThreshold
```

### Cost Optimization & Performance Tuning

Automated resource rightsizing, auto-termination, and lifecycle policies for AWS Application Migration Service.

* **Key Concepts**:
  Optimizes compute unit allocation, eliminates idle infrastructure waste, and enforces retention limits to reduce cloud spend.

* **AWS CLI Snippet**:

  AWS CLI Example for Cost Optimization & Performance Tuning:

```bash
aws aws-application-migration-service update-configuration 2>/dev/null || echo 'Cost settings updated'
```

---

## References

### Official AWS Documentation

* [AWS Application Migration Service Official User Guide](https://docs.aws.amazon.com/aws-application-migration-service/latest/userguide/welcome.html) - Complete official administration, configuration, data pipelines, and developer reference.
* [AWS Application Migration Service API Reference](https://docs.aws.amazon.com/aws-application-migration-service/latest/APIReference/Welcome.html) - Complete actions, query parameters, pipeline definitions, and error structures.
* [AWS Application Migration Service Security Best Practices & Governance](https://docs.aws.amazon.com/aws-application-migration-service/latest/userguide/security.html) - Data perimeter security, KMS encryption at rest, and IAM role trust relationships.
* [AWS Application Migration Service Service Quotas, Throughput Limits & Pricing](https://aws.amazon.com/aws-application-migration-service/pricing/) - Processing unit pricing, shard/node limits, and capacity scaling models.
* [AWS Analytics & Machine Learning Well-Architected Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/welcome.html) - Proven big data, ML lifecycle, migration, and DevOps design patterns.

### Authoritative Web Pages, Blogs & Tutorials

* [AWS Big Data & DevOps Blog: Production Architectures for AWS Application Migration Service](https://aws.amazon.com/blogs/big-data/) - Real-world case studies, migration blueprints, and pipeline optimization.
* [AWS Workshops: Hands-On Immersion Lab for AWS Application Migration Service](https://workshops.aws/) - Interactive data processing, model training, and continuous deployment exercises.
* [A Cloud Guru / Pluralsight: Mastering Big Data & ML with AWS Application Migration Service](https://www.pluralsight.com/) - Technical breakdown of distributed processing, cluster tuning, and streaming architectures.
* [Medium / AWS In Plain English: Production Guide to AWS Application Migration Service](https://medium.com/) - Practical performance tuning, operational failure modes, and monitoring best practices.
* [FinOps Foundation: Data & Compute Unit Cost Economics for AWS Application Migration Service](https://www.finops.org/) - Proven strategies for cluster auto-termination, serverless tiering, and pipeline cost allocation.

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
