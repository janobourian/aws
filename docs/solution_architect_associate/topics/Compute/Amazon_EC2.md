# AWS Topic: Amazon EC2
**Category:** Compute
**Status:** ✅ Completed

---

## 1. High-Level Overview
Amazon Elastic Compute Cloud (EC2) is a foundational web service designed to provide resizable, secure virtual compute capacity in the AWS Cloud. In traditional IT infrastructures, provisioning physical servers required capital investments, hardware procurement delays, and physical datacenter maintenance. Amazon EC2 eliminates these challenges by allowing organizations to launch virtual servers (known as instances) in seconds. By providing complete control over virtual computing resources, EC2 enables developers to select optimal OS configurations, CPU cores, memory capacity, and storage types (EBS) to fit their applications.

EC2 instances are available in a wide variety of **Instance Families** optimized for different workloads: General Purpose (T and M families), Compute Optimized (C family), Memory Optimized (R and X families), Storage Optimized (I and D families), and Accelerated Computing (G and P families). EC2 supports multiple purchasing options, enabling organizations to balance cost and flexibility: On-Demand (pay per second, no commitment), Reserved Instances (up to 72% discount for 1/3 year commitment), Savings Plans (flexible commit-based discounts), Spot Instances (up to 90% discount utilizing spare capacity), and Dedicated Hosts (for licensing compliance). By automating capacity provisioning and integrating with EBS, ELB, and Auto Scaling, EC2 forms the backbone of cloud compute architectures, enabling highly scalable and performant deployments.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Provides on-demand, virtual computing servers in the cloud, replacing the need to purchase, rack, wire, and maintain physical server hardware in expensive private data centers.
* **How It Works**: Allows engineers to provision virtual servers of any size (from tiny web servers to massive supercomputing machines) in seconds, running standard operating systems (Linux, Windows) with complete control.
* **Key Business Value & Use Cases**: Powers dynamic web applications, backend APIs, data processing workers, and enterprise ERP systems with zero upfront hardware capital expenditure and pay-as-you-go pricing.

## 2. Core Architecture & Key Concepts
Amazon EC2 provides virtual compute servers. Key concepts include:
* **AMI (Amazon Machine Image)**: The template that contains the OS, application server, and configurations.
* **Instance Type**: The hardware configuration (CPU, memory, storage) grouped into families (e.g., General Purpose, Compute Optimized).
* **EBS (Elastic Block Store)**: Persistent block storage volumes attached to EC2 instances.
* **Instance Store**: Temporary, ephemeral block storage physically attached to the host server.
* **Security Group**: A stateful virtual firewall that controls traffic to and from the instance.

---

## 3. Common Use Cases
* **Web Application Hosting**: Running dynamic web servers (Apache, Nginx, IIS) to host enterprise websites.
* **Application Ingest Processing**: Running custom message consumer workers that pull payloads from SQS and process them.
* **Legacy System Migration**: Migrating a custom C++ application from on-premises servers to EC2 with minimal modifications.
* **High-Performance Computing (HPC)**: Running complex parallel calculations on GPU-optimized EC2 clusters.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)
* ⚠️ **Key Constraints**: Instance Store data is lost when the instance is stopped or terminated (EBS data persists). Changing instance types requires stopping the instance.
* 🔒 **Security & Encryption**: Security Groups are stateful; Network ACLs are stateless. Systems Manager Session Manager eliminates key pairs management.
* ⚙️ **Performance/Scaling**: Recommend EBS-optimized instances and Graviton processors for the best price-performance.

---

## 5. Comparison with Similar Services
| Service | Management Overhead | Storage Durability | Pricing Model |
| :--- | :--- | :--- | :--- |
| **Amazon EC2** | High (You manage OS, patching, security) | High (via EBS) | Hourly instance fee / Commitments / Spot |
| **AWS Lambda** | None (Serverless) | Ephemeral (or S3 integration) | Pay per invocation and duration |
| **AWS Fargate** | Low (Serverless containers) | Ephemeral (or EFS integration) | Pay per vCPU and memory per second |
| **AWS Lightsail** | Low (Simplified VPS) | High | Flat monthly plan fee |

---

## 6. Cost Optimization
Optimize EC2 costs by:
* Rightsizing instance sizes using AWS Compute Optimizer.
* Deploying Spot Instances for stateless processing tasks.
* Utilizing Graviton-based instances.
* Purchasing Savings Plans or Reserved Instances for continuous baseline workloads.

---

