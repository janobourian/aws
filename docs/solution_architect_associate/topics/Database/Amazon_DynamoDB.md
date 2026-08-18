# AWS Topic: Amazon DynamoDB
**Category:** Database
**Status:** ✅ Completed

---

## 1. High-Level Overview
Amazon DynamoDB is a serverless, fully managed, multi-region, and multi-active NoSQL database service designed to provide fast, consistent, and single-digit millisecond performance at any scale. In traditional relational or NoSQL database architectures, scaling to support millions of concurrent requests required partitioning databases, configuring complex replica sets, and manually tuning sharding keys, which introduced high database administration overhead. Amazon DynamoDB eliminates these bottlenecks by operating as an entirely serverless platform.

The database supports both key-value and document data structures, and handles partitioning and scaling automatically. DynamoDB offers two capacity modes: **Provisioned capacity** (where you define read/write capacity units with Auto Scaling) and **On-Demand capacity** (which scales up and down in response to request traffic automatically, charging per request). For high-performance read requirements, **DynamoDB Accelerator (DAX)** can be deployed as an in-memory cache to deliver microsecond response times. By managing replication, capacity planning, backups, and encryption automatically, DynamoDB serves as the core database solution for highly scaling, serverless cloud applications.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: A blazing-fast, fully managed NoSQL database built for extreme scale, delivering guaranteed single-digit millisecond response times regardless of data volume or user traffic.
* **How It Works**: Spreads data across solid-state drives in multiple facilities, automatically partitioning and scaling throughput up or down to match global user activity without downtime.
* **Key Business Value & Use Cases**: Powers high-volume e-commerce shopping carts, mobile gaming leaderboards, real-time user sessions, and IoT device telemetry with zero operational maintenance.

## 2. Core Architecture & Key Concepts
Amazon DynamoDB is a serverless key-value NoSQL database. Key concepts include:
* **Table, Item, Attribute**: Table is a collection of items (rows); Item is a collection of attributes (columns).
* **Primary Key**: Partition Key (determines partition routing) or Composite Key (Partition Key + Sort Key).
* **RCU & WCU**: Read Capacity Units and Write Capacity Units used to define provisioned throughput capacity.
* **DAX (DynamoDB Accelerator)**: An in-memory, clustered cache that delivers microsecond read performance.
* **Global Tables**: Active-active multi-region table replication with conflict resolution.

---

## 3. Common Use Cases
* **Web Session Store**: Storing active user session tokens with TTL auto-deletion to optimize storage.
* **E-commerce Shopping Carts**: Managing user shopping cart data with flexible JSON document attributes.
* **IoT Device Data Logging**: Ingesting high-frequency temperature readings from millions of devices in real time.
* **Gaming Leaderboards**: Tracking real-time player scores using composite keys (PlayerId + Score).

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)
* ⚠️ **Key Constraints**: Partition keys must be designed carefully to avoid hot partition issues (uneven load distribution). Item size limit is 400 KB.
* 🔒 **Security & Encryption**: Supports fine-grained access control using IAM conditions. All data is encrypted with KMS.
* ⚙️ **Performance/Scaling**: Scales automatically; DAX delivers microsecond latency for read-intensive workloads.

---

## 5. Comparison with Similar Services
| Service | Scaling Speed | Latency | Database Type |
| :--- | :--- | :--- | :--- |
| **Amazon DynamoDB** | Milliseconds | Milliseconds (Microseconds with DAX) | Key-Value / Document NoSQL |
| **Amazon DocumentDB** | Minutes | Milliseconds | Document NoSQL |
| **Amazon Aurora** | Milliseconds (Serverless v2) | Milliseconds | Relational (MySQL/Postgres) |
| **Amazon ElastiCache** | Minutes | Microseconds | In-Memory (Redis/Memcached) |

---

## 6. Cost Optimization
Optimize DynamoDB costs by:
* Using On-Demand mode for highly variable, low-traffic workloads.
* Transitioning archival tables to the Standard-IA table class.
* Enabling TTL to delete expired records at no charge.
* Using DAX to offload read queries and reduce RCU consumption.

---

## 7. In-Depth Perspectives

