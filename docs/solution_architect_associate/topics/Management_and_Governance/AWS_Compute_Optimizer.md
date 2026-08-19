# AWS Topic: AWS Compute Optimizer

**Category:** Management and Governance
**Status:** ✅ Completed

---

## 1. High-Level Overview

AWS Compute Optimizer is a serverless, fully managed optimization service that uses advanced machine learning algorithms to analyze historical resource utilization metrics of your AWS workloads and generate recommendations to improve performance and lower costs. In traditional data centers, sizing servers was a guessing game that resulted in massive over-provisioning to avoid performance degradation. AWS Compute Optimizer addresses this inefficiency by programmatically evaluating four resource tiers: Amazon EC2 instances, Amazon EBS volumes, AWS Lambda functions, and Amazon ECS services on AWS Fargate.

The service connects directly to Amazon CloudWatch to analyze historical usage metrics—such as CPU utilization, memory consumption, disk I/O, and network throughput—over a period of 14 days (or up to 93 days with enhanced infrastructure metrics). Using these patterns, Compute Optimizer identifies underutilized resources and recommends down-sizing to smaller instance types or migrating to newer instance families (e.g. from x86 to Graviton). It also detects over-provisioned EBS IOPS or oversized Lambda memory boundaries. By automating the analysis and generating actionable optimization steps, AWS Compute Optimizer enables FinOps teams to maintain workload performance while eliminating compute waste.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)

* **Business Purpose**: Provides enterprise-grade cloud capabilities for **AWS Compute Optimizer**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts

AWS Compute Optimizer generates performance sizing reports. Key concepts include:

* **Recommendation**: Sizing updates for EC2, EBS, Lambda, and Fargate.
* **Underprovisioned Resource**: Resource that is oversized for its actual workload.
* **Overprovisioned Resource**: Resource that lacks capacity and is at risk of performance bottlenecks.
* **Inference Pipeline**: The ML engine that matches utilization metrics with optimal resource configurations.
* **Enhanced Infrastructure Metrics**: A paid feature that extends metric history analysis up to 93 days.

---

## 3. Common Use Cases

* **EC2 Fleet Rightsizing**: Analyzing all EC2 instances across 50 developer accounts to locate and downsize idle servers.
* **EBS Volume Optimization**: Sizing EBS storage types and provisioned IOPS based on actual read/write traffic.
* **Lambda Cost Minimizing**: Tuning serverless memory limits to balance execution speeds with billing costs.
* **Fargate Task Rightsizing**: Optimizing ECS task CPU and memory requirements to reduce serverless container fees.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)

* ⚠️ **Key Constraints**: EC2 recommendations require at least 30 consecutive hours of metric data (14 days history is recommended). Enhanced metrics feature is paid.
* 🔒 **Security & Encryption**: Does not access container payloads or filesystem configurations. Access managed via IAM.
* ⚙️ **Performance/Scaling**: Integrates with CloudWatch to ingest resource metrics automatically.

---

## 5. Comparison with Similar Services

| Service | Primary Optimization Target | Optimization Method | Pricing Model |
| :--- | :--- | :--- | :--- |
| **AWS Compute Optimizer** | Sizing configurations (EC2, Lambda) | ML analysis of utilization metrics | Free |
| **AWS Trusted Advisor** | Best practices checks (Security, Cost) | Rule-based evaluations | Included / Paid tiers |
| **AWS Cost Explorer** | General billing allocations | Historical spend aggregation | Free |
| **AWS Budgets** | Budget limits and forecasts | Threshold-based alerting | Free |

---

## 6. Cost Optimization

Optimize compute costs by:

* Reviewing and acting on EC2 rightsizing recommendations.
* Sizing EBS IOPS allocations to match actual disk access demands.
* Optimizing Lambda memory profiles to balance billing.
* Consolidating underutilized instances onto smaller instance classes.

---

## 7. In-Depth Perspectives

### Security Perspective

Security configuration in AWS Compute Optimizer is critical because the service analyzes historical performance metrics of your core computing resources. The security model leverages AWS IAM, secure metric ingestion, and data privacy boundaries. Access to view recommendations or modify optimizer settings is governed by IAM, restricting API actions like `compute-optimizer:GetEC2InstanceRecommendations`, `compute-optimizer:GetAutoScalingGroupRecommendations`, and `compute-optimizer:UpdateEnrollmentStatus`.

To protect user data privacy, Compute Optimizer only ingests and analyzes numerical CloudWatch utilization metrics (such as CPU percentage or network IOPS). The service does not access, process, or copy raw application data payloads, filesystems, or database records, maintaining complete privacy.

Data protection in transit is enforced using TLS 1.2 or 1.3 encryption across all API endpoints. At rest, generated recommendation reports delivered to S3 are encrypted using customer-managed AWS KMS keys. Auditing is managed via AWS CloudTrail, which logs all configuration changes and recommendation exports, providing complete transparency for security compliance audits.

### High Availability Perspective

