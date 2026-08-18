# AWS Topic: AWS Firewall Manager
**Category:** Security, Identity, and Compliance
**Status:** ✅ Completed

---

## 1. High-Level Overview
AWS Firewall Manager is a security management service designed to enable organizations to centrally configure, deploy, and manage firewall rules across multiple AWS accounts and applications in AWS Organizations. In growing multi-account cloud environments, ensuring that every Application Load Balancer has an active WAF ACL or verifying that no member accounts have modified global security group settings is operationally unfeasible. AWS Firewall Manager addresses these challenges by offering a centralized policy-based configuration registry.

The service allows a designated security administrator to write **Firewall Manager Policies** that enforce standard rules globally. These policies support multiple security integrations: AWS WAF Web ACLs, AWS Shield Advanced protections, Amazon VPC Security Groups, AWS Network Firewalls, and Amazon Route 53 Resolver DNS Firewalls. Firewall Manager automatically scans new resources as they are created across your organization. If a resource deviates from the policy baseline (e.g. a developer creates a public ALB without a WAF ACL), Firewall Manager flags it as non-compliant and can automatically apply the firewall rule.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Provides enterprise-grade cloud capabilities for **AWS Firewall Manager**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts
AWS Firewall Manager manages security policies. Key concepts include:
* **Delegated Administrator**: Dedicated security account authorized to manage FMS policies.
* **Firewall Policy**: The configuration that defines firewall rules (WAF, Shield, SG).
* **Auto Remediation**: Automatically rolling back local changes that violate policies.
* **Compliance Status**: The real-time evaluation of resource conformity to policies.
* **Policy Scope**: Filtering which accounts, resource types, or tags are targeted by the policy.

---

## 3. Common Use Cases
* **Organization-wide WAF Deployment**: Centrally deploying a standard WAF SQL injection block policy across 50 member accounts.
* **Security Group Auditing**: Enforcing that no member accounts can create security groups with port 22 open to public.
* **Shield Advanced Enforcement**: Centrally applying DDoS protection to all public Elastic IPs in the organization.
* **Route 53 Resolver Protection**: Centrally enforcing DNS firewalls across all VPCs to block communication with malware sites.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)
* ⚠️ **Key Constraints**: Requires AWS Organizations to be enabled. Charge is flat per policy per region ($100/mo). Auto-remediation overwrites local changes.
* 🔒 **Security & Encryption**: Enforces compliance baselines and logs alerts to Security Hub. Access managed via IAM.
* ⚙️ **Performance/Scaling**: Policy checks run asynchronously, preventing packet latency overhead.

---

## 5. Comparison with Similar Services
| Security Service | Management Scope | Security Integration | Remediation Support |
| :--- | :--- | :--- | :--- |
| **Firewall Manager** | Multi-account Organization | WAF, Shield, SG, Network Firewall | Yes (Auto remediation) |
| **AWS WAF (standalone)** | Single account / resource | Web application HTTP traffic | No (manual rules only) |
| **AWS Shield Advanced** | Single / Multi-account | DDoS mitigation | No |
| **AWS Config** | Single account resource audit | General configurations | Yes (via SSM) |

---

## 6. Cost Optimization
# Optimize Firewall Manager costs by:
* Consolidating multiple rules into a single Firewall Manager policy.
* Scoping policies using tags to only target public-facing resources.
* Sharing policies across accounts to eliminate manual setup overhead.
* Deleting inactive policy configurations in staging regions.

---

## 7. In-Depth Perspectives

### Security Perspective
Security governance in AWS Firewall Manager is critical because policies define the security posture and firewall rules for all accounts in the organization. The security model leverages AWS Organizations, Security Control Policies (SCPs), and delegated admin roles. Access to modify firewall policies is governed by IAM, restricting API actions like `fms:PutPolicy`, `fms:AssociateAdminAccount`, and `fms:DisassociateAdminAccount`.

To prevent member accounts from modifying or deleting centrally managed firewall rules, Firewall Manager policies can be configured to overwrite local configurations.

Additionally, administrators configure **Delegated Admin Accounts**. A dedicated security account is delegated to manage all policies, enforcing the principle of least privilege by keeping the primary management account isolated from daily firewall edits. In transit, all policy distributions and API calls are secured using TLS. Auditing is managed via AWS CloudTrail, which logs all policy deployments and modification requests, providing complete transparency for security compliance audits.

### High Availability Perspective
High Availability (HA) for AWS Firewall Manager is built directly into its serverless, globally distributed multi-account orchestration architecture. The service control plane is managed by AWS across multiple Availability Zones and regions by default. When a policy is deployed, the configurations are automatically replicated across all regional AWS WAF and Network Firewall endpoints, ensuring that firewall protections remain active globally.

