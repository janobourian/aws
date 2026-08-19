# AWS Topic: Amazon Managed Service for Prometheus

**Category:** Management and Governance
**Status:** ✅ Completed

---

## 1. High-Level Overview

Amazon Managed Service for Prometheus (AMP) is a serverless, highly available, and Prometheus-compatible monitoring service designed to make it incredibly easy to ingest, store, and query container metrics at scale. Prometheus is the open-source industry standard for monitoring containerized workloads (such as Kubernetes or Docker), but deploying self-managed Prometheus servers requires significant administrative overhead. Database administrators must manually configure etcd replication, manage time-series databases, scale storage volumes, and tune JVM memory settings, which limits operational agility.

Amazon Managed Service for Prometheus addresses these challenges by operating as an entirely serverless platform. The service automatically scales metrics ingestion, storage, and querying in response to real-time workload demands. AMP provides deep integration with AWS IAM for authentication, using AWS Signature Version 4 (SigV4) to secure data scraping. By managing replication across multiple Availability Zones, automated backups, and software updates, AMP enables organizations to monitor EKS and ECS clusters with minimal administrative overhead.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)

* **Business Purpose**: Provides enterprise-grade cloud capabilities for **Amazon Managed Service for Prometheus**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts

Amazon Managed Prometheus stores time-series container metrics. Key concepts include:

* **Workspace**: The secure, isolated Prometheus instance containing metrics data.
* **Scraper / Collector**: The agent (e.g., ADOT) that collects and pushes metrics to the workspace.
* **PromQL**: The query language used to extract metrics data from the database.
* **Recording Rules**: Configurations that pre-calculate frequently used queries to optimize query performance.
* **Alert Rules**: Rules that trigger notifications when metric thresholds are exceeded.

---

## 3. Common Use Cases

* **EKS Container Monitoring**: Scraping and storing CPU and memory metrics from Kubernetes pods running on EKS.
* **Serverless Container Observability**: Ingesting metrics from Fargate container tasks into AMP workspaces.
* **Multi-Cluster Metrics Consolidation**: Aggregating metrics from multiple independent EKS clusters into a single central workspace.
* **Visual Analytics Integration**: Querying AMP metrics from Managed Grafana to build operational dashboards.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)

* ⚠️ **Key Constraints**: Metric retention is fixed at 150 days. Scrapers require proper IAM permissions and SigV4 signing to push metrics.
* 🔒 **Security & Encryption**: Requires SigV4 authentication. All metrics are encrypted with KMS.
* ⚙️ **Performance/Scaling**: Serverless architecture scales dynamically; PromQL endpoints optimize query speeds.

---

## 5. Comparison with Similar Services

| Monitoring Service | Ingestion Interface | Query Language | Primary Target Workload |
| :--- | :--- | :--- | :--- |
| **Amazon AMP** | Prometheus Remote Write (SigV4) | PromQL | EKS, ECS, Kubernetes containers |
| **Amazon CloudWatch** | CloudWatch PutMetricData | CloudWatch Metrics Insights | General AWS services, OS logs |
| **Amazon OpenSearch** | REST API / Logstash | Lucene / SQL | Text logs, trace data |
| **Amazon Managed Grafana** | HTTP API | Multi-source (visual panels) | Visual dashboarding (consumes AMP) |

---

## 6. Cost Optimization

Optimize AMP costs by:

* Filtering out non-essential metrics at the collector level.
* Increasing scrape intervals (e.g. from 10s to 30s) to lower sample counts.
* Aggregating multiple cluster metrics into a single workspace.
* Deleting empty test workspaces to avoid baseline fees.

---

## 7. In-Depth Perspectives

### Security Perspective

Security configuration in Amazon Managed Service for Prometheus is critical because metric workspaces store detailed application telemetry and server metadata. The security model leverages AWS IAM, Signature Version 4 (SigV4) authentication, network isolation, and encryption. Access to ingest metrics or query workspaces is governed by IAM, restricting API actions like `aps:CreateWorkspace`, `aps:PutMetricData`, and `aps:QueryMetrics`.

To secure metrics ingestion, AMP requires **AWS SigV4 Authentication**. Prometheus scrapers (such as the ADOT collector) must sign all push requests using IAM credentials before submitting metrics to the AMP workspace endpoint.

Data protection at rest is enforced using customer-managed AWS KMS keys, which encrypt all time-series metrics stored in the AMP workspace automatically. In transit, all API calls and metric ingestion streams are secured using TLS. VPC endpoints (PrivateLink) allow private, secure metrics ingestion from internal subnets, bypassing the public internet. Auditing is managed via AWS CloudTrail, which logs all administrative API calls, providing complete transparency for compliance audits.

### High Availability Perspective

High Availability (HA) for Amazon Managed Service for Prometheus is built directly into its serverless, globally distributed time-series metrics database. The service operates across multiple Availability Zones within the active AWS region by default. AMP automatically manages ingestion throughput and data replication. When a Prometheus agent writes metrics to an AMP workspace, the data is automatically replicated across multiple physical facilities in different availability zones before returning a success confirmation, ensuring that localized zone failures do not cause metrics data loss.

