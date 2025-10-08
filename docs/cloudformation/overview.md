# CloudFormation Overview

## What is AWS CloudFormation?

AWS CloudFormation is a service that helps you model and set up your AWS resources using Infrastructure as Code (IaC). You create templates that describe your AWS resources, and CloudFormation provisions and configures those resources for you.

## Key Concepts

### Templates
JSON or YAML files that define your infrastructure resources and their properties.

### Stacks
A collection of AWS resources that you can manage as a single unit.

### Change Sets
Preview changes to your stack before implementing them.

## Benefits

- **Infrastructure as Code**: Version control your infrastructure
- **Consistency**: Deploy identical environments repeatedly
- **Cost Control**: Easy to estimate costs and delete entire environments
- **Automation**: Reduce manual errors and deployment time

## Template Structure

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Template description'
Parameters:
  # Input parameters
Resources:
  # AWS resources to create
Outputs:
  # Values to return
```

## Common Use Cases

- Multi-tier web applications
- Development/staging environments
- Disaster recovery setups
- Compliance and governance

## Important Links

* [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)