### Security Perspective
Security governance in Amazon DynamoDB is critical since the service stores core application metadata, user profiles, and operational logs. The security model leverages AWS IAM, fine-grained access control, and storage encryption. Access to tables is governed by IAM, restricting API actions like `dynamodb:GetItem`, `dynamodb:PutItem`, and `dynamodb:Query`. Fine-grained IAM controls allow organizations to permit specific roles to access only specific attributes or items in the database.

Using **Fine-Grained Access Control (FGAC)** with IAM condition keys allows administrators to restrict access based on the partition key. For example, a mobile application user can be authorized to read and write rows where the partition key matches their user ID, while blocking access to other users' rows.

Data protection at rest is enforced using customer-managed AWS KMS keys, which encrypt all data stored in the tables, indexes, and automated backups automatically. In transit, all communications are secured using TLS 1.2 or 1.3 across all endpoints. Auditing is managed via AWS CloudTrail, which logs administrative API calls, and CloudWatch Metrics, which can track throughput usage and throttle events, providing complete transparency for compliance audits.

### High Availability Perspective
High Availability (HA) for Amazon DynamoDB is built into its serverless, globally distributed database architecture. The service operates across multiple Availability Zones within an AWS region by default. DynamoDB automatically replicates table data across three Availability Zones, ensuring that a single zone outage does not result in data loss or query latency.

For global high availability, DynamoDB supports **Global Tables**. Global tables replicate data asynchronously across multiple AWS regions in an active-active configuration. Developers can write to any regional replica table, and DynamoDB automatically propagates changes to all other regions, typically in under a second. If a regional AWS outage occurs, applications can route traffic to an active table in a secondary region, preserving database availability.

Additionally, to optimize read performance and maintain high availability during traffic spikes, **DynamoDB Accelerator (DAX)** can be deployed. DAX is a clustered, in-memory cache that replicates cached data across multiple Availability Zones, ensuring that dashboards remain responsive even if the primary database is experiencing high concurrent read requests. By combining Multi-AZ replication, global active-active replication, and DAX caching, Amazon DynamoDB provides a highly available, robust database platform.

### Resilience Perspective
Resilience in Amazon DynamoDB focuses on database partition self-healing, Point-in-Time Recovery (PITR), and disaster recovery. The service possesses built-in self-healing capabilities: if an underlying partition server experiences a hardware failure, DynamoDB automatically promotes a replica server and rebuilds the partition on a healthy host, maintaining query latency with zero RTO.

To protect against data corruption or accidental deletions, DynamoDB supports **Point-in-Time Recovery (PITR)**. PITR provides continuous backups of your table data for up to 35 days. If a developer accidentally drops a table or runs an incorrect update script, administrators can restore the table to any second in the last 35 days.

To handle database throttling and rate limits, client applications must implement connection pooling and exponential backoff with jitter in their SDK calls. If write or read requests exceed the table's capacity limits, DynamoDB returns `ProvisionedThroughputExceededException`. Managing the database table schema, Global Tables, and DAX clusters as code using CloudFormation or Terraform templates ensures rapid disaster recovery (DR) of the database structure in a secondary region.

### Cost Optimizing Perspective
Cost Optimization for Amazon DynamoDB involves choosing the right capacity mode, monitoring throughput usage, and utilizing caching. DynamoDB pricing is based on the selected capacity mode:
* **Provisioned Capacity**: Best for stable, predictable traffic baselines (charges per RCU/WCU). Auto Scaling should be enabled to adjust capacity dynamically.
* **On-Demand Capacity**: Best for unpredictable, bursty traffic baselines (charges per read/write request).

To optimize database costs, developers should use the **DynamoDB Standard-IA (Infrequent Access)** table class for cold tables containing historical logs. Standard-IA offers up to 60% lower storage costs than standard tables, making it ideal for data archives.

Another cost optimization strategy is utilizing DynamoDB Accelerator (DAX) to cache reads. Caching read responses in DAX reduces the number of Read Capacity Units (RCUs) consumed on the primary table, lowering overall database charges. Implementing table cleanup using **Time to Live (TTL)** allows automatically deleting expired records (e.g. session tokens) without incurring delete write costs, optimizing storage capacity. Utilizing AWS Budgets allows setting cost alerts to notify when database spending exceeds allocations, ensuring that database costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment
* **Cost Optimization (Pillar 5)**: Charges per actual consumption and scales compute automatically via On-Demand capacity, eliminating idle server expenses.
* **Reliability (Pillar 6)**: Multi-AZ data replication and automated PITR protect against data loss and localized failures.
* **Security (Pillar 2)**: Enforces fine-grained access controls using IAM conditions, securing user data metrics.

