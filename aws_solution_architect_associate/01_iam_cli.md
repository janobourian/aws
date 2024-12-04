# IAM and AWS CLI

* IAM = Identity and Access Management, Global Service
* Root account created by default, should not be used or shared
  * One AWS Account = One User
* Users are people within your organization, and can be grouped
* Groups only contain users, not other groups
* User can belong to multiple groups
* In AWS you apply the least privilige principle
* You can change the account name using a verbose name instead of twelve digits

* IAM: Permissions
    * JSON document called policies
    * VIS - SEPARC
      * VIS: 
        * Version: "2012-10-17"
        * Id: an identifier
        * Statement: [{}]
      * SEPARC: 
        * Sid: an statement-identifier
        * Effect: Allow, Deny
        * Principal: account, user, root
        * Action: list of actions, examples:
          * s3:Get*
          * s3:List*
        * Resource: []
        * Condition: {}

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "UsePrincipalArnInsteadOfNotPrincipalWithDeny",
      "Effect": "Deny",
      "Action": "s3:*",
      "Principal": "*",
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket/*",
        "arn:aws:s3:::amzn-s3-demo-bucket"
      ],
      "Condition": {
        "ArnNotEquals": {
          "aws:PrincipalArn": "arn:aws:iam::444455556666:user/user-name"
        }
      }
    }
  ]
}
```

* Points to mantain safe your account:
    * Password Policy
    * Activate MFA
        * Virtual MFA
        * Universal 2nd Factor (U2F) Security Key (USB)
        * Harwdare Key For MFA Device
        * Hardware Key For MFA device for AWS Gov

* Ways to connect with AWS
  * Console
    * You also can use CloudShell
  * CLI (Using Access Keys):
    * aws configure (to configure Access Keys)
  * SDK (AWS Software Development Key)

```bash
aws help
aws <command> help
aws <command> <subcommand> help
aws iam list-users
aws iam create-user help
```

* Roles:
  * Permissions for AWS Services
  * Common roles:
    * EC2
    * Lambda Functions
    * CloudFormation

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sts:AssumeRole"
      ],
      "Principal": {
        "Service": [
          "ec2.amazonaws.com"
        ]
      }
    }
  ]
}
```

* IAM Security Tools:
  * IAM Credentials Report (account-level)
  * IAM Access Advisor (user-level) / IAM Access Analyzer
  * IAM LastAccess (by user)

* IAM Guidelines and Best Practices
  * Do not use your root account
  * One physical user = One AWS user
  * Assing users to groups
  * Create a strong password policy
  * Activate MFA
  * Create and use Roles for AWS Services
  * Use Access Keys for programmatic Access
  * Audit permissions

## AWS Organizations

* Global Services
* Organizational Units:
  * By business unit
  * By environmental Lifecycle
  * By project
* Allows to manage multiple AWS accounts
* Management account / Member account
* Member account can only be part of one organization
* Benefits:
  * Consolidated Billing across all accounts
  * Pricing benefits from aggregated usage
  * Shared reserved instances and Saving Plans discounts across accounts
  * API is available to automate AW account creation
* Advantages:
  * Multi account vs One account Multi VPC
  * Use tagging standards for billing purposes
  * Enable CloudTrail on all accounts, send logs to central S3 account
  * Send CloudWatch Logs to central logging account
  * Establish Cross Account Roles for Admin purposes
* Security Control Policies (SCP):
  * IAM policies applied to OU
  * Management account has full admin power
  * It does not allow anything by default

### Hands-on

* You can create a new account or send an invitation
* You can create Organizational Units
* You can create a Secury Control Policies
  * FullAWSPolicy
  * Example:
    * DenyS3Service

## IAM Conditions

There are some examples:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": [
            "192.0.2.0/24",
            "203.0.113.0/24"
          ]
        }
      }
    }
  ]
}
```

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "ec2:*",
        "rds:*",
        "dynamodb:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": [
            "eu-central-1",
            "eu-west-1"
          ]
        }
      }
    }
  ]
}
```

* IAM for S3 
  * s3:ListBucket permission applies to arn:aws:s3:::test -> bucket level permission
  * s3:GeObject permission applies to arn:aws:s3:::test/* -> object level permission

* Case with AWS Organization for s3 bucket, only AWS Organization members can perform operations in this bucket

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::2022-financial-data/*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": [
            "o-yyyyyyyyy"
          ]
        }
      }
    }
  ]
}
```

## Resource-based Policies versus IAM Roles

* Case one:
  * Account A -> IAM Role -> S3 Bucket
* Case two:
  * Account A -> Resource-based Policy -> S3 Bucket

In case of EventBridge you can invoke resources with Resource-based Policy, but in some resources such as Kinesis stream, EC2 Auto Scaling, Systems Manager Run Command, ECS task you are going to need IAM role

* Policy Boundaries limit the users actions
* IAM Policy Evaluation Logic:
  * Deny Evaluation
  * Organizations SCP (Secure Control Policy)
  * Resource-based policies
  * Identity-based policies
  * IAM permissions boundaries
  * Sessions policies

## AWS IAM Identity Center

* Single Sign-On
* You Can connect with SAML-2.0 Applications
* Permissions assignments:
  * Multi-Account Permissions
  * Application Assignments
  * Attribute-Based Access Control (ABAC)