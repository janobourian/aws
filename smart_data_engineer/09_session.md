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

## AWS Lake Formation

* Permite configurar y administrar un lago de datos en AWS
* Cargar datos y supervisar flujos de datos
* Construido sobre Glue
* Gobernanza sobre los datos. 
    * Crawler
    * ETL
    * Data Catalog
    * Security
    * ACL
    * Cleaning
    * Transformations
* Inputs:
    * S3
    * RDBMS
    * NoSQL
* Outputs
    * Athena
    * Redshift
    * EMR
* AWS Lake Formation es gratis
* Servicios subyacentes son costosos

* Steps:
    * Create user
    * Glue connection to get data
    * Create bucket

* AWS Resource Access Manager para cuentas externas a su organización
* Tablas gobernadas admiten transacciones ACID en S3 (nuevo tipo de tabla)
* Permisos por columnas o por filtro (SELECT de SQL)

## Amazon Athena

* Leer datos desde S3 utilizando SQL
* Utiliza Presto
* Serverless
* CSV, TSV, JSON, ORC, Parquet, Avro, Compresión
* Datos estructurados, semiestructurados, no estructurados

* Integraciones:
    * Jupyter, Zeppelin, RStudio
    * Quicksight
    * ODBC/JDBC

* Common pattern:
    * Amazon S3 -> AWS Glue (Crawler, job, Glue Catalog) -> Amazon Athena -> Quicksight

* Athena Workgroups
    * Organizar
        * Usuarios
        * Equipos
        * Aplicaciones
        * Cargas de trabajo
    * Se pueden limitar los datos a los que se acceden

* Modelo de costes de Athena:
    * Pago por uso
        * 5 USD por TB escaneado
        * Consultas correctas y canceladas cuentas, las fallidas no
        * No cargos por DDL (CREATE/ALTER/DROP)
    * Se ahorra mucho en ORC y Parquet

* Seguridad:
    * Políticas de IAM, ACL y bucket de S3
    * Cifrados en reposo de S3
    * Cifrado en tránsito entre Athena y S3

* Antipatterns:
    * Informes/Visualizaciones
        * Usar QuickSight
    * ETL
        * Usar Glue

* Optimización
    * Optimización en columnas ORC, Parquet
    * Un número pequeño de archivos grandes funciona mejor que un gran número de archivos pequeños
    * Usar particiones

* Transacciones ACID:
    * Desarrollado por Apache Iceberg
    * Compatible con EMR, Spark
    * Elimina la necesidad de un bloqueo de registro personalizado
    * Operaciones de viaje en el tiempo
    * Tablas gobernadas por AWS Lake Formation

## Amazon Elastic Map Reduce (EMR)

* Framework de Hadoop administrado en instancias EC2
* Clúster:
    * Master node: administra el clúster
    * Core node: Aloja datos de HDFS y ejecuta tareas
    * Task node: Ejecuta tareas, no aloja datos
        * Opcionales
        * Puedes utilizar instancias spot

* Uso de EMR:
    * Transient:
        * Al terminar la tarea el nodo se apaga
    * Long-running:
        * Los clúster se deben apagar manualmente

* Uso de EMR:
    * Frameworks y aplicaciones se especifican en el inicio del clúster
    * Conéctese directamente al maestro para ejecutar trabajos directamente
    * Pasos por la consola:
        * Procesar datos en S3 o HDFS
        * Salidas de datos a S3 u otro lugar
        * Ya definidos, los pasos se pueden invocar usando la consola

* EMR y AWS:
    * Ocupas instancias EC2
    * Amazon VPC para la red virtual en la que se lanzan las instancias
    * Amazon S3
    * Amazon CloudWatch
    * AWS IAM
    * AWS CloudTrail
    * AWS Data Pipeline

* Almacenamiento:
    * HDFS
        * Hadoop Distrubuited File System
        * Permite redundancia
        * Archivos almacenados como bloque
        * Efímero
        * Para guardar caché, información intermedia o cargas de trabajo
    * EMRFS
        * Accede a S3 como si fuera HDFS
        * Permite almacenamiento persistente después de la finalización del clúster
        * EMRFS Consistent View
            * Utiliza DynamoDB para realizar un seguimiento con la coherencia
            * Modificabas la lectura/escritura
        * S3 is now Strongly Consistent