---

## 9. Hands-On Walkthrough
### Create a DynamoDB Table and Enable TTL
1. Open the **AWS Console** and search for **DynamoDB**.
2. Click **Tables** on the left menu, then click **Create table**.
3. **Table name**: `SessionStore`.
4. **Partition key**: `sessionId` (String).
5. **Table settings**: Select **Default settings** (This sets the capacity mode to Provisioned with Auto Scaling).
6. Click **Create table**.
7. Once active, select the table, go to **Additional settings**:
   * Scroll to **Time to Live (TTL)** and click **Turn on**.
   * **TTL attribute**: Enter `expirationTime`.
8. Click **Turn on TTL**. Any item containing the `expirationTime` attribute (as an epoch timestamp) will be deleted automatically when expired.

---

## 10. AWS CLI Commands
### 1. Create a DynamoDB Table

Execute the following command:
```bash
aws dynamodb create-table \
    --table-name "SessionStore" \
    --attribute-definitions AttributeName=sessionId,AttributeType=S \
    --key-schema AttributeName=sessionId,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST
```

### 2. Put an Item into the Table

Execute the following command:
```bash
aws dynamodb put-item \
    --table-name "SessionStore" \
    --item '{"sessionId": {"S": "session-123"}, "userId": {"S": "user-456"}, "expirationTime": {"N": "1790000000"}}'
```

### 3. Get an Item from the Table

Execute the following command:
```bash
aws dynamodb get-item \
    --table-name "SessionStore" \
    --key '{"sessionId": {"S": "session-123"}}'
```

---
## 11. Advanced Architectural Perspectives

### Architecture Design Patterns
Amazon DynamoDB is a serverless NoSQL database. A standard pattern is pairing DynamoDB with DAX (DynamoDB Accelerator) to reduce read latencies to microseconds, using DynamoDB Streams to trigger Lambda functions for real-time events.

### Disaster Recovery (DR) & RTO/RPO Targets
To achieve multi-region high availability, configure **DynamoDB Global Tables**. Global Tables replicate data bi-directionally across selected regions with an RPO under 1 second and RTO of minutes during region failovers.

### Common Troubleshooting & Failure Modes
Write requests fail with `ProvisionedThroughputExceededException`. Resolve this by enabling DynamoDB On-Demand capacity mode, or updating partition keys to avoid hot partitions.

### Hybrid Integration & Migration Pathways
Sync on-premises databases with DynamoDB by streaming records using AWS DMS over Direct Connect, or running local worker daemons that update DynamoDB tables dynamically.

---
## 12. Detailed Sub-Services & Sub-Components

### Tables, Items & Attributes

Fully managed serverless NoSQL key-value and document database partitioned across solid-state drives.

* **Key Concepts**:
  A table is a collection of items (rows) up to 400 KB each. Primary key can be a simple Partition Key (HASH) or composite Partition Key + Sort Key (HASH + RANGE). Partition keys determine physical storage node placement.

* **AWS CLI Snippet**:

  AWS CLI Example for Tables, Items & Attributes:
```bash
aws dynamodb create-table \
    --table-name Orders \
    --attribute-definitions AttributeName=CustomerId,AttributeType=S AttributeName=OrderId,AttributeType=S \
    --key-schema AttributeName=CustomerId,KeyType=HASH AttributeName=OrderId,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST
```

### Global & Local Secondary Indexes (GSI / LSI)

Alternate query access paths enabling efficient filtering on non-primary key attributes.

* **Key Concepts**:
  Local Secondary Indexes (LSIs) share the partition key with an alternate sort key (must be created at table creation time). Global Secondary Indexes (GSIs) have a completely different partition and sort key, can be created anytime, and scale independently.

* **AWS CLI Snippet**:

  AWS CLI Example for Global & Local Secondary Indexes (GSI / LSI):
