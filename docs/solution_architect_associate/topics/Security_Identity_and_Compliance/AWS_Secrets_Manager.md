# AWS Topic: AWS Secrets Manager

**Category:** Security, Identity, and Compliance
**Status:** ✅ Completed

---

## 1. High-Level Overview

AWS Secrets Manager is a serverless, fully managed configuration and credentials registry designed to enable organizations to protect secrets needed to access their applications, services, and IT resources. Traditionally, applications stored sensitive parameters—such as database passwords, API keys, and connection strings—directly in configuration files or codebases in cleartext. This practice exposed credentials to code repository leaks and violated compliance standards. AWS Secrets Manager addresses these challenges by offering a secure, API-accessible registry.

The service allows developers to store secrets as encrypted key-value pairs or raw text. Secrets Manager integrates with AWS KMS to encrypt secrets at rest automatically. A key value proposition of the service is **Automated Rotation**. Secrets Manager can run scheduled Lambda functions to change database credentials on target databases (like RDS) and update the secret record simultaneously without application downtime. By eliminating hardcoded credentials, Secrets Manager simplifies credential lifecycle governance.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)

* **Business Purpose**: Provides enterprise-grade cloud capabilities for **AWS Secrets Manager**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts

AWS Secrets Manager stores credentials. Key concepts include:

* **Secret**: The encrypted credential payload managed by the service.
* **Secret Rotation**: Scheduled automated updates of credentials using Lambda.
* **Version Label**: Indicators used to track secret updates (e.g., `AWSCURRENT`, `AWSPREVIOUS`).
* **Resource Policy**: Resource-based JSON policy used to share secrets across accounts.
* **Multi-Region Replica**: Replicated secrets synchronized automatically across regions.

---

## 3. Common Use Cases

* **RDS Database Password Rotation**: Automatically rotating MySQL admin passwords every 30 days.
* **Third-Party API Key Storage**: Storing payment gateway keys securely for serverless web applications.
* **Cross-Account Secret Sharing**: Allowing a central logging account to share connection strings with member accounts.
* **Kubernetes Credentials Ingestion**: Ingesting database credentials into EKS pods using CSI drivers.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)

* ⚠️ **Key Constraints**: Deleting secrets immediately is not possible (minimum recovery window is 7 days). Parameter Store standard is free, while Secrets Manager is paid.
* 🔒 **Security & Encryption**: Payloads encrypted with KMS. Supports automated Lambda rotation.
* ⚙️ **Performance/Scaling**: Client-side caching avoids API rate limits; multi-region replication ensures local DR access.

---

## 5. Comparison with Similar Services

| Parameter Registry | Cost | Built-in Auto Rotation | Size Limit |
| :--- | :--- | :--- | :--- |
| **AWS Secrets Manager** | Paid ($0.40/secret/mo) | Yes (via Lambda templates) | 64 KB |
| **SSM Parameter Store** | Free (Standard parameters) | No (manual rotation required) | 4 KB (Standard) / 8 KB |
| **AWS KMS** | Paid ($1.00/key/mo) | Yes (master key material only) | N/A (Cryptographic key) |
| **AWS AppConfig** | Paid | No | 1 MB |

---

## 6. Cost Optimization

## Optimize Secrets Manager costs by

* Using free SSM Parameter Store for non-sensitive configurations.
* Caching secrets client-side to minimize API query charges.
* Deleting expired or unused secrets promptly.
* Restricting secret replication to required disaster recovery regions.

---

## 7. In-Depth Perspectives

### Security Perspective

Security configuration in AWS Secrets Manager is critical because secrets represent the keys to your databases, external APIs, and corporate credentials. The security model leverages AWS KMS, resource-based policies, IAM access controls, and automated rotation. Access to create or retrieve secrets is governed by IAM, restricting API actions like `secretsmanager:CreateSecret`, `secretsmanager:GetSecretValue`, and `secretsmanager:RotateSecret`.

To protect secrets at rest, Secrets Manager encrypts all secret payloads using customer-managed AWS KMS keys.

For identity boundaries, Secrets Manager supports **Resource-Based Policies**. Resource policies allow sharing specific secrets across different AWS accounts securely (e.g. allowing an application in a production account to retrieve connection strings from a shared services account) without requiring complex cross-account roles. In transit, all secret transfers are secured using TLS. Auditing is managed via AWS CloudTrail, which logs all secret retrievals, providing complete transparency for compliance audits.

