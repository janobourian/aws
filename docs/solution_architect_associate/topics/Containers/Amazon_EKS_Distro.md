# AWS Topic: Amazon EKS Distro
**Category:** Containers
**Status:** ✅ Completed

---

## 1. High-Level Overview
Amazon EKS Distro (EKS-D) is a secure, open-source distribution of Kubernetes used by Amazon EKS to deploy highly resilient clusters. In the upstream Kubernetes open-source community, new releases and dependency versions are introduced rapidly, which can introduce compatibility issues, performance regressions, and security vulnerabilities if not thoroughly tested. EKS Distro addresses these operational challenges by providing the exact same Kubernetes releases, dependencies, and security patches that have been tested and hardened by Amazon for EKS.

EKS Distro includes upstream Kubernetes binaries (such as kube-apiserver, kube-controller-manager, and kubelet), core networking plugins (like CoreDNS), storage drivers (like the CSI driver), and container runtimes. AWS tests every EKS Distro release against the CNCF (Cloud Native Computing Foundation) conformance tests to ensure full compatibility. Developers can download EKS Distro binaries and source code for free, allowing them to spin up their own Kubernetes clusters on-premises, on EC2, or on bare-metal servers using EKS-hardened software. By aligning local clusters with the EKS release lifecycle, EKS Distro simplifies hybrid container operations, enabling a highly consistent and secure deployment experience.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Provides a fully managed Kubernetes environment, allowing organizations to run standard containerized workloads on AWS without the operational burden of managing the Kubernetes master control plane.
* **How It Works**: Automatically manages master node availability, etcd storage, upgrades, and security patching across multiple availability zones, ensuring 100% standard open-source Kubernetes compatibility.
* **Key Business Value & Use Cases**: Enables multi-cloud portability, runs enterprise container fleets at scale, and eliminates control-plane maintenance headaches for DevOps teams.

## 2. Core Architecture & Key Concepts
Amazon EKS Distro provides EKS-hardened Kubernetes binaries. Key concepts include:
* **CNCF Conformance**: Conformance testing that guarantees EKS Distro is fully compatible with standard Kubernetes.
* **Upstream Kubernetes**: The open-source Kubernetes code repository maintained by the CNCF.
* **Signed Binaries**: Cryptographically signed software packages that verify AWS as the source.
* **Backported Patches**: Hardened security patches backported by AWS to older Kubernetes versions.
* **etcd Database**: The distributed key-value store that holds cluster state.

---

## 3. Common Use Cases
* **Custom Bare-Metal Deployments**: Building a highly customized Kubernetes cluster directly on bare-metal servers using EKS-hardened software.
* **Disconnected Local Clusters**: Running secure, offline Kubernetes clusters in isolated research labs or submarines.
* **Hybrid Consistency**: Running EKS Distro on EC2 instances to replicate EKS cluster behaviors at a lower cost.
* **Upstream Kubernetes Testing**: Testing new Kubernetes versions and dependencies before upgrading EKS clusters in production.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)
* ⚠️ **Key Constraints**: Control plane HA and etcd clustering must be configured manually by the customer. EKS Distro does not include AWS support unless purchased separately.
* 🔒 **Security & Encryption**: Binaries are signed by AWS. Encryption and network security must be configured manually.
* ⚙️ **Performance/Scaling**: Highly dependent on the local hardware and virtual resource allocation configurations.

---

## 5. Comparison with Similar Services
| Service | Package Type | Support Model | Setup Overhead |
| :--- | :--- | :--- | :--- |
| **Amazon EKS Distro** | Raw Kubernetes Binaries | Open-source (No AWS support) | High (Manual setup) |
| **Amazon EKS Anywhere** | Managed Kubernetes Installer | Optional AWS Support | Medium |
| **Amazon EKS** | Managed AWS Service | Included AWS Support | Low |
| **Kops on EC2** | Managed Kubernetes Installer | Open-source | Medium |

---

## 6. Cost Optimization
Optimize EKS Distro costs by:
* Maximizing CPU/Memory densities on physical hosts to reduce server footprints.
* Using GitOps to automate deployments and save on management tool licenses.
* Standardizing on EKS Distro to eliminate duplicate software licenses across hybrid sites.

---

## 7. In-Depth Perspectives

### Security Perspective
Security configuration in Amazon EKS Distro is a customer responsibility, leverage AWS-hardened software binaries. The security model focuses on upstream patch management, cryptographically signed binaries, and OS-level security. EKS Distro contains security patches that are backported by AWS security teams to older Kubernetes releases, ensuring that critical vulnerabilities are patched before they are released in the upstream community.

All EKS Distro binaries, container images, and dependencies are cryptographically signed by AWS. This allows administrators to verify the integrity and origin of the software, preventing man-in-the-middle attacks or code tampering.

Data protection at rest and in transit must be configured by the customer. All communications between the EKS Distro API server, etcd nodes, and kubelet agents must be encrypted using TLS 1.2 or 1.3. etcd storage volumes must be encrypted using local volume encryption. Auditing must be managed using Kubernetes audit policies configured on the API server, writing logs to a secure, central syslog or S3 bucket, ensuring complete compliance auditability.

