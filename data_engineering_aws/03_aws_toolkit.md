# The AWS Data Engineer's Toolkit

* Key concepts:
    * Ingesting data
    * Transforming data
    * Orchestating big data pipelines
    * Consuming data

## Ingest data

* Amazon Database Migration Service:
    * Can be used to run continuos replication from a number of common database engines into an Amazon S3 data lake
    * It can use parquet or csv format
    * CDC: Change Data Capture, see the logs in database and update only that changes

* Amazon Kinesis for streaming data ingestion:
    * Ingest data in real or near real time
    * Kinesis Data Firehose:
        * Ingests streaming data, buffers for a configurable period, then writes out a limited set of targets
        * It can buffered the information and trigger the process based on time (1-15 min) or size (1 - 128 Mb)
    * Kinesis Data Streams:
        * Ingests real-time data streams and processing the incoming data
    * Kinesis Data Analytics:
        * Reads data from a streaming source and uses SQL statements or Apache Flink code to perform analytics on the stream
    * Kinesis Video Streaming:
        * Processes streaming video or audio streams
    * Amazon Kinesis Agent:
        * It can be configured to monitor a set of files, and as new data is written to the file
        * It can be installed in servers
    * Amazon Kinesis Producer Library:
        * To emmit notifications to mobile applications or IoT service
    * Amazon Managed Streaming for Apache Kafka (MSK):
        * If Amazon Kinesis Firehose is not supported
    * Kinesis Client Library:
        * It works with Amazon Kinesis Producer Library