### High Availability Perspective

High Availability (HA) for AWS Secrets Manager is built directly into its serverless, globally distributed database registry architecture. The service is hosted by AWS across multiple Availability Zones in each region by default, ensuring continuous availability of secret retrieval APIs. If an Availability Zone experiences an outage, the Secrets Manager control plane remains operational, routing queries to active database nodes in remaining zones without manual intervention.

To ensure high availability across global environments, Secrets Manager supports **Multi-Region Secret Replication**.

Multi-region replication copies secrets automatically to target replica regions, maintaining synchronization. If a primary region experiences an outage, applications in the backup region can retrieve the replicated secrets locally with low latency, preventing regional dependencies. By combining serverless auto-scaling, Multi-AZ database replication, and multi-region replication, AWS Secrets Manager provides a highly available, robust configuration registry.

### Resilience Perspective

Resilience in AWS Secrets Manager focuses on retrieval cache recovery, database connection retries, and disaster recovery. The service possesses built-in connection resilience: if a secret retrieval query fails due to transient API timeouts, the client application can automatically retry the request, preserving database connectivity.

To maintain operational resilience, secret metadata, replication regions, and IAM roles should be managed as code using CloudFormation or Terraform templates.

To optimize application uptime during secret rotation, Secrets Manager maintains **Version Labels**. When a secret is rotated, the service retains the previous password version (`AWSPREVIOUS`) alongside the new version (`AWSCURRENT`). If the target database fails to apply the new credentials immediately, the application can fall back to the previous version, preventing system lockups and maintaining overall operational resilience.

### Cost Optimizing Perspective

Cost Optimization for AWS Secrets Manager involves managing active secret counts, optimizing API request volumes, and choosing the right parameter services. Secrets Manager is a paid service, charging a flat fee per secret per month ($0.40 per secret) and API query charges ($0.05 per 10,000 requests). While this is highly cost-effective, storing thousands of temporary developer environment variables or non-critical config parameters in Secrets Manager can run up significant charges. To optimize these costs, developers should use **AWS Systems Manager Parameter Store** (which is free for standard parameters) for non-sensitive configurations, reserving Secrets Manager only for critical credentials that require automated rotation.

Additionally, optimizing API queries is essential. In high-volume serverless or container applications, developers should implement **Client-Side Caching**.

By caching the retrieved secret value locally in application memory for a short duration (e.g. 5 minutes), the application avoids calling the Secrets Manager API for every individual database connection, reducing API costs by up to 90%. Utilizing AWS Budgets allows setting cost alerts to notify when secret counts or API spending exceeds allocations, ensuring that cloud security costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment

* **Cost Optimization (Pillar 5)**: Charges per secret; client-side caching minimizes API request fees.
* **Security (Pillar 2)**: Integrates with KMS for payload encryption and resource-based policies for cross-account isolation.
* **Operational Excellence (Pillar 1)**: Automates credential rotation, eliminating manual password updates.

---

## 9. Hands-On Walkthrough

### Store and Automatically Rotate an RDS Password

1. Open the **AWS Console** and search for **Secrets Manager**.
2. Click **Store a new secret**.
3. **Secret type**: Select **Credentials for Amazon RDS database**:
   * **Username**: `admin`. **Password**: Enter secure password.
   * **Database**: Select your active RDS database. Click **Next**.
4. **Secret name**: `production/database/rds-mysql`. Click **Next**.
5. **Configure rotation**:
   * Enable **Automatic rotation**.
   * **Rotation schedule**: Select **30 days**.
   * **Rotation function**: Select **Create a new Lambda function** (Enter name `RotateMySQLSecret`). Click **Next**.
6. Review the generated code snippets (displaying how to query the secret in Python/Java), click **Store**.
7. Secrets Manager will deploy the Lambda function and execute the initial rotation test automatically.

---

## 10. AWS CLI Commands

### 1. Retrieve Secret Value

Execute the following command:

```bash
aws secretsmanager get-secret-value \
    --secret-id "production/database/rds-mysql"
```

### 2. Create a Secret

Execute the following command:

```bash
aws secretsmanager create-secret \
    --name "ApiKey" \
    --secret-string "secret-token-12345"
```

