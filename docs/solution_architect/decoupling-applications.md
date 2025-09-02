# Decoupling applications

* Messaging is a way to communicate apps
* There are two patterns of application communication:
    * Synchronous communications
    * Asynchronous / Event Based
* Services to decouple:
    * SQS: Queue model
    * SNS: Pub/Sub model
    * Kinesis: Stream processing
    * EventBridge: Event bus
    * Lambda Triggers: Event based invocations

## SQS

* Simple Queue Service
* Producer -> Send Messages -> SQS -> Poll Messages -> Consumer


* Amazon SQS - Standard Queue
    * Unlimited throughput, unlimited number of messages in queue
    * Default retention of messages: 4 days, maximum of 14 days
    * Low Latency
    * Limitation of 256 Kb per message sent
    * Can have duplicate messages (at least once delivery, occasionally)
    * Can have out of order messages (best effort ordering)
    * Consumer Poll SQS:
        * Receive up to 10 messages at a time
        * DeleteMessage using the API
        * CloudWatch Metric - Queue Length
            * ApproximateNumberOfMessages
        * CloudWatch Alarm
            * Start an Auto Scaling Group
    * Standard at least Once, FIFO only Once

* Message Visibility Timeout
    * During this time other consumers can see the current item
    * You can set a Long time

* Long Polling:
    * Request a lot of messages from a Queue
    * LongPolling decreases the number of API calls made to SQS while increasing the efficiency and reducing latency of your application

* FIFO Queue
    * First In First Out
    * ordering of messages in the queue
    * Limited througput 300 msg/s
    * Exaclty-once send capability
    * Ordering by Message Group ID

* SQS with Auto Scaling Group
    * EC2 poll for messages
    * Cloudwatch Metric - Queue Length
        * Approximate NumberOfMessages
    * Put attention in:
        * Amazon RDS
        * Amazon Aurora
        * Amazon DynamoDB
    * You can use SQS as a buffer to database writes
        * EC2 to enqueue -> SQS -> EC2 dequeue -> Database Layer

## SNS

* It helps you if you want to send one message to many receivers
* It follows the Pub/Sub
* Event producer only sends message to one SNS Topic
* Event receivers as wewant to listen to the SNS topic notificacions
* SNS can have multiple subscribers
    * SQS Queue
    * Lambda Function
    * Kinesis Dara Firehose
    * HTTP Endpoint
    * Email
    * SMS
* SNS can have multiple publishers (specially aws resources)
* Security:
    * Encryption
    * Access Controls
    * SNS Access Policies
* SNS + SQS: Fan Out pattern
    * Push once in SNS
    * Receive in all SQS queues that are subscribers
    * Capabilities:
        * SQS allows for: data persistence, delayed processing and retries of work
        * Ability to add more SQS subscribers over time
        * Make sure your SQS queue access policy allows for SNS to write
        * Cross-Region Delivery: works with SQS Queues in other regions
    * SNS + Amazon Kinesis Firehose + S3
    * SNS FIFO + SQS FIFO
    * SNS - Message filtering
        * JSON policy used to filter messages sent to SNS topic´s subscriptions

## Amazon Kinesis Data Strams

* It is used to process big data streams in real time
* Real-time data -> Producers (Kinesis Agent) -> Amazon Kinesis Dara Streams -> Consumers
* Consumers:
    * Application
    * Lambda
    * Amazon Data Firehose
    * Managed Service for Apache Flink
* Features
    * Retention between up to 365 days
    * Ability to reprocess (replay) data by consumers
    * Data can not be deleted from Kinesis (until it expires)
    * Data up to 1MB (smal real-time data)
    * Data ordering guarantee for data with the same "Partition ID"
    * At-rest KMS encryption, in-flight HTTPS encryption
    * Producers KPL
    * Consumer KCL
* Capacity Modes:
    * Provisioned mode
        * Choose numbers of shard
        * 1MB/s or 1000 records per second (in)
        * 2MB/s per second (out)
        * per-hour
    * On-demand mode
        * No need to provision
        * 4MB/s or 4000 records per second in
        * Scales automatically based on observed throughput peak during last 30 days
        * Pay per stream per hour and data in/out per GB