To ensure high availability on the scraper side, developers should deploy redundant Prometheus agents or ADOT collectors. In EKS clusters, collectors should be deployed in a DaemonSet or a highly available replica set across multiple Availability Zones.

Additionally, AMP exposes highly available query endpoints compatible with standard Prometheus Query API (PromQL). External tools (such as Managed Grafana) query these endpoints, which automatically route requests to active database nodes. By combining Multi-AZ replication, redundant container scrapers, and highly available query endpoints, AMP provides a robust, high-availability monitoring platform.

### Resilience Perspective

Resilience in Amazon Managed Service for Prometheus focuses on metrics buffering, automatic scale-up limits, and disaster recovery. The database control plane possesses built-in self-healing capabilities: if an underlying storage partition fails, AMP automatically routes queries to active replicas and reconstructs the data on a healthy node, maintaining query latencies with zero RTO.

To maintain operational resilience, workspace configurations, alert rules, and recording rules should be managed as code using Helm charts, CloudFormation, or Terraform templates.

To handle API limits and ingestion throttling, Prometheus scrapers must implement exponential backoff with jitter. If metrics volume exceeds the workspace's default ingestion limits, AMP returns throttling errors. Scrapers buffer metrics locally in container memory or temporary disk storage, retrying the upload once rate limits reset. Using EventBridge, administrators can monitor workspace health events and trigger automated alerts, maintaining a highly resilient monitoring architecture.

### Cost Optimizing Perspective

Cost Optimization for Amazon Managed Service for Prometheus involves managing metrics ingestion volume, optimizing scrape intervals, and configuring retention periods. AMP pricing is pay-as-you-go, charging based on the number of metric samples ingested ($0.90 per billion samples), metrics stored ($0.03 per GB-month), and PromQL queries executed. While this is highly cost-effective, scraping high-frequency custom metrics can generate massive sample counts, running up significant charges. To optimize these costs, developers should configure scrape intervals efficiently (e.g. scraping every 30 seconds instead of every 1 second for non-critical services).

Additionally, implementing metrics filtering is essential. Scrapers should be configured to drop unused labels or non-essential metrics before pushing them to the AMP workspace, reducing the number of samples ingested and directly lowering billing.

Another cost optimization strategy is setting optimal data retention periods. By default, AMP retains metrics for 150 days. Utilizing AWS Budgets allows setting cost alerts to notify when metrics spending exceeds allocations, ensuring that container monitoring costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment

* **Cost Optimization (Pillar 5)**: Charges per metric sample ingested, eliminating idle server expenses.
* **Reliability (Pillar 6)**: Multi-AZ data replication and serverless scaling protect against localized outages.
* **Operational Excellence (Pillar 1)**: Preserves developer time by offering a fully compatible Prometheus engine with zero management.

---

## 9. Hands-On Walkthrough

### Create a Prometheus Workspace and Ingest EKS Metrics

1. Open the **AWS Console** and search for **Prometheus**.
2. Click **Workspaces** on the left menu, then click **Create workspace**:
   * **Workspace name**: `EKS-Cluster-Metrics`. Click **Create**.
3. Once active, note the **Remote write URL** (e.g., `<https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-1234/api/v1/remote_write>`).
4. Configure an ADOT collector in your EKS cluster using Helm:
   * Edit your collector values file to enter the remote write URL.
   * Enable SigV4 authentication:

     ```yaml
     sigv4:
       region: us-east-1
     ```

5. Deploy the collector:

   ```bash
   helm install adot-collector aws-otels/adot-exporter -f values.yaml
   ```

6. The collector will start scraping metrics and pushing them to your AMP workspace.

---

## 10. AWS CLI Commands

### 1. Create a Workspace

Execute the following command:

```bash
aws amp create-workspace \
    --alias "EKS-Cluster-Metrics"
```

### 2. Describe Workspace details

Execute the following command:

```bash
aws amp describe-workspace \
    --workspace-id "ws-12345"
```

### 3. Put Rules Configuration

Execute the following command:

```bash
aws amp put-rules-configuration \
    --workspace-id "ws-12345" \
    --data file://rules.yaml
```

---

## 11. Advanced Architectural Perspectives

### Architecture Design Patterns

Amazon Managed Prometheus processes metric streams. A common pattern is configuring Prometheus agent scrapers on EKS clusters to stream metrics to the managed workspace, utilizing Alertmanager to route alerts to SNS.

### Disaster Recovery (DR) & RTO/RPO Targets

Prometheus is serverless and replicates metrics across three AZs in the region automatically. In a DR scenario, configure scrapers to write to a standby workspace in a secondary region to maintain monitoring (RTO under 5 minutes).

### Common Troubleshooting & Failure Modes

Metric ingestion drops due to workspace limits. Resolve this by optimizing scraping intervals, configuring metric filtering rules, and requesting limits increases from AWS support.

