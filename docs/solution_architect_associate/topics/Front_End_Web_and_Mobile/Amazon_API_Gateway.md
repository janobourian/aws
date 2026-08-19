# AWS Topic: Amazon API Gateway

**Category:** Front-End Web and Mobile
**Status:** ✅ Completed

---

## 1. High-Level Overview

Amazon API Gateway is a fully managed, serverless API service designed to enable developers to create, publish, maintain, monitor, and secure APIs at any scale. In modern application architectures, exposing internal backend compute resources (such as AWS Lambda, Amazon ECS container tasks, or RDS databases) directly to the public internet introduces security risks and high management overhead. Amazon API Gateway addresses these challenges by operating as a secure entry gate. It handles up to hundreds of thousands of concurrent API calls, manages traffic routing, translates payloads, and enforces rate limits.

API Gateway supports three primary API types: **REST APIs** (highly customizable, feature-rich HTTP endpoints supporting request/response models and VTL mappings), **HTTP APIs** (faster, lightweight APIs designed for serverless backend proxies at lower cost), and **WebSocket APIs** (enabling persistent, bidirectional, and real-time communication channels). By managing security authorization, CORS policies, response caching, and client API keys, Amazon API Gateway decouples frontend client applications from backend serverless microservices.

### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)

* **Business Purpose**: Provides enterprise-grade cloud capabilities for **Amazon API Gateway**, streamlining operations, reducing infrastructure overhead, and enabling rapid digital innovation.
* **How It Works**: Operates as a fully managed AWS cloud service, handling underlying operational complexities, high-availability replication, security compliance, and automated scaling behind simple API interfaces.
* **Key Business Value & Use Cases**: Reduces operational overhead and time-to-market for digital initiatives, enforces enterprise security standards, and aligns cloud spending with actual business usage.

## 2. Core Architecture & Key Concepts

Amazon API Gateway manages serverless APIs. Key concepts include:

* **Resource and Method**: The path (e.g. `/orders`) and HTTP verb (e.g. `POST`) defined in the API.
* **Stage**: The deployment environment (e.g., `prod` or `dev`) with its own endpoints.
* **Usage Plan**: A configuration that binds API keys to throttling limits and quotas.
* **Integration Request**: The translation mapping that formats incoming payloads before sending to backends.
* **VPC Link**: Secure proxy interface that connects API Gateway to private VPC resources.

---

## 3. Common Use Cases

* **Serverless Backend Gateway**: Exposing a public API endpoint to route client requests to backend Lambda functions.
* **Microservices Aggregator**: Using a single API Gateway endpoint to route requests to multiple independent ECS services.
* **Real-time Chat APIs**: Building a persistent chat backend using WebSocket APIs to handle bidirectional message flows.
* **Third-Party API Monitization**: Exposing internal database services to external clients using API keys and usage plans.

---

## 4. Exam Essentials (SAA-C03 Cheat Sheet)

* ⚠️ **Key Constraints**: Maximum integration timeout is 29 seconds (cannot be increased). Endpoint configurations (Edge-optimized vs Regional) must be chosen during creation.
* 🔒 **Security & Encryption**: Supports Cognito, IAM, and Lambda authorizers. Integrates with AWS WAF for threat protection.
* ⚙️ **Performance/Scaling**: Scales automatically; default account rate limit is 10,000 requests/sec.

---

## 5. Comparison with Similar Services

| API Service | Key Advantage | Throttling Support | Caching Support |
| :--- | :--- | :--- | :--- |
| **API Gateway REST** | Advanced VTL mapping, API keys, usage plans | Yes | Yes |
| **API Gateway HTTP** | Low latency, low cost ($1.00/M) | Yes | No |
| **Application Load Balancer** | Layer 7 routing (HTTP/HTTPS) | No (requires WAF) | No |
| **AWS AppSync** | GraphQL aggregation, real-time sync | Yes | Yes |

---

## 6. Cost Optimization

## Optimize API Gateway costs by

* Deploying HTTP APIs for simple Lambda/VPC proxies to save 70% compared to REST.
* Utilizing API Gateway Caching to offload backend compute charges.
* Connecting API Gateway directly to DynamoDB using VTL mappings to bypass Lambda.
* Restricting client access using Usage Plans to prevent API abuse.

---

## 7. In-Depth Perspectives

### Security Perspective

Security configuration in Amazon API Gateway is critical since APIs represent the primary public-facing interface to corporate backend systems. The security model leverages IAM policies, Cognito User Pools, custom Lambda Authorizers, and network controls. Access to configure APIs is governed by IAM, while client access is controlled at the resource level:

* **Amazon Cognito User Pools**: Authenticates users using JWT tokens before routing requests.
* **IAM Authorization**: Restricts API calls to AWS users and applications using SigV4 signatures.
* **Lambda Authorizers (Custom)**: Executes a custom Lambda function to validate bearer tokens (e.g. OAuth) and returns an IAM policy.
* **API Keys**: Identifies clients and enforces usage plans (not recommended for strict authentication).