---

## 11. Advanced Architectural Perspectives

### Architecture Design Patterns

AWS Secrets Manager stores credentials. A key design pattern is using Secrets Manager with Lambda to execute automated 30-day database credential rotation, updating the secret and RDS DB simultaneously.

### Disaster Recovery (DR) & RTO/RPO Targets

Secrets Manager is serverless and Multi-AZ. To achieve high resilience, configure **Multi-Region Secret Replication** to copy secrets to standby regions automatically, ensuring local access during outages.

### Common Troubleshooting & Failure Modes

Applications experience timeouts during credential rotation. Prevent this by configuring application code to catch login errors and fetch the latest secret version from the API.

### Hybrid Integration & Migration Pathways

Expose database credentials safely to local systems by using Secrets Manager. On-premises server applications retrieve API keys privately over Direct Connect connections via VPC interface endpoints.

---

## 12. Detailed Sub-Services & Sub-Components

### Secrets & Automatic Rotation

Secure, encrypted credential storage with native Lambda-driven rotation for RDS, DocumentDB, and Redshift.

* **Key Concepts**:
  Secrets Manager encrypts credentials at rest with KMS and rotates passwords on a schedule (e.g. every 30 days) using pre-built Lambda rotation templates without application downtime.

* **AWS CLI Snippet**:

  AWS CLI Example for Secrets & Automatic Rotation:

```bash
aws secretsmanager create-secret \
    --name prod/db/mysql \
    --description 'Production MySQL DB credentials' \
    --secret-string '{"username":"admin","password":"ComplexPassword123!"}'
```

### Secret Versioning & Staging Labels

Maintains AWSCURRENT, AWSPREVIOUS, and AWSPENDING staging labels during password rotation.

* **Key Concepts**:
  Ensures seamless multi-stage credential updates: 1) create pending secret, 2) update database user password, 3) test connection, 4) promote pending secret to AWSCURRENT.

* **AWS CLI Snippet**:

  AWS CLI Example for Secret Versioning & Staging Labels:

```bash
aws secretsmanager get-secret-value \
    --secret-id prod/db/mysql \
    --version-stage AWSCURRENT
```

---

## References

### Official AWS Documentation

* [AWS Secrets Manager Official User Guide](https://docs.aws.amazon.com/aws-secrets-manager/latest/userguide/welcome.html) - Complete official administration, configuration, policy grammar, and governance reference.
* [AWS Secrets Manager API Reference](https://docs.aws.amazon.com/aws-secrets-manager/latest/APIReference/Welcome.html) - Comprehensive actions, condition keys, parameters, and error responses.
* [AWS Secrets Manager Security Best Practices & Compliance](https://docs.aws.amazon.com/aws-secrets-manager/latest/userguide/security.html) - Zero-trust principles, least-privilege delegation, and audit logging standards.
* [AWS Secrets Manager Quotas, Limits & Service Controls](https://docs.aws.amazon.com/aws-secrets-manager/latest/userguide/reference_iam-limits.html) - Default limits, adjustable thresholds, and account-level guardrails.
* [AWS Security & Governance Well-Architected Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) - Identity management, detection, data protection, and incident response architecture.

### Authoritative Web Pages, Blogs & Tutorials

* [AWS Security Blog: Deep Dive & Architectural Patterns for AWS Secrets Manager](https://aws.amazon.com/blogs/security/) - Expert analysis, automated compliance blueprints, and threat mitigation strategies.
* [AWS Workshops: Hands-On Security & Governance Immersion Lab for AWS Secrets Manager](https://workshops.aws/) - Interactive security auditing, policy debugging, and drift remediation labs.
* [A Cloud Guru / Pluralsight: Enterprise Governance & Identity with AWS Secrets Manager](https://www.pluralsight.com/) - Technical breakdown of multi-account governance, SCP boundaries, and KMS key policies.
* [Medium / AWS In Plain English: Production Security & Compliance Guide to AWS Secrets Manager](https://medium.com/) - Real-world operational gotchas, IAM privilege escalation prevention, and audit automation.
* [FinOps Foundation: Governance, Tagging & Spend Allocation for AWS Secrets Manager](https://www.finops.org/) - Proven strategies for multi-account chargeback, budget enforcement, and anomaly detection.

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
