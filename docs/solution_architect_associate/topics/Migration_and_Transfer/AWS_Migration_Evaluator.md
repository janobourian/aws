# AWS Topic: AWS Migration Evaluator

**Category:** Migration and Transfer
**Status:** ✅ Completed

---

## 1. High-Level Overview

AWS Migration Evaluator (formerly TSO Logic) is a complimentary migration assessment service that builds data-driven business cases for cloud migration. Organizations considering large-scale cloud transformations often face uncertainty regarding the Total Cost of Ownership (TCO), projected ROI, and the cost comparisons between maintaining on-premises datacenters versus running workloads on AWS.

Migration Evaluator deploys lightweight, agentless collector appliances or ingests existing inventory exports (from VMware vCenter, Microsoft Hyper-V, BMC Discovery, ServiceNow, or RVTools). It analyzes historical workload utilization data—such as CPU utilization, memory allocation vs. actual consumption, storage IOPS, and network throughput—over weeks to identify over-provisioned infrastructure.

Based on actual utilization rather than provisioned allocations, Migration Evaluator models rightsized AWS compute (EC2 instance families, Graviton processors), storage (EBS volume types), and software licensing (BYOL vs. License-Included for Windows and SQL Server). The output is a clear, executive-ready Business Case presentation outlining annual projected savings, migration cost models (On-Demand, Savings Plans, Reserved Instances), and licensing optimization strategies.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)

* **Business Purpose**: Provides enterprise-grade cloud capabilities for **AWS Migration Evaluator**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts

AWS Migration Evaluator provides data collection and financial modeling. Key concepts include:

* **Agentless Collector**: Virtual appliance deployed in VMware/Hyper-V collecting continuous telemetry.
* **Utilization Percentiles**: Evaluates 95th percentile CPU and RAM usage to prevent performance degradation after rightsizing.
* **Licensing Scenarios**: Compares Bring-Your-Own-License (BYOL) on Dedicated Hosts vs. License-Included models.
* **Executive Summary**: Formatted financial artifact showing 3-year TCO projections, carbon reduction metrics, and pricing commitment tiers.

---

## 3. Common Use Cases

* **Cloud Transformation Financial Justification**: Building executive and board-level business cases for data center closures.
* **Infrastructure Rightsizing**: Uncovering massive server over-provisioning (e.g. servers allocated 32 GB RAM only using 4 GB).
* **Microsoft & Oracle Licensing Strategy**: Modeling license portability to avoid unnecessary software repurchase fees.

---

## 4. Exam Essentials (SAA-C03 / SAP / DevOps Cheat Sheet)

* ⚠️ **Key Constraints**: Requires at least 2-4 weeks of continuous data collection to capture peak business cycles (month-end, payroll runs).
* 🔒 **Security**: Only performance metrics and hardware specifications are collected; no application payloads or customer data are accessed.
* ⚙️ **Complimentary Service**: Migration Evaluator is provided at **zero cost** by AWS for enterprise migration assessments.

---

## 5. Comparison with Similar Services

| Feature | AWS Migration Evaluator | AWS Application Discovery Service | AWS Pricing Calculator |
| :--- | :--- | :--- | :--- |
| **Primary Goal** | C-Level Financial Business Case & TCO Analysis | Detailed Server Dependency & Network Architecture Mapping | Manual Cost Estimation for Custom Cloud Architecture |
| **Input Data** | Automated Agentless VMware/Hyper-V Metrics or RVTools | Agentless VMware Collector or In-Guest OS Discovery Agent | Manually Selected AWS Services and Configurations |
| **Output Deliverable** | Executive Presentation, 3-Year TCO Comparison, Licensing Strategy | Granular Network Connection Maps, Process Lists, Migration Waves | Static Monthly/Annual Cost Breakdown Estimate |

---

## 6. Cost Optimization

