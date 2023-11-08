# IAM (Identity and Access Management)

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
    * Owner
    * All permissions
    * Don not use this user
* Team Members:
    * IAM Users
* Federated Users:
    * Identity Management Solution like Active Directory
* Application:
    * It uses Access Key and Secret Key
* External users:
* Cross Account Users
* Customers


## IAM Policy


## IAM Role

## IAM Full Picture

## Apendix

### CLI commands

```bash
aws iam list-users
aws iam help
```