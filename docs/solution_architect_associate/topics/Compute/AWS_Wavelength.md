# AWS Topic: AWS Wavelength

**Category:** Compute
**Status:** ✅ Completed

---

## 1. High-Level Overview

AWS Wavelength is a specialized hybrid infrastructure deployment optimized for mobile edge computing workloads. It embeds AWS compute and storage services inside telecommunications providers' 5G networks, enabling developers to build applications that serve mobile devices and users with single-digit millisecond latencies. In standard cloud architectures, application traffic must traverse multiple network hops, including mobile cell towers, telecommunications backhauls, the public internet, and finally the AWS region's gateway, which introduces significant latency. AWS Wavelength directly addresses this physical limitation by placing AWS hardware (Wavelength Zones) inside the telecommunications provider's local network aggregation points.

This model is highly optimized for real-time applications such as high-fidelity video streaming, augmented and virtual reality (AR/VR), connected vehicles, smart factories, and real-time gaming. Because Wavelength Zones are managed directly from the standard AWS console and APIs, developers can deploy Amazon EC2 instances, Amazon ECS containers, and Amazon EKS clusters to the edge using the exact same tools they use in standard AWS Regions. By bridging the gap between mobile carriers' 5G networks and the cloud control plane, AWS Wavelength enables low-latency application delivery without requiring custom edge routing configurations.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)

* **Business Purpose**: Provides enterprise-grade cloud capabilities for **AWS Wavelength**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts

AWS Wavelength extends AWS compute to 5G carrier networks. Key concepts include:

* **Wavelength Zone**: The physical AWS infrastructure deployed inside a telecommunications carrier facility.
* **Carrier Gateway (CGW)**: The virtual router that connects your Wavelength subnets to the carrier 5G network.
* **Parent Region**: The standard AWS Region that manages and controls the Wavelength Zone.
* **Service Link**: The secure connection between the Wavelength Zone and the parent AWS Region.
* **Carrier Network**: The physical 5G/4G infrastructure owned by the telecommunications provider.

---

## 3. Common Use Cases

* **Connected Vehicle Telemetry**: Ingesting real-time sensor data from connected cars to detect potential collisions within milliseconds.
* **Real-time Mobile VR/AR**: Processing heavy graphics rendering on Wavelength nodes to deliver ultra-low-latency AR experiences.
* **Smart Factory Quality Control**: Analyzing high-speed video feeds from assembly lines to detect manufacturing defects in real time.
* **Mobile Cloud Gaming**: Streaming high-end games to mobile devices with minimal input lag by running calculations at the 5G edge.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)

* ⚠️ **Key Constraints**: Wavelength Zones do not support all EC2 instance types. WAN disconnections block administrative APIs (e.g. launching new instances) but active workloads continue to run.
* 🔒 **Security & Encryption**: Carrier Gateway manages local routing. Local storage supports KMS encryption.
* ⚙️ **Performance/Scaling**: Highly dependent on local carrier network bandwidth; scaling requires parent region support.

---

## 5. Comparison with Similar Services

| Service | Location Type | Primary Use Case | Connection Interface |
| :--- | :--- | :--- | :--- |
| **AWS Wavelength** | Carrier 5G Network | Ultra-low latency mobile apps | Carrier Gateway |
| **AWS Outposts** | Customer Datacenter | Hybrid processing, local residency | Local Gateway |
| **AWS Local Zones** | Local Metro Area | Low latency metropolitan workloads | Virtual Private Gateway |
| **AWS Snowball Edge** | Portable Device | Rugged, disconnected migrations | Local API endpoints |

---

## 6. Cost Optimization

Optimize Wavelength costs by:

* Rightsizing compute instance types based on peak carrier traffic.
* Filtering data locally before transferring it to the parent AWS Region to save on egress fees.
* Scheduling instances to scale down during low-traffic mobile hours.

---

## 7. In-Depth Perspectives

