# Getting Started with AWS DevOps

## Prerequisites

- AWS account with appropriate permissions
- Basic understanding of Git and CI/CD concepts
- Application code in a repository

## Key concepts about DevOps:

* Continuous Integration
* Continuous Delivery
* Infrastructure as Code
* Monitoring and logging
* Communication and collaboration
* Security

## AWS Well-Architected Framework

* Operational Excellence
* Security
* Reliability
* Performance
* Cost-effective
* Sustainability

## Setting Up Your First Pipeline

### Step 1: Create a CodeCommit Repository

```bash
aws codecommit create-repository --repository-name my-app
```

### Step 2: Create a buildspec.yml

```yaml
version: 0.2
phases:
  install:
    runtime-versions:
      nodejs: 18
  pre_build:
    commands:
      - npm install
  build:
    commands:
      - npm run build
  post_build:
    commands:
      - echo Build completed
artifacts:
  files:
    - '**/*'
  base-directory: dist
```

### Step 3: Create CodeBuild Project

```bash
aws codebuild create-project \
  --name my-app-build \
  --source type=CODECOMMIT,location=https://git-codecommit.region.amazonaws.com/v1/repos/my-app \
  --artifacts type=S3,location=my-build-artifacts \
  --environment type=LINUX_CONTAINER,image=aws/codebuild/amazonlinux2-x86_64-standard:3.0 \
  --service-role arn:aws:iam::account:role/CodeBuildServiceRole
```

### Step 4: Create CodePipeline

```json
{
  "pipeline": {
    "name": "my-app-pipeline",
    "roleArn": "arn:aws:iam::account:role/CodePipelineServiceRole",
    "stages": [
      {
        "name": "Source",
        "actions": [
          {
            "name": "Source",
            "actionTypeId": {
              "category": "Source",
              "owner": "AWS",
              "provider": "CodeCommit",
              "version": "1"
            },
            "configuration": {
              "RepositoryName": "my-app",
              "BranchName": "main"
            },
            "outputArtifacts": [{"name": "SourceOutput"}]
          }
        ]
      },
      {
        "name": "Build",
        "actions": [
          {
            "name": "Build",
            "actionTypeId": {
              "category": "Build",
              "owner": "AWS",
              "provider": "CodeBuild",
              "version": "1"
            },
            "configuration": {
              "ProjectName": "my-app-build"
            },
            "inputArtifacts": [{"name": "SourceOutput"}],
            "outputArtifacts": [{"name": "BuildOutput"}]
          }
        ]
      }
    ]
  }
}
```

## Next Steps

- Add automated testing stages
- Implement deployment to multiple environments
- Set up monitoring and alerting
- Configure approval gates for production deployments