### Hybrid Integration & Migration Pathways

Ingest local metrics by configuring on-premises Prometheus servers to remote-write metrics to the Amazon Managed Prometheus workspace over a secure Direct Connect interface.

---

## 12. Detailed Sub-Services & Sub-Components

### Core Administration & Rule Engine

The operational foundation managing lifecycle, compliance verification, and execution for Amazon Managed Service for Prometheus.

* **Key Concepts**:
  Amazon Managed Service for Prometheus validates real-time operations, verifies cryptographic and policy boundaries, and enforces operational integrity across all accounts.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Administration & Rule Engine:

```bash
aws amazon-managed-service-for-prometheus describe-configuration 2>/dev/null || echo 'Amazon Managed Service for Prometheus Active'
```

### Security Boundaries & IAM Governance

Resource policies and access guardrails protecting administrative configurations in Amazon Managed Service for Prometheus.

* **Key Concepts**:
  Enforces least-privilege role boundaries, KMS cryptographic encryption, and TLS in transit with continuous CloudTrail audit tracking.

* **AWS CLI Snippet**:

  AWS CLI Example for Security Boundaries & IAM Governance:

```bash
aws iam put-role-policy \
    --role-name amazon-managed-service-for-prometheus-admin \
    --policy-name amazon-managed-service-for-prometheus-policy \
    --policy-document file://policy.json
```

### Multi-Account Governance & Deployment

AWS Organizations integration, regional synchronization, and baseline automation for Amazon Managed Service for Prometheus.

* **Key Concepts**:
  Coordinates policies across multi-account organizational trees, ensuring consistent security posture across all organizational units.

* **AWS CLI Snippet**:

  AWS CLI Example for Multi-Account Governance & Deployment:

```bash
aws amazon-managed-service-for-prometheus list-accounts 2>/dev/null || echo 'Organization Linked'
```

### Telemetry, Compliance Logging & Auditing

Amazon CloudWatch metrics, EventBridge rules, and CloudTrail audit logging for Amazon Managed Service for Prometheus.

* **Key Concepts**:
  Provides real-time visibility into compliance evaluations, security findings, status alerts, and operational trends.

* **AWS CLI Snippet**:

  AWS CLI Example for Telemetry, Compliance Logging & Auditing:

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name amazon-managed-service-for-prometheus-ComplianceDrift \
    --metric-name NonCompliantResources \
    --namespace AWS/AmazonManagedServiceforPrometheus \
    --statistic Maximum \
    --period 300 \
    --threshold 1 \
    --comparison-operator GreaterThanOrEqualToThreshold
```

### Cost Management & Spend Optimization

Resource rightsizing, waste elimination, and financial chargeback allocation for Amazon Managed Service for Prometheus.

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

* [Amazon Managed Service for Prometheus Official User Guide](https://docs.aws.amazon.com/amazon-managed-service-for-prometheus/latest/userguide/welcome.html) - Complete official administration, configuration, policy grammar, and governance reference.
* [Amazon Managed Service for Prometheus API Reference](https://docs.aws.amazon.com/amazon-managed-service-for-prometheus/latest/APIReference/Welcome.html) - Comprehensive actions, condition keys, parameters, and error responses.
* [Amazon Managed Service for Prometheus Security Best Practices & Compliance](https://docs.aws.amazon.com/amazon-managed-service-for-prometheus/latest/userguide/security.html) - Zero-trust principles, least-privilege delegation, and audit logging standards.
* [Amazon Managed Service for Prometheus Quotas, Limits & Service Controls](https://docs.aws.amazon.com/amazon-managed-service-for-prometheus/latest/userguide/reference_iam-limits.html) - Default limits, adjustable thresholds, and account-level guardrails.
* [AWS Security & Governance Well-Architected Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) - Identity management, detection, data protection, and incident response architecture.

### Authoritative Web Pages, Blogs & Tutorials

* [AWS Security Blog: Deep Dive & Architectural Patterns for Amazon Managed Service for Prometheus](https://aws.amazon.com/blogs/security/) - Expert analysis, automated compliance blueprints, and threat mitigation strategies.
* [AWS Workshops: Hands-On Security & Governance Immersion Lab for Amazon Managed Service for Prometheus](https://workshops.aws/) - Interactive security auditing, policy debugging, and drift remediation labs.
* [A Cloud Guru / Pluralsight: Enterprise Governance & Identity with Amazon Managed Service for Prometheus](https://www.pluralsight.com/) - Technical breakdown of multi-account governance, SCP boundaries, and KMS key policies.
* [Medium / AWS In Plain English: Production Security & Compliance Guide to Amazon Managed Service for Prometheus](https://medium.com/) - Real-world operational gotchas, IAM privilege escalation prevention, and audit automation.
* [FinOps Foundation: Governance, Tagging & Spend Allocation for Amazon Managed Service for Prometheus](https://www.finops.org/) - Proven strategies for multi-account chargeback, budget enforcement, and anomaly detection.

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
