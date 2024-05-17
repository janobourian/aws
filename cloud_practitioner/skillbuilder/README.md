# AWS Cloud Practitioner

https://explore.skillbuilder.aws/learn/mycourses

## Index

- [Introducción a Amazon Web Services](#section1)
- [Cómputo en la nube](#section2)

<div id="section1"> </div>

## Introducción a Amazon Web Services

Servicios:
- Cómputo
- Almacenamiento
- Seguridad de red
- Blockchain
- Machine learning
- Inteligencia artificial

El modelo Cliente-Servidor es el modelo base. Amazon Elastic Compute Cloud (EC2)

Conceptos clave:
- Se paga por lo que se usa.

### Cómputo en la nube

La entrega bajo demanda de recursos de TI a través de internet con precios de pago por uso. 

Diferenciar el Transporte pesado indiferenciado de TI.

Modelos de implementación:
- Basada en la nube (pública)
- Basada en las instalaciones (privada)
- Híbrida

Beneficios del cómputo en la nube:
- Cambiar gastos iniciales por gastos variables.
- Dejar de gastar dinero en la ejecución y el mantenimiento de centros de datos
- Deje de hacer conjeturas sobre la capacidad
- Obtener beneficios de las grandes economías de escala
- Aumentar la velocidad y la agilidad
- Convertirse en una empresa global en minutos

Well-Architected Framework
- Operational excellence: Mejora continua de procesos.
- Security: Protect data and information.
- Reliability: Recovery and adapting.
- Performance efficiency: Select the correct services based on requirements.
- Cost optimization: Scaling without overspending
- Sustainability: Reduce the environment impact.

<div id="section2"> </div>

## Cómputo en la nube

Amazon Elastic Compute Cloud (IaaS)

* Tipos de instancias
* Opciones de facturación
* Amazon EC2 Auto Scaling
* Elastic Load Balancing
* Amazon SNS and Amazon SQS

Tenencia múltiple, el hypervisor coordina y AWS administra.

Configuraciones:
* SO:
    * Windows
    * Linux
* Aplicaciones empresariales internas
* Aplicaciones web
* Bases de datos
* Software de terceros

Escalado vertical
Escalado Horizontal
Controlar aspectos de red de EC2

### Tipo de instancias EC2

Capacidades de cómputo, memoria, redes y almacenamiento.

* De uso general:
    * Recursos equilibrados
    * Cargas de trabajo diversas
    * Servidores Web
    * Repositorios de código
* Optimizada para cómputo:
    * Altos niveles de cómputo
    * Servidores de juego
    * Cómputo de alto rendimiento (HPC)
    * Modelado científico
* Optimizadas para memoria
    * Tareas de alto uso de memoria
* Cómputo acelerado
    * Cálculos de números en coma flotante
    * Procesamiento gráfico
    * Coincidencias de patrones de datos
    * Utilizar aceleradores de software
* Optimizadas para almacenamiento
    * Alto rendimiento para datos almacenados localmente

### Precios de instancias EC2

* Bajo demanda
* Savings Plans: 
    * Compromiso de uso constante en 1 o 3 años. 
    * Ahorros de hasta 72%.
    * Compromiso de gasto por hora a una familia de instancias 
* Instancia reservadas: Uso predecible. Hasta 75%
    * Standard: Indicas la familia y el tamaño, la plataforma, la tenencia y la región de la instancia.
    * Convertibles: Zonas de disponibilidad diferentes
* Instancias tipo spot: Cómputo adicional con hasta 90%. Carga de trabajo por lotes. 
* Servidores dedicados: No son compartidos. 

### Escalado de Amazon EC2

Servicio: Amazon EC2 Autoscaling:
* Escalado dinámico: responde a la demanda cambiante
* Escalado predictivo: programa automáticamente el número correcto de instancias de Amazon EC2 en función de la demanda prevista
* Escalado Horizontal
* Escalado Vertical

Grupo de Autoscaling:
* Mínimo
* Capacidad deseada
* Capacidad máxima

### Arquitecturas desacopladas
* Elastic Load Balancing
* Simple Queu Service
* Simple Notification Service

### Elastic Load Balancing

* Servicio administrado
* Es regional
* Balanceo de carga

### Amazon SQS and Amazon SNS

* SQS: Servicios de colas:
    * Enviar, almacenar y recibir mensajes entre componentes de software a cualquier volumen
    * Carga: datos en un mensaje
* SNS: Servicios de mensajes
    * Enviar mensajes entre servicios
    * Enviar mensajes a usuarios finales mediante email, sms o notificaciones push
    * Pub/Sub: Modelo publicación subscripción
    * Enviar mensaje a tema que a su vez envía mensaje a usuarios de ese tema

### Servicios de cómputo adicionales


* Amazon Elastic Container Service (ECS)
* Amazon Elastic Kubernetes Service (EKS)
* Serverless:
    * AWS Lambda
    * AWS Fargate (For ECS and EKS)

<div id="section3"> </div>

## Infraestructura global y fiabilidad

<div id="section4"> </div>

## Redes

<div id="section5"> </div>

## Almacenamiento y bases de datos

<div id="section6"> </div>

## Seguridad

<div id="section7"> </div>

## Monitoreo y análisis

<div id="section8"> </div>

## Precios y soporte

<div id="section9"> </div>

## Migración e innovación

<div id="section10"> </div>

## El traspaso a la nube

<div id="section11"> </div>

## Conceptos básicos de AWS Certified Cloud Practitioner

