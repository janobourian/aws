# AWS Topic: Amazon ECR
**Category:** Containers
**Status:** ✅ Completed

---

## 1. High-Level Overview
Amazon Elastic Container Registry (ECR) is a serverless, fully managed container registry service designed to make it incredibly easy for developers to share, manage, and deploy Docker container images, Open Container Initiative (OCI) images, and related artifacts. In modern application architectures, packaging code as container images is the standard practice. Storing and distributing these images across distributed container clusters require highly available registries that scale compute and network bandwidth dynamically. Self-hosting registries requires provisioning storage volumes, configuring registry software, managing access control lists, and scaling ingress/egress bandwidth, which increases administrative overhead. Amazon ECR eliminates these challenges by operating as a managed service.

The service provides deep integrations with Amazon ECS, EKS, and AWS Identity and Access Management (IAM), simplifying the container deployment lifecycle. ECR automatically stores image layers in Amazon S3, ensuring massive durability and scalability. When an ECS task or EKS pod starts, ECR delivers the container image over high-bandwidth AWS network pathways. ECR supports both private repositories (for internal corporate deployments) and public repositories (via ECR Public Gallery, allowing developers to share container images globally). By offering built-in features such as image vulnerability scanning, lifecycle policies, and cross-region repository replication, ECR streamlines container deployment workflows.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Provides enterprise-grade cloud capabilities for **Amazon ECR**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts
Amazon ECR manages container images. Key concepts include:
* **Registry**: The central host account container storage repository.
* **Repository**: A logical collection of related container images (e.g., `web-app` or `database`).
* **Image Tag**: Labels that identify specific image versions (e.g., `latest` or `v1.0`).
* **Image Scanning**: Automate vulnerability scan checks on container layers.
* **Pull-Through Cache**: Cache external public images inside your private repository automatically.

---

## 3. Common Use Cases
* **Secure Enterprise Repository**: Storing proprietary application Docker images privately and restricting access via IAM.
* **CI/CD Build Delivery**: Automatically pushing newly built images from Jenkins or GitHub Actions to ECR, and triggering ECS deployments.
* **Public Software Distribution**: Sharing open-source container images globally using ECR Public Gallery.
* **Registry Mirroring**: Caching common third-party images (like Nginx or Redis) internally to prevent Docker Hub rate limits.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)
* ⚠️ **Key Constraints**: ECR authorization tokens expire after 12 hours. Data transfer out to the internet incurs standard charges (free to EC2/ECS/EKS in the same region).
* 🔒 **Security & Encryption**: Supports KMS encryption at rest. Repository policies manage cross-account permissions.
* ⚙️ **Performance/Scaling**: Integrates directly with S3 to scale storage and retrieval bandwidth automatically.

---

## 5. Comparison with Similar Services
| Registry Service | Hosting Model | Authentication Model | Key Advantage |
| :--- | :--- | :--- | :--- |
| **Amazon ECR** | Managed AWS Service | IAM Integration | Native ECS/EKS credentials integration |
| **Docker Hub** | SaaS Registry | Username/Password, Access Tokens | Largest public repository collection |
| **Self-Hosted Registry** | EC2 / Kubernetes | Custom certificates | Custom network isolation controls |
| **GitHub Packages** | SaaS Registry | GitHub Personal Access Tokens | Integrated with GitHub repository workflows |

---

## 6. Cost Optimization
Optimize ECR costs by:
* Creating Lifecycle Policies to automatically delete untagged or old development images.
* Compressing images using multi-stage builds and minimal base layers.
* Centralizing repositories to avoid duplicate storage costs across accounts.

---

## 7. In-Depth Perspectives

### Security Perspective
Security configuration in Amazon ECR is critical because container registries store core intellectual property and operational application packages. The security model leverages AWS IAM, resource-based policies, vulnerability scanning, and storage encryption. Access to pull or push images is governed by IAM, restricting API actions like `ecr:GetDownloadUrlForLayer`, `ecr:BatchGetImage`, and `ecr:PutImage`. ECR uses **Repository Policies** (resource-based policies) to grant cross-account access, ensuring that only trusted developer accounts can pull images from a central registry.

To secure container deployments against vulnerabilities, ECR supports **Image Scanning**. ECR integrates with Clair and AWS Inspector to automatically scan container images on push or on a schedule. The scan results identify software vulnerabilities (CVEs), allowing developers to patch images before deploying them to production.

Data protection at rest is enforced using customer-managed AWS KMS keys, which encrypt all image layers stored in the S3 backend. In transit, all registry push/pull operations and API communications are secured using TLS 1.2 or 1.3 HTTPS. Auditing is managed via AWS CloudTrail, which logs registry logins (`GetAuthorizationToken`) and repository modifications, providing complete transparency for security compliance audits.