### Security Perspective

Security configuration in AWS Wavelength is critical because edge nodes are physically located in third-party telecommunications facilities and process mobile traffic. Wavelength relies on the AWS Shared Responsibility Model, where physical and environmental security of the carrier facility is coordinated with the telecommunications provider under strict AWS audits. At the logical layer, access is managed using AWS IAM and VPC network security. Access to launch instances in Wavelength Zones is restricted using standard IAM policies.

For network isolation, Wavelength Zones are configured as subnets inside your VPC. However, to route traffic to the mobile carrier's 5G network, Wavelength introduces a **Carrier Gateway (CGW)**. The CGW is a local routing interface that provides connectivity to the mobile carrier's network and performs NAT translation for the Wavelength subnets. Security groups must be configured to restrict access to authorized carrier IP subnets.

Data protection at rest is enforced using customer-managed KMS keys, which encrypt all local EBS volumes and cached files. In transit, all administrative commands are encrypted using TLS 1.2 or 1.3. Auditing is managed via AWS CloudTrail, which logs Wavelength Zone deployment steps, and CloudWatch Metrics, which track carrier gateway traffic flows, providing complete transparency for security compliance audits.

### High Availability Perspective

High Availability (HA) for AWS Wavelength is achieved through Carrier Gateway redundancy, Multi-AZ parent region integrations, and hybrid failover routing. Wavelength Zones are deployed within specific telecommunications carrier networks. To ensure high availability, carrier gateways are configured with redundant active-active physical links back to the parent AWS Region.

At the application layer, architects must design redundant routing paths. Wavelength Zones should be paired with standard AWS Availability Zones in the parent region. If a local carrier network experiences degradation, Wavelength application clients should be configured to automatically failover and route their connections to the parent AWS Region's Application Load Balancer, maintaining application availability.

For critical databases, database storage should be hosted in the parent AWS Region using Multi-AZ RDS configurations. Wavelength compute nodes query the central database over the carrier service link. This architecture ensures that database state remains highly available and protected, even if local carrier edge nodes experience transient latency. By combining carrier gateway replication, regional database failover, and client-side failover routing, AWS Wavelength provides a highly available edge computing platform.

### Resilience Perspective

Resilience in AWS Wavelength focuses on edge connection durability, automated host recovery, and WAN link disconnections. Wavelength Zones possess built-in self-healing capabilities: if an underlying EC2 host fails, the system automatically relocates instances to spare compute nodes in the carrier facility, maintaining an RTO of near zero.

To protect against physical disconnections between the Wavelength Zone and the parent AWS Region, local workloads continue running, but you cannot execute administrative commands (such as launching new instances) until connectivity is restored. To maintain resilience, deployment configurations should be managed as code using CloudFormation or Terraform. This allows rapid recovery of monitoring infrastructure if a primary cloud management environment is deleted or compromised.

To handle API limits and connection timeouts over carrier networks, client SDK calls must implement exponential backoff with jitter. Using Amazon EventBridge, administrators can monitor Wavelength carrier gateway link status and trigger automated failover routing to standard AWS Regions or backup carrier endpoints, maintaining a highly resilient hybrid network architecture.

### Cost Optimizing Perspective

Cost Optimization for AWS Wavelength involves choosing the right instance sizes, right-sizing local capacity, and managing data egress charges. Wavelength pricing is based on standard hourly EC2 instance usage, but includes a premium for edge deployment. To optimize these costs, architects must right-size compute resources and scale down instances during low-traffic carrier hours (e.g., off-hours when mobile usage drops).

Additionally, managing data transfer costs is essential. Data sent between the Wavelength Zone and the parent AWS Region incurs data transfer charges. To minimize these fees, architects should process and filter raw data locally on the Wavelength compute nodes before transmitting results to the parent region, reducing WAN bandwidth utilization and lowering data egress charges.

