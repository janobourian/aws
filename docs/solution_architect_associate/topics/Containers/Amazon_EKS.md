# AWS Topic: Amazon EKS
**Category:** Containers
**Status:** ✅ Completed

---

## 1. High-Level Overview
Amazon Elastic Kubernetes Service (EKS) is a managed Kubernetes service designed to simplify the deployment, operation, and scaling of Kubernetes clusters in the AWS Cloud. Kubernetes is the open-source industry standard for container orchestration, but deploying and managing self-managed Kubernetes clusters on-premises or on EC2 instances introduces significant complexity. Administrators must manually manage ZooKeeper/etcd databases, coordinate API master nodes across subnets, provision local storage volumes, configure secure networking plugins, and handle rolling software updates. Amazon EKS eliminates this operational burden by managing the Kubernetes control plane.

The service automatically provisions and scales the Kubernetes API servers and etcd database across three Availability Zones to ensure high availability. EKS supports multiple node deployment types: **Managed Node Groups** (where EKS handles EC2 provisioning and patching), self-managed node groups, and serverless container execution via **AWS Fargate profiles**. EKS integrates with AWS IAM for user authentication and AWS KMS for secret encryption. By managing the Kubernetes control plane and integrating with native AWS services (such as ALBs via the AWS Load Balancer Controller and S3 for persistent storage), Amazon EKS enables organizations to run standard, enterprise-grade Kubernetes workloads with minimal administrative overhead.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Provides a fully managed Kubernetes environment, allowing organizations to run standard containerized workloads on AWS without the operational burden of managing the Kubernetes master control plane.
* **How It Works**: Automatically manages master node availability, etcd storage, upgrades, and security patching across multiple availability zones, ensuring 100% standard open-source Kubernetes compatibility.
* **Key Business Value & Use Cases**: Enables multi-cloud portability, runs enterprise container fleets at scale, and eliminates control-plane maintenance headaches for DevOps teams.

## 2. Core Architecture & Key Concepts
Amazon EKS manages Kubernetes clusters. Key concepts include:
* **Control Plane**: The managed Kubernetes master nodes (API server, etcd, controller manager).
* **Managed Node Group**: The collection of EC2 worker nodes managed and patched by AWS.
* **IRSA**: IAM Roles for Service Accounts, mapping AWS IAM roles to Kubernetes pods.
* **VPC CNI Plugin**: The networking plugin that assigns native VPC IP addresses to Kubernetes pods.
* **Karpenter**: A high-performance Kubernetes node autoscaling agent built for AWS.

---

## 3. Common Use Cases
* **Multi-Cloud Application Ingestion**: Hosting containerized microservices on EKS to maintain API compatibility with on-premises Kubernetes environments.
* **Highly Scaling Containerized APIs**: Deploying web applications on EKS clusters that scale dynamically based on request traffic.
* **Enterprise Microservices Architecture**: Coordinating communication between hundreds of internal services using Kubernetes service mesh.
* **Machine Learning Pipelines**: Running parallel training jobs on EKS clusters equipped with GPU compute nodes.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)
* ⚠️ **Key Constraints**: EKS control plane fee is $0.10/hour. Pod IP allocation is limited by the EC2 instance type's ENI capacity (requires warm pool management).
* 🔒 **Security & Encryption**: Requires KMS configuration to encrypt Kubernetes secrets in etcd. IRSA is recommended for pod access control.
* ⚙️ **Performance/Scaling**: Recommend Karpenter and VPC CNI for highly scaling workloads.

---

## 5. Comparison with Similar Services
| Service | API Compatibility | Control Plane Management | Setup Complexity |
| :--- | :--- | :--- | :--- |
| **Amazon EKS** | Standard Kubernetes | Managed by AWS ($0.10/hr) | High |
| **Amazon ECS** | AWS Native ECS | Managed by AWS (Free) | Low |
| **AWS App Runner** | Serverless Container | Managed by AWS | Low (Zero config) |
| **Fargate Profile** | Kubernetes / ECS | Managed by AWS | Medium |

---

