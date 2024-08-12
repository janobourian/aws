# Identity and Access Management

To test policies: https://policysim.aws.amazon.com/

AAA: Authentication, Authorization, Audit

* To access:
    * Console
    * CLI
    * SDK

* Key concepts:
    * IAM User
    * IAM Group
    * IAM Role
    * IAM Policy

* Six types of policies:
    * Identity-based policies:
        * Maged AWS Policies
        * Customer-managed policies
        * Inline policies
    * Resource-based policies
    * Permission boundaries
    * Organization Service Control Policies (SCPs)
    * Access Control Lists (ACLs)
    * Session Policies

* SEPARC:
    * Statement
    * Effect
    * Principal
    * Action
    * Resource 
    * Condition

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Resource": "*"
        }
    ]
}
```

* ARN: Amazon Resource Name:
    * arn:partition:service:region:account-id:resource-id
    * arn:partition:service:region:account-id:resource-type/resource-id
    * arn:partition:service:region:account-id:resource-type:resource-id

* IAM Roles:
    * When an aws service in your account want to access to another service in the same aws account
    * For IAM user in another account needs to access to services in your account via cross-account access
    * A federated user from another web Identity Provider (Idp)
    * A federated corporate user using an identity service such as Microsoft Active Directory

1.- A, B
2.- B
3.- A
4.- B
5.- A
6.- A
7.- A
8.- A
9.- C
10.- B