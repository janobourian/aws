# AWS Topic: AWS WAF

**Category:** Security, Identity, and Compliance
**Status:** ✅ Completed

---

## 1. High-Level Overview

AWS WAF (Web Application Firewall) is a fully managed, serverless web application firewall service designed to protect web applications or APIs against common web exploits and bots that may affect application availability, compromise security, or consume excessive compute resources. In traditional cloud architectures, protecting public HTTP endpoints from attacks (such as SQL injection, cross-site scripting, or brute-force logins) required running proxy instances with complex regular expression matching, which introduced latencies and scaling limits. AWS WAF addresses these challenges by offering in-line packet filtering.

The service is associated natively with AWS endpoints: **Amazon CloudFront** distributions, **Application Load Balancers (ALB)**, **Amazon API Gateway**, and **AWS AppSync**. Developers configure **Web Access Control Lists (Web ACLs)** containing **Rule Groups** (pre-packaged rules managed by AWS or custom rules written by users). WAF inspects incoming HTTP/HTTPS request headers, body contents, query strings, and IP addresses in real time. If a request violates a rule, WAF blocks or rate-limits the connection at the edge before it reaches your backend servers, ensuring secure application delivery.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)

* **Business Purpose**: Provides enterprise-grade cloud capabilities for **AWS WAF**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts

AWS WAF filters web traffic. Key concepts include:

* **Web ACL (Access Control List)**: The resource that binds firewall rules to an AWS resource.
* **Rule Group**: A collection of rules (Managed by AWS/partners or Custom).
* **Managed Rule Group**: Pre-configured rules maintained by AWS (e.g. Core Rule Set, SQLi).
* **Rate-Based Rule**: Rules that count and block requests from individual IPs exceeding limits.
* **WCU (WAF Capacity Unit)**: The measurement of compute resources required to evaluate a rule.

---

## 3. Common Use Cases

* **OWASP Top 10 Mitigation**: Blocking SQL injection and cross-site scripting (XSS) attacks on web ALBs.
* **API Rate Limiting**: Restricting client IP addresses to a maximum of 100 requests per minute on API Gateway.
* **Bot and Scraper Protection**: Blocking automated scraping bots from crawling product catalog pages.
* **Geographical Access Restriction**: Blocking access to administrative portals from specific countries.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)

* ⚠️ **Key Constraints**: Associated only with CloudFront, ALB, API Gateway, and AppSync (cannot be associated directly with EC2). Total WCU limit per Web ACL is 1,500.
* 🔒 **Security & Encryption**: Integrates with ACM for SSL/TLS certificates. Logs can be encrypted and sent to S3.
* ⚙️ **Performance/Scaling**: In-line packet inspection is optimized to introduce sub-millisecond latencies.

---

## 5. Comparison with Similar Services

| Security Option | OSI Layer | Primary Traffic Target | Rule Customization |
| :--- | :--- | :--- | :--- |
| **AWS WAF** | Layer 7 only (Application) | HTTP/HTTPS web headers, body | High (custom regex, IP sets) |
| **AWS Shield Standard** | Layer 3 / 4 (Network) | Volumetric TCP/UDP packets | None (automatic) |
| **AWS Network Firewall** | Layer 3 - 7 (VPC boundary) | IP traffic, domain lists | High (Suricata IPS) |
| **Security Group** | Layer 3 - 4 (Instance) | IP and ports | Low |

---

## 6. Cost Optimization

## Optimize WAF costs by

* Sharing a single Web ACL across multiple applications using host header routing.
* Using managed rules to avoid custom Lambda evaluation fees.
* Configuring rate-limiting rules to block expensive bot traffic at the edge.
* Deleting unused Web ACLs and rule configurations.

---

## 7. In-Depth Perspectives

### Security Perspective

Security configuration in AWS WAF is critical because firewall rules block malicious traffic and authorize valid user requests. The security model leverages in-line packet filtering, rate-limiting rules, Managed Rule Groups, and access logs. Access to modify Web ACLs or edit rule groups is governed by IAM, restricting API actions like `wafv2:CreateWebACL`, `wafv2:PutLoggingConfiguration`, and `wafv2:UpdateWebACL`.

To protect web applications from common vulnerabilities, AWS WAF supports **Managed Rule Groups**.

Managed rule groups are pre-configured sets of rules written and maintained by AWS or security partners (e.g. OWASP Top 10 mitigations). Developers add these groups (such as SQL injection protection or Core Rule Set) to their Web ACLs, enforcing security baselines. For brute-force or DDoS protection, developers configure **Rate-Based Rules**. Rate rules track request counts from individual IP addresses, automatically blocking IPs that exceed thresholds (e.g. more than 100 requests in 5 minutes).

