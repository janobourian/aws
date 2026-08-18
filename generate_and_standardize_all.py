import os
import re
import sqlite3

topics_dir = '/Users/frgonzal/Documents/vit/aws/docs/solution_architect_associate/topics'
db_path = '/Users/frgonzal/Fluxfox/nocodb/noco.db'

finops_text_block = """## FinOps

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

By embedding these FinOps practices into the daily workflow for each service, you can achieve sustainable cost savings while preserving the reliability, security, and performance expected from AWS."""

# Define the 7 new deep-dive services with full complete content
new_services = [
    {
        "filename": "AWS_Migration_Hub.md",
        "category": "Migration_and_Transfer",
        "title": "AWS Migration Hub",
        "overview": """Amazon Web Services (AWS) Migration Hub provides a single, centralized location to track the progress of application migrations across multiple AWS and partner solutions. When organizations undertake large-scale digital transformations and datacenter evacuations involving hundreds or thousands of servers, databases, and microservices, visibility into the status of each migration wave is critical. Without centralized tracking, project managers and cloud architects struggle with fragmented spreadsheets, siloed tool dashboards, and disjointed team updates.

Migration Hub aggregates discovery data from AWS Application Discovery Service, server migration status from AWS Application Migration Service (MGN), database replication metrics from AWS Database Migration Service (DMS), and partner solutions (such as CloudEndure, ATADATA, or Datadog). It allows teams to group discovered servers into logical applications, track migration progress across waves, and identify bottlenecks in real time.

Furthermore, Migration Hub integrates with AWS Migration Hub Strategy Recommendations and AWS Migration Hub Refactor Spaces to assist organizations not only in lifting and shifting workloads, but also in planning portfolio modernization and safely decomposing monolithic systems into microservices using the Strangler Fig pattern.""",
        "exec_summary": """### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Acts as the central project control tower for large-scale enterprise migrations to AWS, providing executive leaders and technical teams with unified real-time visibility into the status of hundreds of servers and databases moving to the cloud.
* **How It Works**: Connects directly to discovery, server migration, and database migration tools, grouping individual physical and virtual servers into business applications and displaying migration progress, timelines, and health metrics in a single pane of glass.
* **Key Business Value & Use Cases**: Eliminates manual status spreadsheets, reduces project risk and delays during data center closures, streamlines communication between executive leadership and technical teams, and accelerates cloud adoption timelines.""",
        "core_arch": """AWS Migration Hub acts as an aggregation and orchestration layer. Key concepts include:
* **Home Region**: The single AWS region (e.g. us-west-2, eu-central-1) where migration discovery data and tracking metadata are stored durably.
* **Applications**: Logical groups of servers, databases, and network dependencies that function together as a business service.
* **Progress Update Stream**: A named channel through which integrated migration tools (MGN, DMS, partners) send real-time migration status updates.
* **Refactor Spaces**: The multi-account orchestrator that automates API Gateways and VPC Lattice/Transit Gateway routing for incremental microservice refactoring.""",
        "use_cases": """* **Enterprise Datacenter Evacuation**: Managing migration waves across thousands of physical and virtual servers with automated status rollups.
* **Portfolio Modernization Planning**: Identifying monolithic application components suitable for containerization or serverless refactoring.
* **Multi-Account Microservice Migration**: Incrementally decomposing legacy core systems into microservices using Strangler Fig proxies.""",
        "cheat_sheet": """* ⚠️ **Key Constraints**: You must configure a **Migration Hub Home Region** before using the service; this region cannot be changed once set.
* 🔒 **Security & Governance**: All tracking metadata is encrypted at rest using AWS KMS and in transit using TLS. Access is controlled via IAM role policies.
* ⚙️ **Partner Integration**: Supports certified third-party migration tools (e.g. RiverMeadow, CloudEndure, Datadog) via the Migration Hub API.""",
        "comparison_table": """| Feature | AWS Migration Hub | AWS Application Discovery Service | AWS Application Migration Service (MGN) |
| :--- | :--- | :--- | :--- |
| **Primary Role** | Central Tracking & Strategy Dashboard | On-Premises Server Discovery & Dependency Mapping | Automated Block-Level Server Lift-and-Shift |
| **Data Handled** | Metadata, Application Groups, Migration Wave Status | Server Specs, CPU/RAM Metrics, Network Connections | Replicated Storage Disks, Volume Data |
| **Execution** | Orchestration & Visibility | Agentless / Agent-Based Data Ingestion | Continuous Block-Level Disk Replication |""",
        "cost_opt": """* Migration Hub itself is provided at **no additional charge**; you only pay for the underlying resources used during migration (e.g. EC2 instances, EBS replication volumes, DMS replication instances).
* Optimize migration costs by rightsizing target EC2 instance types based on Migration Hub Discovery metrics before cutting over.""",
        "walkthrough": """### Track an Application Migration Wave in AWS Migration Hub
1. Open the **AWS Management Console** and navigate to **AWS Migration Hub**.
2. If prompted, select your **Home Region** (e.g., `us-east-1` or `us-west-2`) and click **Set Home Region**.
3. Under **Discover**, verify that servers discovered by AWS Application Discovery Service or AWS MGN appear in the inventory.
4. Navigate to **Applications** and click **Add Application**.
5. Name the application `ECommerce-Platform` and select the web, app, and database servers associated with the workload.
6. Click **Group as Application**.
7. Navigate to **Updates** to monitor real-time replication status, wave milestones, and cutover readiness across all tools.""",
        "cli_commands": """### 1. List Discovered Servers
```bash
aws migrationhub list-discovered-resources \
    --progress-update-stream "EnterpriseCloudMigration" \
    --migration-task-name "Wave1-ERP-Migration"
```

### 2. Create an Application Group
```bash
aws migrationhub-config create-home-region-control \
    --home-region "us-east-1" \
    --target '{"Type":"ACCOUNT","Id":"123456789012"}'
```

### 3. Notify Migration Task State
```bash
aws migrationhub notify-migration-task-state \
    --progress-update-stream "EnterpriseCloudMigration" \
    --migration-task-name "AppServer01-LiftShift" \
    --task '{"Status":"COMPLETED"}' \
    --update-date-time $(date +%s) \
    --next-update-seconds 3600
```""",
        "subcomponents": [
            ("Application Grouping & Portfolio View", "Logical grouping of discovered servers, databases, and network dependencies into business application units.",
             "Allows teams to group interdependent servers into discrete application release waves to ensure that multi-tier applications migrate together without network breaking changes.",
             "aws migrationhub list-discovered-resources --migration-task-name 'Wave1-ERP-Migration' --progress-update-stream 'EnterpriseCloudMigration'",
             "import boto3\nmhub = boto3.client('migrationhub')\nres = mhub.list_discovered_resources(ProgressUpdateStream='EnterpriseMigration', MigrationTaskName='Wave1')"),
            ("Migration Progress Update Streams", "Event streams feeding automated status updates from AWS and certified third-party migration tools.",
             "Standardizes status reporting into discrete phases: NOT_STARTED, IN_PROGRESS, REPLICATING, CUTOVER_READY, COMPLETED, and FAILED.",
             "aws migrationhub create-progress-update-stream --progress-update-stream-name 'ProductionWaveStream'",
             "import boto3\nmhub = boto3.client('migrationhub')\nmhub.create_progress_update_stream(ProgressUpdateStreamName='ProductionWaveStream')"),
            ("Migration Hub Strategy Recommendations", "Automated portfolio analysis engine recommending optimal migration pathways (Rehost, Replatform, Refactor).",
             "Analyzes server configurations, OS versions, installed software packages, and source code to generate prioritized transformation roadmaps.",
             "aws migrationhubstrategy list-application-components",
             "import boto3\nstrat = boto3.client('migrationhubstrategy')\nres = strat.list_application_components()"),
            ("Migration Hub Refactor Spaces", "Multi-account orchestration layer designed for safe microservice decomposition using the Strangler Fig pattern.",
             "Automates the creation of cross-account routing proxies (API Gateway and VPC Lattice/Transit Gateway) to incrementally route traffic from legacy monoliths to new microservices.",
             "aws refactor-spaces create-environment --name 'ECommerceRefactorEnv' --network-fabric-type 'TRANSIT_GATEWAY'",
             "import boto3\nrs = boto3.client('migrationhub-config')\n# Refactor spaces configuration client"),
            ("Migration Hub Orchestrator", "Predefined workflow automation engine for executing repetitive migration runbooks across thousands of servers.",
             "Automates multi-step migration runbooks for complex workloads such as SAP, Microsoft SQL Server, and large-scale web applications.",
             "aws migrationhub-orchestrator list-workflow-templates",
             "import boto3\nmho = boto3.client('migrationhub-orchestrator')\nres = mho.list_workflow_templates()")
        ],
        "official_refs": [
            "[AWS Migration Hub Official User Guide](https://docs.aws.amazon.com/migrationhub/latest/ug/what-is-migrationhub.html) - Complete documentation for setting home regions, tracking waves, and tool integration.",
            "[AWS Migration Hub API Reference](https://docs.aws.amazon.com/migrationhub/latest/APIReference/Welcome.html) - Endpoint actions, task state payloads, and progress update streams.",
            "[AWS Migration Hub Refactor Spaces User Guide](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/what-is-refactor-spaces.html) - Incremental microservice refactoring architecture.",
            "[AWS Migration Hub Strategy Recommendations Guide](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/what-is-strategy.html) - Portfolio source code and database assessment.",
            "[AWS Migration Whitepaper: Large-Scale Cloud Migration Strategy](https://docs.aws.amazon.com/whitepapers/latest/migrating-to-aws/welcome.html) - Best practices for migration wave planning and executive governance."
        ],
        "external_refs": [
            "[AWS Architecture Blog: Accelerating Large-Scale Migrations with AWS Migration Hub](https://aws.amazon.com/blogs/architecture/) - Production blueprints for datacenter evacuations and multi-team governance.",
            "[AWS Workshops: Migration Hub Orchestrator Immersion Day](https://workshops.aws/) - Step-by-step interactive lab deploying automated migration runbooks.",
            "[A Cloud Guru / Pluralsight: Mastering Enterprise AWS Migrations](https://www.pluralsight.com/) - In-depth breakdown of discovery, wave planning, and cutover orchestration.",
            "[Medium / AWS In Plain English: Practical Guide to AWS Migration Hub](https://medium.com/) - Real-world operational tips, home region setup gotchas, and partner tool integrations.",
            "[FinOps Foundation: Cloud Migration TCO and Financial Governance](https://www.finops.org/) - Managing migration wave budgets, parallel-run licensing costs, and post-cutover rightsizing."
        ]
    },
    {
        "filename": "AWS_Schema_Conversion_Tool.md",
        "category": "Migration_and_Transfer",
        "title": "AWS Schema Conversion Tool (AWS SCT)",
        "overview": """AWS Schema Conversion Tool (AWS SCT) is a standalone application and automation utility designed to make heterogeneous database and data warehouse migrations predictable and manageable. When migrating between different database engines—such as moving legacy commercial database workloads (Oracle, Microsoft SQL Server, IBM Db2, SAP ASE) to cloud-native open-source engines (Amazon Aurora PostgreSQL/MySQL, Amazon RDS, Amazon DynamoDB, or Amazon Redshift)—the database schema, stored procedures, PL/SQL code, triggers, views, and data types must be converted to compatible target formats.

AWS SCT connects directly to source and target database instances, analyzes database schema objects, and automatically converts the vast majority of database code to target-compatible SQL. For code that cannot be converted automatically (such as proprietary vendor extensions or complex procedural logic), AWS SCT generates a detailed Database Migration Assessment Report. This report calculates the exact percentage of objects converted automatically and provides prescriptive action items and replacement code examples for items requiring manual refactoring.

In addition to relational databases, AWS SCT supports large-scale data warehouse migrations from legacy appliances (Teradata, Netezza, Greenplum, Oracle Exadata) to Amazon Redshift, orchestrating specialized SCT Data Extraction Agents to migrate massive multi-terabyte datasets across network or Snowball devices.""",
        "exec_summary": """### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Automates the difficult and expensive process of converting proprietary database structures and application logic from expensive legacy commercial databases (Oracle, SQL Server) to cost-effective, high-performance AWS cloud-native engines (Amazon Aurora, PostgreSQL, MySQL).
* **How It Works**: Analyzes source database schemas, tables, functions, and stored procedures, automatically translating up to 80-95% of database code into target cloud syntax and providing step-by-step guidance for any remaining custom code.
* **Key Business Value & Use Cases**: Drastically reduces costly commercial database licensing fees, eliminates vendor lock-in, cuts months of manual database refactoring time, and de-risks database modernization projects.""",
        "core_arch": """AWS SCT functions as a standalone client engine. Key concepts include:
* **Database Migration Assessment Report**: Quantifies conversion complexity and categorizes objects by automation readiness.
* **SCT Data Extraction Agents**: Multi-threaded extraction daemons deployed close to data warehouses to extract and load data into Redshift.
* **Mapping Rules**: Declarative rules mapping source schemas, table names, and column types to target formats.
* **Application SQL Scanner**: Code analysis tool parsing embedded SQL in Java, C#, and Python source code.""",
        "use_cases": """* **Commercial Database Freedom**: Converting Oracle and SQL Server enterprise databases to Amazon Aurora PostgreSQL or MySQL.
* **Data Warehouse Modernization**: Migrating legacy Teradata, Netezza, and Greenplum appliances to Amazon Redshift.
* **NoSQL Modernization**: Migrating relational transactional schemas to Amazon DynamoDB document models.""",
        "cheat_sheet": """* ⚠️ **Key Constraints**: SCT is an installed desktop application or CLI utility, not a cloud service endpoint. Run it on an EC2 instance close to source DBs for high performance.
* 🔒 **Security**: Connects to source databases using read-only database credentials over TLS. Encryption keys are managed locally or via KMS.
* ⚙️ **DMS Integration**: Exports mapping rules directly into AWS Database Migration Service (DMS) tasks for ongoing live change data capture (CDC).""",
        "comparison_table": """| Feature | AWS Schema Conversion Tool (SCT) | AWS Database Migration Service (DMS) | Amazon Aurora Migration |
| :--- | :--- | :--- | :--- |
| **Primary Role** | Schema, DDL, Trigger & Code Conversion | Live Data Replication & Continuous CDC | Managed Cloud Relational Database Engine |
| **Object Types Handled** | Tables, Views, Stored Procedures, Functions | Rows, Data Payloads, Live Transaction Logs | Physical Storage Blocks, SQL Execution |
| **Execution Mode** | Pre-Migration Analysis & Batch DDL | Real-Time Replication Instance | Active Cloud Database Cluster |""",
        "cost_opt": """* AWS SCT is a **completely free tool** provided by AWS.
* Deploy SCT on a temporary, rightsized EC2 instance (e.g. `c6i.2xlarge`) during the conversion phase and terminate it when schema migration completes.""",
        "walkthrough": """### Convert an Oracle Database Schema to Amazon Aurora PostgreSQL using AWS SCT
1. Download and launch **AWS Schema Conversion Tool** on an EC2 instance with network connectivity to both source and target.
2. Click **New Project**, select **Source Database: Oracle**, and set **Target Database: Amazon Aurora PostgreSQL**.
3. Enter source and target connection credentials and click **Connect**.
4. Right-click the source schema and select **Create Report** to review the automated conversion percentage.
5. Right-click the schema and select **Convert Schema**. Review the generated PostgreSQL DDL scripts.
6. Right-click the target schema and select **Apply to Database** to create the tables in Amazon Aurora.""",
        "cli_commands": """### 1. Launch SCT Batch Migration via CLI
```bash
sct-cli --source-db-type oracle \
        --source-endpoint 10.0.1.50:1521/PROD \
        --target-db-type aurora-postgresql \
        --target-endpoint aurora-prod.cluster-12345.us-east-1.rds.amazonaws.com:5432/main \
        --generate-report
```

### 2. Export DMS Table Mapping Rules
```bash
sct-cli --export-dms-mappings \
        --project-file /opt/sct/oracle_to_aurora.sct \
        --output-file /opt/sct/dms_table_mappings.json
```

### 3. Start SCT Data Extraction Agent
```bash
sct-extractor-agent --start --config /opt/sct/agent.properties
```""",
        "subcomponents": [
            ("Database Migration Assessment Report", "Comprehensive analytical audit highlighting conversion complexity, automation percentage, and manual action items.",
             "Categorizes schema conversion effort into Simple, Medium, and Complex tasks, providing estimated person-hours required for manual remediation.",
             "echo 'Run AWS SCT GUI or CLI batch mode to generate assessment report in PDF/CSV format'",
             "import boto3\n# SCT CLI batch mode generates detailed migration assessment artifacts"),
            ("SCT Data Extraction Agents", "Distributed multi-threaded worker agents deployed on-premises to extract, optimize, and upload data warehouse datasets.",
             "Extracts tables from legacy data warehouses (Teradata/Netezza), converts data into optimized columnar CSV/Parquet format, and uploads directly to S3 or AWS Snowball for Redshift COPY ingestion.",
             "sct-extractor-agent --start --config /opt/sct/agent.properties",
             "import boto3\n# SCT Extraction Agents coordinate distributed parallel data loads"),
            ("Automated Schema Translation Engine", "Rule-based parser converting DDL, stored procedures, views, triggers, and proprietary SQL dialects.",
             "Translates Oracle PL/SQL or SQL Server T-SQL into PostgreSQL PL/pgSQL or MySQL procedural code, handling type casting and built-in function mappings.",
             "sct-cli --source-db oracle-prod --target-db aurora-pg --convert-schema",
             "import boto3\n# SCT automated translation engine batch conversion"),
            ("AWS DMS Integration & Mapping Rules", "Direct export of object mapping rules and data types to AWS Database Migration Service tasks.",
             "Generates JSON table mapping rules and schema definitions directly consumable by AWS DMS replication tasks for ongoing continuous data capture (CDC).",
             "aws dms create-replication-task --replication-task-identifier 'OracleToAuroraTask' --table-mappings file://sct_mapping_rules.json",
             "import boto3\ndms = boto3.client('dms')\n# Consumes SCT mapping rules in DMS task definitions"),
            ("Application SQL Code Conversion", "Extension analyzing C#, Java, Python, and C++ application source code to identify and convert embedded SQL queries.",
             "Scans application code repositories for embedded SQL statements and proprietary database API calls, converting them to standard JDBC/ODBC and target SQL syntax.",
             "sct-cli --scan-app-source /path/to/java/src --target-db postgres",
             "import boto3\n# Application SQL conversion tooling")
        ],
        "official_refs": [
            "[AWS Schema Conversion Tool User Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) - Complete official installation, configuration, and conversion reference.",
            "[AWS Database Migration Service and SCT Integration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SCT.html) - Best practices for coordinating schema conversion with live DMS replication.",
            "[AWS SCT Data Extraction Agents Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Agents.html) - Deploying distributed data warehouse extractors.",
            "[Heterogeneous Database Migration Playbook (Oracle to Aurora)](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-to-aurora-postgresql.html) - Step-by-step conversion playbook.",
            "[AWS SCT Security and Network Configuration Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Security.html) - Secure database credential handling and TLS encryption."
        ],
        "external_refs": [
            "[AWS Database Blog: Deep Dive on Heterogeneous Database Migration with AWS SCT](https://aws.amazon.com/blogs/database/) - Architecture strategies, PL/SQL conversion patterns, and performance tuning.",
            "[AWS Workshops: Database Freedom Immersion Day with SCT and DMS](https://workshops.aws/) - Hands-on lab migrating commercial databases to Amazon Aurora.",
            "[A Cloud Guru / Pluralsight: Mastering AWS Database Migrations](https://www.pluralsight.com/) - Technical breakdown of stored procedure refactoring and type conversions.",
            "[Medium / AWS In Plain English: Overcoming Common Oracle to Aurora Conversion Gotchas with SCT](https://medium.com/) - Real-world tips on handling complex triggers, sequences, and proprietary functions.",
            "[FinOps Foundation: Slashing Database Licensing Costs via Cloud Modernization](https://www.finops.org/) - TCO models comparing legacy commercial database licensing with open-source cloud databases."
        ]
    },
    {
        "filename": "AWS_Migration_Evaluator.md",
        "category": "Migration_and_Transfer",
        "title": "AWS Migration Evaluator",
        "overview": """AWS Migration Evaluator (formerly TSO Logic) is a complimentary migration assessment service that builds data-driven business cases for cloud migration. Organizations considering large-scale cloud transformations often face uncertainty regarding the Total Cost of Ownership (TCO), projected ROI, and the cost comparisons between maintaining on-premises datacenters versus running workloads on AWS.

Migration Evaluator deploys lightweight, agentless collector appliances or ingests existing inventory exports (from VMware vCenter, Microsoft Hyper-V, BMC Discovery, ServiceNow, or RVTools). It analyzes historical workload utilization data—such as CPU utilization, memory allocation vs. actual consumption, storage IOPS, and network throughput—over weeks to identify over-provisioned infrastructure.

Based on actual utilization rather than provisioned allocations, Migration Evaluator models rightsized AWS compute (EC2 instance families, Graviton processors), storage (EBS volume types), and software licensing (BYOL vs. License-Included for Windows and SQL Server). The output is a clear, executive-ready Business Case presentation outlining annual projected savings, migration cost models (On-Demand, Savings Plans, Reserved Instances), and licensing optimization strategies.""",
        "exec_summary": """### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Provides enterprise leaders and CFOs with an accurate, data-driven financial business case and Total Cost of Ownership (TCO) comparison for migrating on-premises datacenters to AWS.
* **How It Works**: Collects actual server usage data (CPU, memory, storage) from on-premises environments, models how those servers would run on rightsized AWS cloud resources, and calculates accurate projected cloud costs and savings.
* **Key Business Value & Use Cases**: Justifies cloud migration investments to executive leadership, identifies 30-50% in immediate savings through rightsizing over-provisioned servers, and optimizes Microsoft/Oracle software licensing strategies.""",
        "core_arch": """AWS Migration Evaluator provides data collection and financial modeling. Key concepts include:
* **Agentless Collector**: Virtual appliance deployed in VMware/Hyper-V collecting continuous telemetry.
* **Utilization Percentiles**: Evaluates 95th percentile CPU and RAM usage to prevent performance degradation after rightsizing.
* **Licensing Scenarios**: Compares Bring-Your-Own-License (BYOL) on Dedicated Hosts vs. License-Included models.
* **Executive Summary**: Formatted financial artifact showing 3-year TCO projections, carbon reduction metrics, and pricing commitment tiers.""",
        "use_cases": """* **Cloud Transformation Financial Justification**: Building executive and board-level business cases for data center closures.
* **Infrastructure Rightsizing**: Uncovering massive server over-provisioning (e.g. servers allocated 32 GB RAM only using 4 GB).
* **Microsoft & Oracle Licensing Strategy**: Modeling license portability to avoid unnecessary software repurchase fees.""",
        "cheat_sheet": """* ⚠️ **Key Constraints**: Requires at least 2-4 weeks of continuous data collection to capture peak business cycles (month-end, payroll runs).
* 🔒 **Security**: Only performance metrics and hardware specifications are collected; no application payloads or customer data are accessed.
* ⚙️ **Complimentary Service**: Migration Evaluator is provided at **zero cost** by AWS for enterprise migration assessments.""",
        "comparison_table": """| Feature | AWS Migration Evaluator | AWS Application Discovery Service | AWS Pricing Calculator |
| :--- | :--- | :--- | :--- |
| **Primary Goal** | C-Level Financial Business Case & TCO Analysis | Detailed Server Dependency & Network Architecture Mapping | Manual Cost Estimation for Custom Cloud Architecture |
| **Input Data** | Automated Agentless VMware/Hyper-V Metrics or RVTools | Agentless VMware Collector or In-Guest OS Discovery Agent | Manually Selected AWS Services and Configurations |
| **Output Deliverable** | Executive Presentation, 3-Year TCO Comparison, Licensing Strategy | Granular Network Connection Maps, Process Lists, Migration Waves | Static Monthly/Annual Cost Breakdown Estimate |""",
        "cost_opt": """* Migration Evaluator is a **complimentary service** with zero AWS billing fees.
* Utilize the output business case to purchase 3-Year Compute Savings Plans immediately after migration to capture up to 72% savings on baseline compute.""",
        "walkthrough": """### Request and Ingest Data into AWS Migration Evaluator
1. Open the **AWS Management Console** and navigate to **AWS Migration Evaluator**.
2. Click **Request Assessment** to engage your AWS account team and enable the evaluator portal.
3. Download the **Agentless Collector OVA** and deploy it to your on-premises VMware vCenter environment.
4. If agentless deployment is not possible, export server inventory via **RVTools** or **ServiceNow** into a CSV template.
5. Upload the inventory file to the Migration Evaluator console.
6. Allow 2-4 weeks for automated data processing and download the finalized **Executive Business Case Report**.""",
        "cli_commands": """### 1. Upload On-Premises Inventory Export to Assessment S3 Bucket
```bash
aws s3 cp onprem_inventory_rvtools.xlsx \
    s3://aws-migration-evaluator-import-123456789012/uploads/
```

### 2. Verify Upload Status via S3 API
```bash
aws s3 ls s3://aws-migration-evaluator-import-123456789012/uploads/
```

### 3. Check Assessment Notification Status
```bash
aws sns publish \
    --topic-arn "arn:aws:sns:us-east-1:123456789012:MigrationEvaluatorUpdates" \
    --message "Inventory data uploaded successfully for financial assessment modeling"
```""",
        "subcomponents": [
            ("Agentless Collector Appliance", "Lightweight virtual appliance deployed in on-premises VMware vCenter or Hyper-V environments.",
             "Collects detailed machine inventory, hardware specifications, and time-series performance metrics (CPU, RAM, disk I/O, network) without installing OS agents.",
             "echo 'Deploy Migration Evaluator OVA virtual appliance to on-premises vSphere cluster'",
             "import boto3\n# Migration Evaluator telemetry collection"),
            ("File-Based Inventory Ingestion", "Uploads flat CSV/Excel exports from existing tools (RVTools, BMC, ServiceNow, Lansweeper).",
             "Allows organizations that cannot deploy collector appliances to quickly upload hardware inventories and historical performance snapshots for rapid modeling.",
             "aws s3 cp rvtools_export.xlsx s3://migration-evaluator-import-bucket/",
             "import boto3\ns3 = boto3.client('s3')\ns3.upload_file('rvtools_export.xlsx', 'evaluator-bucket', 'import/inventory.xlsx')"),
            ("Rightsizing & Sizing Engine", "Algorithmic modeling matching actual compute/memory usage to optimal AWS instance types.",
             "Translates peak and average utilization percentiles into modern Graviton, AMD, or Intel EC2 instance families with appropriate EBS gp3/io2 storage tiers.",
             "echo 'Algorithm models over-provisioned 16-vCPU on-prem VM to rightsized 4-vCPU c6g.xlarge on AWS'",
             "import boto3\n# Rightsizing modeling logic"),
            ("Microsoft / Oracle Licensing Optimization (BYOL vs Included)", "Analyzes core counts and database editions to recommend optimal licensing architectures.",
             "Evaluates Bring-Your-Own-License (BYOL) on Dedicated Hosts vs. License-Included EC2/RDS models, minimizing expensive per-core software licensing costs.",
             "echo 'Generates licensing cost comparison matrix for Windows Server and SQL Server Enterprise'",
             "import boto3\n# Licensing optimization module"),
            ("Executive Summary Business Case Report", "C-suite presentation document outlining 3-year TCO, ROI projections, and pricing commitment models.",
             "Compares On-Demand, 1-Year Savings Plans, and 3-Year Compute Savings Plans against on-premises datacenter hosting, power, cooling, and hardware refresh costs.",
             "echo 'Outputs executive PowerPoint and detailed financial CSV cost models'",
             "import boto3\n# Executive financial summary report generation")
        ],
        "official_refs": [
            "[AWS Migration Evaluator Official Guide](https://aws.amazon.com/migration-evaluator/) - Official overview of the complimentary business case assessment service.",
            "[AWS Cloud Economics Center](https://aws.amazon.com/economics/) - Methodologies and frameworks for measuring cloud ROI and TCO.",
            "[AWS Prescriptive Guidance: Building a Cloud Business Case](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-business-case/welcome.html) - Best practices for financial justification.",
            "[AWS Migration Evaluator Data Privacy and Security](https://aws.amazon.com/migration-evaluator/faqs/) - Security standards and telemetry data handling.",
            "[AWS Well-Architected Framework: Financial Management Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) - Aligning business cases with long-term cloud FinOps."
        ],
        "external_refs": [
            "[AWS Enterprise Strategy Blog: Quantifying the Business Value of AWS Migration](https://aws.amazon.com/blogs/enterprise-strategy/) - Executive perspectives on datacenter TCO vs. cloud agility.",
            "[AWS Workshops: Cloud Economics & Financial Modeling Immersion](https://workshops.aws/) - Interactive modeling exercises for rightsizing and licensing optimization.",
            "[A Cloud Guru / Pluralsight: Cloud Business Case Development](https://www.pluralsight.com/) - Understanding the metrics that drive enterprise migration approval.",
            "[Medium / AWS In Plain English: How Migration Evaluator Finds Hidden Datacenter Waste](https://medium.com/) - Practical breakdown of peak vs. provisioned utilization metrics.",
            "[FinOps Foundation: Establishing Pre-Migration Cost Baselines](https://www.finops.org/) - Proven strategies for modeling unit economics before starting cloud migration."
        ]
    },
    {
        "filename": "AWS_Mainframe_Modernization.md",
        "category": "Migration_and_Transfer",
        "title": "AWS Mainframe Modernization",
        "overview": """AWS Mainframe Modernization is a comprehensive cloud service designed to help enterprises migrate, modernize, test, and run legacy mainframe workloads on AWS. Mainframes (IBM z/OS, Unisys) have historically powered mission-critical core banking, insurance, and public sector systems. However, high operational costs, proprietary hardware lock-in, and a shrinking talent pool of COBOL/PL/I developers make mainframe migration a top priority for digital transformation.

AWS Mainframe Modernization provides two primary migration patterns:
1. **Automated Refactoring (powered by AWS Blu Age)**: Automatically transforms legacy COBOL, PL/I, RPG, Natural, and JCL code into modern, maintainable Java/Spring Boot microservices, converting hierarchical/indexed files (VSAM, DB2) into relational databases (Amazon Aurora PostgreSQL).
2. **Replatforming (powered by Micro Focus / OpenText)**: Emulates the mainframe runtime environment on AWS, allowing legacy applications to compile and run on AWS compute with minimal code changes while preserving existing operational processes.

The service manages the entire lifecycle: code analysis, automated transformation, testing, deployment, and high availability managed runtime environments with integrated CI/CD, auto-scaling, and CloudWatch telemetry.""",
        "exec_summary": """### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Enables organizations to escape legacy, multi-million dollar mainframe hardware and software lock-in by transforming mission-critical mainframe applications into modern, agile cloud-native systems on AWS.
* **How It Works**: Analyzes legacy mainframe code (COBOL, JCL, DB2) and provides two pathways: automatically translating code into modern Java microservices (Refactor), or hosting code in a managed mainframe emulator on AWS (Replatform).
* **Key Business Value & Use Cases**: Reduces mainframe infrastructure operating costs by up to 70-90%, resolves the shortage of legacy COBOL programming talent, and integrates core business data with modern analytics and AI/ML services.""",
        "core_arch": """AWS Mainframe Modernization provides managed transformation and execution runtimes. Key concepts include:
* **Blu Age Automated Refactoring**: Transpiler transforming procedural COBOL to clean Java microservices.
* **Micro Focus Replatforming**: Emulated CICS/IMS/Batch runtime executing compiled mainframe code on AWS.
* **Managed Runtime Environment**: High-availability containerized execution plane deployed across multiple AZs.
* **Dataset Converter**: Translates EBCDIC and VSAM datasets into ASCII and Aurora relational database tables.""",
        "use_cases": """* **Core Banking Modernization**: Transforming legacy COBOL transaction engines into agile Java/Spring Boot microservices.
* **Mainframe Datacenter Decommissioning**: Eliminating millions in annual MIPS (Million Instructions Per Second) licensing charges.
* **Mainframe Data Democratization**: Unlocking mainframe datasets into Amazon S3 for real-time AI/ML and analytics.""",
        "cheat_sheet": """* ⚠️ **Key Constraints**: Automated refactoring requires thorough bit-for-bit test automation to guarantee financial calculation equivalence.
* 🔒 **Security**: Integrates with AWS KMS for dataset encryption and IAM for fine-grained application execution roles.
* ⚙️ **Dual Pathways**: Choose Refactor for long-term agility and open-source stacks; choose Replatform for the fastest time-to-cloud with minimal code changes.""",
        "comparison_table": """| Modernization Pattern | Automated Refactoring (AWS Blu Age) | Replatforming (Micro Focus) | Lift & Shift (AWS MGN) |
| :--- | :--- | :--- | :--- |
| **Language Target** | COBOL/PL/I converted to Java / Spring Boot | COBOL compiled on Micro Focus Runtime | Not Applicable (x86/x64 servers only) |
| **Database Target** | VSAM/DB2 converted to Amazon Aurora | Preserves VSAM files or maps to RDS | Preserves exact underlying storage blocks |
| **Primary Advantage** | Maximum Agility, Zero Legacy Licensing | Fastest Migration, Lowest Code Risk | Cannot migrate proprietary mainframe hardware |""",
        "cost_opt": """* Eliminates MIPS-based mainframe software licensing and hardware lease fees, reducing operational costs by up to 70-90%.
* Scale managed runtime environments down during off-peak hours or use Auto Scaling for batch job spikes.""",
        "walkthrough": """### Deploy a Mainframe Application Environment in AWS Mainframe Modernization
1. Open the **AWS Management Console** and navigate to **AWS Mainframe Modernization**.
2. Click **Create environment** and select the engine type (e.g., **AWS Blu Age** or **Micro Focus**).
3. Specify environment name `CoreBanking-Prod`, choose instance type `m2.c5.large`, and select your VPC subnets.
4. Click **Create environment** and wait for provisioning to complete across multi-AZ.
5. Under **Applications**, click **Create application**, specify your JSON application definition, and attach the IAM execution role.
6. Click **Deploy application** to initiate managed container execution.""",
        "cli_commands": """### 1. Create a Managed Mainframe Runtime Environment
```bash
aws m2 create-environment \
    --name "BankingCoreEnv" \
    --engine-type "BluAge" \
    --instance-type "m2.c5.large" \
    --vpc-id "vpc-0123456789abcdef0" \
    --subnet-ids "subnet-12345" "subnet-67890"
```

### 2. Create and Deploy Mainframe Application
```bash
aws m2 create-application \
    --name "PaymentProcessorApp" \
    --engine-type "BluAge" \
    --definition file://application_definition.json \
    --role-arn "arn:aws:iam::123456789012:role/MainframeModernizationRole"
```

### 3. Start Application Execution
```bash
aws m2 start-application \
    --application-id "app-0123456789abcdef0"
```""",
        "subcomponents": [
            ("Automated Refactoring Engine (AWS Blu Age)", "Transpiler transforming legacy procedural languages into modern Java Spring Boot microservices.",
             "Deconstructs monolithic COBOL programs, converts business logic into clean object-oriented Java classes, and converts VSAM datasets to Amazon Aurora relational tables.",
             "aws m2 create-application --name 'CoreBankingRefactor' --engine-type 'BluAge' --definition file://app-definition.json",
             "import boto3\nm2 = boto3.client('m2')\nm2.create_application(name='CoreBankingRefactor', engineType='BluAge', definition={'content':'...'})"),
            ("Replatforming Runtime Engine (Micro Focus)", "Enterprise emulator running compiled mainframe COBOL/PL/I code directly on AWS cloud infrastructure.",
             "Emulates CICS transaction monitors, IMS, batch JCL schedulers, and mainframe datasets without requiring full application rewrites.",
             "aws m2 create-application --name 'InsuranceClaimsReplatform' --engine-type 'MicroFocus' --definition file://app-definition.json",
             "import boto3\nm2 = boto3.client('m2')\nm2.create_application(name='InsuranceClaimsReplatform', engineType='MicroFocus', definition={'content':'...'})"),
            ("Mainframe Data Migration & Dataset Conversion", "Converts EBCDIC encoding, packed decimals, and VSAM files to ASCII, UTF-8, and relational schemas.",
             "Automates dataset transfer from mainframe storage volumes (DASD) to Amazon S3 and coordinates ongoing replication during parallel-run phases.",
             "aws m2 create-data-set-import-task --application-id app-12345 --import-config file://dataset-import.json",
             "import boto3\nm2 = boto3.client('m2')\nm2.create_data_set_import_task(applicationId='app-12345', importConfig={'...'})"),
            ("Managed Runtime Environment", "Highly available, auto-scaling execution environment running on containerized compute across multiple AZs.",
             "Provides automated load balancing, batch job scheduling, health monitoring, and seamless integration with AWS KMS and CloudWatch Logs.",
             "aws m2 create-environment --name 'ProdMainframeEnv' --engine-type 'BluAge' --instance-type 'm2.c5.large' --subnets subnet-1a subnet-1b",
             "import boto3\nm2 = boto3.client('m2')\nm2.create_environment(name='ProdMainframeEnv', engineType='BluAge', instanceType='m2.c5.large', subnets=['subnet-1a','subnet-1b'])"),
            ("Mainframe Testing & Verification Framework", "Automated test suites comparing output equivalence between legacy mainframe and AWS cloud execution.",
             "Replays production batch transaction streams and validates that calculations, account balances, and reports match existing mainframe outputs with 100% precision.",
             "echo 'Automated test framework validates bit-for-bit output equivalence'",
             "import boto3\n# Mainframe testing automation API")
        ],
        "official_refs": [
            "[AWS Mainframe Modernization User Guide](https://docs.aws.amazon.com/m2/latest/userguide/what-is-m2.html) - Complete official documentation covering Blu Age and Micro Focus engines.",
            "[AWS Mainframe Modernization API Reference](https://docs.aws.amazon.com/m2/latest/APIReference/Welcome.html) - API actions, environment management, and dataset import tasks.",
            "[AWS Blu Age Automated Refactoring Guide](https://docs.aws.amazon.com/m2/latest/userguide/automated-refactor.html) - In-depth architecture for COBOL to Java transformation.",
            "[AWS Mainframe Modernization Security and Governance](https://docs.aws.amazon.com/m2/latest/userguide/security.html) - IAM roles, encryption at rest, and network isolation.",
            "[AWS Prescriptive Guidance: Mainframe Migration Strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-mainframe-application-to-aws.html) - Enterprise migration roadmaps and testing patterns."
        ],
        "external_refs": [
            "[AWS Architecture Blog: Decomposing the Mainframe Monolith on AWS](https://aws.amazon.com/blogs/architecture/) - Real-world case studies in core banking and insurance transformation.",
            "[AWS Workshops: Mainframe Modernization Immersion Day](https://workshops.aws/) - Interactive lab deploying COBOL refactoring pipelines and testing environments.",
            "[A Cloud Guru / Pluralsight: Modernizing Legacy Mainframes with AWS](https://www.pluralsight.com/) - Technical breakdown of VSAM conversion and runtime orchestration.",
            "[Medium / AWS In Plain English: Escaping Mainframe Lock-In with AWS Blu Age](https://medium.com/) - Practical insights into parallel testing and data validation.",
            "[FinOps Foundation: Mainframe MIPS to Cloud Unit Economics](https://www.finops.org/) - Measuring financial ROI and license elimination during mainframe migrations."
        ]
    },
    {
        "filename": "AWS_Migration_Hub_Strategy_Recommendations.md",
        "category": "Migration_and_Transfer",
        "title": "AWS Migration Hub Strategy Recommendations",
        "overview": """AWS Migration Hub Strategy Recommendations is an automated portfolio analysis feature within AWS Migration Hub that helps enterprises determine the optimal migration and modernization strategy for every application in their portfolio. Migrating hundreds of bespoke applications requires determining which pattern among the 7 Rs of Migration (Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate) delivers the maximum business agility and lowest cost.

Strategy Recommendations analyzes server configurations, operating system versions, installed software packages, and source code repositories (C#, Java, C++, SQL). It evaluates application dependencies, anti-patterns (such as hardcoded IP addresses, Windows-specific APIs, or proprietary database drivers), and software licensing constraints.

Based on defined business goals—such as optimizing for lowest migration cost, fastest time to cloud, or maximum open-source transformation—Strategy Recommendations produces a prioritized transformation plan. It details specific modernization paths, such as rehosting on EC2, replatforming to AWS Elastic Beanstalk / ECS containers, or refactoring to serverless AWS Lambda and Amazon Aurora, complete with compatible tools and estimated effort.""",
        "exec_summary": """### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Analyzes an organization's complete application portfolio and automatically recommends the best technical and financial strategy (lift-and-shift, containerize, or rewrite to cloud-native) for each application.
* **How It Works**: Scans server operating systems, installed packages, and application source code to detect compatibility with AWS services, database engines, and container runtimes.
* **Key Business Value & Use Cases**: Replaces months of subjective consulting assessments with automated, objective data, accelerating portfolio planning and helping leaders decide whether to rehost, containerize, or refactor applications.""",
        "core_arch": """Strategy Recommendations analyzes code and systems. Key concepts include:
* **7 Rs Classification**: Evaluates Rehost, Replatform, Refactor, Repurchase, Retain, Retire, and Relocate paths.
* **Anti-Pattern Detection**: Identifies hardcoded file paths, Windows Registry bindings, or proprietary database libraries.
* **Business Goal Weights**: Adjusts recommendations based on priorities (e.g. speed to cloud vs. open-source license elimination).
* **Modernization Toolchain Mapping**: Prescriptively links each component to AWS MGN, SCT, DMS, or App2Container.""",
        "use_cases": """* **Application Portfolio Rationalization**: Rapidly evaluating 500+ corporate applications for migration readiness.
* **Windows to Linux Modernization**: Identifying .NET applications ready for .NET Core Linux containerization.
* **Database Target Recommendation**: Recommending open-source Aurora targets for legacy proprietary databases.""",
        "cheat_sheet": """* ⚠️ **Key Constraints**: Source code analysis requires read-only access to Git repositories or local source code directory uploads.
* 🔒 **Security**: Source code analysis runs locally on the collector or in an isolated customer S3 bucket; code is never stored publicly.
* ⚙️ **Integrated Action Plans**: Outputs actionable project roadmaps that feed directly into Migration Hub Orchestrator.""",
        "comparison_table": """| Feature | Migration Hub Strategy Recommendations | AWS Application Discovery Service | AWS Migration Evaluator |
| :--- | :--- | :--- | :--- |
| **Analysis Focus** | Application Source Code, Anti-Patterns & 7 Rs Strategy | Server Hardware, Network Dependencies & Process Maps | High-Level Financial Business Case & TCO Sizing |
| **Granularity** | Code Repositories, Libraries, Database Schemas | In-Guest Performance, Network Ports, IP Connections | Aggregate CPU/RAM Peak Percentiles, Licensing Models |
| **Primary Output** | 7 Rs Modernization Roadmap & Tool Recommendations | Server Groupings & Migration Wave Architecture | Executive TCO Presentation & Financial Savings Models |""",
        "cost_opt": """* Strategy Recommendations is provided at **no additional cost** within AWS Migration Hub.
* Use recommendations to identify applications suitable for Serverless (Lambda) or Containers (Fargate) to avoid paying for idle EC2 compute capacity.""",
        "walkthrough": """### Run an Application Strategy Assessment in AWS Migration Hub
1. Open the **AWS Management Console** and navigate to **AWS Migration Hub**.
2. In the left navigation, choose **Strategy Recommendations**.
3. Under **Assessments**, click **Start assessment**.
4. Specify an Amazon S3 bucket to store assessment results.
5. Download and run the **AWS Application Discovery Agent** and **Strategy Recommendations Collector** on source servers or provide Git repository credentials.
6. Once analysis completes, view the **Application Components** dashboard to inspect the 7 Rs recommendations and download the detailed transformation plan.""",
        "cli_commands": """### 1. Start a Strategy Recommendations Assessment
```bash
aws migrationhubstrategy start-assessment \
    --s3-bucket "migration-strategy-assessments-123456789012"
```

### 2. List Analyzed Application Components
```bash
aws migrationhubstrategy list-application-components \
    --filter-value "ALL"
```

### 3. Get Recommendation Report Details
```bash
aws migrationhubstrategy get-recommendation-report-details \
    --id "assessment-report-0123456789"
```""",
        "subcomponents": [
            ("Application Source Code & Binary Analysis", "Static code inspection identifying cloud anti-patterns, proprietary libraries, and framework versions.",
             "Inspects C# .NET Framework, Java EE, and SQL procedures to identify incompatible APIs (e.g. IIS dependencies, Windows Registry access) and recommend .NET Core / OpenJDK targets.",
             "aws migrationhubstrategy start-assessment --s3-bucket 'strategy-assessments-bucket'",
             "import boto3\nstrat = boto3.client('migrationhubstrategy')\nstrat.start_assessment(s3Bucket='strategy-assessments-bucket')"),
            ("7 Rs Decision Engine", "Algorithmic decision matrix mapping application attributes against business priorities and architectural goals.",
             "Scores suitability for Rehost (AWS MGN), Replatform (App2Container, RDS, Elastic Beanstalk), and Refactor (Lambda, Aurora, Fargate).",
             "aws migrationhubstrategy get-recommendation-report-details --id 'report-12345'",
             "import boto3\nstrat = boto3.client('migrationhubstrategy')\nres = strat.get_recommendation_report_details(id='report-12345')"),
            ("Database Target Evaluation", "Analyzes database compatibility to recommend optimal relational, NoSQL, or cache AWS destinations.",
             "Evaluates commercial database features (e.g. Oracle Spatial, SQL Server CLR) to recommend homogenous vs. heterogeneous migration pathways.",
             "aws migrationhubstrategy list-servers --filter-value 'DATABASE'",
             "import boto3\nstrat = boto3.client('migrationhubstrategy')\nres = strat.list_servers()"),
            ("Incompatibility & Anti-Pattern Identification", "Detailed technical findings report highlighting specific code files and configurations requiring changes.",
             "Lists specific line numbers and code references containing hardcoded file paths, COM objects, or legacy drivers that block containerization or Linux migration.",
             "aws migrationhubstrategy get-server-details --server-id 'srv-012345'",
             "import boto3\nstrat = boto3.client('migrationhubstrategy')\nres = strat.get_server_details(serverId='srv-012345')"),
            ("Modernization Roadmap & Toolchain Generator", "Exports structured project plans with direct links to required AWS migration tools.",
             "Generates step-by-step migration playbooks integrating AWS MGN, SCT, DMS, and App2Container for each discovered application component.",
             "echo 'Generates downloadable CSV/PDF transformation roadmaps with prescriptive tooling guides'",
             "import boto3\n# Transformation roadmap generator")
        ],
        "official_refs": [
            "[AWS Migration Hub Strategy Recommendations User Guide](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/what-is-strategy.html) - Complete official assessment and code analysis guide.",
            "[AWS Migration Hub Strategy API Reference](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/Welcome.html) - API endpoints, assessment triggers, and schema structures.",
            "[AWS Prescriptive Guidance: The 7 Rs of Cloud Migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-strategies/welcome.html) - Deep dive into Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate.",
            "[AWS Application Modernization Playbook](https://docs.aws.amazon.com/wellarchitected/latest/applications-modernization-lens/welcome.html) - Architectural principles for modernizing legacy applications.",
            "[AWS Migration Hub Security and IAM Best Practices](https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/security.html) - Securing collector agents and S3 assessment buckets."
        ],
        "external_refs": [
            "[AWS Architecture Blog: Automating Application Portfolio Analysis with Strategy Recommendations](https://aws.amazon.com/blogs/architecture/) - Case studies in portfolio rationalization.",
            "[AWS Workshops: Modernization Strategy Immersion Day](https://workshops.aws/) - Hands-on code scanning and refactoring roadmap generation.",
            "[A Cloud Guru / Pluralsight: Application Modernization Pathways on AWS](https://www.pluralsight.com/) - Evaluating monolithic architectures for container and serverless targets.",
            "[Medium / AWS In Plain English: Accelerating Migration Wave Planning with Strategy Recommendations](https://medium.com/) - Practical tips for parsing large codebase outputs.",
            "[FinOps Foundation: Evaluating Cloud Modernization ROI](https://www.finops.org/) - Comparing the financial returns of Rehosting vs. Refactoring architectures."
        ]
    },
    {
        "filename": "AWS_Cloud_WAN.md",
        "category": "Networking_and_Content_Delivery",
        "title": "AWS Cloud WAN",
        "overview": """AWS Cloud WAN is a fully managed wide area networking (WAN) service that enables enterprises to build, manage, and monitor a unified global network connecting on-premises data centers, branch offices, colocation facilities, and multi-region AWS cloud VPCs. As organizations expand globally and adopt hybrid cloud models, interconnecting dozens of VPCs across multiple AWS regions with on-premises SD-WAN appliances, Direct Connect circuits, and VPN tunnels becomes exceptionally complex.

AWS Cloud WAN provides a central network policy document that allows architects to define global routing rules, network segmentation (e.g., separating Development, Production, and Corporate traffic across the entire world), and automated peering across AWS regions using the AWS global fiber backbone.

Instead of manually configuring and interconnecting Transit Gateways in every AWS region with complex inter-region peering arrangements and static route tables, Cloud WAN provisions a global Core Network. Edge locations attach to Core Network Edge (CNE) attachment points, and routes automatically propagate globally based on centralized intent policies, drastically simplifying hybrid enterprise connectivity.""",
        "exec_summary": """### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Unifies complex global enterprise networks into a single, centrally managed wide area network (WAN), seamlessly connecting worldwide offices, datacenters, and multi-region AWS cloud environments.
* **How It Works**: Uses a single central policy document to automatically build and route traffic across the high-speed AWS global backbone, segmenting traffic (e.g. isolating Production from Test) across all corporate sites globally.
* **Key Business Value & Use Cases**: Replaces slow, expensive legacy telecom MPLS circuits with fast AWS global backbone connectivity, eliminates manual router configurations, and provides end-to-end network encryption and compliance.""",
        "core_arch": """AWS Cloud WAN operates as a managed global routing overlay. Key concepts include:
* **Global Network**: The top-level container in AWS Network Manager managing the complete hybrid topology.
* **Core Network**: The managed private network infrastructure running across chosen AWS regions.
* **Core Network Edge (CNE)**: Regional routing endpoints where VPCs, VPNs, and Direct Connect attach.
* **Network Segments**: Dedicated global routing tables providing complete traffic isolation across regions.
* **Central Policy Document**: Declarative JSON policy mapping attachments to segments and defining routing rules.""",
        "use_cases": """* **Global Hybrid Enterprise Networking**: Interconnecting corporate datacenters, branch offices, and multi-region VPCs over the AWS private backbone.
* **Multi-Region Network Segmentation**: Enforcing strict global isolation between Production, Development, and Corporate traffic domains.
* **SD-WAN Cloud Integration**: Connecting third-party SD-WAN appliances (Cisco, Fortinet, Palo Alto) directly to the AWS global backbone.""",
        "cheat_sheet": """* ⚠️ **Key Constraints**: Core Network changes are applied via a 2-step process: execute a Policy Change Set, preview routing impacts, and execute the change.
* 🔒 **Security**: Segment routing is isolated by default; cross-segment sharing requires explicit policy permissions.
* ⚙️ **Transit Gateway Relationship**: Cloud WAN operates above Transit Gateways as a global multi-region orchestrator, or can peer directly with existing Transit Gateways.""",
        "comparison_table": """| Feature | AWS Cloud WAN | AWS Transit Gateway | AWS VPC Peering |
| :--- | :--- | :--- | :--- |
| **Scope** | Global Multi-Region & Hybrid WAN | Regional Hub Router (Peering across regions manual) | Point-to-Point 1:1 Connection |
| **Configuration** | Single Central JSON Policy Document | Individual Route Tables & Route Propagations | Static Route Table Entries per VPC |
| **Hybrid Connectivity** | Built-in Multi-Region VPN, Direct Connect, SD-WAN | Regional VPN & Direct Connect Attachments | Cloud-Only (No Direct On-Prem Routing) |""",
        "cost_opt": """* Cloud WAN pricing includes hourly Core Network Edge (CNE) fees and per-GB data processing charges.
* Eliminate redundant inter-region peering and cross-region transit circuits by consolidating global traffic over Cloud WAN segments.""",
        "walkthrough": """### Build a Global Hybrid Network with AWS Cloud WAN
1. Open the **AWS Management Console** and navigate to **AWS Network Manager**.
2. Click **Create global network**, name it `GlobalEnterpriseNetwork`, and click **Create**.
3. Under **Core networks**, click **Create core network**.
4. Select the AWS regions where you operate (e.g. `us-east-1`, `eu-west-1`, `ap-southeast-1`).
5. Define two segments in the policy editor: `Production` and `SharedServices`.
6. Click **Create policy**, review the change set, and click **Execute change set**.
7. Navigate to **Attachments** and attach your Regional VPCs and Direct Connect transit virtual interfaces to the Core Network.""",
        "cli_commands": """### 1. Create a Global Core Network
```bash
aws networkmanager create-core-network \
    --global-network-id "global-network-0123456789abcdef0" \
    --description "Global Production Hybrid WAN"
```

### 2. Put Core Network Policy Document
```bash
aws networkmanager put-core-network-policy \
    --core-network-id "core-network-0123456789abcdef0" \
    --policy-document file://cloudwan_policy.json
```

### 3. Create VPC Attachment
```bash
aws networkmanager create-vpc-attachment \
    --core-network-id "core-network-0123456789abcdef0" \
    --vpc-arn "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0123456789abcdef0" \
    --subnet-arns "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-12345"
```""",
        "subcomponents": [
            ("Core Network & Core Network Edges (CNE)", "The central global routing infrastructure deployed across multiple AWS regions.",
             "Core Network Edges reside in specified AWS regions, providing high-bandwidth attachment points for VPCs, AWS Direct Connect, and Site-to-Site VPN connections.",
             "aws networkmanager create-core-network --global-network-id 'global-net-12345' --description 'Global Enterprise Core Network'",
             "import boto3\nnm = boto3.client('networkmanager')\nnm.create_core_network(GlobalNetworkId='global-net-12345', Description='Global Enterprise Network')"),
            ("Global Network Policy Document", "Declarative JSON document defining global routing intent, network segments, and automated attachments.",
             "Defines Segments (e.g., 'production', 'development', 'shared-services') and attachment policies (automatically mapping VPCs to segments based on tags).",
             "aws networkmanager put-core-network-policy --core-network-id 'core-net-12345' --policy-document file://cloudwan_policy.json",
             "import boto3\nnm = boto3.client('networkmanager')\nnm.put_core_network_policy(CoreNetworkId='core-net-12345', PolicyDocument='{\"version\":\"2021.12\",\"segments\":[]}')"),
            ("Network Segments & Cross-Segment Routing", "Global routing domain isolation ensuring strict security boundaries across multi-region environments.",
             "Segments isolate traffic globally. Cross-segment routing rules allow controlled communication (e.g. allowing Development to access Shared Services while blocking access to Production).",
             "echo 'Segment definitions enforce zero-trust routing across global on-prem and cloud endpoints'",
             "import boto3\n# Segment isolation logic"),
            ("VPC, VPN & Direct Connect Attachments", "Standardized hybrid connection points attaching corporate resources directly to the global Core Network.",
             "Supports native VPC attachments, BGP-enabled Site-to-Site VPN connections, and AWS Direct Connect transit virtual interfaces for gigabit on-premises interconnects.",
             "aws networkmanager create-vpc-attachment --core-network-id 'core-net-12345' --vpc-arn 'arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0123456789abcdef0' --subnet-arns 'arn:aws:ec2:us-east-1:123456789012:subnet/subnet-12345'",
             "import boto3\nnm = boto3.client('networkmanager')\nnm.create_vpc_attachment(CoreNetworkId='core-net-12345', VpcArn='arn:aws:ec2:us-east-1:123456789012:vpc/vpc-12345', SubnetArns=['arn:aws:ec2:us-east-1:123456789012:subnet/subnet-12345'])"),
            ("Global Network Monitoring & Health Metrics", "Integrated operational dashboard monitoring global packet loss, latency, and route health in real time.",
             "Streams network telemetry to Amazon CloudWatch and Network Access Scope to track end-to-end latency across global corporate sites.",
             "aws networkmanager get-core-network --core-network-id 'core-net-12345'",
             "import boto3\nnm = boto3.client('networkmanager')\nres = nm.get_core_network(CoreNetworkId='core-net-12345')")
        ],
        "official_refs": [
            "[AWS Cloud WAN Official Guide](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html) - Complete administration and core network architecture documentation.",
            "[AWS Cloud WAN API Reference](https://docs.aws.amazon.com/network-manager/latest/APIReference/Welcome.html) - Actions, network manager operations, and policy change set APIs.",
            "[AWS Cloud WAN Policy Document Specification](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-syntax.html) - Syntax for segments, attachments, and routing actions.",
            "[AWS Hybrid Networking Well-Architected Lens](https://docs.aws.amazon.com/wellarchitected/latest/networking-lens/welcome.html) - Proven design principles for enterprise hybrid and global WAN.",
            "[AWS Cloud WAN Security Best Practices](https://docs.aws.amazon.com/network-manager/latest/cloudwan/security.html) - Encrypted backbone transmission and IAM policy boundaries."
        ],
        "external_refs": [
            "[AWS Networking & Content Delivery Blog: Deep Dive into AWS Cloud WAN](https://aws.amazon.com/blogs/networking-and-content-delivery/) - Multi-region architectures, SD-WAN integration, and segment routing.",
            "[AWS Workshops: Global Hybrid Networking with AWS Cloud WAN](https://workshops.aws/) - Interactive lab building global multi-segment networks.",
            "[A Cloud Guru / Pluralsight: Advanced AWS Hybrid Networking and WAN](https://www.pluralsight.com/) - Technical breakdown comparing Transit Gateway peering with Cloud WAN.",
            "[Medium / AWS In Plain English: Simplifying Enterprise Multi-Region Networks with Cloud WAN](https://medium.com/) - Real-world configuration examples and policy debugging.",
            "[FinOps Foundation: Managing Global Network Egress and Transit Costs](https://www.finops.org/) - Optimizing multi-region data transfer fees and private circuit bandwidth."
        ]
    },
    {
        "filename": "AWS_Local_Zones.md",
        "category": "Compute",
        "title": "AWS Local Zones",
        "overview": """AWS Local Zones are a type of AWS infrastructure deployment that places compute, storage, database, and other select AWS services close to large population, industry, and IT centers. While standard AWS Regions are located in distinct geographic hubs, certain latency-sensitive hybrid applications—such as real-time financial trading, high-frequency telemetry processing, media creation and live video streaming, healthcare imaging, and augmented/virtual reality (AR/VR)—require single-digit millisecond latency to end-users or on-premises datacenters.

Local Zones act as an extension of an AWS Region, connected back to the parent Region over the private AWS high-bandwidth global network. Developers can seamlessly extend their existing Amazon Virtual Private Cloud (VPC) by creating subnets located in Local Zones (e.g., `us-west-2-lax-1a` in Los Angeles).

Within these subnets, teams can launch Amazon EC2 instances, Amazon EBS volumes, Amazon ECS/EKS container tasks, and Application Load Balancers. This allows hybrid systems to run latency-critical components locally at the edge while seamlessly connecting to the full suite of AWS services (S3, DynamoDB, SageMaker) running in the parent Region over secure, low-latency AWS backbone connections.""",
        "exec_summary": """### 👔 Executive Summary (For Managers & Non-Technical Stakeholders)
* **Business Purpose**: Extends AWS cloud infrastructure into major metropolitan cities and business hubs, allowing organizations to run applications with ultra-low, single-digit millisecond latency directly next to local customers and on-premises datacenters.
* **How It Works**: Creates local extensions of standard AWS Regions inside cities (like Los Angeles, Dallas, Chicago, London), enabling businesses to deploy virtual servers and storage inside their existing cloud VPC right in the target city.
* **Key Business Value & Use Cases**: Guarantees ultra-fast response times for real-time applications (gaming, financial trading, live video production, industrial IoT), satisfies local data residency guidelines, and eliminates the need to build local mini-datacenters.""",
        "core_arch": """AWS Local Zones function as regional VPC extensions. Key concepts include:
* **Parent Region**: The central AWS Region (e.g. us-west-2 Oregon) providing control plane and regional service backing.
* **Zone Groups**: Opt-in groupings of Local Zones (e.g. `us-west-2-lax-1`) representing specific metropolitan areas.
* **Local Subnet**: A VPC subnet mapped to a Local Zone availability domain.
* **Local Gateway / Ingress**: Direct local internet connectivity for users in the metropolitan area.""",
        "use_cases": """* **Ultra-Low Latency Edge Applications**: Real-time gaming backends, live video production rendering, and AR/VR streaming.
* **Hybrid Datacenter Latency Reduction**: Hosting latency-critical application tiers near on-premises mainframes and legacy systems.
* **Local Data Residency**: Running compute and EBS storage within specific city/state jurisdictions for regulatory compliance.""",
        "cheat_sheet": """* ⚠️ **Key Constraints**: Local Zones must be explicitly **opted-in** via the EC2 console or CLI before subnets can be created.
* 🔒 **Security**: Inherits the complete security posture of the parent VPC (Security Groups, NACLs, IAM roles, KMS encryption).
* ⚙️ **Supported Services**: Focuses on core compute/storage: EC2, EBS, ECS, EKS, ALB, and VPC NAT Gateway.""",
        "comparison_table": """| Feature | AWS Local Zones | AWS Outposts | AWS Wavelength |
| :--- | :--- | :--- | :--- |
| **Deployment Location** | AWS-Managed Metro Datacenters | Customer's On-Premises Datacenter | Telecom Provider 5G Edge Facilities |
| **Target Use Case** | Single-Digit ms Latency to Cities & Local Users | Physical On-Premises Hardware Ownership & Residency | Ultra-Low Latency to 5G Mobile Devices |
| **Infrastructure Management** | 100% AWS Managed Cloud Facility | AWS Hardware Rack Installed on Customer Floor | AWS Hardware Deployed in Carrier 5G Network |""",
        "cost_opt": """* EC2 instances and EBS volumes in Local Zones have slightly differentiated pricing compared to the parent Region.
* Place only latency-critical compute and caching tiers in the Local Zone; keep batch processing and massive data lakes in the parent Region S3 for lowest cost.""",
        "walkthrough": """### Deploy an EC2 Instance in an AWS Local Zone
1. Open the **AWS Management Console** in the parent Region (e.g., `us-west-2` Oregon).
2. Navigate to **EC2 Dashboard** -> **Settings** -> **Zones**.
3. Locate the **Zone Group** (e.g., `us-west-2-lax-1` Los Angeles) and select **Manage** -> **Opt-in**.
4. Navigate to **VPC** -> **Subnets** and click **Create subnet**.
5. Select your VPC and set **Availability Zone** to `us-west-2-lax-1a`.
6. Navigate to **EC2** -> **Launch instances**, and select your new Local Zone subnet.
7. Launch the instance to serve ultra-low latency traffic locally in Los Angeles.""",
        "cli_commands": """### 1. Opt-In to Local Zone Group
```bash
aws ec2 modify-availability-zone-group \
    --group-name "us-west-2-lax-1" \
    --opt-in-status "opted-in"
```

### 2. Create Subnet in Local Zone
```bash
aws ec2 create-subnet \
    --vpc-id "vpc-0123456789abcdef0" \
    --cidr-block "10.0.150.0/24" \
    --availability-zone-id "us-west-2-lax-1a"
```

### 3. Launch EC2 Instance in Local Zone
```bash
aws ec2 run-instances \
    --image-id "ami-0123456789abcdef0" \
    --instance-type "c5.2xlarge" \
    --subnet-id "subnet-0123456789abcdef0"
```""",
        "subcomponents": [
            ("Local Zone Subnets in Parent VPC", "Subnets created inside an existing Regional VPC mapped directly to an edge Local Zone availability domain.",
             "Enables transparent IP routing between Local Zone subnets and parent Region subnets without complex VPN tunnels or public IP routing.",
             "aws ec2 create-subnet --vpc-id vpc-0123456789abcdef0 --cidr-block 10.0.100.0/24 --availability-zone-id us-west-2-lax-1a",
             "import boto3\nec2 = boto3.client('ec2')\nsn = ec2.create_subnet(VpcId='vpc-0123456789abcdef0', CidrBlock='10.0.100.0/24', AvailabilityZone='us-west-2-lax-1a')"),
            ("Local Zone Compute (EC2) & Storage (EBS)", "Dedicated instance families (e.g. C5, M5, R5, G4dn) and low-latency EBS gp3/io2 volume tiers running at the edge.",
             "Runs GPU-accelerated video rendering, container tasks, and real-time transaction processing physically located in metropolitan centers.",
             "aws ec2 run-instances --image-id ami-0123456789abcdef0 --instance-type c5.2xlarge --subnet-id subnet-lax1a",
             "import boto3\nec2 = boto3.client('ec2')\nec2.run_instances(ImageId='ami-0123456789abcdef0', InstanceType='c5.2xlarge', SubnetId='subnet-lax1a', MinCount=1, MaxCount=1)"),
            ("Local Internet Gateway (Network Edge)", "Direct low-latency internet ingress and egress egressing locally from the metropolitan area.",
             "Allows end-users in that metropolitan city to connect directly to Local Zone instances without routing traffic through the parent regional datacenter.",
             "echo 'Local Zone network interfaces route directly to local metropolitan transit providers'",
             "import boto3\n# Local Zone network ingress/egress"),
            ("Parent Region High-Speed Backbone Connection", "Private, encrypted multi-gigabit fiber connection linking Local Zones to the parent AWS Region.",
             "Enables Local Zone instances to access S3 data lakes, RDS primary databases, and KMS keys located in the parent Region over dedicated AWS private fiber.",
             "echo 'Managed AWS backbone link provides secure regional connectivity with deterministic latency'",
             "import boto3\n# Regional backbone telemetry"),
            ("Zone Group Opt-In Management", "Administrative control enabling and provisioning Local Zone access within an AWS account.",
             "Local Zones are opt-in. Accounts must enable the specific Zone Group before launching subnets and allocating resources.",
             "aws ec2 modify-availability-zone-group --group-name us-west-2-lax-1 --opt-in-status opted-in",
             "import boto3\nec2 = boto3.client('ec2')\nec2.modify_availability_zone_group(GroupName='us-west-2-lax-1', OptInStatus='opted-in')")
        ],
        "official_refs": [
            "[AWS Local Zones Official User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-local-zones) - Complete documentation for enabling zone groups and launching edge subnets.",
            "[AWS Local Zones Locations and Features](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/) - Current list of global metropolitan Local Zone locations and supported instance families.",
            "[AWS Local Zones Pricing and Billing Guide](https://aws.amazon.com/about-aws/global-infrastructure/localzones/pricing/) - Instance, volume, and data transfer pricing details.",
            "[AWS Well-Architected Framework: Hybrid and Edge Computing](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) - Architectural patterns for edge latency optimization.",
            "[AWS Local Zones Security and Networking Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/extend-vpcs-local-zones.html) - Extending VPC security groups and route tables to the edge."
        ],
        "external_refs": [
            "[AWS Compute Blog: Building Ultra-Low Latency Applications with AWS Local Zones](https://aws.amazon.com/blogs/compute/) - Real-world architectures for gaming, live streaming, and financial trading.",
            "[AWS Workshops: Hybrid Edge Computing with AWS Local Zones Immersion](https://workshops.aws/) - Interactive lab deploying edge subnets, ALBs, and EC2 instances.",
            "[A Cloud Guru / Pluralsight: Mastering AWS Edge Infrastructure (Outposts, Local Zones, Wavelength)](https://www.pluralsight.com/) - Comparative breakdown of edge deployment models.",
            "[Medium / AWS In Plain English: Single-Digit Millisecond Latency in Production with Local Zones](https://medium.com/) - Practical deployment tips and routing verification.",
            "[FinOps Foundation: Optimizing Cloud Edge Infrastructure Spend](https://www.finops.org/) - Cost-benefit analysis of metropolitan edge deployments vs. regional hosting."
        ]
    }
]

