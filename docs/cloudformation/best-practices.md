# CloudFormation Best Practices

## Template Design

### Use Parameters

```yaml
Parameters:
  Environment:
    Type: String
    AllowedValues: [dev, staging, prod]
    Default: dev
```

### Organize with Nested Stacks

Break large templates into smaller, reusable components.

### Use Mappings for Environment-Specific Values

```yaml
Mappings:
  EnvironmentMap:
    dev:
      InstanceType: t3.micro
    prod:
      InstanceType: t3.large
```

## Security

- **Use IAM roles** instead of embedding credentials
- **Enable stack termination protection** for production
- **Use least privilege** for CloudFormation service role
- **Validate templates** before deployment

## Resource Management

### Naming Conventions

```yaml
Resources:
  WebServerInstance:
    Type: AWS::EC2::Instance
    Properties:
      Tags:
        - Key: Name
          Value: !Sub '${AWS::StackName}-web-server'
```

### Use DeletionPolicy

```yaml
Resources:
  Database:
    Type: AWS::RDS::DBInstance
    DeletionPolicy: Snapshot
```

## Deployment Strategies

- **Use change sets** to preview changes
- **Implement blue/green deployments** for zero downtime
- **Tag resources** consistently
- **Monitor stack events** during deployment

## Version Control

- Store templates in Git
- Use semantic versioning
- Document template changes
- Implement code reviews
