# SQS Service

## What is SQS?

* It is a Simple Queue Service
* It is a fully managed message queuing service
* It enables you to decouple and scale microservices, distributed systems, and serverless applications
* It provides two types of message queues: Standard queues and FIFO queues
* Producers -> Send Messages -> SQS Topic -> Poll Messages -> Consumers

## SQS - Standard Queue

* Offers maximum throughput, best-effort ordering, and at-least-once delivery
* Messages might be delivered more than once and might not be in the exact order they were sent
* Suitable for applications that require high throughput and can tolerate occasional duplicate messages
* Unlimited throughput, unlimited number of messages in queue
* Default retention of messages: 4 days, maximum of 14 days
* Low latency (<10ms on publish and receive)
* Limitation of 1,024 KB per message sent

## SQS - Producing Messages

* Producers send messages to an SQS queue using the `SendMessage` API action
* Each message can contain up to 1,024 KB of text in any format
* Messages can include attributes, which are name-value pairs that provide additional information about the message

## SQS - Consuming Messages

* Consumers poll messages from an SQS queue using the `ReceiveMessage` API action
* Poll SQS for messages (receive up to 10 messages at a time)
* Process the messages (example: insert the message into an RDS database)
* Once a consumer receives a message, it becomes invisible to other consumers for a specified period (visibility timeout)
* The consumer processes the message and then deletes it from the queue using the `DeleteMessage`

## SQS - Multiple EC2 Instances Consumers

* Multiple EC2 instances can poll messages from the same SQS queue
* This allows for load balancing and scaling of message processing
* Each instance can process messages independently, and the SQS service ensures that messages are delivered to only one instance at a time

## SQS with Auto Scaling Group (ASG)

* You can configure an Auto Scaling Group to automatically adjust the number of EC2 instances based on the number of messages in the SQS queue
* This allows for dynamic scaling of your message processing capacity based on demand
* You can set up CloudWatch alarms to trigger scaling actions when the number of messages in the queue exceeds a certain threshold
* SQS Queue -> EC2 Instances 
* CloudWatch Metric - Queue Length -> Alarm -> CloudWatch Alarm -> Auto Scaling Group

## SQS to decouple between application tiers

* requests -> Frontend web app -> Send Message -> SQS Queue -> Receive Messages -> Backend app -> S3 bucket

## Amazon SQS - Security

* Ecryption:
    * In-flight encryption using HTTPS API
    * At-rest encryption using KMS Keys
    * Client-side encryption if the client wants to perform encryption/decryption itself
* Access Controls: IAM policies to regulate access to the SQS API
* SQS Access Policies (similar to S3 bucket policies):
    * Useful for cross-account access to SQS queues
    * Useful for allowing other services (SNS, S3,...) to write to an SQS queue

## SQS Queue Access Policy

* Cross Account Access
* Publish S3 Event Notifications to SQS Queue

### For the Access Policy

* Methods:
    * Basic: Use simple criteria to define a basic access policy
    * Advanced: Usea a JSON object to define an advanced access policy
* Who can send messages to the queue:
    * Only the queue owner
    * Only the specified AWS accounts, IAM users and roles
* Who can receive messages from the queue
    * Only the queue owner
    * Only the specified AWS accounts, IAM users and roles

## SQS - Message Visibility Timeout

* When a consumer receives a message from an SQS queue, the message becomes invisible to other consumers for a specified period (visibility timeout)
* This allows the consumer to process the message without worrying about other consumers processing the same message simultaneously
* If the consumer fails to process the message within the visibility timeout, the message becomes visible again
* Default visibility timeout is 30 seconds, but it can be configured up to 12 hours
* If the consumer successfully processes the message, it should delete the message from the queue to prevent it from being processed again
* A consumer could call the `ChangeMessageVisibility` API to get more time

## SQS - Dead Letter Queues

* A dead letter queue is a queue that receives messages that could not be processed successfully by the consumer
* You can configure a redrive policy on the source queue to specify the dead letter queue and the maximum number of times a message can be received before it is sent to the dead letter queue
* This allows you to isolate and analyze messages that could not be processed successfully, without affecting the processing of other messages in the source queue
* You can use the dead letter queue to troubleshoot and debug issues with message processing, and to implement retry logic for messages that fail to process successfully

## SQS DLQ - Redrive to Source

* You can use the `RedrivePolicy` attribute to specify the source queue and the maximum number of times a message can be received before it is sent to the dead letter queue
* This allows you to automatically move messages that could not be processed successfully back to the source queue
* Feature to help consume messages in the DLQ to understand what is wrong with them
* When your code is fixed, we can redrive the messages from the DLQ back into the source queue in batches without writing custom code.

## SQS - Delay Queues

* Delay a messages up to 15 minutes
* Default is 0 seconds
* Can set a default at queue level
* Can override the default on send using the `DelaySeconds` parameter

## SQS Certified Developer Concepts

### Long Polling

* Long Polling: When a consumer requests messages from the queue, it can optionally wait for messages to arrive if there are none in the queue
* `LongPolling` decreases the number of API calls made to SQS while increasing the efficiency and decreasing the latency of your application
* The wait time can be between 1 second to 20 seconds
* `LongPolling` is preferable over `ShortPolling`
* Long Polling can be enabled at the queue level or at the API level using `ReceiveMessageWaitTimeSeconds`

### SQS Extended Client

* Message size limit is 1024 KB, how to send large messages
* Using the SQS Extended Client (Java Library)

### Must know API

* `CreateQueue`, `DeleteQueue`
* `PurgeQueue`
* `SendMessage`, `ReceiveMessage`, `DeleteMessage`
* `MaxNumberOfMessages` (default 1, max 10)
* `ReceiveMessageWaitTimeSeconds`
* `ChangeMessageVisibility`

## SQS - FIFO Queues

* FIFO: First In First Out (ordering of messages in the queue)
* Limited throughout: 300 msg/s without batching, 3000 msg/s with batching
* Exactly-once send capability (by removing duplicates using Deduplication ID)
* Messages are processed in order by the consumer
* Ordering by Message Group ID (all messages in the same group are ordered) - Mandatory parameter

## SQS - FIFO Queues Advanced

### Deduplication

* SQS FIFO queues provide a deduplication mechanism to ensure that messages are not delivered more than once
* When a message is sent to a FIFO queue, it is assigned a deduplication ID
* If a message with the same deduplication ID is sent within a 5-minute window, it will be treated as a duplicate and will not be delivered to the consumer
* Two de-duplication methods:
    * Content-based deduplication: will do a SHA-256 hash of the message body
    * Explicitly provide a Message Deduplication ID

### Message Grouping

* SQS FIFO queues allow you to group messages using a Message Group ID
* Messages with the same Message Group ID are guaranteed to be processed in order by the consumer
* Messages with different Message Group IDs can be processed in parallel by the consumer

## SQS + Auto Scaling Group

* You can configure an Auto Scaling Group to automatically adjust the number of EC2 instances based on the number of messages in the SQS FIFO queue
* This allows for dynamic scaling of your message processing capacity based on demand
* You can set up CloudWatch alarms to trigger scaling actions when the number of messages in the queue exceeds a certain threshold
* SQS a a buffer to databse writes
* SQS to decouple between applications tiers
* SQS FIFO Queue -> EC2 Instances
* CloudWatch Metric - Queue Length -> Alarm -> CloudWatch Alarm -> Auto Scaling Group

## SQS For CloudOps

* Message Visibility Timeout
* Dead Letter Queues
* Message Retention Period
* SQS Access Policy
* SQS Prioritization Pattern