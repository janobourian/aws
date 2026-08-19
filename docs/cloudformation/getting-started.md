# Getting Started with CloudFormation

## Prerequisites

- AWS CLI configured
- Basic understanding of AWS services
- Text editor for YAML/JSON

## Your First Template

Create a simple S3 bucket:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'My first CloudFormation template'

Resources:
  MyS3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub '${AWS::StackName}-bucket-${AWS::AccountId}'

Outputs:
  BucketName:
    Description: 'Name of the S3 bucket'
    Value: !Ref MyS3Bucket
```

## Deployment Steps

1. **Save template** as `first-template.yaml`

2. **Deploy via CLI**:

```bash
aws cloudformation create-stack \
  --stack-name my-first-stack \
  --template-body file://first-template.yaml
```

1. **Check status**:

```bash
aws cloudformation describe-stacks --stack-name my-first-stack
```

1. **Clean up**:

```bash
aws cloudformation delete-stack --stack-name my-first-stack
```

## Next Steps

- Add parameters for customization
- Include multiple resources
- Use intrinsic functions
- Implement cross-stack references
