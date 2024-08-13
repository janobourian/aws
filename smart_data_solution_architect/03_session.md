# Cómputo

* Services:
    * EC2
    * Lambda
    * ECR, ECS, EKS, AWS Fargate
    * AWS Beanstalk

## Elastic Compute Cloud (EC2)

* Tipos de instancias:
    * Uso general:
    * Optimizadas para informática:
        * Computación de alto rendimiento
    * Optimizadas para memoria:
        * Bases de datos relacionales/no relacionales
        * Aplicaciones que realizan el procesamiento en tiempo real de grandes volúmenes de datos no estructurados
    * Optimizadas para el almacenamiento:
        * Bases de datos que requieres alto acceso de lectura y escritura
        * Sistemas de archivos distribuidos
    * Optimizadas para Computación acelerada:
        * Aplicaciones de IA generativa
        * Aplicaciones de HPC (high power compute)
    * Optimizadas para HPC
        * Aprendizaje profundo

* Conectivity:
    * "Tiempo de espera" due to Security Group
    * "Conexión rechazada" due to application issues
    * Ports:
        * 21: FTP
        * 22: SSH
        * 22: SFTP
        * 80: HTTP
        * 433: HTTPS
        * 3389: RDP
    
* Opciones de compra:
    * Instancia bajo demanda:
        * Paga por lo que usas
    * Saving Plans:
        * Bloqueado para una familia de instancias y una región
    * Instancias Reservadas:
        * Elija tipo de instancia, región, arrendamiento, sistema operativo
        * Reserva de un año a tres años
        * Puede utilizarse en bases de datos
    * Instancia Spot:
        * Trabajo por lotes
        * Análisis de datos
        * Tratamiento de imágenes
        * Cargas de trabajo distribuidas
        * Cargas de trabajo con una hora de inicio y finalización flexible
    * Dedicated Host:
        * Un servidor para ti, en las instalaciones de Amazon
    * Instancias dedicadas:
        * Las instancias se ejecutan en hardware dedicado a usted
    * Reservas de capacidad:
        * Zona de disponibilidad específica
        * Para cargas de trabajo ininterrumpidas