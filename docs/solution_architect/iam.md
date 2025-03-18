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
        * Hardware Key Fob MFA Device
        * Hardware Key Fob MFA Device for AWS GovCloud

## Identity and Access Management (IAM) - Advanced