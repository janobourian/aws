# AWS DevOps Best Practices

## Source Control

### Repository Structure

```text
my-app/
├── src/
├── tests/
├── buildspec.yml
├── appspec.yml
├── cloudformation/
└── README.md
```

### Branching Strategy

- Use feature branches for development
- Implement pull request reviews
- Protect main branch with required checks
- Tag releases for version tracking

## Build Practices

### Buildspec Configuration

```yaml
version: 0.2
env:
  variables:
    NODE_ENV: production
phases:
  install:
    runtime-versions:
      nodejs: 18
    commands:
      - npm ci
  pre_build:
    commands:
      - npm run lint
      - npm run test
  build:
    commands:
      - npm run build
  post_build:
    commands:
      - echo Build completed on `date`
artifacts:
  files:
    - '**/*'
  base-directory: dist
cache:
  paths:
    - node_modules/**/*
```

### Build Optimization

- Use build caching to speed up builds
- Run tests in parallel when possible
- Fail fast on critical errors
- Store build artifacts efficiently

## Deployment Strategies

### Blue/Green Deployment

```yaml
## appspec.yml for CodeDeploy
version: 0.0
os: linux
hooks:
  BeforeInstall:
    - location: scripts/install_dependencies.sh
      timeout: 300
  ApplicationStart:
    - location: scripts/start_server.sh
      timeout: 300
  ApplicationStop:
    - location: scripts/stop_server.sh
      timeout: 300
```

### Rolling Deployments

- Deploy to small percentage of instances first
- Monitor health metrics during deployment
- Implement automatic rollback on failures

## Security

### IAM Best Practices

- Use least privilege principle
- Create service-specific roles
- Regularly audit permissions
- Use temporary credentials

### Secrets Management

```yaml
## Use Parameter Store or Secrets Manager
environment:
  variables:
    DB_HOST: !Ref DatabaseEndpoint
  parameter-store:
    DB_PASSWORD: /myapp/prod/db/password
```

## Monitoring and Alerting

### CloudWatch Metrics

- Monitor build success/failure rates
- Track deployment duration
- Set up alerts for pipeline failures
- Monitor application performance

### Logging Strategy

```yaml
## CloudWatch Logs integration
version: 0.2
phases:
  build:
    commands:
      - echo "Build started" | tee /tmp/build.log
      - npm run build 2>&1 | tee -a /tmp/build.log
reports:
  test-reports:
    files:
      - test-results.xml
    file-format: JUNITXML
```

## Pipeline Design

### Multi-Environment Strategy

```text
Source → Build → Test → Deploy-Dev → Deploy-Staging → Manual-Approval → Deploy-Prod
```

### Parallel Execution

- Run independent tests in parallel
- Deploy to multiple regions simultaneously
- Use fan-out patterns for efficiency

## Cost Optimization

- Use spot instances for build environments
- Implement build caching
- Clean up unused resources automatically
- Monitor and optimize pipeline costs