### High Availability Perspective
High Availability (HA) for Amazon ECR is achieved through S3 storage replication, globally distributed registry endpoints, and cross-region replication. Because ECR is serverless, there are no registry servers to manage. The service's data layer stores container images in S3, which provides 99.99% availability by replicating files across multiple Availability Zones in the region.

To ensure high availability across multiple AWS regions, ECR supports **Cross-Region Replication (CRR)**. CRR automatically duplicates container images pushed to a primary repository to destination repositories in secondary regions. If a regional AWS network outage occurs, EC2 instances or container tasks in secondary regions can pull images locally from their regional ECR repositories, preventing deployment halts.

Additionally, ECR manages registry login tokens. The `GetAuthorizationToken` API provides a secure, temporary authorization token valid for 12 hours. By combining Multi-AZ S3 storage, cross-region replication, and highly available regional endpoints, Amazon ECR provides a highly available, robust container registry platform.

### Resilience Perspective
Resilience in Amazon ECR focuses on image durability, pull-through caching, and disaster recovery. ECR relies on S3 to store image layers, providing 11 9s of durability. To maintain operational resilience, repository configurations, replication rules, and lifecycle policies should be managed as code using CloudFormation or Terraform.

To build a resilient container deployment pipeline, developers should configure **Pull-Through Cache Rules**. Pull-through cache rules allow ECR to automatically mirror and cache container images from external registries (such as Docker Hub, Quay.io, or Kubernetes Registry) inside your private ECR repository. If the external registry experiences an outage, container tasks can continue pulling cached images from ECR.

To manage API throttling and registry login timeouts, clients must implement retries. If the `docker login` or `aws ecr` API fails due to rate limits, tools should implement exponential backoff with jitter. Using Amazon EventBridge, administrators can monitor ECR events (such as image scan completions or push events) and trigger automated Slack notifications or build pipelines, ensuring overall resilience.

### Cost Optimizing Perspective
Cost Optimization for Amazon ECR involves managing storage volumes, data transfer fees, and repository lifecycles. ECR is highly cost-effective, charging based on data stored ($0.10 per GB-month) and data transfer. However, in active CI/CD pipelines where new container images are pushed multiple times a day, historical image layers can accumulate rapidly, running up massive storage bills. To optimize these costs, architects must implement **ECR Lifecycle Policies**. Lifecycle policies should be configured to automatically delete untagged images, old development builds (e.g. retaining only the 10 most recent builds), or images older than a set number of days.

Additionally, minimizing container image sizes is essential. Developers should use multi-stage Docker builds and minimal base images (such as Alpine Linux or Distroless) to reduce container sizes. Smaller images reduce ECR storage costs and speed up deployment download times, saving compute costs.

Another cost optimization strategy is utilizing private registry caching. By pulling images locally within the AWS network, developers avoid public internet egress charges. Utilizing AWS Budgets allows setting cost alerts to notify when ECR storage costs exceed allocations, ensuring that registry costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment
* **Cost Optimization (Pillar 5)**: Charges only for storage used, and lowers costs via automated lifecycle deletion rules.
* **Security (Pillar 2)**: Integrates with AWS Inspector for automated vulnerability scanning, securing software delivery.
* **Operational Excellence (Pillar 1)**: Automates repository management, removing the need to patch registry servers.

---

## 9. Hands-On Walkthrough
### Create Private ECR Repository and Push a Docker Image
1. Open the **AWS Console** and search for **ECR**.
2. Click **Create repository**:
   * **Visibility**: Private.
   * **Repository name**: `my-web-app`.
   * **Tag immutability**: Enabled (Recommended to prevent tag overwriting).
   * **Scan on push**: Enabled. Click **Create repository**.
3. Authenticate your local Docker client (replace region and account ID):
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
   ```
4. Build your local Docker image:
   ```bash
   docker build -t my-web-app .
   ```
5. Tag and push the image to ECR:
   ```bash
   docker tag my-web-app:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-web-app:latest
   docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-web-app:latest
   ```

---

## 10. AWS CLI Commands
### 1. Create a Repository

Execute the following command:
```bash
aws ecr create-repository \
    --repository-name "my-service"
```

### 2. Put Lifecycle Policy

Save policy as `policy.json`:
```json
{
  "rules": [
    {
      "rulePriority": 1,
      "description": "Delete untagged images older than 14 days",
      "selection": {
        "tagStatus": "untagged",
        "countType": "sinceImagePushed",
        "countUnit": "days",
        "countNumber": 14
      },
      "action": {
        "type": "expire"
      }
    }
  ]
}
```
Execute the command:

Execute the following command:
```bash
aws ecr put-lifecycle-policy \
    --repository-name "my-service" \
    --lifecycle-policy-text file://policy.json
```

### 3. Describe Image Scan Findings

Execute the following command:
```bash
aws ecr describe-image-scan-findings \
    --repository-name "my-service" \
    --image-id imageTag="latest"