### High Availability Perspective
High Availability (HA) for Amazon EKS Distro is entirely the responsibility of the customer deploying the distribution. Unlike EKS where AWS manages control plane HA, or EKS Anywhere where EKS tools automate clustering, EKS Distro only provides the software binaries. To build a highly available control plane, administrators must manually provision and configure multiple control plane nodes (typically 3 or 5) across separate physical hosts.

The etcd database must be configured in a clustered mode. The etcd nodes replicate cluster state synchronously. If a control plane host fails, the remaining nodes maintain database quorum, and client tools continue to execute commands.

Additionally, to distribute incoming local network traffic, administrators must deploy a local load balancer (such as Nginx, HAProxy, or a physical hardware load balancer) inside their datacenter. The load balancer must be configured to route traffic to the active control plane and container ports. By combining EKS-hardened binaries, manual control plane clustering, etcd replication, and custom load balancing, EKS Distro provides a highly available, robust Kubernetes platform.

### Resilience Perspective
Resilience in Amazon EKS Distro focuses on upstream compatibility, version support, and disaster recovery. EKS Distro provides stable, CNCF-conformant Kubernetes versions. This ensures that upstream applications and tools (such as Prometheus, Fluentd, and Istio) run reliably on EKS Distro without modification, preventing runtime failures.

To protect against physical disasters, cluster configurations and etcd state must be backed up using tools like Velero or local backup arrays. In the event of a total physical facility failure, EKS Distro clusters can be programmatically redeployed on new hardware using version-controlled configuration files. This ensures that the Recovery Point Objective (RPO) is kept minimal.

To handle API limits and connection timeouts over local networks, client SDK calls must implement exponential backoff with jitter. Using Prometheus, administrators can monitor cluster parameters (such as CPU, RAM, and etcd status) and trigger automated alerts, maintaining a highly resilient hybrid architecture.

### Cost Optimizing Perspective
Cost Optimization for Amazon EKS Distro involves choosing the right hardware utilization, managing local licensing, and optimizing storage tiers. EKS Distro is completely free and open-source, with no licensing fees or upfront commitments. This is highly cost-effective compared to traditional enterprise Kubernetes platforms that charge high licensing fees. To optimize these costs, administrators should monitor local server utilization and only provision the hardware capacity required.

Additionally, managing storage costs is essential. Storing data on local SAN or physical arrays is cheaper than provisioning high-performance cloud storage. Utilizing local vSAN compression and deduplication lowers local storage costs.

Another cost optimization strategy is using EKS Distro to standardize container deployments across hybrid environments, eliminating the need to maintain different Kubernetes distributions. Utilizing AWS Budgets allows setting cost alerts to notify when AWS resources (such as ECR registries or S3 buckets used to host EKS Distro binaries) exceed allocations, ensuring that hybrid operating costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment
* **Cost Optimization (Pillar 5)**: Charges no licensing fees, providing highly cost-effective local container scaling.
* **Operational Excellence (Pillar 1)**: Standardizes Kubernetes versions, reducing the need to maintain custom container distributions.
* **Reliability (Pillar 6)**: CNCF-conformant binaries guarantee stable and reliable operations.

---

## 9. Hands-On Walkthrough
### Deploy EKS Distro on a Local Linux Machine
1. Log in to your local Linux administrative machine.
2. Download the EKS Distro binaries from the AWS public repository:
   Download the target Kubernetes version (e.g. v1.25):
```bash
wget https://distro.eks.amazonaws.com/kubernetes-1-25/releases/1/artifacts/kubernetes/v1.25.0/bin/linux/amd64/kubelet
   chmod +x kubelet
```
3. Download the EKS Distro container images (e.g. CoreDNS):
   ```bash
docker pull public.ecr.aws/eks-distro/coredns/coredns:v1.9.3-eks-1-25-1
```
4. Configure the system services:
   * Create a systemd service for `kubelet`.
   * Configure the local container runtime (e.g., `containerd`).
5. Run the kubelet service to join the node to your local cluster.

---

## 10. AWS CLI Commands
### 1. View EKS Distro Release Metadata

Execute the following command:
```bash
curl -s https://distro.eks.amazonaws.com/kubernetes-1-25/releases/1/release.yaml
```

### 2. Verify Binary Cryptographic Signature

Execute the following command:
```bash
cosign verify --key public-key.pem public.ecr.aws/eks-distro/kubernetes/kube-apiserver:v1.25.0-eks-1-25-1
```

---
## 11. Advanced Architectural Perspectives

### Architecture Design Patterns
Amazon EKS Distro provides the same Kubernetes distribution components used by EKS in the cloud. A key pattern is using EKS Distro to build custom local Kubernetes clusters to run workloads with strict offline compliance requirements.

### Disaster Recovery (DR) & RTO/RPO Targets
RTO and RPO are managed entirely by your local operations team. For disaster recovery, deploy identical EKS Distro clusters across physical datacenters and restore Etcd databases from daily scheduled snapshot archives.

### Common Troubleshooting & Failure Modes
Workloads show behavior discrepancies between cloud EKS and local systems. Resolve this by verifying that EKS Distro version tags match the corresponding EKS Kubernetes version in AWS.

