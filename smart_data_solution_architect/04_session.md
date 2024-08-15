# Escalabilidad y alta disponibilidad

## Solicitudes de instancias spot de EC2

* Pujas por la instancia
* Dos minutos de gracia para guardar trabajo
* Spot Block: Bloqueas la instancia de una a seis horas sin interrupciones
* Se utiliza para trabajos por lotes, análisis de datos o cargas de trabajo resistentes a errores
* No recomendable para cargas de trabajo críticas.
* Primero cancelar la petición de la instancia y luego terminarla. 

* Spot Fleets:
    * Instancias spots + instancias bajo demanda
    * Tipos:
        * lowestPrice
        * Diversificado
        * capacityOptimized
        * priceCapacityOptimized

## IP privada vs IP pública vs IP elástica

* Ip pública está expuesta a internet:
    * IPv4 and Ipv6
    * Internet Gateway tiene la dirección pública
* Ip privada, no está expuesta a internet:
    * Se incluye en una red privada
    * Se puede conectar a internet mediante una puerta de enlace NAT
* Ip elástica:
    * Es una Ip fija para la instancia
    * Siempre va a ser tuya, a menos que la liberes
    * Máximo cinco por cuenta

* Buenas prácticas:
    * No utilizar IP elástica
    * Usar IP pública y registrar un nombre de DNS en ella
    * Usa un Load Balancer y no uses la IP pública

* Host bastion: Conectarse a una instancia privada desde una instancia pública.

## Placement Groups

* Estrategias de control de instancias EC2:
    * Clúster: único hardware en única zona de disponibilidad:
        * Big data
        * Latencia baja y alto rendimiento
    * Spread: hardware subyacente en varias zonas de disponibilidad:
        * Limitado a siete instancias de disponibilidad
        * Instancias aisladas de los fallos 
    * Partición:
        * Siete particiones por zona de disponibilidad
        * Hasta 100 instancias en total
        * Casos de uso:
            * HDFS
            * HBase
            * Cassandra
            * Kafka

* ENI: Elastic Network Interface
    * Son tarjetas de red virtuales
    * Enlazada a una zona de disponibilidad
    * Casos de uso:

* Hibernación de EC2:
    * Detener
    * Terminar

* EC2 Hibernate:
    * Se conserva el estado en memoria RAM
    * Arranque mucho más rápido
    * El estado de la RAM se escribe en un archivo en el EBS root
    * El EBS debe estar cifrado
    * Sólo algunas familias admitidas
    * No puede hibernar más de 60 días
    * Instancia bajo demanda, reservadas y spot
    * RAM menor a 150gb
    * Casos de uso: 
        * Procesamiento de larga duración
        * Aplicaciones que tardan en arrancar

* Graviton EC2
    * Mejor relación precio-rendimiento
    * No disponible para instancias windows
    * Casos de uso:
        * Servidores de aplicaciones
        * microservicios
        * HPC
        * ML basado en CPU
        * Codificación de video
        * Juegos
        * Cachés en memoria

* Métricas incluídas en EC2
    * Utilización de CPU
    * Uso de créditos y saldo
    * Comprobación de estado
        * Estado de la instancia
        * Estado del sistema
    * Operaciones del disco
    * RAM no incluída en las métricas de AWS EC2

## Introducción a la alta escalabilidad y alta disponibilidad




