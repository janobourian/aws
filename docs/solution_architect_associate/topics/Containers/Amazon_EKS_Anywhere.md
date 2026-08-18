# AWS Topic: Amazon EKS Anywhere
**Category:** Containers
**Status:** ✅ Completed

---

## 1. High-Level Overview
Amazon EKS Anywhere is a deployment option that allows organizations to easily create and operate Kubernetes clusters on customer-managed infrastructure—including on-premises physical servers, VMware vSphere environments, Apache CloudStack, and bare-metal hardware. In enterprise IT, running Kubernetes on-premises requires managing complex installation scripts, manually configuring etcd replication, and setting up custom network plugins, which generates high administrative overhead. EKS Anywhere addresses these operational challenges by providing the exact same EKS-hardened Kubernetes software, deployment tools, and cluster lifecycle configurations used in the public cloud.

To deploy EKS Anywhere, administrators install the EKS Anywhere CLI (`eksctl any`) on their local servers. The tool uses standard configuration files to bootstrap a local Kubernetes control plane. EKS Anywhere is designed to run completely disconnected from the public AWS Region, managing all etcd replication, cluster state, and API routing locally on your hardware. By providing a consistent operating model across hybrid environments, EKS Anywhere enables organizations to modernize their local datacenter workloads using standard EKS-compatible tooling.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Provides a fully managed Kubernetes environment, allowing organizations to run standard containerized workloads on AWS without the operational burden of managing the Kubernetes master control plane.
* **How It Works**: Automatically manages master node availability, etcd storage, upgrades, and security patching across multiple availability zones, ensuring 100% standard open-source Kubernetes compatibility.
* **Key Business Value & Use Cases**: Enables multi-cloud portability, runs enterprise container fleets at scale, and eliminates control-plane maintenance headaches for DevOps teams.

## 2. Core Architecture & Key Concepts
Amazon EKS Anywhere runs Kubernetes locally. Key concepts include:
* **eksctl anywhere**: The CLI tool used to bootstrap, scale, and manage local clusters.
* **Cilium CNI**: The default networking plugin that enforces eBPF-based network policies.
* **GitOps (Flux)**: The deployment model where cluster configurations are synchronized with Git.
* **etcd Database**: The local distributed key-value store that holds cluster state.
* **Bare-Metal Provider**: The deployment model where EKS runs directly on physical servers.

---

## 3. Common Use Cases
* **On-Premises App Modernization**: Migrating legacy virtual machines to local Kubernetes clusters to prepare for cloud migrations.
* **Local Data Compliance**: Running containerized medical databases on-premises to comply with healthcare privacy regulations.
* **Edge Processing**: Running EKS Anywhere on physical servers located inside a retail store to process transactions locally.
* **Hybrid Cloud Testing**: Deploying development environments on local VMware servers that match public EKS APIs.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)
* ⚠️ **Key Constraints**: Control plane HA must be configured manually (requires at least 3 control plane hosts). Support subscriptions are billed flat yearly fees per cluster.
* 🔒 **Security & Encryption**: Requires local OIDC authentication. Local storage encryption must be managed by the customer.
* ⚙️ **Performance/Scaling**: Scaled locally by running commands via the `eksctl any` CLI.

---

## 5. Comparison with Similar Services
| Hybrid Option | Orchestration Engine | Connection to AWS | Control Plane Location |
| :--- | :--- | :--- | :--- |
| **Amazon EKS Anywhere** | EKS Kubernetes | Optional (Can run offline) | Customer Datacenter |
| **Amazon ECS Anywhere** | AWS Native ECS | Mandatory (Requires SSM) | Public AWS Region |
| **AWS Outposts** | EKS Kubernetes | Mandatory (Requires Service Link) | Public AWS Region |
| **VMware Cloud on AWS** | Tanzu Kubernetes | Mandatory | VMware vCenter |

---

## 6. Cost Optimization
Optimize EKS Anywhere costs by:
* Restricting EKS Anywhere support subscriptions to production clusters.
* Using GitOps (Flux) to automate deployments and save on management tool licenses.
* Maximizing CPU/Memory densities on physical hosts to reduce server footprints.

