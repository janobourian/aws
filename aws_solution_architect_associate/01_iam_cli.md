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
        * Harwdare Key Fob MFA Device
        * HArdware Key Fob MFA device for AWS Gov

