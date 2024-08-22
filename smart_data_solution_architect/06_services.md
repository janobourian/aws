# Almacenamiento en AWS Parte 02

## AWS S3 - Simple Storage Service

* Almacenado infinito
* Casos de uso: 
    * Copia de seguridad y almacenamiento
    * Recuperación ante desastres
    * Archivo
    * Almacenamiento en la nube híbrida
    * Alojamiento de aplicaciones
    * Alojamiento de medios
    * Lagos de datos y análisis de big data
    * Entrega de Software
    * Sitio web estático

* Buckets:
    * Son directorios que dan la ilusión de archivos
    * Nombre único global en todas las regiones y todas las cuentas
    * Se definen a nivel de región
    * Se almacenan como objetos. Tipos de almacenamientos: Objetos, bloques, archivos. 
    * Máximo tamaño de un archivo es de 5TB
    * Máximo tamaño para subir un archivo es de 5GB
        * Más grande utilizar "Multi-part upload"
    
* Seguridad:
    * Basado en el usuario:
        * Políticas de IAM
            * SEPARC
    * Basado en recursos:
        * Bucket policy
            * SEPARC
        * Bucket Access Control List
        * Object Access Control List
    * Encriptación
    * Para hacerlo público es necesario cambiar la BACL and the bucket policy

* Versionamiento:
    * Se habilita a nivel bucket. 
    * Se recomienda:
        * Protección contra eliminación no deseada
        * Vuelve fácilmente a la versión anterior
        * Los objetos cargados antes de la versión tendrán id null
        * La suspensión del control de versiones no elimina las versiones anteriores