```bash
aws dynamodb update-table \
    --table-name Orders \
    --attribute-definitions AttributeName=OrderStatus,AttributeType=S AttributeName=OrderDate,AttributeType=S \
    --global-secondary-index-updates '[{"Create":{"IndexName":"StatusDateIndex","KeySchema":[{"AttributeName":"OrderStatus","KeyType":"HASH"},{"AttributeName":"OrderDate","KeyType":"RANGE"}],"Projection":{"ProjectionType":"ALL"}}}]'
```

### DynamoDB Streams

Time-ordered sequence of item-level modifications captured in near real-time.

* **Key Concepts**:
  Streams capture insert, update, and delete events (KEYS_ONLY, NEW_IMAGE, OLD_IMAGE, NEW_AND_OLD_IMAGES). Streams integrate natively with AWS Lambda to power event-driven architectures and cross-region replication.

* **AWS CLI Snippet**:

  AWS CLI Example for DynamoDB Streams:
```bash
aws dynamodb update-table \
    --table-name Orders \
    --stream-specification StreamEnabled=true,StreamViewType=NEW_AND_OLD_IMAGES
```

### DynamoDB Global Tables

Fully managed active-active multi-region replication delivering local single-digit millisecond read/write latency.

* **Key Concepts**:
  Replicates tables across multiple selected AWS regions automatically. Conflict resolution uses Last-Writer-Wins based on timestamps.

* **AWS CLI Snippet**:

  AWS CLI Example for DynamoDB Global Tables:
```bash
aws dynamodb update-table \
    --table-name Orders \
    --replica-updates '[{"Create":{"RegionName":"eu-west-1"}}]'
```

### DynamoDB Accelerator (DAX)

In-memory hardware cache cluster delivering microsecond response times for read-heavy workloads.

* **Key Concepts**:
  DAX provides seamless in-memory cache clustering without requiring application code changes to cache invalidation logic (write-through cache).

* **AWS CLI Snippet**:

  AWS CLI Example for DynamoDB Accelerator (DAX):
```bash
aws dax create-cluster \
    --cluster-name OrdersCache \
    --node-type dax.r5.large \
    --replication-factor 3 \
    --iam-role-arn arn:aws:iam::123456789012:role/DAXServiceRole
```

---

## References

### Official AWS Documentation
* [Amazon DynamoDB Official User Guide](https://docs.aws.amazon.com/amazon-dynamodb/latest/userguide/welcome.html) - Complete official administration, configuration, and architectural guide.
* [Amazon DynamoDB API Reference](https://docs.aws.amazon.com/amazon-dynamodb/latest/APIReference/Welcome.html) - Comprehensive endpoint actions, data types, query parameters, and error codes.
* [Amazon DynamoDB Security & Compliance Guide](https://docs.aws.amazon.com/amazon-dynamodb/latest/userguide/security.html) - IAM policies, KMS encryption at rest, TLS in transit, and VPC endpoint security.
* [Amazon DynamoDB Pricing & Service Quotas](https://aws.amazon.com/amazon-dynamodb/pricing/) - Detailed pricing models, tier thresholds, soft and hard service limit quotas.
* [AWS Well-Architected Framework: Database Best Practices](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) - Proven design principles and architectural pillars for enterprise scale.

### Authoritative Web Pages, Blogs & Tutorials
* [AWS Architecture Blog: Deep Dive & Patterns for Amazon DynamoDB](https://aws.amazon.com/blogs/architecture/) - Production reference architectures and real-world implementation case studies.
* [AWS Workshops: Hands-On Immersion Lab for Amazon DynamoDB](https://workshops.aws/) - Step-by-step interactive architectural labs, deployments, and testing exercises.
* [A Cloud Guru / Pluralsight: Mastering Amazon DynamoDB Architecture](https://www.pluralsight.com/) - In-depth technical breakdown of high availability, disaster recovery, and failover mechanics.
* [Medium / AWS In Plain English: Advanced Engineering Guide to Amazon DynamoDB](https://medium.com/) - Practical lessons learned, operational gotchas, and monitoring strategies in production.
* [FinOps Foundation: Cloud Financial Optimization for Amazon DynamoDB](https://www.finops.org/) - Proven strategies for waste elimination, commitment discounts, and automated resource scheduling.

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