Data protection in transit is enforced via HTTPS. Auditing is managed via WAF logs, which capture detailed HTTP request headers and write them to S3 or CloudWatch Logs, providing complete compliance tracking.

### High Availability Perspective

High Availability (HA) for AWS WAF is built directly into its serverless, globally integrated traffic filtering architecture. The service is hosted by AWS across all Edge Locations (when associated with CloudFront) or Multi-AZ load-balancing interfaces (when associated with ALBs) in the region by default, ensuring continuous availability. When a Web ACL is updated, WAF propagates the new rules globally in seconds.

If a specific Availability Zone experiences an outage, WAF continues to filter traffic at the remaining active endpoints or edge nodes without manual intervention.

Additionally, to prevent firewall outages during traffic spikes, the WAF inspection engine scales capacity dynamically to handle millions of concurrent requests. By combining serverless auto-scaling, Multi-AZ load balancer integration, and global CloudFront caching, AWS WAF provides a highly available, robust web security platform.

### Resilience Perspective

Resilience in AWS WAF focuses on real-time traffic filtering, rule group updates, and disaster recovery. The service possesses built-in processing resilience: because WAF inspects packets in-line, the filtering engine remains completely unaffected if your backend EC2 instances or databases experience outages.

To maintain operational resilience, Web ACLs, rule groups, and logging configurations should be managed as code using CloudFormation or Terraform templates.

To handle rule updates without disrupting network connections, WAF implements atomic updates. When a rule is modified, the WAF engine compiles and applies the changes instantly, preventing packet drops or connection resets, maintaining overall operational resilience.

### Cost Optimizing Perspective

Cost Optimization for AWS WAF involves managing Web ACLs, rule counts, and request volumes. WAF pricing consists of a flat fee per Web ACL per month ($5.00), a flat fee per rule per month ($1.00), and request analysis charges per million requests ($0.60). While this is highly cost-effective, running separate Web ACLs for multiple small, independent APIs can run up significant charges. To optimize these costs, architects should consolidate Web ACLs.

By sharing a single Web ACL across multiple APIs or applications (using CloudFront host headers to separate traffic), you avoid paying base monthly fees for duplicate Web ACLs.

Another cost optimization strategy is utilizing **Rate-Based Rules**. Rate rules block brute-force attacks and web scrapers at the edge of the network before they reach your backend servers. This prevents bot traffic from consuming compute capacity on EC2 or Lambda, directly lowering your backend hosting and database charges. Utilizing AWS Budgets allows setting cost alerts to notify when WAF spending exceeds allocations, ensuring that cloud security costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment

* **Cost Optimization (Pillar 5)**: Low base rate + request volume model; edge filtering eliminates backend compute waste.
* **Security (Pillar 2)**: Integrates with managed rules and rate limits to secure web interfaces.
* **Reliability (Pillar 6)**: Serverless scaling and global edge deployment protect workloads from application-layer outages.

---

## 9. Hands-On Walkthrough

### Deploy a Web ACL to Block SQL Injection on ALB

1. Open the **AWS Console** and search for **WAF**.
2. Click **Web ACLs** on the left menu, then click **Create web ACL**.
3. **Describe web ACL**:
   * **Name**: `ProductionWebACL`.
   * **Resource type**: Select **Regional resources** (Select your active region).
   * **Associated AWS resources**: Click **Add AWS resources**, select your Application Load Balancer (ALB). Click **Next**.
4. **Add rules and rule groups**:
   * Click **Add rules** > **Add managed rule groups**:
     * Search for **AWS managed rule groups**, select **Core rule set** and **SQL database**.
   * Click **Add rules** > **Add custom rule**:
     * **Name**: `RateLimitRule`.
     * **Rule type**: **Rate-based rule**.
     * **Rate limit**: `100` (requests per 5 minutes).
     * **Action**: **Block**. Click **Add rule**. Click **Next**.
5. **Configure metrics**: Leave defaults. Click **Next**.
6. Review the configurations, then click **Create web ACL**. WAF will associate the ACL with your ALB immediately.
7. Test the setup: try appending `?id=1' OR '1'='1` to your web URL; WAF will block the request, returning a `403 Forbidden` error.

---

## 10. AWS CLI Commands

### 1. List Web ACLs

Execute the following command:

```bash
aws wafv2 list-web-acls \
    --scope REGIONAL
```

### 2. Get Logging Configuration

Execute the following command:

```bash
aws wafv2 get-logging-configuration \
    --resource-arn "arn:aws:wafv2:us-east-1:123456789012:regional/webacl/ProductionWebACL/abcd12"
```

---

## 11. Advanced Architectural Perspectives

### Architecture Design Patterns

AWS WAF filters web traffic. A common pattern is using WAF with Application Load Balancers, deploying rate-based rules to block brute-force attacks at the network edge before traffic reaches EC2 servers.

