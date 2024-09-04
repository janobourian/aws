# Servicios de Analítica Parte 02

* About kinesis:
    * Familia de servicios totalmente administrado
    * Transmisión y procesamiento de datos en tiempo real
    * Maneja grandes volúmenes de datos de diversas fuentes
    * Aprendizaje automático en tiempo real 

## AWS Kinesis Data Streams

* Key concepts:
    * Permite crear aplicaciones personalizadas que procesan o analizan datos
    * Maneja TB de datos por hora de diversas fuentes
    * Ideal para aplicaciones de aprendizaje automático
    * Retienes información por un tiempo específico
    * En tránsito mediante SSL y en reposo mediante KMS
    * Pattern:
        * Input Data
        * Kinesis Data Streams
        * Ouput Options:
            * Lambda
            * EC2
            * Kinesis Firehose
            * Kinesis Data Analytics
    * Features:
        * Retención entre 1 a 365 días
        * Datos insertados no pueden ser eliminados
        * Producers:
            * AWS SDK
            * Kinesis Producer Library (KPL)
            * Kinesis Agent
        * Consumers:
            * Propios:
                * Kinesis Client Library
                * Kinesis Connector Library
                * SDK
            * Administrados:
                * Lambda
                * Kinesis Data Firehose
                * Kinesis Data Analytics
    * Capacity modes:
        * Aprovisionado
        * On demand
    * Security:
        * VPC Enpoints
    * Kinesis Producer Library:
        * Para crear productores de alto rendimiento y larga duración
        * Kinesis Agent:
            * Supervisa los archivos de registro y los envía a Kinesis Data Streams
            * Instalar en entornos de servidor basados en Linux
    * Kinesis Client Library:
        * To receive messages
    * Kinesis Connector Library
        * Ahora es con Kinesis Data Firehose

* Kinesis Enhanced Fan Out
    * 2MB por consumidor y ~70ms. Máximo 20 consumidores
    * En formato normal se tiene 2MB por shard con ~200ms

Puedes fusionar shards

* Lab

```bash
aws --version
aws kinesis put-record --stream-name rabbit-kds --partition-key user1 --data "user signup" --cli-binary-format raw-in-base64-out
aws kinesis describe-stream --stream-name rabbit-kds
aws kinesis get-shard-iterator --stream-name rabbit-kds --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON
aws kinesis get-records --shard-iterator AAAAAAAAAAFj6XjGfJEseRRQSorxyxYzStkMtpl3o7RNxref/mvYD+TX9enZUKscx9uKnZ8dyPHSl/W/pFT0hC40CzY3uHznrVMA6lOewMzu0WG3gjQlqgWu+a2tDKG0xtGdGh1lT3DBMb/puLqXeXmJXJdNH3T5Hk2asN1GPzlXocibUP0KEt6ccJbvEu2RlreTgC3tjPrCmuXzBSFCZ+ZicGlPPbwU8MMhevqsZ+VLM9U/cRep9A==
```

## Amazon Kinesis Data Firehose

* Near Real Time
* Send information to Redshift/Amazon S3/OpenSearch/Splunk
* Convert JSON to Parquet/ORC (only for S3)
* Compresions in GZIP (Redshift only admit this), ZIP, SNAPPY
* Buffer Sizing se vacía según las reglas de tiempo y tamaño

## Kinesis Data Analytics

* To create tables for analysis from Kinesis Data Streams and Kinesis Data Firehose
* It uses Apache Flink
* Use cases:
    * Streaming ETL
    * Continuos generation of Insights
    * Analytics
* RANDOM_CUT_FOREST:
    * Help you to detect anomaly columns

## Amazon Managed Streaming for Apache Kafka

* Alternativa a Kinesis
* Puede implementar clúster Multi-AZ
* Los datos se almacenan en EBS
* Puede crear Producers and Consumers
* Seguridad:
    * Encriptación
    * Grupos de seguridad
    * Autenticación y Autorización
* Monitoreo:
    * CloudWatch
    * Prometheus
    * Broker Log Delivery:
        * CloudWatch Logs
        * Amazon S3
        * Kinesis Data Stream
* También tiene versión Serverless