## 7. In-Depth Perspectives

### Security Perspective
Security configuration in Amazon EC2 is critical because virtual servers interact directly with public networks and database backends. The security model leverages Key Pairs, Security Groups, Network ACLs, IAM Instance Profiles, and storage encryption. At the host access level, EC2 instances require **EC2 Key Pairs** (public-private key cryptography) to authorize SSH (Linux) or RDP (Windows) logins. However, for modern administrative access, AWS Systems Manager **Session Manager** is recommended. Session Manager allows secure terminal access without opening SSH port 22 or managing key pairs, routing traffic over secure AWS APIs.

At the network level, **Security Groups** act as stateful virtual firewalls that control traffic to and from instances. By default, incoming traffic is blocked, and outgoing traffic is allowed. Security group rules should restrict ingress ports to authorized subnets (e.g. only allowing HTTP traffic on port 80/443 from the Application Load Balancer). **Network Access Control Lists (NACLs)** act as stateless subnets firewalls, providing a secondary layer of defense.

Data protection at rest is enforced using customer-managed AWS KMS keys, which encrypt all Amazon Elastic Block Store (EBS) volumes attached to the instances. In transit, all administrative API communications are secured using TLS. IAM Instance Profiles are used to grant EC2 instances permissions to access S3 or DynamoDB without hardcoding credentials in application files. Auditing is managed via AWS CloudTrail, which logs EC2 API actions, and CloudWatch Agent, which can capture local OS system logs and deliver them to CloudWatch Logs, ensuring complete compliance auditability.

### High Availability Perspective
High Availability (HA) for Amazon EC2 is achieved through multi-AZ distribution, Elastic Load Balancing (ELB), and Multi-AZ database integrations. A single EC2 instance is a single point of failure. To design a highly available architecture, architects must distribute EC2 instances across multiple Availability Zones within the active AWS region.

An **Application Load Balancer (ALB)** is deployed to act as the single traffic entry point. The ALB monitors instance health and distributes incoming HTTP/HTTPS traffic across instances in different zones. If an instance in one zone fails, the ALB automatically stops routing traffic to it, and active instances in remaining zones handle the workload, preventing application downtime.

Additionally, database tiers should be decoupled from the EC2 web servers and deployed using RDS Multi-AZ databases, which replicate data synchronously to a standby database in a different zone. If the primary zone fails, RDS fails over automatically. By combining Multi-AZ instance distribution, ALB routing, and Multi-AZ database endpoints, Amazon EC2 provides a highly available, robust computing architecture.

### Resilience Perspective
Resilience in Amazon EC2 focuses on host auto-recovery, EBS snapshot backups, and disaster recovery. If an EC2 instance experiences an underlying hardware failure, AWS's built-in **EC2 Auto Recovery** mechanism automatically recovers the instance on a healthy physical host, retaining the same IP address, volume attachments, and metadata, minimizing manual intervention.

To protect against data loss or corruption, administrators should schedule automated **EBS Snapshots** using Amazon Data Lifecycle Manager (DLM). Snapshots are stored in S3, which provides 11 9s of durability. For disaster recovery across regions, AMIs (Amazon Machine Images) can be replicated to a secondary AWS region. In the event of a regional outage, instances can be redeployed immediately from the replicated AMIs, maintaining a minimal Recovery Time Objective (RTO).

To handle load spikes and maintain performance resilience, EC2 instances are paired with Amazon EC2 Auto Scaling. Auto Scaling Groups automatically launch or terminate instances based on actual demand metrics, ensuring the application remains responsive. Using CloudWatch Alarms to monitor instance parameters (such as `CPUUtilization` and `StatusCheckFailed`) ensures that operators are immediately notified of resource limits, maintaining a highly resilient compute architecture.

### Cost Optimizing Perspective
Cost Optimization for Amazon EC2 is one of the most critical design constraints because compute charges can consume a major portion of your AWS budget. SAA-C03 exam questions heavily emphasize choosing the correct purchase option to optimize costs:
* **Reserved Instances (RIs) / Savings Plans**: Best for stable, continuous baseline workloads (provides up to 72% savings for 1/3 year commitment).
* **Spot Instances**: Best for stateless, fault-tolerant workloads (provides up to 90% savings).
* **On-Demand**: Best for unpredictable, short-term workloads.

Additionally, rightsizing instances is essential. FinOps teams should use **AWS Compute Optimizer** to analyze EC2 utilization metrics (CPU, Memory, Network) and identify oversized instances. Compute Optimizer recommends down-sizing to smaller instance types or migrating to newer families (e.g. from `m5` to `m6g`).

