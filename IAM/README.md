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


## IAM Role

## IAM Full Picture

## Apendix

### CLI commands

```bash
aws configure
aws iam list-users
aws iam help
aws s3api create-bucket --bucket janobourian-demo-03 --region us-east-1
aws s3 ls
aws s3 ls janobourian-demo-01
```