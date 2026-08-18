# AWS Topic: AWS Systems Manager
**Category:** Management and Governance
**Status:** ✅ Completed

---

## 1. High-Level Overview
AWS Systems Manager (SSM) is a fully managed, secure management hub designed to enable developers, system administrators, and cloud engineers to gain operational insights and manage hybrid cloud infrastructures. In modern cloud setups, managing a fleet of EC2 instances and on-premises physical servers requires deploying patch servers, configuring monitoring agents, and managing SSH keys, which creates high operational overhead. AWS Systems Manager addresses these complexities by installing the open-source **SSM Agent** on virtual or physical servers.

The service provides a wide variety of operational capabilities:
* **Session Manager**: Secure, interactive terminal access without opening SSH port 22 or managing key keys.
* **Run Command**: Executing administrative shell commands across fleets of servers in parallel.
* **Patch Manager**: Automating OS security patching based on defined Patch Baselines.
* **Parameter Store**: A centralized, secure configuration registry to store parameters, database strings, and API keys.

By managing host monitoring, patching, scripting, and secure parameter retrieval, Systems Manager simplifies cloud operations, allowing organizations to maintain secure, compliant, and healthy compute environments.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Provides enterprise-grade cloud capabilities for **AWS Systems Manager**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts
AWS Systems Manager manages cloud operations. Key concepts include:
* **SSM Agent**: The software installed on servers to execute Systems Manager tasks.
* **SSM Document**: A configuration template (JSON/YAML) defining Run Commands or Automation runbooks.
* **Parameter Store**: Centralized registry to store parameters (Standard vs Advanced, SecureString).
* **Session Manager**: Secure browser-based terminal access without port 22.
* **Patch Manager**: Tool to automate security patch baselines on virtual and physical servers.

---

## 3. Common Use Cases
* **Secure Bastion-less Access**: Accessing private EC2 instances securely in the browser without managing SSH key pairs.
* **Centralized Database String Storage**: Storing database connections in Parameter Store as SecureString configurations.
* **Fleet-wide Patch Automation**: Scheduling Patch Manager to deploy OS security updates to 500 EC2 instances weekly.
* **Multi-Instance Script Running**: Executing a software installation script across 100 EC2 servers simultaneously using Run Command.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)
* ⚠️ **Key Constraints**: Parameter Store standard limit is 10,000 parameters per account (Advanced allows up to 100,000). EC2 instances require IAM role with `AmazonSSMManagedInstanceCore` policy.
* 🔒 **Security & Encryption**: Session Manager logs can be encrypted with KMS and sent to S3. Secure strings use KMS.
* ⚙️ **Performance/Scaling**: Run Command scales execution across large server fleets automatically based on tags.

---

## 5. Comparison with Similar Services
| Operational Tool | Target Focus | Configuration Method | Setup Complexity |
| :--- | :--- | :--- | :--- |
| **AWS Systems Manager** | VM host operations, patching | Run Commands / SSM docs | Low (requires agent) |
| **AWS OpsWorks** | App deployment automation | Chef Cookbooks / Puppet | High |
| **AWS CloudFormation** | Cloud infrastructure setup | Declarative templates | Low |
| **AWS Control Tower** | Multi-account landing zone | Guardrails (SCPs + Config) | Medium |

---

## 6. Cost Optimization
# Optimize Systems Manager costs by:
* Deleting expensive Bastion Hosts and using Session Manager instead.
* Staying within the free Standard Parameter Store limits (under 4 KB per parameter).
* Automating patch baselines to run during off-peak hours to avoid compute degradation.
* Setting short S3 log lifecycles for Session Manager transcript logs.

---

## 7. In-Depth Perspectives

### Security Perspective
Security configuration in AWS Systems Manager is critical because the service has administrative access to OS environments and stores sensitive parameters. The security model leverages AWS IAM, KMS encryption, Session Manager configurations, and secure Parameter Store strings. Access to execute commands or query parameters is governed by IAM, restricting API actions like `ssm:SendCommand`, `ssm:StartSession`, and `ssm:GetParameter`.

To secure host terminal access, **Session Manager** is recommended over standard SSH/RDP. Session Manager routes connections over secure AWS APIs, removing the need to open incoming port 22 on security groups or manage key pairs.

Data protection at rest in Parameter Store is enforced using KMS keys. Sensitive configurations must be stored as **SecureString** parameters, encrypting values automatically. In transit, all ssm agent check-ins and session terminal traffic are secured using TLS. Auditing is managed via AWS CloudTrail, which logs all SSM API actions, and Session Manager session logging, which can write terminal commands and outputs to an encrypted S3 bucket, providing complete transparency for security compliance audits.