At the network level, API Gateway can integrate with AWS WAF (Web Application Firewall) to block common web exploits (SQL injection, XSS) and restrict access based on IP address. For secure backend integration, API Gateway supports VPC Link, enabling private traffic routing to ALBs or ECS tasks located in private subnets without public endpoints.

Data protection in transit is enforced using TLS 1.2 or 1.3 encryption. Auditing is managed via AWS CloudTrail, which logs administrative API calls, and CloudWatch Logs, which can be configured to capture detailed execution logs (including request parameters and backend response times), providing complete transparency for security compliance audits.

### High Availability Perspective

High Availability (HA) for Amazon API Gateway is built into its serverless, globally distributed routing architecture. The service is deployed across multiple Availability Zones within the active AWS region by default. API Gateway automatically scales to handle incoming request spikes, distributing workloads across serverless proxy nodes running in parallel.

For global deployments, API Gateway supports **Edge-Optimized APIs**. Edge-optimized APIs route traffic automatically through Amazon CloudFront edge locations, reducing latency and providing high availability of static data. If a localized AWS region experiences service degradation, CloudFront can route requests to alternate regions (when using multi-region backends with Route 53 latency routing).

For regional deployments, **Regional APIs** bypass CloudFront and are hosted in the same region, reducing latency for local clients. By combining serverless auto-scaling, Multi-AZ routing, and CloudFront integration, Amazon API Gateway provides a highly available, robust API gateway platform.

### Resilience Perspective

Resilience in Amazon API Gateway focuses on traffic management, API rate limits, response caching, and disaster recovery. To protect backend services (such as Lambda and databases) from being overwhelmed by load spikes (which can cause cascade failures), API Gateway supports **Throttling**. Administrators configure rate limits (requests per second) and burst limits (using the Token Bucket algorithm) at the account level, stage level, or individual API key level.

To handle processing failures, API Gateway supports custom gateway responses and integration timeouts. If a backend Lambda function fails or times out, API Gateway returns a structured error payload to the client.

To optimize performance and reduce backend load, **API Gateway Caching** can be enabled. Caching responses on the API Gateway reduces the number of calls made to backend databases, lowering downstream compute costs. Managing the API configuration, routing resources, and integration models as code using CloudFormation or Terraform templates ensures rapid disaster recovery (DR) of the API structure in a secondary region.

### Cost Optimizing Perspective

Cost Optimization for Amazon API Gateway involves choosing the right API type, monitoring execution counts, and managing response caching. API Gateway pricing is pay-as-you-go, charging per million API calls ($3.50 per million for REST APIs, $1.00 per million for HTTP APIs). While this is highly cost-effective, a poorly designed client application that continuously calls the API can run up significant monthly bills. To optimize these costs, developers should use **HTTP APIs** for simple serverless proxies, which offer up to 70% savings compared to REST APIs.

Additionally, implementing API Gateway Caching is essential. Caching responses on the API Gateway reduces the number of database queries executed on backend data stores (such as DynamoDB and Lambda), lowering downstream compute costs.

Another key cost optimization strategy is using mapping templates (VTL) to connect API Gateway directly to AWS services (such as DynamoDB or SQS) without an intermediate Lambda function, completely eliminating Lambda compute costs for simple write/read integrations. Utilizing AWS Budgets allows setting cost alerts to notify when API Gateway spending exceeds allocations, ensuring that hosting costs remain aligned with the enterprise budget.

---

## 8. AWS Well-Architected Framework Alignment

* **Cost Optimization (Pillar 5)**: Charges per request, eliminating idle gateway costs, and lowers compute costs using direct service integrations.
* **Security (Pillar 2)**: Integrates with Cognito for secure token validation and VPC Link for private network boundaries.
* **Operational Excellence (Pillar 1)**: Simplifies API distribution and deployment stages, reducing custom proxy code.

---

## 9. Hands-On Walkthrough

### Create an HTTP API with Lambda Integration

1. Open the **AWS Console** and search for **API Gateway**.
2. Click **Create API**, select **HTTP API**, click **Build**.
3. **Integrations**: Click **Add integration**, select **Lambda**.
   * **Lambda function**: Choose your target function (e.g., `ProcessOrder`).
4. **API name**: `OrdersAPI`. Click **Next**.
5. **Configure routes**:
   * **Method**: `POST`.
   * **Resource path**: `/orders`.
   * **Integration target**: Select `ProcessOrder` Lambda. Click **Next**.
6. **Configure stages**: Leave as default (`$default` auto-deploy). Click **Next**.
7. Review and click **Create**. API Gateway will output a public URL.
8. Test the POST request using Curl:

   ```bash
   curl -X POST <https://abcd123.execute-api.us-east-1.amazonaws.com/orders> -d '{"orderId":"1"}'
   ```

---

## 10. AWS CLI Commands

### 1. Create a REST API

Execute the following command:

```bash
aws apigateway create-rest-api \
    --name "MyRestAPI"
```

### 2. Get Resources for API

Execute the following command:

```bash
aws apigateway get-resources \
    --rest-api-id "abcd-1234"
```

