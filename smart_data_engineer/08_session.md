# Databases, Migration and Container

## Amazon Redshift

* Diseñado para OLAP no for OLTP
* Escala o reduzca verticalmente bajo demanda
* Almacenamiento en columnas
* Casos de uso:
    * Acelere las cargas de trabajo de análisis
    * Almacén de datos unificado y lago de datos
    * Modernización del almacé de datos
    * Analizar, en general
* Rendimiento:
    * MPP, Massive Paralel Process
    * Almacenamiento de datos en columnas
* Durabilidad:
    * Datos replicados dentro del clúster (por si un nodo falla)
    * Copias de seguridad en S3
    * Limitado a una sola zona de disponibilidad:
        * Ya está disponible Multi-AZ para clústeres RA3
* Escalamiento:
    * Escalado vertical y horizontal
    * Estilos:
        * Auto: Redshift calcula en función del tamaño de los datos
        * Even: Filas distribuidad en porciones en round-robin
        * Key: Filas distribuidas en función de una columna
        * All: Toda la tabla se copia en cada nodo

* Architecture:
    * Leader Node
    * Node Types:
        * Dense Storage (DS)
        * Dense Compute (DC)

* Redshift Spectrum:
    * Consultar exabytes de datos no estructurados en S3 sin cargar
    * Escalado horizontal
    * Separar los recursos de almacenamiento y cómputo
    * Compatibilidad con comprensión Gzip and Snappy

* Redshift Sort Keys:
    * Las filas se almacenan en el disco en orden ordenado en función de la columna que designe como clave de ordenación
    * Es como un índice, para realizar consultas rápido
    * Types:
        * Columna única
        * Compuesto
        * Intercalado

* Importación/Exportación de datos:
    * Importar con el comando COPY
        * S3, EMR, DynamoDB o hosts remotos
    * Comando UNLOAD:
        * Descargar de una tabla en archivos en S3
    * Enrutamiento de VPC y copia de seguridad desde Amazon S3
    * Integración de cero ETL de Amazon Aurora
    * Ingesta de streaming de Redshift desade Kinesis Data Streams o MSK

* Redshift copy grantes para copias Snapshot entre regiones:
    * Snapshots para salvaguardar datos con KMS

* DBLINK:
    * Conectar con base postgreSQL (RDS)
    * Es bidireccional

* Integración con otros servicio:
    * S3
    * DynamoDB
    * EMR
    * EC2
    * Data Pipeline
    * DMS (Database Migration Service)

* Redshift Workload Management (WLM)
    * Prioriza consultas cortas y rápidas frente consultar largas y lentas
    * Colas de consultas
    * A través de la consola, la CLI o API
    * Escalado de simultaneidad:
        * Agrega clústers para consultas read
        * Admite consultas y usuarios simultáneos
        * Gestiona las colas
    * Administración:
        * Crea hasta ocho colas
        * Cola de superusuario con nivel de simultaneidad uno
        * Predeterminado cinco con asignación uniforme de memoria
        * Se puede habilitar el salto de consulta
        * Configuración de colas de consultas:
            * Prioridad
            * Modo de escalado de simultaneidad
            * Grupos de usuarios
            * Grupos de consultas
            * Reglas de supervisión

* Short Query Acceleration (SQA):
    * Prioriza las consultas cortas 
    * Se puede utilizar en lugar de Redshift-WLM
    * Utiliza ML para predecir el tiempo de consulta
    * Puede configurar el tiempo para "short"

* Cambiar tamaño de clúster:
    * Elastic resize
    * Classic resize
    * Snapshot, restore, resize

* Comando VACUUM:
    * VACCUM FULL
    * VACCUM DELETE ONLY
    * VACCUM SORT ONLY
    * VACCUM REINDEX

* Nuevas funciones:
    * Nodos RA3:
        * Escala de manera independiente la computación y el almacenamiento
    * Exportación del lago de datos de Redshift
        * Formato Parquet, dos veces menos pesado al descargar y hasta seis veces menos almacenamiento
    * Tipos de datos espaciales
        * GEOMETRY
        * GEOGRAPHY
    * Uso compartido entre regiones
        * Se comparten datos en tiempo real entre clústers sin copiarlos

* AQUA (Advanced Query Accelerator):
    * Hasta 10 veces más rápido
    * Conexión de ancho de banda con S3
    * Sin costos
    * Amazon Redshift > AQUA > S3

* Amazon Redshift ML:
    * Usando SageMaker
    * Collect > Amazon Redshift ML > Create > Train > Deploy > Predict

* Redshift Anti-patterns:
    * Pequeños conjuntos de datos (RDS)
    * OLTP (RDS o DynamoDB)
    * Datos no estructurados (ETL con EMR)
    * Datos BLOB (Almacenar referencia a archivos binarios grandes en S3)

* Problemas de seguridad de Redshift
    * Usando un Hardware Security Module (HSM):
        * Certificado de cliente y servidor
    * Definición de privilegios
        * GRANT o REVOKE

* Redshift Serverless:
    * Escalado automático
    * Optimiza los costes
    * Utiliza ML para mantener el rendimiento
    * Puesta en marcha sencilla
    * Hace todo, menos:
        * Redshift Spectrum
        * Grupos de parámetros
        * Gestión de la carga de trabajo
        * Integración de socios de AWS
        * Ventanas de mantenimiento
        * No hay endpoint público, debe acceder dentro de una VPC

* Escalado de recursos en Redshift Serverless:
    * Capacidad medida en Redshifts Processing Units (RPU)

* Redshift Serverless Monitoreo:
    * Monitoreo
    * CloudWatch 
    * CloudWatch metrics

* Redshift Vistas materializadas:
    * Es un query con resultados precalculados
    * Son particularmente beneficiosos para consultas predecibles y recurrentes
    * Útil para reutilizar queries costosas

* Intercambio de datos de redshift:
    * Comparta datos para fines de lectura
    * Útil para:
        * Aislamiento de la carga de trabajo
        * Colaboración entre grupos
        * Uso compartido de datos entre dev/qa/prod
    * Arquitecura consumer-producer

* User Defined Functions (UDF) Redshift Lambda
    * Puedes llamar a otros servicios como IA
    * Acceder a sistemas externos
    * Integración con el servicio de ubicación

* Consultas Federadas de Redshift:
    * Consulta RDS o Aurora, pero no al revés
    * Operaciones de sólo lectura
    * El costo se carga a RDS
    * Se incorporan datos en tiempo real
    * Evita las canalizaciones ETL

## Snow Family

* Migración de datos:
    * Snowcone
    * Snowball Edge
    * Snowmobile
* Computación perimetral
    * Snowcone
    * Snowball Edge

* Snowcone:
    * 8Tb o 14TB
* Snowball Edge:
    * TB o PB
* Snowmobile:
    * 100 PB
    * Usarlo si vas a transferir más de 10PB

* Edge computing:
    * Ubicaciones sin internet o sin infraestructura
    * Snowcone and snowcone SSD
    * Snowball edge - compute optimized
    * Snowball edge - storage optimized

* AWS OpsHub:
    * Software para administrar la familia Snow*

## DataSync

* Mover datos:
    * On-premise - Cloud or Cloud - On-premise (with agent)
    * AWS to AWS (without agent)
    * Se puede sincronizar con:
        * Amazon S3 
        * Amazon EFS
        * Amazon FSx