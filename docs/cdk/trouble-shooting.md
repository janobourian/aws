# Some guidelines to resolve potential problems

## About the credentials

You can use CloudShell to generate temporary credentials to assume roles, but first you need to create a role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::XXXXXXXXXXXX:user/XXXXXXXXX"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

```bash
XXXXXXXXX.json
aws iam create-role --role-name general-role-janobourian --assume-role-policy-document file://XXXXXXXXXX.json
```

Now you can assume the role:

```bash
aws sts assume-role --role-arn arn:aws:iam::XXXXXXXX:role/general-role-janobourian --role-session-name janobourian-session
```

### Create MFA

```bash
aws iam create-virtual-mfa-device --virtual-mfa-device-name MyUserMFA --outfile /Users/frgonzal/Documents/mfa_qr_code.png --bootstrap-method QRCodePNG
aws iam create-virtual-mfa-device --virtual-mfa-device-name MyUserMFA --outfile /Users/frgonzal/Documentsmfa_qr_code.png
aws iam enable-mfa-device --user-name <IAM-username> --serial-number <MFA-device-ARN> --authentication-code1 <first-MFA-code> --authentication-code2 <second-MFA-code>

```