### 3. Create a Stage Deployment

Execute the following command:

```bash
aws apigateway create-deployment \
    --rest-api-id "abcd-1234" \
    --stage-name "prod"
```

---

## 11. Advanced Architectural Perspectives

### Architecture Design Patterns

Amazon API Gateway is a serverless API host. A standard pattern is deploying API Gateway in front of Lambda functions, configuring custom domains, usage plans, and API keys to manage and throttle customer traffic.

### Disaster Recovery (DR) & RTO/RPO Targets

API Gateway is serverless and highly available across all AZs. For cross-region disaster recovery, deploy APIs in primary and standby regions, using Route 53 latency routing or CloudFront CDN to route API queries (RTO under 5 minutes).

### Common Troubleshooting & Failure Modes

Queries return `504 Gateway Timeout` when backend Lambda functions take longer than the API Gateway limit (29 seconds). Fix this by optimizing Lambda code, or executing tasks asynchronously using SQS.

### Hybrid Integration & Migration Pathways

Expose local APIs safely by using API Gateway private integrations. API Gateway routes requests to local servers privately over Direct Connect virtual connections using private ALB targets.

---

## 12. Detailed Sub-Services & Sub-Components

### REST, HTTP & WebSocket APIs

Fully managed front-door routing endpoints managing traffic authentication, throttling, and protocol transformation.

* **Key Concepts**:
  HTTP APIs provide low-latency, low-cost proxy routing (up to 70% cheaper); REST APIs offer enterprise features (WAF, request validation, usage plans, API keys); WebSocket APIs enable real-time bidirectional communication.

* **AWS CLI Snippet**:

  AWS CLI Example for REST, HTTP & WebSocket APIs:

```bash
aws apigatewayv2 create-api \
    --name ModernHTTPGateway \
    --protocol-type HTTP \
    --target http://internal-alb-12345.us-east-1.elb.amazonaws.com
```

### Authorizers & Security

Authentication gateways securing API requests via IAM, Cognito User Pools, or Custom Lambda Authorizers.

* **Key Concepts**:
  Lambda Authorizers validate Bearer tokens or request headers, returning generated IAM policy documents. Cognito Authorizers validate JWT access tokens seamlessly.

* **AWS CLI Snippet**:

  AWS CLI Example for Authorizers & Security:

```bash
aws apigateway create-authorizer \
    --rest-api-id abc123def4 \
    --name CognitoAuth \
    --type COGNITO_USER_POOLS \
    --provider-arns arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_abcdef123
```

### Usage Plans & API Keys

Throttling, rate-limiting, and quota enforcement policies applied to external API consumers.

* **Key Concepts**:
  Defines request burst limits (Token Bucket algorithm), steady-state rate limits (requests per second), and monthly quota limits per API key.

* **AWS CLI Snippet**:

  AWS CLI Example for Usage Plans & API Keys:

```bash
aws apigateway create-usage-plan \
    --name BronzeTier \
    --throttle burstLimit=100,rateLimit=50 \
    --quota limit=10000,period=MONTH
```

---

## References

### Official AWS Documentation

* [Amazon API Gateway Official Developer Guide](https://docs.aws.amazon.com/amazon-api-gateway/latest/developerguide/welcome.html) - Architecture patterns, deployment models, and developer best practices.
* [Amazon API Gateway API Reference](https://docs.aws.amazon.com/amazon-api-gateway/latest/APIReference/Welcome.html) - Complete API specifications, schema parameters, error structures, and response objects.
* [Amazon API Gateway Security & IAM Reference](https://docs.aws.amazon.com/amazon-api-gateway/latest/developerguide/security.html) - Granular resource policies, IAM execution roles, and network isolation configurations.
* [Amazon API Gateway Quotas, Limits & Pricing](https://aws.amazon.com/amazon-api-gateway/pricing/) - Burst limits, concurrency quotas, payload size restrictions, and cost breakdown.
* [AWS Serverless & Container Well-Architected Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) - Architectural guidance for resilient microservices and decoupled event-driven systems.

### Authoritative Web Pages, Blogs & Tutorials

* [AWS Architecture Blog: Real-World Modern Applications with Amazon API Gateway](https://aws.amazon.com/blogs/architecture/) - Production blueprints, microservice choreography, and decoupling patterns.
* [AWS Workshops: Hands-On Immersion Lab for Amazon API Gateway](https://workshops.aws/) - Interactive deployment labs, CI/CD pipeline automation, and local development testing.
* [Serverless Land / Containers on AWS: Patterns and Deep Dives for Amazon API Gateway](https://serverlessland.com/) - Curated architectural recipes, event mappings, and performance optimization guides.
* [Medium / AWS In Plain English: Production Lessons & Observability with Amazon API Gateway](https://medium.com/) - Distributed tracing with X-Ray, CloudWatch metrics, and error handling strategies.
* [FinOps Foundation: Serverless & Container Unit Cost Economics for Amazon API Gateway](https://www.finops.org/) - Concurrency optimization, provisioned capacity rightsizing, and invocation cost management.

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