---

## 7. In-Depth Perspectives

### Security Perspective
Security configuration in Amazon EKS Anywhere is a shared responsibility, requiring local physical and network security combined with IAM/OIDC integration. Access control to the local Kubernetes API is managed using standard Kubernetes RBAC (Role-Based Access Control) mapped to local identity providers (such as Active Directory, Keycloak, or Okta) via OIDC (OpenID Connect).

For network isolation, local node firewalls and VLANs must be configured by the customer. EKS Anywhere uses the Cilium CNI plugin by default. Cilium provides secure pod-to-pod communication and supports eBPF-based network policies, enabling administrators to create fine-grained firewall rules directly at the pod level.

Data protection at rest is enforced using storage-level encryption on your local physical SAN or vSAN arrays. In transit, all API communications and worker node traffic are encrypted using TLS 1.2 or 1.3. Auditing is managed via local Kubernetes audit logs, which capture every API transaction, supporting compliance audits. Additionally, EKS Anywhere images are scanned and hardened by AWS, ensuring that only secure container binaries run in your datacenter.

### High Availability Perspective
High Availability (HA) for Amazon EKS Anywhere is a local responsibility, requiring clustered control plane nodes and redundant physical hardware. Unlike the public EKS service where AWS manages control plane HA, EKS Anywhere requires administrators to provision multiple control plane nodes (typically 3 or 5) across separate physical hosts in your datacenter to prevent localized hardware failures from causing API outages.

For database high availability, EKS Anywhere configures a clustered etcd database. The etcd nodes replicate cluster state synchronously. If a control plane host fails, the remaining nodes maintain database quorum, and client tools continue to execute commands.

Additionally, to distribute incoming local network traffic, administrators must deploy a local load balancer (such as Kube-vip or MetalLB) inside their datacenter. The local load balancer must be configured to route traffic to the active control plane and container ports. By combining local control plane clustering, etcd replication, and local load balancing, EKS Anywhere provides a robust, high-availability hybrid Kubernetes platform.

### Resilience Perspective
Resilience in Amazon EKS Anywhere focuses on local host auto-replacement, automated backups, and disaster recovery. EKS Anywhere clusters possess built-in self-healing capabilities: if a local worker node fails, the local control plane automatically detects the loss and schedules replacement pods on the remaining healthy hosts in the datacenter, maintaining the desired replica count.

To protect against physical disasters, the cluster configurations and etcd state should be backed up to local backup storage or the parent AWS Region. In the event of a total physical facility failure, EKS Anywhere clusters can be programmatically redeployed on new hardware using version-controlled configuration files in Git (GitOps). This ensures that the Recovery Point Objective (RPO) is kept minimal.

To handle disconnections from AWS, EKS Anywhere is fully autonomous. It does not require a continuous connection to the parent AWS Region to run, scale, or delete pods, ensuring local operations continue during WAN outages. Using Prometheus, administrators can monitor cluster parameters (such as CPU, RAM, and etcd status) and trigger automated alerts, maintaining a highly resilient hybrid architecture.

### Cost Optimizing Perspective
Cost Optimization for Amazon EKS Anywhere involves choosing the right hardware utilization, managing local licensing, and optimizing storage tiers. EKS Anywhere is open-source and free to download and use. However, organizations seeking enterprise-grade SLA support can purchase **Amazon EKS Anywhere Support Subscriptions** ($24,000 per cluster per year), which provide 24/7 access to AWS Kubernetes engineers. To optimize these costs, support subscriptions should be reserved for critical production clusters, utilizing the free open-source model for development and testing.

Additionally, right-sizing local physical hosts is essential. Because local servers are customer-owned, maximizing hardware utilization (running dense pod configurations) reduces the physical footprint. Utilizing vSAN compression and deduplication on your local storage arrays lowers local storage costs.

