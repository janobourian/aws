# Servicios de Analítica 01

## AWS Glue

* Detección sin servidor y definición de definiciones de tablas y esquemas
    * S3 
    * RDS
    * Redshift
    * DynamoDB
    * SQL Databases
* Trabajos de ETL personalizados

* Glue Crawler (rastreador de Glue) / Data Catalog
    * Detectar cambios en el esquema
    * Rellena el Glue Data Catalog
    * Al finalizar los datos no estructurados se tratan como estructurados:
        * Redshift Spectrum
        * Athena
        * EMR
        * Quicksight
    * Pensar cómo se van a ordenar los datos
        * YYYY/MM/DD/DEVICE
        * DEVICE/YYYY/MM/DD

* Glue + Hive 
    * Permite ejecutar consultas similares a SQL desde EMR (Elastic Map Reduce)
    * El catálogo de datos puede servir como un `metastore` de Hive

* Glue ETL
    * Generar automáticamente código en Python o Scala
    * Encriptación:
        * Lado del servidor (Reposo)
        * SSL (En tránsito)
    * Puede ser basado en eventos
    * Puede aprovisionar DPU
        * Data Process Units
    * Trabaja con PySpark o Spark
    * Destinos:
        * S3
        * RDS
    * Se ejecuta en Spark serverless

* Glue ETL: DynamicFrame
    * Colección de DynamicRecords (Parecido a DataFrame)
    * Puedes mapear

* Glue ETL - Transformations
    * Bundled Transformations
    * Machine Learning Transformations
        * FindMatches ML
    * Conversiones de formato
    * Transformaciones de Apache Spark
        * Convert Spark DataFrame to Glue DynamicFrame

* Glue ETL: Modifing Data Catalog
    * Adición de nuevas particiones
    * Actualización del esquema de la tabla
    * Creación de nuevas tablas
    * Restricciones:
        * S3
        * Sólo JSON, CSV, AVRO, PARQUET
        * No se admiten esquemas anidados

* AWS Glue points
    * Desarrollo de scripts ETL utilizando un notebook

* Glue jobs
    * Estilo Cron
    * Job Bookmarks
        * Conserva el estado de la ejecución del trabajo
        * Evita el procesamiento de datos antiguos
        * Sólo procesar datos nuevos

* Cost model for Glue:
    * Facturado por segundo para trabajaos de rastreo (Crawler) y ETL
    * Puntos de conexión de desarrollo para desarrollar código ETL cobrados por minuto

* Antipatterns:
    * Múltiples motores de ETL
        * La mejor opción es EMR

* Glue with streaming:
    * Kinesis o Kafka
    * On the fly

DAG: Directed Acyclic Graph

* AWS Glue Studio: Interfaz visual para flujos de trabajo ETL

* AWS Glue Data Quality
    * Reglas de calidad de los datos
    * Utiliza DQDL Data Quality Definition Language
    * Para producir errores o notificar en CloudWatch

* AWS Glue DataBrew
    * Herramienta visual de preparación de datos
    * Salida a S3
    * Seguridad:
        * Puede integrarse con KMS
        * SSL en tránsito
        * IAM
        * CloudWatch and CloudTrail

LAB: https://catalog.us-east-1.prod.workshops.aws/workshops/976050cc-0606-4b23-b49f-ca7b8ac4b153/en-US
LAB: https://catalog.us-east-1.prod.workshops.aws/workshops/976050cc-0606-4b23-b49f-ca7b8ac4b153/en-US/600