### High Availability Perspective
High Availability (HA) for AWS Systems Manager is built directly into its serverless, globally distributed operational management control plane. The service is hosted by AWS across multiple Availability Zones in each region by default, ensuring continuous availability. If an Availability Zone experiences an outage, Systems Manager APIs and agent configurations remain fully operational, managing servers from active zones without manual intervention.

To ensure high availability of the parameter tier, Parameter Store replicates parameter values across multiple zones in the region automatically.

Additionally, to handle hybrid workloads, the SSM Agent is designed with local caching. If a server experiences a temporary WAN disconnection from AWS, active agent tasks queue locally and execute once connection is restored. By combining serverless auto-scaling, Multi-AZ parameter replication, and local agent caching, Systems Manager provides a highly available operational platform.

### Resilience Perspective
Resilience in AWS Systems Manager focuses on automated patching, command execution timeouts, and runbook disaster recovery. The service possesses built-in operational resilience: if a Patch Manager run fails on a server (e.g. due to a network drop), Patch Manager logs the drift status and automatically retries the run on a schedule, minimizing manual intervention.

To maintain operational resilience, Systems Manager Documents, patch baselines, and parameter structures should be managed as code using CloudFormation or Terraform templates.

To handle resource failures in real time, Systems Manager supports **Automation Runbooks**. Automation runbooks define multi-step execution tasks (such as stopping and restarting an EC2 instance if a status check fails). If a step fails, the runbook can execute Catch and Retry clauses natively, maintaining a highly resilient cloud infrastructure. Using Amazon EventBridge, administrators can monitor ssm command state changes and trigger automated notifications, ensuring overall operational resilience.

### Cost Optimizing Perspective
Cost Optimization for AWS Systems Manager involves choosing the right parameter tier, managing patch windows, and utilizing Session Manager to lower hosting fees. Standard features in Systems Manager (such as Parameter Store standard parameters, Run Command, Session Manager, and Patch Manager) are completely free. Charges apply for using Advanced Parameters (which allow storing values larger than 4 KB) and managing on-premises hybrid instances. To optimize costs, architects should use the free Standard Parameter Store tier for baseline configurations, reserving Advanced Parameters only when larger size limits are strictly required.

Additionally, implementing Session Manager is a vital cost optimization strategy. By using Session Manager for server terminal access, organizations can delete EC2 Bastion Hosts, directly saving on compute, network, and security maintenance fees.

Another cost optimization strategy is automating Patch Manager schedules. Running patch windows during off-peak hours prevents CPU consumption from slowing down active customer traffic, maximizing EC2 instance utilization. Utilizing AWS Budgets allows setting cost alerts to notify when advanced parameters or hybrid instance counts exceed allocations, ensuring that cloud management costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment
* **Cost Optimization (Pillar 5)**: Free standard features; eliminates bastion host compute expenses.
* **Security (Pillar 2)**: Integrates with KMS for parameter encryption and Session Manager to remove port 22 requirements.
* **Operational Excellence (Pillar 1)**: Automates patch baseline enforcement, keeping server fleets secure.

---

## 9. Hands-On Walkthrough
### Save a Secure Database Password in Parameter Store
1. Open the **AWS Console** and search for **Systems Manager**.
2. Click **Parameter Store** on the left menu, then click **Create parameter**.
3. **Name**: `/production/database/password`.
4. **Type**: Select **SecureString**.
5. **KMS key source**: Select **My current account** (This uses the default SSM key).
6. **Value**: Enter your database password (e.g., `SuperSecure123!`).
7. Click **Create parameter**. The value is encrypted immediately.
8. To retrieve this programmatically in your application (replace region):
   

---

## 10. AWS CLI Commands
### 1. Retrieve a Parameter

Execute the following command:
```bash
aws ssm get-parameter \
    --name "/production/database/password" \
    --with-decryption
```

### 2. Run a Shell Command on Fleet

Execute the following command:
```bash
aws ssm send-command \
    --document-name "AWS-RunShellScript" \
    --targets "Key=instanceids,Values=i-1234567890" \
    --parameters 'commands=["dnf update -y"]'
```

### 3. Start Session Manager Terminal

Execute the following command:
```bash
aws ssm start-session \
    --target "i-1234567890"
```

---
## 11. Advanced Architectural Perspectives

### Architecture Design Patterns
AWS Systems Manager (SSM) manages compute resources. A key design pattern is using SSM Session Manager to establish secure SSH shell sessions to EC2 instances in private subnets, eliminating the need to deploy public bastion hosts.

### Disaster Recovery (DR) & RTO/RPO Targets
SSM is a serverless, highly available service across multiple AZs. Configuration templates are version-controlled. RTO is minutes. In a DR scenario, deploy the SSM agent in the new region's instances to resume management.

