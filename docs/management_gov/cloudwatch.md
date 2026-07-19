# CloudWatch

CloudWatch is a monitoring and observability service provided by AWS that allows you to collect and track metrics, collect and monitor log files, set alarms, and automatically react to changes in your AWS resources. It provides insights into the performance and health of your applications and infrastructure.

## Metrics

* We can create Alarms based on services and specific operations like:
    * Cloudfront
        * Request
        * Alarm based on a rate of request in a period
* CloudWatch provides metrics for every services in AWS
* Metric is a variable to monitor
    * CPUUtilization
    * NetworkIn
    * NetworkOut
    * DiskReadOps
    * DiskWriteOps
* Metrics belong to namespaces
    * AWS/EC2
    * AWS/S3
    * AWS/Lambda
    * AWS/RDS
* Metrics have dimensions
    * InstanceId
    * AutoScalingGroupName
    * FunctionName
    * DBInstanceIdentifier
* Metrics have statistics
    * Average
    * Sum
    * Minimum
    * Maximum
    * SampleCount
* Metrics have units
    * Seconds
    * Microseconds
    * Milliseconds
    * Bytes
    * Bytes/Second
    * Bits/Second
* Up to 30 dimensions per metric
* Metrics have timestamps
* Can create CloudWatch dashboards of metrics
* Can create CloudWatch Custom Metrics
    * RAM
    * CPU Credit Usage
    * CPU Credit Balance
    * Memory Utilization
    * Disk Space Utilization
    * Application-specific metrics

### Streams

* Stream CloudWatch metrics to a destination of your choice
    * Near-real-time
    * Low latency
* Options
    * Amazon Kinesis Data Firehose
    * Amazon Kinesis Data Streams
    * AWS Lambda
    * Amazon S3
    * Amazon Redshift
    * Amazon Elasticsearch Service
    * Amazon OpenSearch Service
    * Amazon SNS
    * Amazon SQS
    * Amazon EventBridge
* Third party service provider
    * Datadog
    * Dynatrace
    * New Relic
    * Splunk
    * Sumo Logic

## Logs

* In log Management -> Log group -> Metrics you can create metrics based on some patterns like %ERROR%
* CloudWatch Logs allows you to monitor, store, and access log files from AWS resources, applications, and services.
* Log groups: arbitrary name, usually representing an application
* Log stream: instances within application/log files/containers
* Can define log expiration policies
* Logs are encrypted by default
* Can setup KMS-based encryption with your own keys

### Sources

* SDK, CloudWatch Logs Agent, CloudWatch Unified Agent
* ELastic Beanstalk
* ECS
* AWS Lambda
* VPC Flow Logs
* API Gateway
* CloudTrail
* Route53

### Insights

* The query tool
* Search an analyze log data stored in CloudWatch Logs
* Can create metric filters to extract metric data from log events
* Can create CloudWatch Logs Insights queries to analyze log data
* It is a query engine, not a real-time engine

### Subscriptions

* Get a real-time log events from CloudWatch Logs for processing and analysis
* Send to Kinesis Data Streams, Kinesis Data Firehose, or Lambda
* Subscription Filter - filter which logs are events delivered to yout destination
* Cross-Account Subscription - send log events to resources in a different AWS account (KDS, KDF)

## CloudWatch Logs for EC2

* By default, no logs from your EC2 machine will go to CloudWatch
* Install CloudWatch Logs Agent or CloudWatch Unified Agent to send logs from EC2 to CloudWatch Logs

## Agents

## Alarms

## Network Synthetic Monitor