## 6. Cost Optimization
Optimize EKS costs by:
* Deploying Karpenter for high-performance node consolidation.
* Utilizing Spot Instances for stateless pod workloads.
* Using Graviton-based EC2 instance families for worker nodes.
* Deploying Fargate profiles for serverless pod execution.

---

## 7. In-Depth Perspectives

### Security Perspective
Security configuration in Amazon EKS is critical because Kubernetes API endpoints are public by default and interact with backend resources. EKS implements a multi-layered security model spanning network isolation, identity authentication, pod security, and encryption. Access to the Kubernetes API is managed using **IAM Identity Association for Service Accounts (IRSA)**. IRSA allows mapping IAM roles directly to Kubernetes Service Accounts, granting fine-grained AWS permissions (e.g. read access to an S3 bucket) to specific pods rather than sharing permissions across the entire worker node, adhering to the principle of least privilege.

To secure cluster networking, EKS utilizes the Amazon VPC CNI plugin. VPC CNI assigns a dedicated private IP address from your VPC CIDR to every pod. This allows applying standard VPC Security Groups directly to pods. To isolate pod-to-pod communications, Kubernetes **Network Policies** (using plugins like Calico) should be implemented.

Data protection at rest is enforced using customer-managed AWS KMS keys. KMS encrypts all Kubernetes Secrets (such as API keys and passwords) stored within the etcd database. In transit, all communications between the API server, worker nodes, and client tools (like `kubectl`) are encrypted using TLS 1.2 or 1.3. Auditing is managed via AWS CloudTrail, which logs EKS cluster API calls, and EKS Control Plane Logging, which writes Kubernetes audit and authenticator logs directly to CloudWatch Logs, ensuring complete compliance auditability.

### High Availability Perspective
High Availability (HA) for Amazon EKS is built into its managed control plane and Multi-AZ node distribution. EKS automatically provisions and runs a highly available Kubernetes control plane across three Availability Zones within the active AWS region. The API servers and etcd database nodes are distributed evenly to prevent localized failures. If a zone experiences an outage, the control plane fails over automatically, and client tools continue to execute commands using active API nodes.

To ensure high availability of the data plane, worker nodes must be distributed across subnets spanning multiple Availability Zones. When using Managed Node Groups, EKS automatically balances the EC2 instances across the defined subnets.

For serverless execution, Fargate profiles provision container resources across multiple zones natively, handling hardware failovers transparently. Additionally, to distribute incoming traffic across the pods, EKS integrates with Application Load Balancers via the AWS Load Balancer Controller. If a pod fails health checks, the ALB stops routing traffic to it, and Kubernetes automatically schedules a replacement pod on a healthy node in an active zone. By combining Multi-AZ control plane replication, Multi-AZ node groups, and ALB target group routing, Amazon EKS provides a highly available, robust Kubernetes platform.

### Resilience Perspective
Resilience in Amazon EKS focuses on pod self-healing, node recovery, API rate limit tolerance, and disaster recovery. Kubernetes clusters possess built-in self-healing capabilities: if a container crashes, the kubelet agent on the node automatically restarts the container. If a worker node fails, the Kubernetes scheduler automatically reschedules the affected pods on healthy nodes in active zones, maintaining the desired replica count.

To maintain operational resilience, cluster configurations and deployments should be managed as code using Helm charts, CloudFormation, or Terraform. This allows rapid recovery of the cluster structure in a secondary region. Because the workloads should be stateless, storing raw user data in S3 and utilizing RDS for database storage ensures that the Recovery Time Objective (RTO) is minimal, and the Recovery Point Objective (RPO) is zero.

To handle cluster scaling and node limits during traffic spikes, EKS integrates with **Karpenter** or the Kubernetes Cluster Autoscaler. Karpenter analyzes unscheduled pods and programmatically provisions the optimal EC2 instance types and counts, reducing scaling latency. Ingestion scripts must implement exponential backoff with jitter to handle API rate limits. Using EventBridge, administrators can monitor EKS cluster state changes and trigger automated notifications or failover workflows, maintaining a highly resilient application architecture.