```

---
## 11. Advanced Architectural Perspectives

### Architecture Design Patterns
Amazon ECR acts as the registry for containerized workloads. A common architectural pattern is linking ECR with AWS CodePipeline and ECS/EKS to automate continuous delivery, using ECR Image Scanning on push to run static vulnerability checks before deployment.

### Disaster Recovery (DR) & RTO/RPO Targets
ECR is serverless and highly available, storing images in S3 across multiple AZs natively (RPO of zero). To achieve cross-region disaster recovery, configure **Replication Rules** in ECR to copy images automatically to a registry in a standby region (RTO of ~5 minutes).

### Common Troubleshooting & Failure Modes
Container pull failures on EC2/Fargate occur due to missing permissions (`ImagePullBackOff`). Fix this by verifying the ECS task execution role contains the policy `AmazonEC2ContainerRegistryReadOnly` and public network routing is active.

### Hybrid Integration & Migration Pathways
Support hybrid container deployments by using ECR with on-premises servers. Authenticate local Docker daemons using the AWS CLI and pull images over a secure VPN or Direct Connect private network connection.

---
## 12. Detailed Sub-Services & Sub-Components

### Private & Public Repositories

High-performance Docker/OCI compliant container image registries stored durably in Amazon S3.

* **Key Concepts**:
  Repositories support semantic tagging, tag immutability (preventing malicious image overwrites), and cross-region/cross-account replication.

* **AWS CLI Snippet**:

  AWS CLI Example for Private & Public Repositories:
```bash
aws ecr create-repository \
    --repository-name payment-service \
    --image-tag-mutability IMMUTABLE \
    --image-scanning-configuration scanOnPush=true
```

### Image Scanning & Security

Automated vulnerability scanning powered by Amazon Inspector for Common Vulnerabilities and Exposures (CVEs).

* **Key Concepts**:
  Basic scanning uses the open-source Clair engine; Enhanced scanning leverages Amazon Inspector to continuously scan container layers against vulnerability databases.

* **AWS CLI Snippet**:

  AWS CLI Example for Image Scanning & Security:
```bash
aws ecr describe-image-scan-findings \
    --repository-name payment-service \
    --image-id imageTag=latest
```

### Lifecycle Policies

Automated cleanup rules preventing registry bloat by expiring untagged or outdated container images.

* **Key Concepts**:
  Lifecycle policies retain only the latest N images or expire images older than specified days, optimizing ECR storage costs.

* **AWS CLI Snippet**:

  AWS CLI Example for Lifecycle Policies:
```bash
aws ecr put-lifecycle-policy \
    --repository-name payment-service \
    --lifecycle-policy-text '{"rules":[{"rulePriority":1,"description":"Retain last 10 images","selection":{"tagStatus":"any","countType":"imageCount","countNumber":10},"action":{"type":"expire"}}]}'
```

---

## References

### Official AWS Documentation
* [Amazon ECR Official Developer Guide](https://docs.aws.amazon.com/amazon-ecr/latest/developerguide/welcome.html) - Architecture patterns, deployment models, and developer best practices.
* [Amazon ECR API Reference](https://docs.aws.amazon.com/amazon-ecr/latest/APIReference/Welcome.html) - Complete API specifications, schema parameters, error structures, and response objects.
* [Amazon ECR Security & IAM Reference](https://docs.aws.amazon.com/amazon-ecr/latest/developerguide/security.html) - Granular resource policies, IAM execution roles, and network isolation configurations.
* [Amazon ECR Quotas, Limits & Pricing](https://aws.amazon.com/amazon-ecr/pricing/) - Burst limits, concurrency quotas, payload size restrictions, and cost breakdown.
* [AWS Serverless & Container Well-Architected Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) - Architectural guidance for resilient microservices and decoupled event-driven systems.

### Authoritative Web Pages, Blogs & Tutorials
* [AWS Architecture Blog: Real-World Modern Applications with Amazon ECR](https://aws.amazon.com/blogs/architecture/) - Production blueprints, microservice choreography, and decoupling patterns.
* [AWS Workshops: Hands-On Immersion Lab for Amazon ECR](https://workshops.aws/) - Interactive deployment labs, CI/CD pipeline automation, and local development testing.
* [Serverless Land / Containers on AWS: Patterns and Deep Dives for Amazon ECR](https://serverlessland.com/) - Curated architectural recipes, event mappings, and performance optimization guides.
* [Medium / AWS In Plain English: Production Lessons & Observability with Amazon ECR](https://medium.com/) - Distributed tracing with X-Ray, CloudWatch metrics, and error handling strategies.
* [FinOps Foundation: Serverless & Container Unit Cost Economics for Amazon ECR](https://www.finops.org/) - Concurrency optimization, provisioned capacity rightsizing, and invocation cost management.

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