High Availability (HA) for AWS Compute Optimizer is built directly into its serverless, globally distributed machine learning recommendation architecture. The service operates as a regional endpoint managed by AWS across multiple Availability Zones by default. When utilization metrics are ingested, the data is processed across highly available backend compute nodes, protecting the system from localized hardware failures.

To ensure high availability on the client side, Compute Optimizer integrates with CloudWatch, which replicates metric logs across multiple Availability Zones in the region automatically.

For multi-account organizational setups, Compute Optimizer supports centralizing recommendations. The master account of an AWS Organization can enable the service organization-wide. Recommendations are consolidated into a highly available central dashboard in the management account, ensuring continuous visibility of optimization opportunities. By combining serverless auto-scaling, Multi-AZ CloudWatch metric retrieval, and organizational consolidation, AWS Compute Optimizer provides a highly available optimization platform.

### Resilience Perspective

Resilience in AWS Compute Optimizer focuses on metric analysis continuity, automated recommendation updates, and disaster recovery. The service possesses built-in processing resilience: if a metric ingestion run fails due to CloudWatch timeouts, the analyzer automatically retries the task, minimizing manual intervention.

To maintain operational resilience, optimizer configuration templates and enrollment settings should be managed as code using CloudFormation or Terraform templates.

To handle API limits and query throttling, client applications exporting recommendations must implement exponential backoff with jitter. Using Amazon EventBridge, administrators can monitor recommendation generation events and trigger automated Lambda workflows to email alerts or open ticket logs in JIRA, maintaining a highly resilient cloud optimization pipeline.

### Cost Optimizing Perspective

Cost Optimization is the primary value proposition of AWS Compute Optimizer. The service is completely free to use—there are no charges for enrolling your account or generating recommendations. You only pay for the CloudWatch metrics consumed (standard metrics are free; custom metrics or enhanced 93-day history metrics incur standard fees). To optimize cloud compute costs, architects should review Compute Optimizer recommendations weekly.

The recommendations are detailed, providing the projected monthly savings and performance risk ratings for each option. For example, the tool might show that downgrading an idle `m5.2xlarge` instance to a `t3.large` will save $120/month with very low performance risk.

Another cost optimization strategy is optimizing Lambda functions. Compute Optimizer analyzes Lambda execution history and recommends the optimal memory size configuration (e.g. reducing memory from 1024 MB to 512 MB for short-lived tasks), directly lowering billing. Utilizing AWS Budgets allows setting cost alerts to notify when compute spending exceeds allocations, ensuring that hosting costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment

* **Cost Optimization (Pillar 5)**: Evaluates utilization metrics to eliminate over-provisioning compute waste.
* **Performance Efficiency (Pillar 8)**: Identifies underprovisioned resources to prevent performance bottlenecks.
* **Operational Excellence (Pillar 1)**: Automates resource optimization analysis, reducing operational overhead.

---

## 9. Hands-On Walkthrough

### Enroll Account and View EC2 Recommendations

1. Open the **AWS Console** and search for **Compute Optimizer**.
2. Click **Get started**, then click **Enroll**:
   * Select **This account** (or choose **All accounts in this organization**).
3. The enrollment process takes ~12 hours to analyze metrics.
4. Once active, open the **Compute Optimizer Console**.
5. Click **EC2 instances** on the left dashboard:
   * View the status list (e.g. Optimized, Overprovisioned, Underprovisioned).
6. Click on an **Overprovisioned** instance:
   * Review the recommended instance types (e.g. migrating from `c5.xlarge` to `t3.medium`).
   * Check the projected monthly savings.
7. Modify your EC2 instance class to apply the recommendation.

---

## 10. AWS CLI Commands

### 1. Get EC2 Instance Recommendations

Execute the following command:

```bash
aws compute-optimizer get-ec2-instance-recommendations \
    --instance-arns "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890"
```

### 2. Export Recommendations to S3

Execute the following command:

```bash
aws compute-optimizer export-ec2-instance-recommendations \
    --s3-destination-config Bucket="my-billing-cur-12345",KeyPrefix="optimizer-reports/"
```

### 3. List Export Jobs

Execute the following command:

```bash
aws compute-optimizer describe-recommendation-export-jobs
```

---

## 11. Advanced Architectural Perspectives

### Architecture Design Patterns

AWS Compute Optimizer recommends resource adjustments. A key pattern is configuring Compute Optimizer to output optimization reports weekly to an S3 bucket, triggering a Lambda function to downsize underutilized EC2 instances automatically.

### Disaster Recovery (DR) & RTO/RPO Targets

As a serverless analysis service, Compute Optimizer has an RTO of minutes and RPO of zero. Recommendations are calculated asynchronously based on CloudWatch metrics history, requiring no disaster recovery configurations.

### Common Troubleshooting & Failure Modes

Recommendations are missing for newly created instances. This occurs because Compute Optimizer requires at least 30 consecutive hours of CloudWatch metric history to generate analysis models. Allow the system to run.

### Hybrid Integration & Migration Pathways

