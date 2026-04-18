# Introduction to messaging

* All our applications have to be communicated:
    * Synchronous communication
        * buying service <-> Shipping service
    * Asynchronous / Event based
        * buying service -> Queue -> Shipping service

* Decouple your applications:
    * SQS for queue model
    * SNS for pub/sub model
    * Kinesis for real-time streaming model
    * Firehose
    * Amazon MQ