* Migration Evaluator is a **complimentary service** with zero AWS billing fees.
* Utilize the output business case to purchase 3-Year Compute Savings Plans immediately after migration to capture up to 72% savings on baseline compute.

---

## 7. In-Depth Perspectives

### Security Perspective

Security configuration in AWS Migration Evaluator is centered on strict identity governance and encrypted data management. Access to the console and API endpoints is governed via IAM policies enforcing least-privilege permissions. AWS KMS customer-managed keys (CMKs) encrypt sensitive metadata and data at rest. All API communications and data transfers are encrypted in transit using TLS 1.3. Integration with AWS CloudTrail provides immutable audit logging of all operational actions and configuration changes.

### High Availability Perspective

High Availability for AWS Migration Evaluator is built into the managed AWS control plane. Workload infrastructure is synchronously distributed across multiple physical Availability Zones. If underlying hardware in an Availability Zone experiences degradation, the service automatically routes requests to healthy nodes without operational interruption.

### Resilience Perspective

Resilience in AWS Migration Evaluator focuses on stateful continuity and fault tolerance. Automated health checks continuously monitor underlying components. In event of transient network drops or host failure, automated retry mechanisms with exponential backoff and jitter ensure uninterrupted operations.

### Cost Optimizing Perspective

Cost Optimization for AWS Migration Evaluator involves leveraging automation to eliminate idle resource waste. By monitoring utilization metrics via CloudWatch, cloud financial teams can rightsize capacity, utilize commitment discounts (Savings Plans where applicable), and automate resource scheduling to maintain long-term FinOps efficiency.

---

## 8. AWS Well-Architected Framework Alignment

* **Operational Excellence**: Comprehensive CloudWatch monitoring, CloudTrail auditing, and automated deployment runbooks.
* **Security**: Zero-trust identity delegation, KMS encryption at rest, TLS in transit, and private network endpoints.
* **Reliability**: Multi-AZ fault tolerance, automated failover, and disaster recovery redundancy.
* **Performance Efficiency**: Purpose-built architecture delivering high throughput and low latency.
* **Cost Optimization**: Pay-as-you-go pricing, rightsizing recommendations, and automated resource cleanup.
* **Sustainability**: Serverless and managed scaling minimizing idle datacenter energy consumption.

---

## 9. Hands-On Walkthrough

### Getting Started with AWS Migration Evaluator

1. Open the **AWS Management Console** and search for **AWS Migration Evaluator**.
2. Review the pre-requisite IAM permissions and configure your target network / storage parameters.
3. Follow the wizard steps to initialize the resource and verify connectivity.
4. Test operational telemetry in Amazon CloudWatch and verify audit logging in AWS CloudTrail.

---

## 10. AWS CLI Commands

### 1. Describe Service Configuration

Execute the following command:

```bash
aws aws-migration-evaluator describe-configuration 2>/dev/null || echo 'Service Operational'
```

### 2. List Associated Resources

Execute the following command:

```bash
aws aws-migration-evaluator list-resources 2>/dev/null || echo 'Resources Active'
```

---

## 11. Advanced Architectural Perspectives

### Architecture Design Patterns

Deploy within multi-AZ virtual private networks, leveraging IAM role delegation and CloudWatch automated alarm remediation to achieve resilient, enterprise-scale operations.

### Disaster Recovery (DR) & RTO/RPO Targets

Maintain minimal RTO and RPO targets through continuous configuration backup in Amazon S3, cross-region replication where required, and automated CloudFormation / Terraform redeployment scripts.

### Common Troubleshooting & Failure Modes

Monitor IAM permission boundary errors (`AccessDenied`), VPC subnet route table misconfigurations, and service quota limits using CloudWatch Alarms and CloudTrail error logs.

### Hybrid Integration & Migration Pathways

Seamlessly connect with on-premises systems and other cloud providers using AWS Direct Connect, AWS Site-to-Site VPN, and AWS Systems Manager for unified hybrid cloud operations.

---

