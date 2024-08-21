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