Another cost optimization strategy is utilizing Graviton processors. Graviton instances (t4g, m6g, c6g) offer up to 40% better price-performance than standard x86 processors, lowering compute charges. Setting up auto-scaling policies to scale instances down to zero or a minimum baseline during off-hours (such as nights and weekends) avoids paying for idle resources. Utilizing AWS Budgets allows setting cost alerts to notify when compute spending exceeds allocations, ensuring that hosting costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment
* **Cost Optimization (Pillar 5)**: Integrates with Auto Scaling and Savings Plans to minimize compute waste.
* **Security (Pillar 2)**: Enforces network isolation using VPC and stateful firewalls (Security Groups).
* **Performance Efficiency (Pillar 8)**: Offers a wide variety of instance families tailored to specific performance needs.

---

## 9. Hands-On Walkthrough
### Launch a Web Server EC2 Instance using AWS Console
1. Open the **AWS Console** and search for **EC2**.
2. Click **Instances** on the left menu, then click **Launch instances**.
3. **Name**: `MyWebServer`.
4. **Application and OS Image**: Select **Amazon Linux 2023** (Free tier eligible).
5. **Instance type**: Select `t2.micro` (or `t3.micro`).
6. **Key pair**: Choose an existing key pair or select **Proceed without a key pair** (SSM Session Manager is recommended).
7. Under **Network settings**:
   * Select **Allow HTTP traffic from the internet** and **Allow HTTPS traffic from the internet**.
8. Under **Advanced details**:
   * Scroll to **User data** and paste the script below to install a web server:
     ```bash
     #!/bin/bash
     dnf update -y
     dnf install -y httpd
     systemctl start httpd
     systemctl enable httpd
     echo "<h1>Hello, Amazon EC2!</h1>" > /var/www/html/index.html
     ```
9. Click **Launch instance**. Copy the public IP and open it in your browser to verify the web server.

---

## 10. AWS CLI Commands
### 1. Launch an EC2 Instance

Execute the following command:
```bash
aws ec2 run-instances \
    --image-id "ami-0123456789abcdef0" \
    --instance-type t2.micro \
    --key-name my-key-pair \
    --security-group-ids sg-12345 \
    --subnet-id subnet-12345
```

### 2. Describe Running Instances

Execute the following command:
```bash
aws ec2 describe-instances \
    --filters Name=instance-state-name,Values=running
```

### 3. Terminate an Instance

Execute the following command:
```bash
aws ec2 terminate-instances \
    --instance-ids i-1234567890abcdef0
```

---

## 11. Advanced Architectural Perspectives

### Architecture Design Patterns
Amazon EC2 provides virtual servers. A standard pattern is deploying EC2 instances in private subnets across multiple AZs behind an Application Load Balancer, using Auto Scaling to dynamically adjust instance count based on CPU utilization.

### Disaster Recovery (DR) & RTO/RPO Targets
To protect EC2 workloads from outages, automate the creation of **AMIs (Amazon Machine Images)** using AWS Backup. For cross-region DR, replicate AMIs to a standby region, allowing rapid instance launches using CloudFormation (RTO under 15 minutes).

### Common Troubleshooting & Failure Modes
Instances fail to launch with `InsufficientInstanceCapacity` errors. This occurs when AWS lacks physical hardware in the selected AZ. Resolve this by selecting a different AZ, changing the instance family, or using On-Demand Capacity Reservations.

### Hybrid Integration & Migration Pathways
Integrate EC2 with local systems by deploying the AWS Systems Manager (SSM) agent. This allows running commands and applying security patches to both EC2 instances and on-premises virtual machines using a unified dashboard.

---

## 12. Detailed Sub-Services & Sub-Components

### Security Groups

Stateful virtual firewalls operating at the network interface level to filter ingress and egress traffic.

* **Key Concepts**:
  Security groups maintain stateful connection tracking. Ingress rules default to deny-all; egress rules default to allow-all. They can reference other security groups as sources or destinations for secure multi-tier communication.

* **AWS CLI Snippet**:

  AWS CLI Example for Security Groups:
```bash
aws ec2 authorize-security-group-ingress \
    --group-id sg-0123456789abcdef0 \
    --protocol tcp \
    --port 443 \
    --cidr 10.0.0.0/16
```

### Key Pairs

Public-private key pairs used for initial SSH (Linux) or RDP password decryption (Windows).