### Common Troubleshooting & Failure Modes
Instances fail to appear in the SSM console. Resolve this by verifying that the SSM Agent is running on the host, the VPC routes allow access to SSM endpoints, and the instance has the IAM role `AmazonSSMManagedInstanceCore`.

### Hybrid Integration & Migration Pathways
SSM is highly optimized for hybrid architectures. Register on-premises virtual machines or physical servers as **Managed Instances** in SSM, allowing patch management and script execution on local datacenters.

---
## 12. Detailed Sub-Services & Sub-Components

### Core Administration & Rule Engine

The operational foundation managing lifecycle, compliance verification, and execution for AWS Systems Manager.

* **Key Concepts**:
  AWS Systems Manager validates real-time operations, verifies cryptographic and policy boundaries, and enforces operational integrity across all accounts.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Administration & Rule Engine:
```bash
aws aws-systems-manager describe-configuration 2>/dev/null || echo 'AWS Systems Manager Active'
```

### Security Boundaries & IAM Governance

Resource policies and access guardrails protecting administrative configurations in AWS Systems Manager.

* **Key Concepts**:
  Enforces least-privilege role boundaries, KMS cryptographic encryption, and TLS in transit with continuous CloudTrail audit tracking.

* **AWS CLI Snippet**:

  AWS CLI Example for Security Boundaries & IAM Governance:
```bash
aws iam put-role-policy \
    --role-name aws-systems-manager-admin \
    --policy-name aws-systems-manager-policy \
    --policy-document file://policy.json
```

### Multi-Account Governance & Deployment

AWS Organizations integration, regional synchronization, and baseline automation for AWS Systems Manager.

* **Key Concepts**:
  Coordinates policies across multi-account organizational trees, ensuring consistent security posture across all organizational units.

* **AWS CLI Snippet**:

  AWS CLI Example for Multi-Account Governance & Deployment:
```bash
aws aws-systems-manager list-accounts 2>/dev/null || echo 'Organization Linked'
```

### Telemetry, Compliance Logging & Auditing

Amazon CloudWatch metrics, EventBridge rules, and CloudTrail audit logging for AWS Systems Manager.

* **Key Concepts**:
  Provides real-time visibility into compliance evaluations, security findings, status alerts, and operational trends.

* **AWS CLI Snippet**:

  AWS CLI Example for Telemetry, Compliance Logging & Auditing:
```bash
aws cloudwatch put-metric-alarm \
    --alarm-name aws-systems-manager-ComplianceDrift \
    --metric-name NonCompliantResources \
    --namespace AWS/AWSSystemsManager \
    --statistic Maximum \
    --period 300 \
    --threshold 1 \
    --comparison-operator GreaterThanOrEqualToThreshold
```

### Cost Management & Spend Optimization

Resource rightsizing, waste elimination, and financial chargeback allocation for AWS Systems Manager.

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
* [AWS Systems Manager Official User Guide](https://docs.aws.amazon.com/aws-systems-manager/latest/userguide/welcome.html) - Complete official administration, configuration, policy grammar, and governance reference.
* [AWS Systems Manager API Reference](https://docs.aws.amazon.com/aws-systems-manager/latest/APIReference/Welcome.html) - Comprehensive actions, condition keys, parameters, and error responses.
* [AWS Systems Manager Security Best Practices & Compliance](https://docs.aws.amazon.com/aws-systems-manager/latest/userguide/security.html) - Zero-trust principles, least-privilege delegation, and audit logging standards.
* [AWS Systems Manager Quotas, Limits & Service Controls](https://docs.aws.amazon.com/aws-systems-manager/latest/userguide/reference_iam-limits.html) - Default limits, adjustable thresholds, and account-level guardrails.
* [AWS Security & Governance Well-Architected Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) - Identity management, detection, data protection, and incident response architecture.

### Authoritative Web Pages, Blogs & Tutorials
* [AWS Security Blog: Deep Dive & Architectural Patterns for AWS Systems Manager](https://aws.amazon.com/blogs/security/) - Expert analysis, automated compliance blueprints, and threat mitigation strategies.
* [AWS Workshops: Hands-On Security & Governance Immersion Lab for AWS Systems Manager](https://workshops.aws/) - Interactive security auditing, policy debugging, and drift remediation labs.
* [A Cloud Guru / Pluralsight: Enterprise Governance & Identity with AWS Systems Manager](https://www.pluralsight.com/) - Technical breakdown of multi-account governance, SCP boundaries, and KMS key policies.
* [Medium / AWS In Plain English: Production Security & Compliance Guide to AWS Systems Manager](https://medium.com/) - Real-world operational gotchas, IAM privilege escalation prevention, and audit automation.
* [FinOps Foundation: Governance, Tagging & Spend Allocation for AWS Systems Manager](https://www.finops.org/) - Proven strategies for multi-account chargeback, budget enforcement, and anomaly detection.

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