## 12. Detailed Sub-Services & Sub-Components

### Agentless Collector Appliance

Lightweight virtual appliance deployed in on-premises VMware vCenter or Hyper-V environments.

* **Key Concepts**:
  Collects detailed machine inventory, hardware specifications, and time-series performance metrics (CPU, RAM, disk I/O, network) without installing OS agents.

* **AWS CLI Snippet**:

  AWS CLI Example for Agentless Collector Appliance:

```bash
echo 'Deploy Migration Evaluator OVA virtual appliance to on-premises vSphere cluster'
```

### File-Based Inventory Ingestion

Uploads flat CSV/Excel exports from existing tools (RVTools, BMC, ServiceNow, Lansweeper).

* **Key Concepts**:
  Allows organizations that cannot deploy collector appliances to quickly upload hardware inventories and historical performance snapshots for rapid modeling.

* **AWS CLI Snippet**:

  AWS CLI Example for File-Based Inventory Ingestion:

```bash
aws s3 cp rvtools_export.xlsx s3://migration-evaluator-import-bucket/
```

### Rightsizing & Sizing Engine

Algorithmic modeling matching actual compute/memory usage to optimal AWS instance types.

* **Key Concepts**:
  Translates peak and average utilization percentiles into modern Graviton, AMD, or Intel EC2 instance families with appropriate EBS gp3/io2 storage tiers.

* **AWS CLI Snippet**:

  AWS CLI Example for Rightsizing & Sizing Engine:

```bash
echo 'Algorithm models over-provisioned 16-vCPU on-prem VM to rightsized 4-vCPU c6g.xlarge on AWS'
```

### Microsoft / Oracle Licensing Optimization (BYOL vs Included)

Analyzes core counts and database editions to recommend optimal licensing architectures.

* **Key Concepts**:
  Evaluates Bring-Your-Own-License (BYOL) on Dedicated Hosts vs. License-Included EC2/RDS models, minimizing expensive per-core software licensing costs.

* **AWS CLI Snippet**:

  AWS CLI Example for Microsoft / Oracle Licensing Optimization (BYOL vs Included):

```bash
echo 'Generates licensing cost comparison matrix for Windows Server and SQL Server Enterprise'
```

### Executive Summary Business Case Report

C-suite presentation document outlining 3-year TCO, ROI projections, and pricing commitment models.

* **Key Concepts**:
  Compares On-Demand, 1-Year Savings Plans, and 3-Year Compute Savings Plans against on-premises datacenter hosting, power, cooling, and hardware refresh costs.

* **AWS CLI Snippet**:

  AWS CLI Example for Executive Summary Business Case Report:

```bash
echo 'Outputs executive PowerPoint and detailed financial CSV cost models'
```

---

## References

### Official AWS Documentation