* **Key Concepts**:
  AWS stores the public key in instance metadata (~/.ssh/authorized_keys) and the client holds the private key. Modern governance recommends AWS Systems Manager Session Manager over Key Pairs to eliminate port 22/3389 exposure.

* **AWS CLI Snippet**:

  AWS CLI Example for Key Pairs:
```bash
aws ec2 create-key-pair \
    --key-name AppAdminKey \
    --key-type ed25519 \
    --query 'KeyMaterial' \
    --output text > AppAdminKey.pem
```

### Amazon Machine Images (AMIs)

Packaged templates containing the operating system, initial software, and volume block mappings.

* **Key Concepts**:
  AMIs can be public AWS-managed images, Marketplace offerings, or custom private AMIs created from existing instances. AMIs are regional and can be replicated cross-region or shared with other AWS accounts via launch permissions.

* **AWS CLI Snippet**:

  AWS CLI Example for Amazon Machine Images (AMIs):
```bash
aws ec2 create-image \
    --instance-id i-0123456789abcdef0 \
    --name 'Golden-Web-v2' \
    --no-reboot
```

### EBS Snapshots

Incremental point-in-time backups of EBS volumes stored durably in Amazon S3.

* **Key Concepts**:
  Snapshots capture only blocks that changed since the previous snapshot. Amazon Data Lifecycle Manager (DLM) automates snapshot retention policies, and Fast Snapshot Restore (FSR) eliminates initial I/O latency upon volume creation.

* **AWS CLI Snippet**:

  AWS CLI Example for EBS Snapshots:
```bash
aws ec2 create-snapshot \
    --volume-id vol-0123456789abcdef0 \
    --description 'Automated daily backup'
```

### Elastic Network Interfaces (ENIs)

Virtual network interfaces that can be attached and detached from EC2 instances in a VPC.

* **Key Concepts**:
  Each ENI has a primary private IP, secondary private IPs, a MAC address, and attached security groups. ENIs allow dual-homing across subnets and graceful failover of network interfaces during high availability recovery events.

* **AWS CLI Snippet**:

  AWS CLI Example for Elastic Network Interfaces (ENIs):
```bash
aws ec2 attach-network-interface \
    --network-interface-id eni-0123456789abcdef0 \
    --instance-id i-0123456789abcdef0 \
    --device-index 1
```

### Placement Groups

Hardware placement policies influencing how instances are distributed across physical racks.

* **Key Concepts**:
  Cluster placement groups pack instances in a single AZ for low-latency 100Gbps networking. Spread placement groups isolate instances across distinct hardware racks (max 7 per AZ). Partition placement groups divide instances across hardware partitions.

* **AWS CLI Snippet**:

  AWS CLI Example for Placement Groups:
```bash
aws ec2 create-placement-group \
    --group-name HPCCluster \
    --strategy cluster
```

### Launch Templates

Versioned blueprints containing instance configurations used by Auto Scaling and EC2 Fleet.

* **Key Concepts**:
  Launch Templates support parameter inheritance, mixed instance policies (combining On-Demand and Spot with multiple instance types), and advanced metadata configurations like IMDSv2 enforcement.

* **AWS CLI Snippet**:

  AWS CLI Example for Launch Templates:
```bash
aws ec2 create-launch-template \
    --launch-template-name WebTierTemplate \
    --launch-template-data '{"ImageId":"ami-0123456789abcdef0","InstanceType":"t4g.medium"}'
```

---

## References

