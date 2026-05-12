# IAM services

## Identity and Access Management and AWS CLI

IAM is a global service.

* Basic concepts
    * Root account
    * Users
    * Groups
    * Roles
    * IAM: Permissions
        * Users or Groups can be assigned JSON documents called policies
        * These policies define the permissions of the users
        * least privilege principle
        * VIS - SEPARC
            * VIS
                * Version
                * Id
                * Statement
            * SEPARC
                * Sid
                * Effect
                * Principal:
                    * account/user/role to which this policy applied to
                * Action 
                * Resource
                * Condition

### The administrator access

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

### MFA - Multi Factor Authentication

* Password Policy
    * Password length
    * Password expiration
    * Prevent password re-use

* MFA:
    * MFA = password you know + security device you own => Succesful login
    * Options:
        *   Virtual MFA device
            * Google Authenticator
            * Authy
        * Universal 2nd Factor (U2F) Security Key
            * Yubikey
        * Hardware Key For MFA Device
        * Hardware Key For MFA Device for AWS GovCloud

* Password policy:
    * IAM > Account Settings

* MFA:
    * In the top right menu
    * Security Credentials

### Access Keys, CLI and SDK

* AWS Management Console
    * Protected by Password + MFA
* AWS Command Line Interface (CLI)
    * Protected by Access Keys
* AWS Software Development Kit (SDK)
    * Protected by Access Keys

* Users manage their own access keys

#### Hands On

Start the CLI configuration

```bash
aws configure
Access Key ID
Secret Access Key 
Region `us-east-1`
Output `json`
```

The next exercises are using `CloudShell` 

```bash
aws --version
aws iam list-users
```

You can update and download files on `CloudShell`

### IAM Roles

To do so, we will assign permissions to AWS services with IAM Roles.

Common Roles:
    * EC2 Instance Roles
    * Lambda Function Roles
    * CloudFormation

#### Trusted entities

Who can use the role in Principal, this is not the role permissions, is the Trust relationships.

```json
{
    "Version": "2012-10-17",
    "Id": "something",
    "Statement":[
        {
            "Sid": "something_nested",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "ec2.amazonaws.com"
                ]
            },
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": "*",
            "Condition": ""
        }
    ]
}
```

### IAM Security Tools

* IAM Credentials Report (account-level)
* Access Analyzer (user-level)

### IAM Guidelines & Best Practices

* Do not use the root account except for AWS account setup
* One physical user = One AWS user
* Assign users to groups and assign permissions to groups
* Create a strong password policy
* Use and enforce the use of MFA
* Create and use Roles for giving permissions to AWS services
* Use Access Keys fro Programmatic Access (CLI/SDK)
* Audit permissions of your account using IAM Credentials Report and Access Analyzer
* Never share IAM users and Access Keys

## Identity and Access Management (IAM) - Advanced

### Organizations

* Global Service
* Allows to manage multiple AWS accounts
* Consolidated Billing across all accounts - single payment method
* Pricing benefits from aggregated usage
* Shared reserved instances and Savings Plans
* Main Account is the management account, other accounts are member accounts
* API is available to automate AWS account creation
* OU: Organizational Unit

* Nested Organization:
    * Root Organizational Unit: Management Account
        * Dev Organizational Unit: Member Accounts
        * Prod Organizational Unit: 
            * Human Resources Organizational Unit:
            * Finance Organizational Unit

* Ways to create Organizational Units:
    * Business Unit
        * Sales
        * Retail
        * Finance
    * Environmental Lifecycle
        * Prod
        * QA
        * Dev
    * Project-Based
        * Project 1
        * Project 2
        * Project 3

* Advantages:
    * Multi account vs One account Multi VPC
    * Use tagging standards for billing purposes
    * Enable CloudTrail on all accounts, send logs to central S3 account
    * Send CloudWatch Logs to central logging account 
    * Establish Cross Account Roles for Admin purposes

* Security: Service Control Policies (SCP)
    * IAM policies applied to OU or Accounts to restrict Users and Roles
    * They do not apply to the management account (full admin power)
    * Must have an explicit allow from the root through each OU in the direct path to the target account (does not allow anything by default - like IAM)

### Advanced Policies

#### IAM Conditions

* aws:SourceIp - restrict the client IP from which the API calls are being made

Example:

```json
{
    "Version":"2012-10-17",
    "Id":"AWSPolicy",
    "Statement":[
        {
            "Sid":"AllowSomeResources",
            "Effect":"Deny",
            "Principal":"",
            "Action":"*",
            "Resource":"*",
            "Condition":{
                "NotIpAddress"{
                    "aws:SourceIp":["192.0.2.0/24","203.0.113.0/24"]
                }
            }
        }
    ]
}
```

