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

* Escalabilidad
    * Capacidad de una aplicación o sistema para adaptarse
    * Horizontal -> Elasticidad
    * Escalabilidad vertical:
        * Bases de datos
        * Sistemas no distribuidos
        * RDS y ElastiCache
    * Escalabilidad horizontal (Elasticidad):
        * Incrementar el número de instancias

* Alta disponibilidad:
    * Capacidad de una aplicación o sistema operativo de permanecer accesible
    * Dos o más zonas de disponibilidad

* Caso de EC2
    * Escalabilidad: más poder de cómputo
    * Escalado horizontal: Más instancias
        * Grupo de Auto Scaling
        * Balanceador de carga
    * Alta disponibilidad: Varias zonas de disponibilidad
        * Grupo de Auto Scaling
        * Balanceador de carga
        * Ambos multi AZ
    
## Amazon Elastic Load Balancing

* Único punto de entrada que reenvía el tráfico a varios servidores
* Distribuye el tráfico entrante
* Escala el balanceador de carga
* Stick cookies: mantener a un cliente en la misma instancia
* Comprobación de estado
    * Health check

* Tipos de balanceadores de carga:
    * Classic Load Balancer (capa 7 y capa 4 transporte)
    * Application Load Balancer 
    * Network Load Balancer (capa 4)
    * Balanceador de carga de puerta de enlace (capa 3)
        * Dirigir tráfico a firewall

* Load Balancer Security Group
    * Allow traffic

## ALB, NLB and GWLB

* Application Load Balancer:
    * Capa 7
    * Soporta contenedores
    * HTTP/2 and WebSocket
    * Puede ser configurado por 
        * Path /user
        * Subdomain
        * Query Parameters
    * Target Groups
        * Instancias EC2 (Pueden ser administradas por un Auto Scaling Group)
        * Tareas de ECS 
        * Funciones Lambda
        * Direcciones IP
        * ALB varios grupos de objetivos
        * La IP del cliente no se ve directamente

* Network Load Balancer:
    * Capa 4
    * Equilibrador de carga de red
    * Rendimiento extremo
    * Necesita IP estática
    * No incluído en la capa gratuita de AWS
    * Baja latencia como videojuegos en tiempo real
    * Target Groups:
        * EC2
        * On Premises
        * ALB

* Gateway Load Balancer:
    * Firewalls, detección de intrusos
    * Funciona en capa 3, de red
    * Target Groups:
        * EC2 
        * Onpremises

* Sticky Sessions:
    * Mismo cliente a la misma instancia
    * Controlamos la fecha de vencimiento de la cookie
    * Casos de uso:
        * Asegurar que el usuario no pierda los datos de sesión
    * Puede provocar un desequilibrio en la carga
    * Cookie personalizada:
        * Basadas en aplicación
        * Basadas en la duración

* Equilibrio de carga entre zonas:
    * With Cross Zone Load Balancing
    * Without Cross Zone Load Balancing
    * Habilitado para ALB, sin cobro
    * Deshabilitado para NLB, GWLB con cobro
    * Deshabilitado para CLB, sin cobro

* SSL/TSL:
    * Se puede adjuntar al ELB
    * Un servicio que se puede utilizar es AWS CM (Certificate Manager)

* SNI:
    * Service Name Indication
    * Balancea según el certificado y el dominio

* Drenaje de conexión:
    * Se completan las solicitudes en curso mientras se apaga la instancia por escalamiento o por errores

## Autoscaling groups

* Auto escalado:
    * Manual
    * Programado:
        * Anticipar basado en patrones
        * Para días de mayor venta
    * Dinámico:
        * Based on metrics
    * Bajo demanda 
    * Predictivo:
        * Usando Machine Learning

* Se crean grupos de Auto scaling
* AWS CloudWatch is a good service that fits with AutoScaling
* Es gratuito
* Capacidades:
    * Mínima
    * Deseada
    * Máxima

* Métricas para escalar:
    * CPUUtilization
    * RequestCountPerTarget
    * Promedio de entrada por red

* Tiempos de reutilización de escalado
    * Debes configurar una AMI para reducir el tiempo de configuración (Golden AMIs)