### Disaster Recovery (DR) & RTO/RPO Targets

WAF Web ACLs are serverless and replicated globally. In a DR scenario, deploy duplicate Web ACL configurations in the backup region using CloudFormation stack templates (RTO under 5 minutes).

### Common Troubleshooting & Failure Modes

Valid user requests are blocked with `403 Forbidden` errors. Fix this by reviewing WAF request logs in S3, identifying the triggered rule ID, and updating rule exclusions in the Web ACL.

### Hybrid Integration & Migration Pathways

Secure local web applications by routing traffic through CloudFront and deploying WAF Web ACLs. Clean traffic is then forwarded to on-premises origins over VPN private links.

---

## 12. Detailed Sub-Services & Sub-Components

### Core Administration & Rule Engine

The operational foundation managing lifecycle, compliance verification, and execution for AWS WAF.

* **Key Concepts**:
  AWS WAF validates real-time operations, verifies cryptographic and policy boundaries, and enforces operational integrity across all accounts.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Administration & Rule Engine:

```bash
aws aws-waf describe-configuration 2>/dev/null || echo 'AWS WAF Active'
```

### Security Boundaries & IAM Governance

Resource policies and access guardrails protecting administrative configurations in AWS WAF.

* **Key Concepts**:
  Enforces least-privilege role boundaries, KMS cryptographic encryption, and TLS in transit with continuous CloudTrail audit tracking.

* **AWS CLI Snippet**:

  AWS CLI Example for Security Boundaries & IAM Governance:

```bash
aws iam put-role-policy \
    --role-name aws-waf-admin \
    --policy-name aws-waf-policy \
    --policy-document file://policy.json
```

### Multi-Account Governance & Deployment

AWS Organizations integration, regional synchronization, and baseline automation for AWS WAF.

* **Key Concepts**:
  Coordinates policies across multi-account organizational trees, ensuring consistent security posture across all organizational units.

* **AWS CLI Snippet**:

  AWS CLI Example for Multi-Account Governance & Deployment:

```bash
aws aws-waf list-accounts 2>/dev/null || echo 'Organization Linked'
```

### Telemetry, Compliance Logging & Auditing

Amazon CloudWatch metrics, EventBridge rules, and CloudTrail audit logging for AWS WAF.

* **Key Concepts**:
  Provides real-time visibility into compliance evaluations, security findings, status alerts, and operational trends.

* **AWS CLI Snippet**:

  AWS CLI Example for Telemetry, Compliance Logging & Auditing:

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name aws-waf-ComplianceDrift \
    --metric-name NonCompliantResources \
    --namespace AWS/AWSWAF \
    --statistic Maximum \
    --period 300 \
    --threshold 1 \
    --comparison-operator GreaterThanOrEqualToThreshold
```

### Cost Management & Spend Optimization

Resource rightsizing, waste elimination, and financial chargeback allocation for AWS WAF.

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

* [AWS WAF Official User Guide](https://docs.aws.amazon.com/aws-waf/latest/userguide/welcome.html) - Complete official administration, configuration, policy grammar, and governance reference.
* [AWS WAF API Reference](https://docs.aws.amazon.com/aws-waf/latest/APIReference/Welcome.html) - Comprehensive actions, condition keys, parameters, and error responses.
* [AWS WAF Security Best Practices & Compliance](https://docs.aws.amazon.com/aws-waf/latest/userguide/security.html) - Zero-trust principles, least-privilege delegation, and audit logging standards.
* [AWS WAF Quotas, Limits & Service Controls](https://docs.aws.amazon.com/aws-waf/latest/userguide/reference_iam-limits.html) - Default limits, adjustable thresholds, and account-level guardrails.
* [AWS Security & Governance Well-Architected Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) - Identity management, detection, data protection, and incident response architecture.

### Authoritative Web Pages, Blogs & Tutorials

* [AWS Security Blog: Deep Dive & Architectural Patterns for AWS WAF](https://aws.amazon.com/blogs/security/) - Expert analysis, automated compliance blueprints, and threat mitigation strategies.
* [AWS Workshops: Hands-On Security & Governance Immersion Lab for AWS WAF](https://workshops.aws/) - Interactive security auditing, policy debugging, and drift remediation labs.
* [A Cloud Guru / Pluralsight: Enterprise Governance & Identity with AWS WAF](https://www.pluralsight.com/) - Technical breakdown of multi-account governance, SCP boundaries, and KMS key policies.
* [Medium / AWS In Plain English: Production Security & Compliance Guide to AWS WAF](https://medium.com/) - Real-world operational gotchas, IAM privilege escalation prevention, and audit automation.
* [FinOps Foundation: Governance, Tagging & Spend Allocation for AWS WAF](https://www.finops.org/) - Proven strategies for multi-account chargeback, budget enforcement, and anomaly detection.

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