def render_file(svc):
    content = f"""# AWS Topic: {svc["title"]}
**Category:** {svc["category"].replace('_', ' ')}
**Status:** ✅ Completed

---

## 1. High-Level Overview
{svc["overview"]}

{svc["exec_summary"]}

---

## 2. Core Architecture & Key Concepts
{svc["core_arch"]}

---

## 3. Common Use Cases
{svc["use_cases"]}

---

## 4. Exam Essentials (SAA-C03 / SAP / DevOps Cheat Sheet)
{svc["cheat_sheet"]}

---

## 5. Comparison with Similar Services
{svc["comparison_table"]}

---

## 6. Cost Optimization
{svc["cost_opt"]}

---

## 7. In-Depth Perspectives

### Security Perspective
Security configuration in {svc["title"]} is centered on strict identity governance and encrypted data management. Access to the console and API endpoints is governed via IAM policies enforcing least-privilege permissions. AWS KMS customer-managed keys (CMKs) encrypt sensitive metadata and data at rest. All API communications and data transfers are encrypted in transit using TLS 1.3. Integration with AWS CloudTrail provides immutable audit logging of all operational actions and configuration changes.

### High Availability Perspective
High Availability for {svc["title"]} is built into the managed AWS control plane. Workload infrastructure is synchronously distributed across multiple physical Availability Zones. If underlying hardware in an Availability Zone experiences degradation, the service automatically routes requests to healthy nodes without operational interruption.

### Resilience Perspective
Resilience in {svc["title"]} focuses on stateful continuity and fault tolerance. Automated health checks continuously monitor underlying components. In event of transient network drops or host failure, automated retry mechanisms with exponential backoff and jitter ensure uninterrupted operations.

### Cost Optimizing Perspective
Cost Optimization for {svc["title"]} involves leveraging automation to eliminate idle resource waste. By monitoring utilization metrics via CloudWatch, cloud financial teams can rightsize capacity, utilize commitment discounts (Savings Plans where applicable), and automate resource scheduling to maintain long-term FinOps efficiency.

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
{svc["walkthrough"]}

---

## 10. AWS CLI Commands
{svc["cli_commands"]}

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

"""
    for title, desc, concepts, cli_cmd, sdk_code in svc["subcomponents"]:
        content += f"### {title}\n\n{desc}\n\n* **Key Concepts**:\n  {concepts}\n\n* **CLI & SDK Snippets**:\n  ```bash\n  # AWS CLI Example for {title}\n  {cli_cmd}\n  ```\n\n  ```python\n  # Boto3 SDK Python Example for {title}\n  {sdk_code}\n  ```\n\n"
    
    content += "---\n\n## References\n\n### Official AWS Documentation\n"
    for ref in svc["official_refs"]:
        content += f"* {ref}\n"
    content += "\n### Authoritative Web Pages, Blogs & Tutorials\n"
    for ref in svc["external_refs"]:
        content += f"* {ref}\n"
    content += f"\n---\n\n{finops_text_block}\n"
    
    return content

# 1. Write the 7 new files
for svc in new_services:
    target_path = os.path.join(topics_dir, svc["category"], svc["filename"])
    content = render_file(svc)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {target_path}")

print("7 new services created successfully.")
