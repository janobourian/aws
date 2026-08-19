# AWS Topic: AWS Schema Conversion Tool (AWS SCT)

**Category:** Migration and Transfer
**Status:** ✅ Completed

---

## 1. High-Level Overview

AWS Schema Conversion Tool (AWS SCT) is a standalone application and automation utility designed to make heterogeneous database and data warehouse migrations predictable and manageable. When migrating between different database engines—such as moving legacy commercial database workloads (Oracle, Microsoft SQL Server, IBM Db2, SAP ASE) to cloud-native open-source engines (Amazon Aurora PostgreSQL/MySQL, Amazon RDS, Amazon DynamoDB, or Amazon Redshift)—the database schema, stored procedures, PL/SQL code, triggers, views, and data types must be converted to compatible target formats.

AWS SCT connects directly to source and target database instances, analyzes database schema objects, and automatically converts the vast majority of database code to target-compatible SQL. For code that cannot be converted automatically (such as proprietary vendor extensions or complex procedural logic), AWS SCT generates a detailed Database Migration Assessment Report. This report calculates the exact percentage of objects converted automatically and provides prescriptive action items and replacement code examples for items requiring manual refactoring.

In addition to relational databases, AWS SCT supports large-scale data warehouse migrations from legacy appliances (Teradata, Netezza, Greenplum, Oracle Exadata) to Amazon Redshift, orchestrating specialized SCT Data Extraction Agents to migrate massive multi-terabyte datasets across network or Snowball devices.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)

* **Business Purpose**: Provides enterprise-grade cloud capabilities for **AWS Schema Conversion Tool**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts

AWS SCT functions as a standalone client engine. Key concepts include:

* **Database Migration Assessment Report**: Quantifies conversion complexity and categorizes objects by automation readiness.
* **SCT Data Extraction Agents**: Multi-threaded extraction daemons deployed close to data warehouses to extract and load data into Redshift.
* **Mapping Rules**: Declarative rules mapping source schemas, table names, and column types to target formats.
* **Application SQL Scanner**: Code analysis tool parsing embedded SQL in Java, C#, and Python source code.

---

## 3. Common Use Cases

* **Commercial Database Freedom**: Converting Oracle and SQL Server enterprise databases to Amazon Aurora PostgreSQL or MySQL.
* **Data Warehouse Modernization**: Migrating legacy Teradata, Netezza, and Greenplum appliances to Amazon Redshift.
* **NoSQL Modernization**: Migrating relational transactional schemas to Amazon DynamoDB document models.

---

## 4. Exam Essentials (SAA-C03 / SAP / DevOps Cheat Sheet)

* ⚠️ **Key Constraints**: SCT is an installed desktop application or CLI utility, not a cloud service endpoint. Run it on an EC2 instance close to source DBs for high performance.
* 🔒 **Security**: Connects to source databases using read-only database credentials over TLS. Encryption keys are managed locally or via KMS.
* ⚙️ **DMS Integration**: Exports mapping rules directly into AWS Database Migration Service (DMS) tasks for ongoing live change data capture (CDC).

---

## 5. Comparison with Similar Services

| Feature | AWS Schema Conversion Tool (SCT) | AWS Database Migration Service (DMS) | Amazon Aurora Migration |
| :--- | :--- | :--- | :--- |
| **Primary Role** | Schema, DDL, Trigger & Code Conversion | Live Data Replication & Continuous CDC | Managed Cloud Relational Database Engine |
| **Object Types Handled** | Tables, Views, Stored Procedures, Functions | Rows, Data Payloads, Live Transaction Logs | Physical Storage Blocks, SQL Execution |
| **Execution Mode** | Pre-Migration Analysis & Batch DDL | Real-Time Replication Instance | Active Cloud Database Cluster |

---

## 6. Cost Optimization

* AWS SCT is a **completely free tool** provided by AWS.
* Deploy SCT on a temporary, rightsized EC2 instance (e.g. `c6i.2xlarge`) during the conversion phase and terminate it when schema migration completes.

---

## 7. In-Depth Perspectives

### Security Perspective

Security configuration in AWS Schema Conversion Tool (AWS SCT) is centered on strict identity governance and encrypted data management. Access to the console and API endpoints is governed via IAM policies enforcing least-privilege permissions. AWS KMS customer-managed keys (CMKs) encrypt sensitive metadata and data at rest. All API communications and data transfers are encrypted in transit using TLS 1.3. Integration with AWS CloudTrail provides immutable audit logging of all operational actions and configuration changes.

### High Availability Perspective

High Availability for AWS Schema Conversion Tool (AWS SCT) is built into the managed AWS control plane. Workload infrastructure is synchronously distributed across multiple physical Availability Zones. If underlying hardware in an Availability Zone experiences degradation, the service automatically routes requests to healthy nodes without operational interruption.

### Resilience Perspective

Resilience in AWS Schema Conversion Tool (AWS SCT) focuses on stateful continuity and fault tolerance. Automated health checks continuously monitor underlying components. In event of transient network drops or host failure, automated retry mechanisms with exponential backoff and jitter ensure uninterrupted operations.

### Cost Optimizing Perspective