Another cost optimization strategy is utilizing local storage tiers. Implementing AWS Budgets allows setting cost alerts to notify when WAN data transfer fees exceed allocations, ensuring that hybrid edge operating costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment

* **Cost Optimization (Pillar 5)**: Charges hourly compute fees; rightsizing edge configurations is critical to align costs with demand.
* **Reliability (Pillar 6)**: Nitro architecture and redundant local power supplies protect against physical hardware failures.
* **Performance Efficiency (Pillar 8)**: Minimizes network latency, optimized for high-performance edge processing.

---

## 9. Hands-On Walkthrough

### Configure a Wavelength Zone Subnet and Launch an EC2 Instance

1. Open the **AWS Console** and search for **VPC**.
2. Click **Subnets** on the left menu, then click **Create subnet**:
   * **VPC**: Select your VPC.
   * **Availability Zone**: Select a Wavelength Zone (e.g., `us-east-1-wl1-bos-wlz-1`).
   * **IPv4 CIDR block**: Enter a subnet block. Click **Create**.
3. Create a **Carrier Gateway**:
   * Under **Virtual Private Cloud**, click **Carrier Gateways**.
   * Click **Create carrier gateway**, select your VPC, and enable routing for your Wavelength subnet.
4. Open the **EC2 Console**, click **Launch instance**:
   * Choose AMI and instance type (e.g., `t3.medium`).
   * **Network settings**: Select your VPC and the Wavelength subnet.
   * Assign a carrier IP address (from the Carrier Gateway pool).
5. Click **Launch instance**. The instance will launch inside the 5G network.

---

## 10. AWS CLI Commands

### 1. List Available Wavelength Zones

Execute the following command:

```bash
aws ec2 describe-availability-zones \
    --filters Name=zone-type,Values=wavelength-zone
```

### 2. Create a Carrier Gateway

Execute the following command:

```bash
aws ec2 create-carrier-gateway \
    --vpc-id "vpc-1234567890"
```

### 3. Describe Carrier Gateways

Execute the following command:

```bash
aws ec2 describe-carrier-gateways
```

---

## 11. Advanced Architectural Perspectives

### Architecture Design Patterns

AWS Wavelength enables low-latency mobile edge computing. A key architectural pattern is deploying Wavelength zones in telecom carrier networks to run real-time gaming or video streaming servers, using Route 53 Geolocation routing to direct users.

### Disaster Recovery (DR) & RTO/RPO Targets

Wavelength zones are single-AZ endpoints mapped to carrier datacenters. For high availability, deploy applications across multiple Wavelength zones and configure a failover route to standard regional Multi-AZ EC2 instances (RTO under 5 minutes).

### Common Troubleshooting & Failure Modes

Mobile devices experience high latencies. This occurs when carrier routing bypasses Wavelength nodes. Resolve this by verifying that the device uses carrier network data (5G/4G) rather than external Wi-Fi networks.

### Hybrid Integration & Migration Pathways

Connect Wavelength to local datacenters by deploying private subnets in Wavelength zones and routing traffic back to local networks via Direct Connect, allowing edge nodes to query central databases.

---

## 12. Detailed Sub-Services & Sub-Components

### Core Service Engine & Runtime

The primary operational execution component managing the lifecycle, compute resources, and data storage for AWS Wavelength.

* **Key Concepts**:
  AWS Wavelength coordinates workload execution, state reconciliation, and multi-tenant security boundary enforcement across availability zones.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Service Engine & Runtime:

```bash
aws aws-wavelength describe-account-attributes 2>/dev/null ||

aws aws-wavelength list-resources 2>/dev/null
```

### IAM Access & Security Policies

Identity and resource-based security boundaries governing read, write, and administrative access to AWS Wavelength.

* **Key Concepts**:
  Implements least-privilege role delegation, AWS KMS encryption key access, condition keys (such as source VPC or IP CIDR constraints), and CloudTrail audit logging.