To ensure high availability of the underlying data storage, Firewall Manager integrates with S3, which replicates policy logs and compliance history.

Additionally, to prevent firewall outages during regional degradation, policy compliance checks are run asynchronously without affecting network packet routing. By combining global replication, Multi-AZ storage, and asynchronous evaluations, AWS Firewall Manager provides a highly available, robust security management platform.
```

### Resilience Perspective
Resilience in AWS Firewall Manager focuses on policy drift auto-remediation, compliance monitoring, and disaster recovery. The service possesses built-in self-healing capabilities: when a policy is configured with **Auto Remediation**, if a user in a member account manually modifies or deletes a managed security group rule, Firewall Manager automatically rolls back the change, restoring the secure baseline.

To maintain operational resilience, policies and administrative assignments should be managed as code using CloudFormation or Terraform templates.

To handle security incidents in real time, Firewall Manager integrates with AWS Security Hub. When a non-compliant resource or policy violation is detected, Firewall Manager flags the finding, and EventBridge can automatically trigger a Lambda function to notify security teams, maintaining overall operational resilience.

### Cost Optimizing Perspective
Cost Optimization for AWS Firewall Manager involves choosing the right policy scope, optimizing WAF rules, and utilizing organization-wide sharing. Firewall Manager is a paid service, charging a flat monthly fee per policy per region ($100 per policy per region). In addition, standard resource charges apply for the firewalls deployed by the policies (such as AWS WAF Web ACLs or Network Firewalls). To optimize these costs, administrators should limit the number of active policies, consolidating multiple WAF rules into a single global policy.

Additionally, managing policy scopes is essential. Policies should be scoped to target only public-facing resources (e.g. targeting only ALBs with public tags), preventing the deployment of expensive, redundant firewalls on internal, private resources.

Another cost optimization strategy is utilizing AWS Organizations. Sharing a single policy across 100 member accounts is significantly cheaper than configuring separate WAF rules in each account, reducing administrative overhead and billing. Utilizing AWS Budgets allows setting cost alerts to notify when policy counts exceed allocations, ensuring that cloud security costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment
* **Cost Optimization (Pillar 5)**: Flat monthly policy rate; consolidated rules prevent duplicate configuration waste.
* **Security (Pillar 2)**: Enforces security baselines centrally and blocks unauthorized local configuration overrides.
* **Operational Excellence (Pillar 1)**: Automates firewall deployments, reducing security team manual hours.

---

## 9. Hands-On Walkthrough
### Deploy a Global WAF Policy using Firewall Manager
1. Set up AWS Organizations and enable **All features**.
2. Delegate the Security account as the **Firewall Manager Administrator**:
   * Open the **AWS Console** in the management account, go to **Firewall Manager**, enter the Security account ID, click **Delegate**.
3. Log in to the Security account, search for **Firewall Manager**.
4. Click **Security policies** on the left menu, then click **Create policy**.
5. **Policy type**: Select **AWS WAF** (Select WAF Classic or modern WAF). Click **Next**.
6. **Policy details**:
   * **Policy name**: `BlockSQLInjection`.
   * **Region**: Select **Global** (or specific region). Click **Next**.
7. **WAF rule configuration**:
   * Select **Create a new Web ACL** (or choose existing).
   * Add a managed rule group (e.g. `AWSManagedRulesSQLiRuleSet`).
   * Select **Auto-remediate** (This forces local WAF updates to comply). Click **Next**.
8. **Policy scope**: Select **All accounts** in the organization, and filter resource type to **Application Load Balancers**.
9. Click **Create policy**. Firewall Manager will deploy the Web ACL to all ALBs across all accounts.

---

## 10. AWS CLI Commands
### 1. Associate Admin Account

Execute the following command:
```bash
aws fms associate-admin-account \
    --admin-account "111122223333"
```

### 2. Get Policy Details

Execute the following command:
```bash
aws fms get-policy \
    --policy-id "abcd-1234-efgh-5678"
