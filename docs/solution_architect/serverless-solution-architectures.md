# Serveless Solution Architecture Discussions

## Mobile Application: MyTodoList

* Requirements
    * Expose as REST API with HTTPS
    * Users should be able to directly interact with their own folder in S3
    * users should authenticate through a managed serverless service
    * The users can write and read to-dos, but they mostly read them
    * The database should scale, and have some high read throughput
* Starting simple:
    * Amazon API Gateway + AWS Lambda + Amazon DynamoDB
    * Add Amazon Cognito + Amazon API Gateway
    * Add Amazon Cognito + Amazon S3 (using Permissions to Store and retrieve files)
    * Add DAX as Caching Layer (DynamoDB Technology)
    * Add Caching of Responses at Amazon API Gateway layer

## Serverless Website: MyBlog.com

* Requirements:
    * Should scale globally
    * Blogs are rarely written, but often read
    * Website is purely static files
    * Caching must be implement where possible
    * Any new users should receive an email
    * Images should have a thumbnail version
* Starting Simple:
    * Amazon API Gateway + AWS Lambda + DAX + DynamoDb Global Tables
    * Amazon S3 + CloudFront Global Distribution + Bucket Policy (Only authorize from CloudFront Distribution)
    * Add SynamoDB Stream (To stream changes) + AWS Lambda + Amazon Simple Email Service (SES)
    * Amazon S3 + Amazon Cloudfront + AWS Lambda + Amazon S3 + SQS + SNS (For thumbnail photos)

## Microservices Architecture

* ELB + ECS + DynamoDB
* Amazon API Gateway + AWS Lambda + ElastiCache
* ELB + Amazon EC2 + RDS
* Synchronous patterns: AP Gateway, ELB
* Asynchronous patters: SQS, Kinesis, SNS, Lambda Triggers (S3)

## Software updates distribution

* Use CloudFront