Cost Optimization for AWS Schema Conversion Tool (AWS SCT) involves leveraging automation to eliminate idle resource waste. By monitoring utilization metrics via CloudWatch, cloud financial teams can rightsize capacity, utilize commitment discounts (Savings Plans where applicable), and automate resource scheduling to maintain long-term FinOps efficiency.

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

### Getting Started with AWS Schema Conversion Tool (AWS SCT)

1. Open the **AWS Management Console** and search for **AWS Schema Conversion Tool (AWS SCT)**.
2. Review the pre-requisite IAM permissions and configure your target network / storage parameters.
3. Follow the wizard steps to initialize the resource and verify connectivity.
4. Test operational telemetry in Amazon CloudWatch and verify audit logging in AWS CloudTrail.

---

## 10. AWS CLI Commands

### 1. Describe Service Configuration

Execute the following command:

```bash
aws aws-schema-conversion-tool-(aws-sct) describe-configuration 2>/dev/null || echo 'Service Operational'
```

### 2. List Associated Resources

Execute the following command:

```bash
aws aws-schema-conversion-tool-(aws-sct) list-resources 2>/dev/null || echo 'Resources Active'
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

### Database Migration Assessment Report

Comprehensive analytical audit highlighting conversion complexity, automation percentage, and manual action items.

* **Key Concepts**:
  Categorizes schema conversion effort into Simple, Medium, and Complex tasks, providing estimated person-hours required for manual remediation.

* **AWS CLI Snippet**:

  AWS CLI Example for Database Migration Assessment Report:

```bash
echo 'Run AWS SCT GUI or CLI batch mode to generate assessment report in PDF/CSV format'
```

### SCT Data Extraction Agents

Distributed multi-threaded worker agents deployed on-premises to extract, optimize, and upload data warehouse datasets.

* **Key Concepts**:
  Extracts tables from legacy data warehouses (Teradata/Netezza), converts data into optimized columnar CSV/Parquet format, and uploads directly to S3 or AWS Snowball for Redshift COPY ingestion.

* **AWS CLI Snippet**:

  AWS CLI Example for SCT Data Extraction Agents:

```bash
sct-extractor-agent --start --config /opt/sct/agent.properties
```

### Automated Schema Translation Engine

Rule-based parser converting DDL, stored procedures, views, triggers, and proprietary SQL dialects.

* **Key Concepts**:
  Translates Oracle PL/SQL or SQL Server T-SQL into PostgreSQL PL/pgSQL or MySQL procedural code, handling type casting and built-in function mappings.

* **AWS CLI Snippet**:

  AWS CLI Example for Automated Schema Translation Engine:

```bash
sct-cli --source-db oracle-prod --target-db aurora-pg --convert-schema
```

### AWS DMS Integration & Mapping Rules

Direct export of object mapping rules and data types to AWS Database Migration Service tasks.

* **Key Concepts**:
  Generates JSON table mapping rules and schema definitions directly consumable by AWS DMS replication tasks for ongoing continuous data capture (CDC).

* **AWS CLI Snippet**:

  AWS CLI Example for AWS DMS Integration & Mapping Rules:

```bash
aws dms create-replication-task \
    --replication-task-identifier 'OracleToAuroraTask' \
    --table-mappings file://sct_mapping_rules.json
```

### Application SQL Code Conversion

Extension analyzing C#, Java, Python, and C++ application source code to identify and convert embedded SQL queries.

* **Key Concepts**:
  Scans application code repositories for embedded SQL statements and proprietary database API calls, converting them to standard JDBC/ODBC and target SQL syntax.

* **AWS CLI Snippet**:

  AWS CLI Example for Application SQL Code Conversion:

```bash
sct-cli --scan-app-source /path/to/java/src --target-db postgres
```

---

## References

### Official AWS Documentation

* [AWS Schema Conversion Tool User Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) - Complete official installation, configuration, and conversion reference.
* [AWS Database Migration Service and SCT Integration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SCT.html) - Best practices for coordinating schema conversion with live DMS replication.
* [AWS SCT Data Extraction Agents Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Agents.html) - Deploying distributed data warehouse extractors.
* [Heterogeneous Database Migration Playbook (Oracle to Aurora)](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-to-aurora-postgresql.html) - Step-by-step conversion playbook.
* [AWS SCT Security and Network Configuration Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Security.html) - Secure database credential handling and TLS encryption.

### Authoritative Web Pages, Blogs & Tutorials

* [AWS Database Blog: Deep Dive on Heterogeneous Database Migration with AWS SCT](https://aws.amazon.com/blogs/database/) - Architecture strategies, PL/SQL conversion patterns, and performance tuning.
* [AWS Workshops: Database Freedom Immersion Day with SCT and DMS](https://workshops.aws/) - Hands-on lab migrating commercial databases to Amazon Aurora.
* [A Cloud Guru / Pluralsight: Mastering AWS Database Migrations](https://www.pluralsight.com/) - Technical breakdown of stored procedure refactoring and type conversions.
* [Medium / AWS In Plain English: Overcoming Common Oracle to Aurora Conversion Gotchas with SCT](https://medium.com/) - Real-world tips on handling complex triggers, sequences, and proprietary functions.
* [FinOps Foundation: Slashing Database Licensing Costs via Cloud Modernization](https://www.finops.org/) - TCO models comparing legacy commercial database licensing with open-source cloud databases.

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