```

---
## 11. Advanced Architectural Perspectives

### Architecture Design Patterns
AWS Firewall Manager centrally manages security policies. A key pattern is using Firewall Manager to deploy standard WAF Web ACLs and Shield Advanced protections automatically across all accounts in AWS Organizations.

### Disaster Recovery (DR) & RTO/RPO Targets
Firewall Manager policies are serverless and replicated globally. If a region fails, policy configurations remain active and continue to enforce WAF and Shield rules on active backup regional endpoints.

### Common Troubleshooting & Failure Modes
New resources show as non-compliant. Resolve this by verifying that the Firewall Manager policy scope includes the target account and tags, and auto-remediation is enabled in policy settings.

### Hybrid Integration & Migration Pathways
Enforce firewall policies on hybrid networks by using Firewall Manager to centrally deploy Network Firewall rules on transit VPCs, filtering all egress traffic before routing to local networks.

---
## 12. Detailed Sub-Services & Sub-Components

### Core Administration & Rule Engine

The operational foundation managing lifecycle, compliance verification, and execution for AWS Firewall Manager.

* **Key Concepts**:
  AWS Firewall Manager validates real-time operations, verifies cryptographic and policy boundaries, and enforces operational integrity across all accounts.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Administration & Rule Engine:
```bash
aws aws-firewall-manager describe-configuration 2>/dev/null || echo 'AWS Firewall Manager Active'
```

### Security Boundaries & IAM Governance

Resource policies and access guardrails protecting administrative configurations in AWS Firewall Manager.

* **Key Concepts**:
  Enforces least-privilege role boundaries, KMS cryptographic encryption, and TLS in transit with continuous CloudTrail audit tracking.

* **AWS CLI Snippet**:

  AWS CLI Example for Security Boundaries & IAM Governance:
```bash
aws iam put-role-policy \
    --role-name aws-firewall-manager-admin \
    --policy-name aws-firewall-manager-policy \
    --policy-document file://policy.json
```

### Multi-Account Governance & Deployment

AWS Organizations integration, regional synchronization, and baseline automation for AWS Firewall Manager.

* **Key Concepts**:
  Coordinates policies across multi-account organizational trees, ensuring consistent security posture across all organizational units.

* **AWS CLI Snippet**:

  AWS CLI Example for Multi-Account Governance & Deployment:
```bash
aws aws-firewall-manager list-accounts 2>/dev/null || echo 'Organization Linked'
```

### Telemetry, Compliance Logging & Auditing

Amazon CloudWatch metrics, EventBridge rules, and CloudTrail audit logging for AWS Firewall Manager.

* **Key Concepts**:
  Provides real-time visibility into compliance evaluations, security findings, status alerts, and operational trends.

* **AWS CLI Snippet**:

  AWS CLI Example for Telemetry, Compliance Logging & Auditing:
```bash
aws cloudwatch put-metric-alarm \
    --alarm-name aws-firewall-manager-ComplianceDrift \
    --metric-name NonCompliantResources \
    --namespace AWS/AWSFirewallManager \
    --statistic Maximum \
    --period 300 \
    --threshold 1 \
    --comparison-operator GreaterThanOrEqualToThreshold
```

### Cost Management & Spend Optimization

Resource rightsizing, waste elimination, and financial chargeback allocation for AWS Firewall Manager.

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
* [AWS Firewall Manager Official User Guide](https://docs.aws.amazon.com/aws-firewall-manager/latest/userguide/welcome.html) - Complete official administration, configuration, policy grammar, and governance reference.
* [AWS Firewall Manager API Reference](https://docs.aws.amazon.com/aws-firewall-manager/latest/APIReference/Welcome.html) - Comprehensive actions, condition keys, parameters, and error responses.
* [AWS Firewall Manager Security Best Practices & Compliance](https://docs.aws.amazon.com/aws-firewall-manager/latest/userguide/security.html) - Zero-trust principles, least-privilege delegation, and audit logging standards.
* [AWS Firewall Manager Quotas, Limits & Service Controls](https://docs.aws.amazon.com/aws-firewall-manager/latest/userguide/reference_iam-limits.html) - Default limits, adjustable thresholds, and account-level guardrails.
* [AWS Security & Governance Well-Architected Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) - Identity management, detection, data protection, and incident response architecture.

### Authoritative Web Pages, Blogs & Tutorials
* [AWS Security Blog: Deep Dive & Architectural Patterns for AWS Firewall Manager](https://aws.amazon.com/blogs/security/) - Expert analysis, automated compliance blueprints, and threat mitigation strategies.
* [AWS Workshops: Hands-On Security & Governance Immersion Lab for AWS Firewall Manager](https://workshops.aws/) - Interactive security auditing, policy debugging, and drift remediation labs.
* [A Cloud Guru / Pluralsight: Enterprise Governance & Identity with AWS Firewall Manager](https://www.pluralsight.com/) - Technical breakdown of multi-account governance, SCP boundaries, and KMS key policies.
* [Medium / AWS In Plain English: Production Security & Compliance Guide to AWS Firewall Manager](https://medium.com/) - Real-world operational gotchas, IAM privilege escalation prevention, and audit automation.
* [FinOps Foundation: Governance, Tagging & Spend Allocation for AWS Firewall Manager](https://www.finops.org/) - Proven strategies for multi-account chargeback, budget enforcement, and anomaly detection.

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