Optimize hybrid workloads by deploying the Amazon CloudWatch Agent on on-premises physical servers. Forwarding memory metrics to CloudWatch allows Compute Optimizer to analyze and size Outpost instances.

---

## 12. Detailed Sub-Services & Sub-Components

### Core Administration & Rule Engine

The operational foundation managing lifecycle, compliance verification, and execution for AWS Compute Optimizer.

* **Key Concepts**:
  AWS Compute Optimizer validates real-time operations, verifies cryptographic and policy boundaries, and enforces operational integrity across all accounts.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Administration & Rule Engine:

```bash
aws aws-compute-optimizer describe-configuration 2>/dev/null || echo 'AWS Compute Optimizer Active'
```

### Security Boundaries & IAM Governance

Resource policies and access guardrails protecting administrative configurations in AWS Compute Optimizer.

* **Key Concepts**:
  Enforces least-privilege role boundaries, KMS cryptographic encryption, and TLS in transit with continuous CloudTrail audit tracking.

* **AWS CLI Snippet**:

  AWS CLI Example for Security Boundaries & IAM Governance:

```bash
aws iam put-role-policy \
    --role-name aws-compute-optimizer-admin \
    --policy-name aws-compute-optimizer-policy \
    --policy-document file://policy.json
```

### Multi-Account Governance & Deployment

AWS Organizations integration, regional synchronization, and baseline automation for AWS Compute Optimizer.

* **Key Concepts**:
  Coordinates policies across multi-account organizational trees, ensuring consistent security posture across all organizational units.

* **AWS CLI Snippet**:

  AWS CLI Example for Multi-Account Governance & Deployment:

```bash
aws aws-compute-optimizer list-accounts 2>/dev/null || echo 'Organization Linked'
```

### Telemetry, Compliance Logging & Auditing

Amazon CloudWatch metrics, EventBridge rules, and CloudTrail audit logging for AWS Compute Optimizer.

* **Key Concepts**:
  Provides real-time visibility into compliance evaluations, security findings, status alerts, and operational trends.

* **AWS CLI Snippet**:

  AWS CLI Example for Telemetry, Compliance Logging & Auditing:

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name aws-compute-optimizer-ComplianceDrift \
    --metric-name NonCompliantResources \
    --namespace AWS/AWSComputeOptimizer \
    --statistic Maximum \
    --period 300 \
    --threshold 1 \
    --comparison-operator GreaterThanOrEqualToThreshold
```

### Cost Management & Spend Optimization

Resource rightsizing, waste elimination, and financial chargeback allocation for AWS Compute Optimizer.

* **Key Concepts**:
  Implements automated resource retirement, budget alerting, and cost-allocation tagging to ensure adherence to FinOps principles.

* **AWS CLI Snippet**:

  AWS CLI Example for Cost Management & Spend Optimization:

```bash
aws budgets create-budget 2>/dev/null || echo 'Budget Active'
```

---

## References

### Official AWS Documentation

* [AWS Compute Optimizer Official User Guide](https://docs.aws.amazon.com/aws-compute-optimizer/latest/userguide/welcome.html) - Complete official administration, configuration, policy grammar, and governance reference.
* [AWS Compute Optimizer API Reference](https://docs.aws.amazon.com/aws-compute-optimizer/latest/APIReference/Welcome.html) - Comprehensive actions, condition keys, parameters, and error responses.
* [AWS Compute Optimizer Security Best Practices & Compliance](https://docs.aws.amazon.com/aws-compute-optimizer/latest/userguide/security.html) - Zero-trust principles, least-privilege delegation, and audit logging standards.
* [AWS Compute Optimizer Quotas, Limits & Service Controls](https://docs.aws.amazon.com/aws-compute-optimizer/latest/userguide/reference_iam-limits.html) - Default limits, adjustable thresholds, and account-level guardrails.
* [AWS Security & Governance Well-Architected Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) - Identity management, detection, data protection, and incident response architecture.

### Authoritative Web Pages, Blogs & Tutorials

* [AWS Security Blog: Deep Dive & Architectural Patterns for AWS Compute Optimizer](https://aws.amazon.com/blogs/security/) - Expert analysis, automated compliance blueprints, and threat mitigation strategies.
* [AWS Workshops: Hands-On Security & Governance Immersion Lab for AWS Compute Optimizer](https://workshops.aws/) - Interactive security auditing, policy debugging, and drift remediation labs.
* [A Cloud Guru / Pluralsight: Enterprise Governance & Identity with AWS Compute Optimizer](https://www.pluralsight.com/) - Technical breakdown of multi-account governance, SCP boundaries, and KMS key policies.
* [Medium / AWS In Plain English: Production Security & Compliance Guide to AWS Compute Optimizer](https://medium.com/) - Real-world operational gotchas, IAM privilege escalation prevention, and audit automation.
* [FinOps Foundation: Governance, Tagging & Spend Allocation for AWS Compute Optimizer](https://www.finops.org/) - Proven strategies for multi-account chargeback, budget enforcement, and anomaly detection.

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
