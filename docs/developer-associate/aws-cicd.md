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
        * Build: actual buils commands
        * post_buils¿d
    * artifacts
    * cache

## CodeDeploy

## CodeStar

## CodeArtifact

## CodeGuru