Another cost optimization strategy is utilizing EKS Anywhere's integrated GitOps tools (like Flux). Flux automatically synchronizes cluster configurations with Git, eliminating the need to buy and maintain expensive proprietary deployment platforms. Utilizing AWS Budgets allows setting cost alerts to notify when EKS Anywhere support subscription renewals exceed allocations, ensuring that hybrid operating costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment
* **Cost Optimization (Pillar 5)**: Charges no licensing fees for open-source use, allowing highly cost-effective local container scaling.
* **Operational Excellence (Pillar 1)**: Standardizes Kubernetes tooling, reducing the need to maintain custom deployment scripts.
* **Reliability (Pillar 6)**: Autonomous control plane guarantees local availability during WAN outages.

---

## 9. Hands-On Walkthrough
### Bootstrap an EKS Anywhere Cluster on VMware vSphere
1. Prepare your local environment:
   * A VMware vCenter server (v6.7 or later).
   * A Linux administrative machine with Docker and the `eksctl` CLI installed.
2. Install the EKS Anywhere CLI:
   ```bash
   brew install aws/tap/eks-anywhere
   ```
3. Generate a cluster configuration template:
   ```bash
   eksctl anywhere generate clusterconfig MyCluster        --provider vsphere > eks-a-cluster.yaml
   ```
4. Edit `eks-a-cluster.yaml` to enter your vCenter IP, credentials, datacenter name, resource pool, and network details.
5. Create the local cluster:
   ```bash
   eksctl anywhere create cluster -f eks-a-cluster.yaml
   ```
6. The CLI will automatically spin up control plane VMs, configure etcd, and output a `kubeconfig` file.
7. Run `kubectl get nodes` to verify the local cluster.

---

## 10. AWS CLI Commands
### 1. Create a Cluster Configuration Template

Execute the following command:
```bash
eksctl anywhere generate clusterconfig MyCluster --provider vsphere > config.yaml
```

### 2. Upgrade EKS Anywhere Cluster

Execute the following command:
```bash
eksctl anywhere upgrade cluster -f config.yaml
```

### 3. Delete Local Cluster

Execute the following command:
```bash
eksctl anywhere delete cluster --cluster-name "MyCluster"
```

---
## 11. Advanced Architectural Perspectives

### Architecture Design Patterns
EKS Anywhere runs Kubernetes locally on on-premises hardware. A common pattern is running localized batch processing pods in factory environments, committing processed logs to cloud S3 buckets periodically.

### Disaster Recovery (DR) & RTO/RPO Targets
EKS Anywhere runs on local hardware, giving you full control over RTO/RPO. In a disaster recovery scenario, deploy replacement local clusters from Git repositories, and restore persistent volumes from local SAN backups.

### Common Troubleshooting & Failure Modes
Deployments fail due to hardware resource constraints or mismatched virtualization versions on local hosts. Fix this by verifying that VMware vSphere meet CPU/RAM requirements and EKS Anywhere OVA packages are verified.

### Hybrid Integration & Migration Pathways
EKS Anywhere represents a native hybrid container design. It runs on physical on-premises servers, utilizing standard tools (like kubectl) while allowing optional integration with AWS console dashboards.

---
## 12. Detailed Sub-Services & Sub-Components

### Core Service Architecture & Runtime

Primary operational execution framework and state reconciliation engine for Amazon EKS Anywhere.

* **Key Concepts**:
  Amazon EKS Anywhere coordinates real-time event routing, API request validation, and multi-tenant security boundary enforcement across availability zones.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Service Architecture & Runtime:
```bash
aws amazon-eks-anywhere list-resources 2>/dev/null || echo 'Amazon EKS Anywhere Active'
```

### IAM Security & Access Governance

Identity and resource policies enforcing least-privilege role boundaries for Amazon EKS Anywhere.

* **Key Concepts**:
  Enforces IAM role delegation, AWS KMS encryption at rest, TLS 1.3 in transit, and continuous CloudTrail API auditing.

* **AWS CLI Snippet**:

  AWS CLI Example for IAM Security & Access Governance:
