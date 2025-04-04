# Solution Architect SAA-C03

## Identity and Access Management and AWS CLI

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
                * Principal
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
    
### Access Keys, CLI and SDK

* AWS Management Console
* AWS Command Line Interface (CLI)
* AWS Software Development Kit (SDK)

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

To do so, we eill assign permissions to AWS services with IAM Roles.

Common Roles:
* EC2 Instance Roles
* Lambda Function Roles
* CloudFormation

#### Trusted entities

Who can use the role in Principal

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

### Resource-based Policies vs IAM Roles

### Policy Evaluation Logic

### IAM Identity Center

### Directory Services

### Control Tower