* aws:RequestedRegion - restrict the region the API calls are made to

Example:

```json
{
    "Version":"2012-10-17",
    "Id":"AWSPolicy",
    "Statement":[
        {
            "Sid":"AllowSomeResources",
            "Effect":"Deny",
            "Principal":"",
            "Action":"*",
            "Resource":"*",
            "Condition":{
                "StringEquals"{
                    "aws:RequestedRegion":["eu-central-1","eu-west-1"]
                }
            }
        }
    ]
}
```

* ec2:ResourceTag - restrict based on tags

Example:

```json
{
    "Version":"2012-10-17",
    "Id":"AWSPolicy",
    "Statement":[
        {
            "Sid":"AllowSomeResources",
            "Effect":"Allow",
            "Action":["ec2:startInstances", "ec2:stopInstances"],
            "Resource":"arn:aws:ec2:us-east-1:123456789012:instance/*",
            "Condition":{
                "StringEquals"{
                    "ec2:ResourceTag/Project": "DataAnalytics",
                    "aws:PrincipalTag/Department": "Data"
                }
            }
        }
    ]
}
```

* aws:MultiFactorAuthPresent - to force MFA

Example:

```json
{
    "Version":"2012-10-17",
    "Id":"AWSPolicy",
    "Statement":[
        {
            "Effect":"Allow",
            "Action":"ec2:*",
            "Resource":"*"
        },
        {
            "Effect":"Deny",
            "Action":["ec2:startInstances", "ec2:stopInstances"],
            "Resource":"*",
            "Condition":{
                "BoolIfExists":{
                    "aws:MultiFactorAuthPresent":false
                }
            }
        }
    ]
}
```

* IAM for S3 policy level:
    * object level
    * bucket level

* Resource Policies and aws:PrincipalOrgID
    * aws:PrincipalOrgID can be used in any resource policies to restrict access to accounts that are member of an AWS Organization

Example:

```json
{
    "Condition": {
        "StringEquals": {
            "aws:PrincipalOrgID": ["o-yyyyyyyyyy"]
        }
    }
}
```

### Resource-based Policies vs IAM Roles

* Cross-account:
    * attaching a resource-based policy to a resource (example: S3 bucket policy)
    * OR using a role as a proxy

* Cases:
    * User Account A -> Role Account B -> Amazon S3
    * User Account A -> S3 Bucket Policy -> Amazon S3

* Important notes:
    * When you assume a role, you give up your original permissions and take the permissions assigned to the role
    * When using a resource-based policy, the principal does not have to give up his permissions

* Disclaimer about Event Bridge:
    * EventBridge rule and Resource-based policy
        * Lambda, SNS, SQS, S3 bucket, API Gateway
    * EventBridge rule and IAM role to assume
        * Kinesis Stream, EC2 Auto Scaling, System Manager Run Command, ECS Task

### Policy Evaluation Logic

#### IAM Permission Boundaries

* IAM Permission Boundaries are supported for users and roles (not groups)
* Advanced feature to use a manged policy to set the maximum permissions and IAM entity can get
* Example: 
    * IAM Permission Boundary + IAM Permissions Trhough IAM Policy

#### IAM Policy Evaluation Logic

* Deny Evaluations
* Organizations Service Control Policy
* Resource-based policies -> Review the resource-based policy in the resource
* Identity-based policies -> IAM roles
* IAM permissions boundaries
* Session policies

### IAM Identity Center

* SSO: single sign-on
* One login (single sign-on) for all your
* Identity providers
    * Built-in identity store in IAM Identity Center
    * Third party: Active Directory (AD), OneLogin, Okta
* Login Flow:
    * Login
    * AWS IAM Identity Center
    * SSO to access:
        * AWS Cloud
        * Business Cloud Apps
        * Custom SAML2.0-enabled Apps

### Directory Services

* What is Microsoft Active Directory (AD)?
    * AWS Managed Microsoft AD
        * auth -> AWS Managed AD -> trust -> On-prem AD -> auth
    * AD Connector
        * auth -> AD Connector -> proxy -> On-prem AD
    * Simple AD
        * Simple AD

### Control Tower

* Easy way to set up and govern a secure and compliant multi-account AWS environment based on best practices
* AWS Control Tower uses AWS Organizations to create accounts
* Benefits:
    * Automate the set up your environment in a few clicks
    * Automate ongoing policy management using guardrails
    * Detect policy violations and remediate them
    * Monitor compliance through an interactive dashboard

* AWS Control Tower - Guardrails
    * Preventive Guardrail - using SCPs (e.g, Restrict Regions across all your accounts)
    * Detective Guardrail - using AWS Config (e.g., Identify untagged resources)