* Almacenamiento EMR
    * Sistema de archivos locales
    * EBS para HDFS
        * Se elimina cuando se termina el clúster
        * Los volúmenes de EBS sólo se pueden asociar cuando se lanza un clúster
        * Si desconecta manualmente un volumen de EBS, EMR lo trata como un error y lo reemplaza

* Promesas de EMR:
    * EMR cobra por hora + Cargos de EC2
    * Aprovisiona nuevos nodos
    * Puede agregar y eliminar nodos de tareas sobre la marcha
    * Puede cambiar el tamaño de los nodos principales de un clúster en ejecución
    * Los nodos principales también se pueden agregar o eliminar, pero se corre el riesgo de perder datos. 

* EMR Serverless:
    * Elige versión y un tiempo de ejecución
    * EMR gestiona la capacidad subyacente
    * Ventajas Serverless, más bien, ventajas de autoadministración
    * Debes llamar la API para operaciones como:
        * CreateApplication
        * StartApplication
        * StopApplication
        * DeleApplication

* Spark agrega un 10% de sobre carga, por lo cual la capacidad debe ser superior a ese 10%

* EMR Serverless:
    * Lo mismo que EMR
    * EMRFS:
        * Cifrado S3
        * TLS en tránsito entre los nodos de EMR y S3
    * S3:
        * SSE-S3, SSE-KMS
    
* EMR puede trabajar con EKS y es totalmente gestionado

* Hadoop: 
    * Framework para el procesamiento de datos distribuidos:
        * MapReduce
        * YARN
        * HDFS

* Apache Spark:
    * Framework de procesamiento distribuido para Big Data:
        * Map Reduce - Spark
        * YARN
        * HDFS

* Spark:
    * Ejecuta procesos independientes en un clúster
    * No está diseñado para OLTP
    * Componentes:
        * SPARK CORE
        * Over it:
            * Spark Streaming
            * Spark SQL
            * MLLib
            * GraphX

* Spark Streaming:
    * Kinesis Producer -> Amazon Kinesis Data Streaming -> Spark Dataset implemented from KCL

* Spark + Redshift:
    * Amazon S3 -> Amazon Redshift -> Amazon EMR with Spark -> Amazon Redshift

* Amazon Athena para Apache Spark:
    * Ejecuta Jupyter Notebooks con Spark
        * Jypiter notebooks cifrados automáticamente o KMS
    
* Apache Hive
    * Big Data
    * Consultas OLAP 
    * Utiliza SQL con HiveQL
    * Hive metastore similar al AWS Glue Catalog
        * Se almacena en MySQL en el Clúster Maestro
    * Puntos de integración
        * S3
        * DynamoDB

* Apache Pig
    * Pig Latin para definir el Map Reduce

* HBase:
    * NoSQL a escala de PetaBytes
    * Sobre HDFS
    * Almacenamiento en memoria, integración con Hive

* Presto:
    * Se conecta a diversos motores de base de datos
    * Sintaxis de SQL
    * Optimizado por OLAP

* Apache Zeppelin:
    * Similar a iPython

* EMR Notebook:
    * Similar a Zeppelin, pero integrado con EMR

* HUE:
    * Hadoop User Experience
    * Front-end gráfico para aplicaciones en su clúster de EMR

* Splunk:
    * Herramienta operativa para mostrar datos y que sean accesibles, utilizables y valiosos

* MXNet:
    * Similar a TensorFLow

* S3DistCP:
    * Herramienta para copiar grandes cantidades de datos:
        * De S3 a HDFS
        * De HDFS a S3

* Otras herramientas de EMR / Hadoop:
    * Ganglia
    * Mahout
    * Accumulo
    * Sqoop
    * HCatalog
    * Kinesis Conector
    * Tachyon
    * Derby
    * Ranger

* Seguridad EMR
    * Políticas de IAM
    * Kerberos
    * SSH
    * Roles de IAM

* EMR Instancias:
    * m5.xlarge si < 50 nodes, Mayor si 50 > nodes
    * m5.xlarge suele ser bueno
    * Instancias spot para task nodes