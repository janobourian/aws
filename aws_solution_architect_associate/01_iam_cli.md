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

```bash
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