### Cost Optimizing Perspective
Cost Optimization for Amazon EKS involves choosing the right node group types, utilizing Karpenter for scaling, and managing storage allocations. EKS charges a flat hourly fee for running the managed control plane ($0.10 per hour per cluster). You also pay for the underlying compute resources (EC2 or Fargate) consumed by your worker nodes. To optimize these costs, architects should use **Karpenter** for node autoscaling. Karpenter automatically consolidates underutilized pods onto fewer EC2 instances and terminates empty nodes, reducing compute charges by up to 50% compared to traditional scaling tools.

Additionally, implementing Spot Instances within Managed Node Groups is critical. Spot instances offer up to 90% savings compared to standard On-Demand pricing, making them ideal for stateless, fault-tolerant Kubernetes deployments. For compute-heavy workloads, Graviton-based EC2 instance families provide better price-performance than standard x86 processors.

Another cost optimization strategy is rightsizing pod resources. Developers should analyze container resource utilization using tools like Prometheus or CloudWatch Container Insights and adjust pod CPU and memory requests to match actual usage, avoiding over-provisioning worker nodes. Utilizing AWS Budgets allows setting cost alerts to notify when compute spending exceeds allocations, ensuring that hosting costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment
* **Cost Optimization (Pillar 5)**: Integrates with Karpenter to adjust capacity based on demand, eliminating compute waste.
* **Operational Excellence (Pillar 1)**: Automates Kubernetes master patching and scaling, reducing operational overhead.
* **Reliability (Pillar 6)**: Replicates control plane nodes across 3 Availability Zones, protecting against localized outages.

---

## 9. Hands-On Walkthrough
### Deploy a Sample Application on Amazon EKS
1. Open the **AWS Console** and search for **EKS**.
2. Create an EKS cluster using `eksctl` tool (executed from client EC2):
   ```bash
   eksctl create cluster        --name "ProductionEKS"        --region "us-east-1"        --nodegroup-name "standard-nodes"        --node-type "t3.medium"        --nodes 2        --nodes-min 1        --nodes-max 3        --managed
   ```
3. Once active (~15 minutes), configure `kubectl` locally:
   ```bash
   aws eks update-kubeconfig --name ProductionEKS --region us-east-1
   ```
4. Create a sample deployment:
   ```yaml
   # Save as deployment.yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx-deployment
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: web
     template:
       metadata:
         labels:
           app: web
       spec:
         containers:
         - name: nginx
           image: nginx:latest
           ports:
           - containerPort: 80
   ```
5. Apply the deployment:
   ```bash
   kubectl apply -f deployment.yaml
   ```

---

## 10. AWS CLI Commands
### 1. Create EKS Cluster

Execute the following command:
```bash
aws eks create-cluster \
    --name "ProductionEKS" \
    --role-arn "arn:aws:iam::123456789012:role/EKSClusterRole" \
    --resources-vpc-config subnetIds="subnet-12345,subnet-67890"
```

### 2. Describe Cluster Details

Execute the following command:
```bash
aws eks describe-cluster \
    --name "ProductionEKS"
```

### 3. List Clusters

Execute the following command:
```bash
aws eks list-clusters
```

---
## 11. Advanced Architectural Perspectives

### Architecture Design Patterns
Amazon EKS provides managed Kubernetes clusters. A standard design pattern is deploying EKS in three private subnets across multiple AZs, using Karpenter or Cluster Autoscaler to launch EC2 nodes dynamically based on pod resource requests.

### Disaster Recovery (DR) & RTO/RPO Targets
EKS clusters require backing up Kubernetes configurations (Helm charts, manifest files). For disaster recovery, deploy an EKS cluster in a standby region, using git-based CI/CD (ArgoCD) to synchronize workloads (RTO under 15 minutes).

### Common Troubleshooting & Failure Modes
Pods fail to communicate across different nodes due to VPC IP exhaustion. Resolve this by configuring the AWS VPC CNI plug-in to allocate secondary IP CIDRs or implementing custom subnet configurations.

### Hybrid Integration & Migration Pathways
Run hybrid Kubernetes clusters by deploying **Amazon EKS Anywhere**. EKS Anywhere lets you create and run Kubernetes clusters locally on your own infrastructure (such as VMware vSphere) managed using AWS tools.

