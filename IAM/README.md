# IAM (Identity and Access Management)

Identity and access management is a Global service and it manages who can do what.

## Introduction

We have basic steps:

* User:
    * Access Key
    * Credentials
* Group Policy:
    * Statement ID
    * Effect
    * Action
    * Resource
    * Principal
* Role:
    * Assume Role
    * Cross Account
    * Federated Access
* AWS Organization:
    * Service Control Policy
* Policy Evaluation Logic

## IAM Users and Groups

User: someone or something that can access aws resources. 

You have to option for your new user:
* Programmatic access:
    * Pair of access credentials
* AWS Management Console Access:
    * The user has access to console via email and password

Root user:
* Email
* Password

IAM User:
* Account_ID
* Email
* Password

Max users by account: 5000

### Real World Users

Type of users:
* Root User:
    * One per account
    * Owner
    * Able to delete account
    * All permissions
    * Don not use this user
* Team Members:
    * A set of IAM Users
* Federated Users:
    * Identity Management Solution like Active Directory
    * MyCorporation/Jane + Password
    * A single sign on to access some AWS Services
* Application:
    * It uses Access Key and Secret Key
    * SDK and APIs communications doesn't allow User + Password
* External users:
    * Venders, Consultants and Partnerships
* Cross Account Users
* Customers

### Access Key

* AWS CLI (Command Line Interface)
* AWS SDK (Software Development Kit)

You can have up to two access keys.

### IAM Group

Steps:
* Group name
* Attach policy 
* Review

You can add users in a group using the Group menu or the User menu.
User can belong up to ten groups and a group can have another group.
Account has up to 300 IAM Groups. 

## IAM Policy

### Introduction

IAM Policy is Authorization, that means all actions that one user can do.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:us-east-1:153266797400:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:us-east-1:153266797400:log-group:/aws/lambda/get_s3_update:*"
            ]
        }
    ]
}
```

Exits two types of Policies:
* Customer Managed Policy (You can create, edit, delete)
* AWS Managed Policy (Read Only)

### IAM policy structure

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Statement1",
			"Effect": "Allow",
			"Action": [],
			"Resource": []
		}
	]
}
``` 

SEPARC. 

* Version: The version
* Statement: A list of policies, the main or root part in the JSON structure
* Sid (Statement ID): It needs to be unique and is a good way to retrieve information fast.
* Effect: It has two values "Deny" and "Allow", by default explicit "Deny" override "Allow" policy.
* Principal:
* Action:To specify action related with an AWS Resources.
    * "ServicePrefix:Action" -> "S3:ListBucket" Check the next [link](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html)
    * Action: ["S3:DeleteBucket", "S3:CreateBucket", "S3:ListBucket"]
    * Action: ["S3:*" ]
    * Action: ["S3:Get*" ]
    * Action: ["S3:\*Bucket\*" ] 
    * Action: ["*" ]
* Resource: 
    * ARN: Amazon Resource Name
        * arn:partition:service:region:account-id:resource-id/path
        * arn:aws:cloud9:us-east-1:153289687400:environment:4567
    * Resource: ["*" ]
    * ? <- Question mark means one character after the string, only one character.
        * arn:aws:cloud9:us-east-1:153289687400:environment:456? 
    * Action needs a Resource Type (*Required)
* Condition:
    * {"{condition-operator}": {"{condition-key}":"{condition-value}"}}
    * {"StringEquals": {"aws:username":"janobourian"}}
    * Some conditions:
        * StringEquals
        * StringEqualsIgnoreCase
    * condition-operator: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html
    * condition-key: 
        * Global: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html
        * Service: https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html#context_keys_table
    * Tag Based Policy:
        * {"DataSecurity" : "General"}
        * {"DataSecurity" : "Confidential"}
        * {"DataSecurity" : "Secret"}
        * {"DataSecurity" : "General"}
        * None

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "S3Policy",
			"Effect": "Allow",
			"Action": [
				"S3:DeleteObject",
				"S3:GetBucketLocation",
				"S3:GetObject*"
			],
			"Resource": [
				"arn:aws:s3:::janobourian-demo-*"
			], 
			"Condition": {
			    "StringEquals": {
			        "aws:username": [
                        "janobourian",
                        "bob",
                        "jenny"
                    ],
                    "aws:principaltype": [
                        "User",
                        "FederatedUser"
                    ],
                    "s3:ExistingObjectTag/DataSecurity": [
                        "General"
                    ]
			    },
                "DateGreaterThan":{
                    "aws:CurrentTime": "2019-10-15T12:00:00Z"
                }
			}
		},

	]
}
``` 

## IAM Role

## IAM Full Picture

## CLI commands

```bash
aws configure
aws iam list-users
aws iam help
aws s3api create-bucket --bucket janobourian-demo-03 --region us-east-1
aws s3 ls
aws s3 ls janobourian-demo-01
aws s3api get-object --bucket janobourian-demo-01 --key <file_name>
aws s3api get-object-tagging --bucket janobourian-demo-01 --key <file_name>
```