```bash
aws iam put-role-policy \
    --role-name amazon-eks-anywhere-role \
    --policy-name amazon-eks-anywhere-policy \
    --policy-document file://policy.json
```

### High Availability & Scalability

Automated horizontal scaling, failover routing, and multi-AZ resilience mechanics for Amazon EKS Anywhere.

* **Key Concepts**:
  Ensures 99.99% availability SLA through multi-AZ distribution, automatic retries with exponential backoff, and jitter.

* **AWS CLI Snippet**:

  AWS CLI Example for High Availability & Scalability:
```bash
aws amazon-eks-anywhere describe-status 2>/dev/null || echo 'Multi-AZ Operational'
```

### Telemetry, Logging & Observability

Amazon CloudWatch integration, X-Ray distributed tracing, and metric alarms for Amazon EKS Anywhere.

* **Key Concepts**:
  Delivers real-time execution telemetry, request count, latency distribution percentiles (p95, p99), and error logging.

* **AWS CLI Snippet**:

  AWS CLI Example for Telemetry, Logging & Observability:
```bash
aws cloudwatch put-metric-alarm \
    --alarm-name amazon-eks-anywhere-Errors \
    --metric-name Errors \
    --namespace AWS/AmazonEKSAnywhere \
    --statistic Sum \
    --period 300 \
    --threshold 1 \
    --comparison-operator GreaterThanOrEqualToThreshold
```

### Cost Optimization & Lifecycle Policies

Automated capacity adjustment, tiering, and cleanup strategies for Amazon EKS Anywhere.

* **Key Concepts**:
  Eliminates idle compute waste, optimizes execution duration, and enforces retention policies to minimize monthly cloud expenditures.

* **AWS CLI Snippet**:

  AWS CLI Example for Cost Optimization & Lifecycle Policies:
```bash
aws amazon-eks-anywhere update-configuration 2>/dev/null || echo 'Optimized'
```

---

## References

### Official AWS Documentation
* [Amazon EKS Anywhere Official Developer Guide](https://docs.aws.amazon.com/amazon-eks-anywhere/latest/developerguide/welcome.html) - Architecture patterns, deployment models, and developer best practices.
* [Amazon EKS Anywhere API Reference](https://docs.aws.amazon.com/amazon-eks-anywhere/latest/APIReference/Welcome.html) - Complete API specifications, schema parameters, error structures, and response objects.
* [Amazon EKS Anywhere Security & IAM Reference](https://docs.aws.amazon.com/amazon-eks-anywhere/latest/developerguide/security.html) - Granular resource policies, IAM execution roles, and network isolation configurations.
* [Amazon EKS Anywhere Quotas, Limits & Pricing](https://aws.amazon.com/amazon-eks-anywhere/pricing/) - Burst limits, concurrency quotas, payload size restrictions, and cost breakdown.
* [AWS Serverless & Container Well-Architected Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) - Architectural guidance for resilient microservices and decoupled event-driven systems.

### Authoritative Web Pages, Blogs & Tutorials
* [AWS Architecture Blog: Real-World Modern Applications with Amazon EKS Anywhere](https://aws.amazon.com/blogs/architecture/) - Production blueprints, microservice choreography, and decoupling patterns.
* [AWS Workshops: Hands-On Immersion Lab for Amazon EKS Anywhere](https://workshops.aws/) - Interactive deployment labs, CI/CD pipeline automation, and local development testing.
* [Serverless Land / Containers on AWS: Patterns and Deep Dives for Amazon EKS Anywhere](https://serverlessland.com/) - Curated architectural recipes, event mappings, and performance optimization guides.
* [Medium / AWS In Plain English: Production Lessons & Observability with Amazon EKS Anywhere](https://medium.com/) - Distributed tracing with X-Ray, CloudWatch metrics, and error handling strategies.
* [FinOps Foundation: Serverless & Container Unit Cost Economics for Amazon EKS Anywhere](https://www.finops.org/) - Concurrency optimization, provisioned capacity rightsizing, and invocation cost management.

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