---
## 12. Detailed Sub-Services & Sub-Components

### EKS Control Plane & Clusters

Fully managed Kubernetes master nodes running across 3 Availability Zones with automated API server scaling.

* **Key Concepts**:
  AWS manages the Kubernetes control plane (etcd, kube-apiserver, kube-controller-manager) with 99.95% availability SLA and zero-downtime version upgrades.

* **AWS CLI Snippet**:

  AWS CLI Example for EKS Control Plane & Clusters:
```bash
aws eks create-cluster \
    --name prod-cluster \
    --role-arn arn:aws:iam::123456789012:role/EKSClusterRole \
    --resources-vpc-config subnetIds=subnet-1a,subnet-1b,securityGroupIds=sg-eks
```

### Managed Node Groups & Fargate Profiles

Automated worker node provisioning with automated AMI patching, health checks, and spot instance scaling.

* **Key Concepts**:
  Managed Node Groups run on EC2 instances inside your VPC with automatic draining during upgrades; EKS Fargate profiles run pods without any EC2 instance management.

* **AWS CLI Snippet**:

  AWS CLI Example for Managed Node Groups & Fargate Profiles:
```bash
aws eks create-nodegroup \
    --cluster-name prod-cluster \
    --nodegroup-name worker-nodes \
    --node-role arn:aws:iam::123456789012:role/EKSNodeRole \
    --subnets subnet-1a subnet-1b \
    --scaling-config minSize=2,maxSize=10,desiredSize=4
```

### IAM Roles for Service Accounts (IRSA)

Fine-grained pod-level AWS IAM permission mapping using OIDC federated identity authentication.

* **Key Concepts**:
  IRSA injects temporary AWS STS credentials directly into Kubernetes pods using an OpenID Connect (OIDC) identity provider, replacing dangerous node-level IAM instance profiles.

* **AWS CLI Snippet**:

  AWS CLI Example for IAM Roles for Service Accounts (IRSA):
```bash
aws eks update-kubeconfig \
    --region us-east-1 \
    --name prod-cluster
```

---

## References

### Official AWS Documentation
* [Amazon EKS Official Developer Guide](https://docs.aws.amazon.com/amazon-eks/latest/developerguide/welcome.html) - Architecture patterns, deployment models, and developer best practices.
* [Amazon EKS API Reference](https://docs.aws.amazon.com/amazon-eks/latest/APIReference/Welcome.html) - Complete API specifications, schema parameters, error structures, and response objects.
* [Amazon EKS Security & IAM Reference](https://docs.aws.amazon.com/amazon-eks/latest/developerguide/security.html) - Granular resource policies, IAM execution roles, and network isolation configurations.
* [Amazon EKS Quotas, Limits & Pricing](https://aws.amazon.com/amazon-eks/pricing/) - Burst limits, concurrency quotas, payload size restrictions, and cost breakdown.
* [AWS Serverless & Container Well-Architected Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) - Architectural guidance for resilient microservices and decoupled event-driven systems.

### Authoritative Web Pages, Blogs & Tutorials
* [AWS Architecture Blog: Real-World Modern Applications with Amazon EKS](https://aws.amazon.com/blogs/architecture/) - Production blueprints, microservice choreography, and decoupling patterns.
* [AWS Workshops: Hands-On Immersion Lab for Amazon EKS](https://workshops.aws/) - Interactive deployment labs, CI/CD pipeline automation, and local development testing.
* [Serverless Land / Containers on AWS: Patterns and Deep Dives for Amazon EKS](https://serverlessland.com/) - Curated architectural recipes, event mappings, and performance optimization guides.
* [Medium / AWS In Plain English: Production Lessons & Observability with Amazon EKS](https://medium.com/) - Distributed tracing with X-Ray, CloudWatch metrics, and error handling strategies.
* [FinOps Foundation: Serverless & Container Unit Cost Economics for Amazon EKS](https://www.finops.org/) - Concurrency optimization, provisioned capacity rightsizing, and invocation cost management.

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