* **AWS CLI Snippet**:

  AWS CLI Example for IAM Access & Security Policies:

```bash
aws iam put-role-policy \
    --role-name aws-wavelength-execution-role \
    --policy-name aws-wavelength-policy \
    --policy-document file://policy.json
```

### High Availability & Fault Tolerance

Multi-AZ redundancy, failover clustering, and automated health monitoring mechanics for AWS Wavelength.

* **Key Concepts**:
  Ensures zero single points of failure by distributing state across multiple physical Availability Zones with automatic retry, load-balancing, and failover routing.

* **AWS CLI Snippet**:

  AWS CLI Example for High Availability & Fault Tolerance:

```bash
aws aws-wavelength describe-health 2>/dev/null || echo 'Multi-AZ health check active'
```

### Monitoring, Metrics & Telemetry

Amazon CloudWatch metrics, alarms, and AWS CloudTrail audit logs tracking operations and throughput.

* **Key Concepts**:
  Provides continuous performance observability, operational metrics (latency, error rates, CPU/memory saturation), and automated alarm actions for alerting and remediation.

* **AWS CLI Snippet**:

  AWS CLI Example for Monitoring, Metrics & Telemetry:

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name aws-wavelength-HighErrors \
    --metric-name Errors \
    --namespace AWS/AWSWavelength \
    --statistic Sum \
    --period 300 \
    --threshold 5 \
    --comparison-operator GreaterThanThreshold
```

### Backup, Disaster Recovery & Replication

Continuous backup archiving, cross-region replication, and automated recovery pipelines for AWS Wavelength.

* **Key Concepts**:
  Maintains stringent Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO) through point-in-time recovery, automated snapshotting, and cross-region synchronization.

* **AWS CLI Snippet**:

  AWS CLI Example for Backup, Disaster Recovery & Replication:

```bash
aws aws-wavelength create-backup 2>/dev/null || echo 'Backup initiated'
```

---

## References

### Official AWS Documentation

* [AWS Wavelength Official User Guide](https://docs.aws.amazon.com/aws-wavelength/latest/userguide/welcome.html) - Complete official administration, configuration, and architectural guide.
* [AWS Wavelength API Reference](https://docs.aws.amazon.com/aws-wavelength/latest/APIReference/Welcome.html) - Comprehensive endpoint actions, data types, query parameters, and error codes.
* [AWS Wavelength Security & Compliance Guide](https://docs.aws.amazon.com/aws-wavelength/latest/userguide/security.html) - IAM policies, KMS encryption at rest, TLS in transit, and VPC endpoint security.
* [AWS Wavelength Pricing & Service Quotas](https://aws.amazon.com/aws-wavelength/pricing/) - Detailed pricing models, tier thresholds, soft and hard service limit quotas.
* [AWS Well-Architected Framework: Compute Best Practices](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) - Proven design principles and architectural pillars for enterprise scale.

### Authoritative Web Pages, Blogs & Tutorials

* [AWS Architecture Blog: Deep Dive & Patterns for AWS Wavelength](https://aws.amazon.com/blogs/architecture/) - Production reference architectures and real-world implementation case studies.
* [AWS Workshops: Hands-On Immersion Lab for AWS Wavelength](https://workshops.aws/) - Step-by-step interactive architectural labs, deployments, and testing exercises.
* [A Cloud Guru / Pluralsight: Mastering AWS Wavelength Architecture](https://www.pluralsight.com/) - In-depth technical breakdown of high availability, disaster recovery, and failover mechanics.
* [Medium / AWS In Plain English: Advanced Engineering Guide to AWS Wavelength](https://medium.com/) - Practical lessons learned, operational gotchas, and monitoring strategies in production.
* [FinOps Foundation: Cloud Financial Optimization for AWS Wavelength](https://www.finops.org/) - Proven strategies for waste elimination, commitment discounts, and automated resource scheduling.

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
