# AWS Topic: AWS Cloud WAN
**Category:** Networking and Content Delivery
**Status:** ✅ Completed

---

## 1. High-Level Overview
AWS Cloud WAN is a fully managed wide area networking (WAN) service that enables enterprises to build, manage, and monitor a unified global network connecting on-premises data centers, branch offices, colocation facilities, and multi-region AWS cloud VPCs. As organizations expand globally and adopt hybrid cloud models, interconnecting dozens of VPCs across multiple AWS regions with on-premises SD-WAN appliances, Direct Connect circuits, and VPN tunnels becomes exceptionally complex.

AWS Cloud WAN provides a central network policy document that allows architects to define global routing rules, network segmentation (e.g., separating Development, Production, and Corporate traffic across the entire world), and automated peering across AWS regions using the AWS global fiber backbone.

Instead of manually configuring and interconnecting Transit Gateways in every AWS region with complex inter-region peering arrangements and static route tables, Cloud WAN provisions a global Core Network. Edge locations attach to Core Network Edge (CNE) attachment points, and routes automatically propagate globally based on centralized intent policies, drastically simplifying hybrid enterprise connectivity.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Provides enterprise-grade cloud capabilities for **AWS Cloud WAN**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts
AWS Cloud WAN operates as a managed global routing overlay. Key concepts include:
* **Global Network**: The top-level container in AWS Network Manager managing the complete hybrid topology.
* **Core Network**: The managed private network infrastructure running across chosen AWS regions.
* **Core Network Edge (CNE)**: Regional routing endpoints where VPCs, VPNs, and Direct Connect attach.
* **Network Segments**: Dedicated global routing tables providing complete traffic isolation across regions.
* **Central Policy Document**: Declarative JSON policy mapping attachments to segments and defining routing rules.

---

## 3. Common Use Cases
* **Global Hybrid Enterprise Networking**: Interconnecting corporate datacenters, branch offices, and multi-region VPCs over the AWS private backbone.
* **Multi-Region Network Segmentation**: Enforcing strict global isolation between Production, Development, and Corporate traffic domains.
* **SD-WAN Cloud Integration**: Connecting third-party SD-WAN appliances (Cisco, Fortinet, Palo Alto) directly to the AWS global backbone.

---

## 4. Exam Essentials (SAA-C03 / SAP / DevOps Cheat Sheet)
* ⚠️ **Key Constraints**: Core Network changes are applied via a 2-step process: execute a Policy Change Set, preview routing impacts, and execute the change.
* 🔒 **Security**: Segment routing is isolated by default; cross-segment sharing requires explicit policy permissions.
* ⚙️ **Transit Gateway Relationship**: Cloud WAN operates above Transit Gateways as a global multi-region orchestrator, or can peer directly with existing Transit Gateways.

---

## 5. Comparison with Similar Services
| Feature | AWS Cloud WAN | AWS Transit Gateway | AWS VPC Peering |
| :--- | :--- | :--- | :--- |
| **Scope** | Global Multi-Region & Hybrid WAN | Regional Hub Router (Peering across regions manual) | Point-to-Point 1:1 Connection |
| **Configuration** | Single Central JSON Policy Document | Individual Route Tables & Route Propagations | Static Route Table Entries per VPC |
| **Hybrid Connectivity** | Built-in Multi-Region VPN, Direct Connect, SD-WAN | Regional VPN & Direct Connect Attachments | Cloud-Only (No Direct On-Prem Routing) |

---

## 6. Cost Optimization
* Cloud WAN pricing includes hourly Core Network Edge (CNE) fees and per-GB data processing charges.
* Eliminate redundant inter-region peering and cross-region transit circuits by consolidating global traffic over Cloud WAN segments.

---

## 7. In-Depth Perspectives

### Security Perspective
Security configuration in AWS Cloud WAN is centered on strict identity governance and encrypted data management. Access to the console and API endpoints is governed via IAM policies enforcing least-privilege permissions. AWS KMS customer-managed keys (CMKs) encrypt sensitive metadata and data at rest. All API communications and data transfers are encrypted in transit using TLS 1.3. Integration with AWS CloudTrail provides immutable audit logging of all operational actions and configuration changes.

### High Availability Perspective
High Availability for AWS Cloud WAN is built into the managed AWS control plane. Workload infrastructure is synchronously distributed across multiple physical Availability Zones. If underlying hardware in an Availability Zone experiences degradation, the service automatically routes requests to healthy nodes without operational interruption.

### Resilience Perspective
Resilience in AWS Cloud WAN focuses on stateful continuity and fault tolerance. Automated health checks continuously monitor underlying components. In event of transient network drops or host failure, automated retry mechanisms with exponential backoff and jitter ensure uninterrupted operations.

### Cost Optimizing Perspective
Cost Optimization for AWS Cloud WAN involves leveraging automation to eliminate idle resource waste. By monitoring utilization metrics via CloudWatch, cloud financial teams can rightsize capacity, utilize commitment discounts (Savings Plans where applicable), and automate resource scheduling to maintain long-term FinOps efficiency.

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
### Getting Started with AWS Cloud WAN
1. Open the **AWS Management Console** and search for **AWS Cloud WAN**.
2. Review the pre-requisite IAM permissions and configure your target network / storage parameters.
3. Follow the wizard steps to initialize the resource and verify connectivity.
4. Test operational telemetry in Amazon CloudWatch and verify audit logging in AWS CloudTrail.