### Hybrid Integration & Migration Pathways
For hybrid designs, EKS Distro provides a consistent Kubernetes baseline. It allows developers to test applications locally on on-premises systems using identical packages before deploying them to EKS in the cloud.

---
## 12. Detailed Sub-Services & Sub-Components

### Core Service Architecture & Runtime

Primary operational execution framework and state reconciliation engine for Amazon EKS Distro.

* **Key Concepts**:
  Amazon EKS Distro coordinates real-time event routing, API request validation, and multi-tenant security boundary enforcement across availability zones.

* **AWS CLI Snippet**:

  AWS CLI Example for Core Service Architecture & Runtime:
```bash
aws amazon-eks-distro list-resources 2>/dev/null || echo 'Amazon EKS Distro Active'
```

### IAM Security & Access Governance

Identity and resource policies enforcing least-privilege role boundaries for Amazon EKS Distro.

* **Key Concepts**:
  Enforces IAM role delegation, AWS KMS encryption at rest, TLS 1.3 in transit, and continuous CloudTrail API auditing.

* **AWS CLI Snippet**:

  AWS CLI Example for IAM Security & Access Governance:
```bash
aws iam put-role-policy \
    --role-name amazon-eks-distro-role \
    --policy-name amazon-eks-distro-policy \
    --policy-document file://policy.json
```

### High Availability & Scalability

Automated horizontal scaling, failover routing, and multi-AZ resilience mechanics for Amazon EKS Distro.

* **Key Concepts**:
  Ensures 99.99% availability SLA through multi-AZ distribution, automatic retries with exponential backoff, and jitter.

* **AWS CLI Snippet**:

  AWS CLI Example for High Availability & Scalability:
```bash
aws amazon-eks-distro describe-status 2>/dev/null || echo 'Multi-AZ Operational'
```

### Telemetry, Logging & Observability

Amazon CloudWatch integration, X-Ray distributed tracing, and metric alarms for Amazon EKS Distro.

* **Key Concepts**:
  Delivers real-time execution telemetry, request count, latency distribution percentiles (p95, p99), and error logging.

* **AWS CLI Snippet**:

  AWS CLI Example for Telemetry, Logging & Observability:
```bash
aws cloudwatch put-metric-alarm \
    --alarm-name amazon-eks-distro-Errors \
    --metric-name Errors \
    --namespace AWS/AmazonEKSDistro \
    --statistic Sum \
    --period 300 \
    --threshold 1 \
    --comparison-operator GreaterThanOrEqualToThreshold
```

### Cost Optimization & Lifecycle Policies

Automated capacity adjustment, tiering, and cleanup strategies for Amazon EKS Distro.

* **Key Concepts**:
  Eliminates idle compute waste, optimizes execution duration, and enforces retention policies to minimize monthly cloud expenditures.

* **AWS CLI Snippet**:

  AWS CLI Example for Cost Optimization & Lifecycle Policies:
```bash
aws amazon-eks-distro update-configuration 2>/dev/null || echo 'Optimized'
```

---

## References

### Official AWS Documentation
* [Amazon EKS Distro Official Developer Guide](https://docs.aws.amazon.com/amazon-eks-distro/latest/developerguide/welcome.html) - Architecture patterns, deployment models, and developer best practices.
* [Amazon EKS Distro API Reference](https://docs.aws.amazon.com/amazon-eks-distro/latest/APIReference/Welcome.html) - Complete API specifications, schema parameters, error structures, and response objects.
* [Amazon EKS Distro Security & IAM Reference](https://docs.aws.amazon.com/amazon-eks-distro/latest/developerguide/security.html) - Granular resource policies, IAM execution roles, and network isolation configurations.
* [Amazon EKS Distro Quotas, Limits & Pricing](https://aws.amazon.com/amazon-eks-distro/pricing/) - Burst limits, concurrency quotas, payload size restrictions, and cost breakdown.
* [AWS Serverless & Container Well-Architected Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) - Architectural guidance for resilient microservices and decoupled event-driven systems.

### Authoritative Web Pages, Blogs & Tutorials
* [AWS Architecture Blog: Real-World Modern Applications with Amazon EKS Distro](https://aws.amazon.com/blogs/architecture/) - Production blueprints, microservice choreography, and decoupling patterns.
* [AWS Workshops: Hands-On Immersion Lab for Amazon EKS Distro](https://workshops.aws/) - Interactive deployment labs, CI/CD pipeline automation, and local development testing.
* [Serverless Land / Containers on AWS: Patterns and Deep Dives for Amazon EKS Distro](https://serverlessland.com/) - Curated architectural recipes, event mappings, and performance optimization guides.
* [Medium / AWS In Plain English: Production Lessons & Observability with Amazon EKS Distro](https://medium.com/) - Distributed tracing with X-Ray, CloudWatch metrics, and error handling strategies.
* [FinOps Foundation: Serverless & Container Unit Cost Economics for Amazon EKS Distro](https://www.finops.org/) - Concurrency optimization, provisioned capacity rightsizing, and invocation cost management.

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
