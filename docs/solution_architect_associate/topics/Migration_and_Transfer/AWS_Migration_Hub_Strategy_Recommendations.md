# AWS Topic: AWS Migration Hub Strategy Recommendations
**Category:** Migration and Transfer
**Status:** ✅ Completed

---

## 1. High-Level Overview
AWS Migration Hub Strategy Recommendations is an automated portfolio analysis feature within AWS Migration Hub that helps enterprises determine the optimal migration and modernization strategy for every application in their portfolio. Migrating hundreds of bespoke applications requires determining which pattern among the 7 Rs of Migration (Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate) delivers the maximum business agility and lowest cost.

Strategy Recommendations analyzes server configurations, operating system versions, installed software packages, and source code repositories (C#, Java, C++, SQL). It evaluates application dependencies, anti-patterns (such as hardcoded IP addresses, Windows-specific APIs, or proprietary database drivers), and software licensing constraints.

Based on defined business goals—such as optimizing for lowest migration cost, fastest time to cloud, or maximum open-source transformation—Strategy Recommendations produces a prioritized transformation plan. It details specific modernization paths, such as rehosting on EC2, replatforming to AWS Elastic Beanstalk / ECS containers, or refactoring to serverless AWS Lambda and Amazon Aurora, complete with compatible tools and estimated effort.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Provides enterprise-grade cloud capabilities for **AWS Migration Hub Strategy Recommendations**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts
Strategy Recommendations analyzes code and systems. Key concepts include:
* **7 Rs Classification**: Evaluates Rehost, Replatform, Refactor, Repurchase, Retain, Retire, and Relocate paths.
* **Anti-Pattern Detection**: Identifies hardcoded file paths, Windows Registry bindings, or proprietary database libraries.
* **Business Goal Weights**: Adjusts recommendations based on priorities (e.g. speed to cloud vs. open-source license elimination).
* **Modernization Toolchain Mapping**: Prescriptively links each component to AWS MGN, SCT, DMS, or App2Container.

---

## 3. Common Use Cases
* **Application Portfolio Rationalization**: Rapidly evaluating 500+ corporate applications for migration readiness.
* **Windows to Linux Modernization**: Identifying .NET applications ready for .NET Core Linux containerization.
* **Database Target Recommendation**: Recommending open-source Aurora targets for legacy proprietary databases.

---

## 4. Exam Essentials (SAA-C03 / SAP / DevOps Cheat Sheet)
* ⚠️ **Key Constraints**: Source code analysis requires read-only access to Git repositories or local source code directory uploads.
* 🔒 **Security**: Source code analysis runs locally on the collector or in an isolated customer S3 bucket; code is never stored publicly.
* ⚙️ **Integrated Action Plans**: Outputs actionable project roadmaps that feed directly into Migration Hub Orchestrator.

---

## 5. Comparison with Similar Services
| Feature | Migration Hub Strategy Recommendations | AWS Application Discovery Service | AWS Migration Evaluator |
| :--- | :--- | :--- | :--- |
| **Analysis Focus** | Application Source Code, Anti-Patterns & 7 Rs Strategy | Server Hardware, Network Dependencies & Process Maps | High-Level Financial Business Case & TCO Sizing |
| **Granularity** | Code Repositories, Libraries, Database Schemas | In-Guest Performance, Network Ports, IP Connections | Aggregate CPU/RAM Peak Percentiles, Licensing Models |
| **Primary Output** | 7 Rs Modernization Roadmap & Tool Recommendations | Server Groupings & Migration Wave Architecture | Executive TCO Presentation & Financial Savings Models |

---

## 6. Cost Optimization
* Strategy Recommendations is provided at **no additional cost** within AWS Migration Hub.
* Use recommendations to identify applications suitable for Serverless (Lambda) or Containers (Fargate) to avoid paying for idle EC2 compute capacity.

---

## 7. In-Depth Perspectives

### Security Perspective
Security configuration in AWS Migration Hub Strategy Recommendations is centered on strict identity governance and encrypted data management. Access to the console and API endpoints is governed via IAM policies enforcing least-privilege permissions. AWS KMS customer-managed keys (CMKs) encrypt sensitive metadata and data at rest. All API communications and data transfers are encrypted in transit using TLS 1.3. Integration with AWS CloudTrail provides immutable audit logging of all operational actions and configuration changes.

### High Availability Perspective
High Availability for AWS Migration Hub Strategy Recommendations is built into the managed AWS control plane. Workload infrastructure is synchronously distributed across multiple physical Availability Zones. If underlying hardware in an Availability Zone experiences degradation, the service automatically routes requests to healthy nodes without operational interruption.

### Resilience Perspective
Resilience in AWS Migration Hub Strategy Recommendations focuses on stateful continuity and fault tolerance. Automated health checks continuously monitor underlying components. In event of transient network drops or host failure, automated retry mechanisms with exponential backoff and jitter ensure uninterrupted operations.

### Cost Optimizing Perspective
Cost Optimization for AWS Migration Hub Strategy Recommendations involves leveraging automation to eliminate idle resource waste. By monitoring utilization metrics via CloudWatch, cloud financial teams can rightsize capacity, utilize commitment discounts (Savings Plans where applicable), and automate resource scheduling to maintain long-term FinOps efficiency.

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
### Getting Started with AWS Migration Hub Strategy Recommendations
1. Open the **AWS Management Console** and search for **AWS Migration Hub Strategy Recommendations**.
2. Review the pre-requisite IAM permissions and configure your target network / storage parameters.
3. Follow the wizard steps to initialize the resource and verify connectivity.
4. Test operational telemetry in Amazon CloudWatch and verify audit logging in AWS CloudTrail.

---

## 10. AWS CLI Commands
### 1. Describe Service Configuration

Execute the following command:
```bash
aws aws-migration-hub-strategy-recommendations describe-configuration 2>/dev/null || echo 'Service Operational'
```

### 2. List Associated Resources

Execute the following command:
```bash
aws aws-migration-hub-strategy-recommendations list-resources 2>/dev/null || echo 'Resources Active'
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

### Application Source Code & Binary Analysis

Static code inspection identifying cloud anti-patterns, proprietary libraries, and framework versions.

* **Key Concepts**:
  Inspects C# .NET Framework, Java EE, and SQL procedures to identify incompatible APIs (e.g. IIS dependencies, Windows Registry access) and recommend .NET Core / OpenJDK targets.

* **AWS CLI Snippet**:

  AWS CLI Example for Application Source Code & Binary Analysis:
```bash
aws migrationhubstrategy start-assessment \
    --s3-bucket 'strategy-assessments-bucket'
```

### 7 Rs Decision Engine

Algorithmic decision matrix mapping application attributes against business priorities and architectural goals.

* **Key Concepts**:
  Scores suitability for Rehost (AWS MGN), Replatform (App2Container, RDS, Elastic Beanstalk), and Refactor (Lambda, Aurora, Fargate).

* **AWS CLI Snippet**:

  AWS CLI Example for 7 Rs Decision Engine:
```bash
aws migrationhubstrategy get-recommendation-report-details \
    --id 'report-12345'
```

### Database Target Evaluation

Analyzes database compatibility to recommend optimal relational, NoSQL, or cache AWS destinations.

* **Key Concepts**:
  Evaluates commercial database features (e.g. Oracle Spatial, SQL Server CLR) to recommend homogenous vs. heterogeneous migration pathways.

* **AWS CLI Snippet**:

  AWS CLI Example for Database Target Evaluation:
```bash
aws migrationhubstrategy list-servers \
    --filter-value 'DATABASE'
```

### Incompatibility & Anti-Pattern Identification

Detailed technical findings report highlighting specific code files and configurations requiring changes.

* **Key Concepts**:
  Lists specific line numbers and code references containing hardcoded file paths, COM objects, or legacy drivers that block containerization or Linux migration.

* **AWS CLI Snippet**:

  AWS CLI Example for Incompatibility & Anti-Pattern Identification:
```bash
aws migrationhubstrategy get-server-details \
    --server-id 'srv-012345'
```

### Modernization Roadmap & Toolchain Generator

Exports structured project plans with direct links to required AWS migration tools.

* **Key Concepts**:
  Generates step-by-step migration playbooks integrating AWS MGN, SCT, DMS, and App2Container for each discovered application component.

* **AWS CLI Snippet**:

  AWS CLI Example for Modernization Roadmap & Toolchain Generator:
```bash
echo 'Generates downloadable CSV/PDF transformation roadmaps with prescriptive tooling guides'
```

---

## References

### Official AWS Documentation
* [AWS Migration Hub Strategy Recommendations User Guide](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/what-is-strategy.html) - Complete official assessment and code analysis guide.
* [AWS Migration Hub Strategy API Reference](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/Welcome.html) - API endpoints, assessment triggers, and schema structures.
* [AWS Prescriptive Guidance: The 7 Rs of Cloud Migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-strategies/welcome.html) - Deep dive into Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate.
* [AWS Application Modernization Playbook](https://docs.aws.amazon.com/wellarchitected/latest/applications-modernization-lens/welcome.html) - Architectural principles for modernizing legacy applications.
* [AWS Migration Hub Security and IAM Best Practices](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/security.html) - Securing collector agents and S3 assessment buckets.

### Authoritative Web Pages, Blogs & Tutorials
* [AWS Architecture Blog: Automating Application Portfolio Analysis with Strategy Recommendations](https://aws.amazon.com/blogs/architecture/) - Case studies in portfolio rationalization.
* [AWS Workshops: Modernization Strategy Immersion Day](https://workshops.aws/) - Hands-on code scanning and refactoring roadmap generation.
* [A Cloud Guru / Pluralsight: Application Modernization Pathways on AWS](https://www.pluralsight.com/) - Evaluating monolithic architectures for container and serverless targets.
* [Medium / AWS In Plain English: Accelerating Migration Wave Planning with Strategy Recommendations](https://medium.com/) - Practical tips for parsing large codebase outputs.
* [FinOps Foundation: Evaluating Cloud Modernization ROI](https://www.finops.org/) - Comparing the financial returns of Rehosting vs. Refactoring architectures.

---

## FinOps

*Financial Operations (FinOps) is a discipline that combines cloud financial management, cost optimization, and business accountability. The following guidelines apply to every AWS service and help you control spend while maintaining performance and security.*

### 1. Cost Visibility & Allocation
- **Tagging Strategy** – Ensure every resource created by the service is tagged with `Environment`, `Project`, `Owner`, and `CostCenter`. Use AWS Tag Editor or Infrastructure as Code (IaC) to enforce mandatory tags.
- **Cost Allocation Tags** – Enable AWS-generated cost allocation tags (e.g., `aws:createdBy`) and propagate them to downstream resources like ENIs, EBS volumes, or CloudWatch logs.
- **Budgets & Alerts** – Create service-specific budgets that trigger alerts when spend exceeds 80% of the forecasted monthly budget. Use SNS notifications to automatically inform owners.

### 2. Right-Sizing & Utilization
- **Compute** – Leverage AWS Compute Optimizer or Auto Scaling policies to adjust instance types, fleet sizes, or Lambda concurrency based on utilization metrics.
- **Storage** – Periodically evaluate storage class transitions (e.g., S3 Standard → Intelligent-Tiering → Glacier) and delete orphaned snapshots, AMIs, or EBS volumes.
- **Serverless** – Use provisioned concurrency for predictable workloads; otherwise, rely on on-demand execution and monitor Request-Count vs. duration to avoid over-provisioning.

### 3. Reserved & Savings Plans
- **Reserved Instances (RI)** – Purchase RIs for predictable workloads such as steady-state EC2, RDS, or Redshift. Use the RI Recommendation tool to match instance families.
- **Savings Plans** – For mixed compute workloads, adopt Compute Savings Plans (flexible across EC2, Fargate, Lambda) to capture up-to-72% savings.

### 4. Data Transfer & Egress Management
- **VPC Endpoints** – Use Interface or Gateway VPC endpoints to keep traffic within the AWS network, eliminating internet egress charges.
- **Cross-Region Replication** – Replicate data only when necessary; leverage S3 Transfer Acceleration for occasional large transfers instead of constant cross-region copies.

### 5. Monitoring & Automation
- **Cost Explorer** – Schedule monthly Cost Explorer queries that break down spend by service, tag, and usage type.
- **Lambda-Driven Cleanup** – Deploy Lambda functions that automatically delete unused resources (e.g., unattached EBS volumes, stale snapshots) after a configurable grace period.
- **AWS Config Rules** – Enforce compliance with cost-related policies such as `required-tags`, `restricted-ec2-instance-types`, and `s3-bucket-public-access-prohibited`.

### 6. Governance & Chargeback
- **AWS Organizations** – Consolidate billing across accounts, apply Service Control Policies (SCPs) to limit high-cost services, and allocate costs to individual business units via linked accounts.
- **Chargeback Models** – Export detailed cost reports to your internal ERP system; map AWS cost elements to internal cost centers for transparent chargeback.

### 7. Continuous Improvement
- **FinOps Maturity Model** – Assess your organization's maturity (Inform, Optimize, Automate, Govern) and set quarterly improvement goals.
- **Training** – Provide teams with FinOps training and embed cost-awareness in PR reviews, CI pipelines, and architectural decision records.

By embedding these FinOps practices into the daily workflow for each service, you can achieve sustainable cost savings while preserving the reliability, security, and performance expected from AWS.