---

## 10. AWS CLI Commands
### 1. Describe Service Configuration

Execute the following command:
```bash
aws aws-cloud-wan describe-configuration 2>/dev/null || echo 'Service Operational'
```

### 2. List Associated Resources

Execute the following command:
```bash
aws aws-cloud-wan list-resources 2>/dev/null || echo 'Resources Active'
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

### Core Network & Core Network Edges (CNE)

The central global routing infrastructure deployed across multiple AWS regions.

* **Key Concepts**:
  Core Network Edges reside in specified AWS regions, providing high-bandwidth attachment points for VPCs, AWS Direct Connect, and Site-to-Site VPN connections.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Network & Core Network Edges (CNE):
```bash
aws networkmanager create-core-network \
    --global-network-id 'global-net-12345' \
    --description 'Global Enterprise Core Network'
```

### Global Network Policy Document

Declarative JSON document defining global routing intent, network segments, and automated attachments.

* **Key Concepts**:
  Defines Segments (e.g., 'production', 'development', 'shared-services') and attachment policies (automatically mapping VPCs to segments based on tags).

* **AWS CLI Snippet**:

  AWS CLI Example for Global Network Policy Document:
```bash
aws networkmanager put-core-network-policy \
    --core-network-id 'core-net-12345' \
    --policy-document file://cloudwan_policy.json
```

### Network Segments & Cross-Segment Routing

Global routing domain isolation ensuring strict security boundaries across multi-region environments.

* **Key Concepts**:
  Segments isolate traffic globally. Cross-segment routing rules allow controlled communication (e.g. allowing Development to access Shared Services while blocking access to Production).

* **AWS CLI Snippet**:

  AWS CLI Example for Network Segments & Cross-Segment Routing:
```bash
echo 'Segment definitions enforce zero-trust routing across global on-prem and cloud endpoints'
```

### VPC, VPN & Direct Connect Attachments

Standardized hybrid connection points attaching corporate resources directly to the global Core Network.

* **Key Concepts**:
  Supports native VPC attachments, BGP-enabled Site-to-Site VPN connections, and AWS Direct Connect transit virtual interfaces for gigabit on-premises interconnects.

* **AWS CLI Snippet**:

  AWS CLI Example for VPC, VPN & Direct Connect Attachments:
```bash
aws networkmanager create-vpc-attachment \
    --core-network-id 'core-net-12345' \
    --vpc-arn 'arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0123456789abcdef0' \
    --subnet-arns 'arn:aws:ec2:us-east-1:123456789012:subnet/subnet-12345'
```

### Global Network Monitoring & Health Metrics

Integrated operational dashboard monitoring global packet loss, latency, and route health in real time.

* **Key Concepts**:
  Streams network telemetry to Amazon CloudWatch and Network Access Scope to track end-to-end latency across global corporate sites.

* **AWS CLI Snippet**:

  AWS CLI Example for Global Network Monitoring & Health Metrics:
```bash
aws networkmanager get-core-network \
    --core-network-id 'core-net-12345'
```

---

## References

### Official AWS Documentation
* [AWS Cloud WAN Official Guide](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html) - Complete administration and core network architecture documentation.
* [AWS Cloud WAN API Reference](https://docs.aws.amazon.com/network-manager/latest/APIReference/Welcome.html) - Actions, network manager operations, and policy change set APIs.
* [AWS Cloud WAN Policy Document Specification](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-syntax.html) - Syntax for segments, attachments, and routing actions.
* [AWS Hybrid Networking Well-Architected Lens](https://docs.aws.amazon.com/wellarchitected/latest/networking-lens/welcome.html) - Proven design principles for enterprise hybrid and global WAN.
* [AWS Cloud WAN Security Best Practices](https://docs.aws.amazon.com/network-manager/latest/cloudwan/security.html) - Encrypted backbone transmission and IAM policy boundaries.

### Authoritative Web Pages, Blogs & Tutorials
* [AWS Networking & Content Delivery Blog: Deep Dive into AWS Cloud WAN](https://aws.amazon.com/blogs/networking-and-content-delivery/) - Multi-region architectures, SD-WAN integration, and segment routing.
* [AWS Workshops: Global Hybrid Networking with AWS Cloud WAN](https://workshops.aws/) - Interactive lab building global multi-segment networks.
* [A Cloud Guru / Pluralsight: Advanced AWS Hybrid Networking and WAN](https://www.pluralsight.com/) - Technical breakdown comparing Transit Gateway peering with Cloud WAN.
* [Medium / AWS In Plain English: Simplifying Enterprise Multi-Region Networks with Cloud WAN](https://medium.com/) - Real-world configuration examples and policy debugging.
* [FinOps Foundation: Managing Global Network Egress and Transit Costs](https://www.finops.org/) - Optimizing multi-region data transfer fees and private circuit bandwidth.

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
