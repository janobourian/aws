# IAM and AWS CLI

* IAM = Identity and Access Management, Global Service
* Root account created by default, should not be used or shared
* Users are people within your organization, and can be grouped
* Groups only contain users, not other groups
* User can belong to multiple groups

* IAM: Permissions
    * JSON document called policies
    * VIS - SEPARC

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
  * CLI (Using Access Keys)
  * SDK (AWS Software Development Key)

```bash
aws help
aws <command> help
aws <command> <subcommand> help
aws iam list-users
```

* Roles:
  * Permissions for AWS Services
  * Common roles:
    * EC2
    * Lambda Functions
    * CloudFormation

* IAM Security Tools:
  * IAM Credentials Report (account-level)
  * IAM Access Advisor (user-level) / IAM Access Analyzer

* IAM Guidelines and Best Practices
  * Do not use your root account
  * One physical user = One AWS user
  * Assing users to groups
  * Create a strong password policy
  * Activate MFA
  * Create and use Roles for AWS Services
  * Use Access Keys for programmatic Access
  * Audit permissions