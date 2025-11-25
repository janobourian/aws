# AWS CICD

## Continuous Integration and Continuous Deployment (CI/CD) on AWS

### CI

* Developers push the code to a code repository often.
* A testing / build server checks the code as soon as it is pushed
* Find bugs early, then fix bugs
* Delivery faster as the code is tested
* Deploy often
* Happier developers :D

### CD

* After the testing process you want to Deploy the code
* Deployment server in application server
* Ensure that the software can be released reliably whenever needed
* Ensure deployments happen oftan and are quick

### Techstack

* Github / BitBucket
    * Code
* AWS CodeBuild
    * Build
    * Test
* AWS CodeDeploy
    * Deploy
    * Provision
All the services are inside **AWS Codepipeline**

## CodeCommit

* Version control is the ability to understand the various changes that happened to the code over time (and possibly roll back)
* All these are enabled by using a version control system such as Git
* AWS CodeCommit is a fully-managed source control service that hosts secure Git-based repositories
* Benefits are:
    * Collaborate with other developers
    * Make sure the code is backed-up somewhere
    * Make sure it is fully viewable and auditable
* Security:
    * SSH Keys
    * HTTPS
    * IAM policies to manage users/role permissions to repositories
    * Encryption
    * Encrypted in transit
    * Cross-account Access with AWS STS 

## CodePipeline

* Visual WorkFlow to orchestrate your CICD:
    * Source - CodeCommit, ECR, S3, Bitbucket, GitHub
    * Build - CodeBuild, Jenkins, CloudBees, TeamCity
    * Test - CodeBuild, AWS Device Farm, 3rd party tools
    * Deploy - CodeDeploy, Elastic Beanstalk, CloudFormation, ECS, S3
    * Invoke - Lambda, Step Functions
    * Consists of stages:
        * Each stage can have sequential actons and/or parallel actions
        * Manual approval can be defined at any stage

* Artifacts stored in an S3 bucket and passed on to the next stage
    * output artifacts -> input artifacts

* Good points:
    * You can use stages for execution
    * Use CloudWatch Events (Amazon EventBridge)
        * You can create events for failed pipelines
        * You can create events for cancelled stages
    * If CodePipeline fails a stage, your pipeline stops, and you can get information in the console
    * AWS CloudTrail can be used to audit AWS API calls

## CodeBuild

* Source: CodeCommit, S3, Bitbucket, Github
* You can cache the dependencies using Amazon S3
* Build instructions:
    * Code file `buildspec.yml` or insert manually in Console
* Output Logs:
    * can be stores in Amazon S3 and CloudWatch Logs
* Build Projects can be defined within CodePipeline or CodeBuild
* Supported Environments:
    * Java, Ruby, Python, Go, Node.js, Android, .Net Core, PHP, Docker
* CodeBuild:
    * buildspec.yml: file must be at the root of your code
    * env:
        * variables
        * parameter-store
        * secret-manager
    * phases
        * install
        * pre_build
        * Build: actual builds commands
        * post_builds
    * artifacts
    * cache

## CodeDeploy

* We can automate application deployments
* Deploy to EC2, Lambda, On-Premises servers, ECS Services
* Automated Rollback
* Deployment Strategies:
    * In-Place Deployments
    * Blue/Green Deployments
* A file named `appspec.yml` defines how the deployment happens

### Deploy strategies

* In-Place Deployment
    * Half At a Time
* Blue-Green Deployment

### EC2 Deployment - Deploy Agent

* The CodeDeploy Agent must be running on the EC2 instances as a pre-requisites
* You can manage it through System Manager
* The EC2 instances must have enough permissions to access Amazon S3
* You must have correct tags to identify the environments

### Lambda Platform

* CodeDeploy can help you automate traffic shift for Lambda aliases
* No Agent required
* The Lambda function must have enough permissions to access Amazon S3
* Feature integrated within the SAM framework
* Strategies:
    * Linear: grow traffic every N minutes until 100%
        * LambdaLinear10PercentEvery3Minutes
        * LambdaLinear10PercentEvery10Minutes
    * Canary: try X percent then 100%
        * LambdaCanary10Percent5Minutes
        * LambdaCanary10Percent30Minutes
    * AllAtOnce: immediate

### ECS Platform

* CodeDeploy can help you automate deployments for ECS services
* No Agent required
* The ECS tasks must have enough permissions to access Amazon S3
* Strategies:
    * Blue/Green Deployments only
        * Linear
        * Canary
        * AllAtOnce

### Deployment to EC2

* In-place deployment:
    * Updates existing EC2 instances
    * Newly created EC2 instances by an ASG will also get automated deployment
* Blue/Green Depoyment:
    * A new Auto-Scaling Group is created
    * Choose how long to keep the old EC2 instances
    * Must be using an ELB

### Redeploys and Rollbacks

* Rollback: redeploy a previuosly deployed revision of your application
* Redeploy: deploy the same revision again
* Deployment can be rolled back:
    * Automatically
    * Manually
* Disable Rollbacks: do not perfom rollbacks for this deployment
* If a roll back happens, CodeDeploy redeploys the last known good revision as a new deployment (not a restored version)

## CodeArtifact

* Software packages depen on each other to be built
* Storing and retrieving these dependencies is called artifact management
* Developers and CodeBuild can then retrieve dependencies straight from CodeArtifact

### CodeArtifact - EventBridge Integration

* Event is created when a Package version is created, modified, or deleted.
* It allows use CrossAccount read packages
* You can configure domain or repository policies

## CodeGuru

* Is an ML-powered service for automated code reviews and application performance recommendations
* It provides two functionalities:
    * CodeGuru Reviewer: automatesd code reviews for static code analysis (development)
    * CodeGuru Profiler: visibility/recommendations about application performance during runtime (production). It supports applications running on AWS or on-premise