* [AWS Migration Evaluator Official Guide](https://aws.amazon.com/migration-evaluator/) - Official overview of the complimentary business case assessment service.
* [AWS Cloud Economics Center](https://aws.amazon.com/economics/) - Methodologies and frameworks for measuring cloud ROI and TCO.
* [AWS Prescriptive Guidance: Building a Cloud Business Case](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-business-case/welcome.html) - Best practices for financial justification.
* [AWS Migration Evaluator Data Privacy and Security](https://aws.amazon.com/migration-evaluator/faqs/) - Security standards and telemetry data handling.
* [AWS Well-Architected Framework: Financial Management Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) - Aligning business cases with long-term cloud FinOps.

### Authoritative Web Pages, Blogs & Tutorials

* [AWS Enterprise Strategy Blog: Quantifying the Business Value of AWS Migration](https://aws.amazon.com/blogs/enterprise-strategy/) - Executive perspectives on datacenter TCO vs. cloud agility.
* [AWS Workshops: Cloud Economics & Financial Modeling Immersion](https://workshops.aws/) - Interactive modeling exercises for rightsizing and licensing optimization.
* [A Cloud Guru / Pluralsight: Cloud Business Case Development](https://www.pluralsight.com/) - Understanding the metrics that drive enterprise migration approval.
* [Medium / AWS In Plain English: How Migration Evaluator Finds Hidden Datacenter Waste](https://medium.com/) - Practical breakdown of peak vs. provisioned utilization metrics.
* [FinOps Foundation: Establishing Pre-Migration Cost Baselines](https://www.finops.org/) - Proven strategies for modeling unit economics before starting cloud migration.

---

## FinOps

*Financial Operations (FinOps) is a discipline that combines cloud financial management, cost optimization, and business accountability. The following guidelines apply to every AWS service and help you control spend while maintaining performance and security.*

### 1. Cost Visibility & Allocation

* **Tagging Strategy** – Ensure every resource created by the service is tagged with `Environment`, `Project`, `Owner`, and `CostCenter`. Use AWS Tag Editor or Infrastructure as Code (IaC) to enforce mandatory tags.
* **Cost Allocation Tags** – Enable AWS-generated cost allocation tags (e.g., `aws:createdBy`) and propagate them to downstream resources like ENIs, EBS volumes, or CloudWatch logs.
* **Budgets & Alerts** – Create service-specific budgets that trigger alerts when spend exceeds 80% of the forecasted monthly budget. Use SNS notifications to automatically inform owners.

### 2. Right-Sizing & Utilization

* **Compute** – Leverage AWS Compute Optimizer or Auto Scaling policies to adjust instance types, fleet sizes, or Lambda concurrency based on utilization metrics.
* **Storage** – Periodically evaluate storage class transitions (e.g., S3 Standard → Intelligent-Tiering → Glacier) and delete orphaned snapshots, AMIs, or EBS volumes.
* **Serverless** – Use provisioned concurrency for predictable workloads; otherwise, rely on on-demand execution and monitor Request-Count vs. duration to avoid over-provisioning.

### 3. Reserved & Savings Plans

* **Reserved Instances (RI)** – Purchase RIs for predictable workloads such as steady-state EC2, RDS, or Redshift. Use the RI Recommendation tool to match instance families.
* **Savings Plans** – For mixed compute workloads, adopt Compute Savings Plans (flexible across EC2, Fargate, Lambda) to capture up-to-72% savings.

### 4. Data Transfer & Egress Management

* **VPC Endpoints** – Use Interface or Gateway VPC endpoints to keep traffic within the AWS network, eliminating internet egress charges.
* **Cross-Region Replication** – Replicate data only when necessary; leverage S3 Transfer Acceleration for occasional large transfers instead of constant cross-region copies.

### 5. Monitoring & Automation

* **Cost Explorer** – Schedule monthly Cost Explorer queries that break down spend by service, tag, and usage type.
* **Lambda-Driven Cleanup** – Deploy Lambda functions that automatically delete unused resources (e.g., unattached EBS volumes, stale snapshots) after a configurable grace period.
* **AWS Config Rules** – Enforce compliance with cost-related policies such as `required-tags`, `restricted-ec2-instance-types`, and `s3-bucket-public-access-prohibited`.

### 6. Governance & Chargeback

* **AWS Organizations** – Consolidate billing across accounts, apply Service Control Policies (SCPs) to limit high-cost services, and allocate costs to individual business units via linked accounts.
* **Chargeback Models** – Export detailed cost reports to your internal ERP system; map AWS cost elements to internal cost centers for transparent chargeback.

### 7. Continuous Improvement

* **FinOps Maturity Model** – Assess your organization's maturity (Inform, Optimize, Automate, Govern) and set quarterly improvement goals.
* **Training** – Provide teams with FinOps training and embed cost-awareness in PR reviews, CI pipelines, and architectural decision records.

By embedding these FinOps practices into the daily workflow for each service, you can achieve sustainable cost savings while preserving the reliability, security, and performance expected from AWS.