### Official AWS Documentation
* [Amazon EC2 Official User Guide](https://docs.aws.amazon.com/amazon-ec2/latest/userguide/welcome.html) - Complete official administration, configuration, and architectural guide.
* [Amazon EC2 API Reference](https://docs.aws.amazon.com/amazon-ec2/latest/APIReference/Welcome.html) - Comprehensive endpoint actions, data types, query parameters, and error codes.
* [Amazon EC2 Security & Compliance Guide](https://docs.aws.amazon.com/amazon-ec2/latest/userguide/security.html) - IAM policies, KMS encryption at rest, TLS in transit, and VPC endpoint security.
* [Amazon EC2 Pricing & Service Quotas](https://aws.amazon.com/amazon-ec2/pricing/) - Detailed pricing models, tier thresholds, soft and hard service limit quotas.
* [AWS Well-Architected Framework: Compute Best Practices](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) - Proven design principles and architectural pillars for enterprise scale.

### Authoritative Web Pages, Blogs & Tutorials
* [AWS Architecture Blog: Deep Dive & Patterns for Amazon EC2](https://aws.amazon.com/blogs/architecture/) - Production reference architectures and real-world implementation case studies.
* [AWS Workshops: Hands-On Immersion Lab for Amazon EC2](https://workshops.aws/) - Step-by-step interactive architectural labs, deployments, and testing exercises.
* [A Cloud Guru / Pluralsight: Mastering Amazon EC2 Architecture](https://www.pluralsight.com/) - In-depth technical breakdown of high availability, disaster recovery, and failover mechanics.
* [Medium / AWS In Plain English: Advanced Engineering Guide to Amazon EC2](https://medium.com/) - Practical lessons learned, operational gotchas, and monitoring strategies in production.
* [FinOps Foundation: Cloud Financial Optimization for Amazon EC2](https://www.finops.org/) - Proven strategies for waste elimination, commitment discounts, and automated resource scheduling.

---

## FinOps

*Financial Operations (FinOps) is a discipline that combines cloud financial management, cost optimization, and business accountability. The following guidelines apply to every AWS service and help you control spend while maintaining performance and security.*

### 1. Cost Visibility & Allocation
- **Tagging Strategy** – Ensure every resource created by the service (e.g., EC2 instances, S3 buckets, Lambda functions) is tagged with `Environment`, `Project`, `Owner`, and `CostCenter`. Use AWS Tag Editor or Infrastructure as Code (IaC) to enforce mandatory tags.
- **Cost Allocation Tags** – Enable AWS‑generated cost allocation tags (e.g., `aws:createdBy`) and propagate them to downstream resources like ENIs, EBS volumes, or CloudWatch logs.
- **Budgets & Alerts** – Create service‑specific budgets that trigger alerts when spend exceeds 80 % of the forecasted monthly budget. Use SNS notifications to automatically inform owners.

### 2. Right‑Sizing & Utilization
- **Compute** – Leverage AWS Compute Optimizer or Auto Scaling policies to adjust instance types, fleet sizes, or Lambda concurrency based on utilization metrics.
- **Storage** – Periodically evaluate storage class transitions (e.g., S3 Standard → Intelligent‑Tiering → Glacier) and delete orphaned snapshots, AMIs, or EBS volumes.
- **Serverless** – Use provisioned concurrency for predictable workloads; otherwise, rely on on‑demand execution and monitor Request‑Count vs. duration to avoid over‑provisioning.

### 3. Reserved & Savings Plans
- **Reserved Instances (RI)** – Purchase RIs for predictable workloads such as steady‑state EC2, RDS, or Redshift. Use the RI Recommendation tool to match instance families.
- **Savings Plans** – For mixed compute workloads, adopt Compute Savings Plans (flexible across EC2, Fargate, Lambda) to capture up‑to‑72 % savings.

### 4. Data Transfer & Egress Management
- **VPC Endpoints** – Use Interface or Gateway VPC endpoints to keep traffic within the AWS network, eliminating internet egress charges.
- **Cross‑Region Replication** – Replicate data only when necessary; leverage S3 Transfer Acceleration for occasional large transfers instead of constant cross‑region copies.

### 5. Monitoring & Automation
- **Cost Explorer** – Schedule monthly Cost Explorer queries that break down spend by service, tag, and usage type.
- **Lambda‑Driven Cleanup** – Deploy Lambda functions that automatically delete unused resources (e.g., unattached EBS volumes, stale snapshots) after a configurable grace period.
- **AWS Config Rules** – Enforce compliance with cost‑related policies such as `required-tags`, `restricted-ec2-instance-types`, and `s3-bucket-public-access-prohibited`.

### 6. Governance & Chargeback
- **AWS Organizations** – Consolidate billing across accounts, apply Service Control Policies (SCPs) to limit high‑cost services, and allocate costs to individual business units via linked accounts.
- **Chargeback Models** – Export detailed cost reports to your internal ERP system; map AWS cost elements to internal cost centers for transparent chargeback.

### 7. Continuous Improvement
- **FinOps Maturity Model** – Assess your organization’s maturity (Inform, Optimize, Automate, Govern) and set quarterly improvement goals.
- **Training** – Provide teams with FinOps training and embed cost‑awareness in PR reviews, CI pipelines, and architectural decision records.

By embedding these FinOps practices into the daily workflow for each service, you can achieve sustainable cost savings while preserving the reliability, security, and performance expected from AWS.
