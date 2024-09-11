# Admisión y Gobernanza

## Estrategias multicuenta

* AWS Organizations
* Service Control Policies (SCP)
    * NO afecta los roles utilizados en servicios de AWS para integración con AWS Organizations
    * Debe tener un ALLOW explícito
* Organization Units
* Descuentos:
    * Ejemplo de instancias compartidas en la misma AZ
* AWS Control Tower: apoyo en la configuración de AWS Organizations
* AWS Resource Access Manager: Compartir recursos entre cuentas dentro o fuera de la organización
* AWS Service Catalog: Servicios permitidos y de rápido acceso

## Trusted Advisor

* Herramienta que proporciona orientación siguiendo las prácticas recomendadas de AWS
* Dimensiones:
    * Cost Optimization
    * Performance
    * Security
    * Fault Tolerance
    * Service Limits

## AWS CloudWatch, CloudTrail, Config

* CloudWatch: Monitoreo de métricas
    * Instancias de EC2
    * Volúmenes de EBS
    * Buckets de S3
    * Facturación 
    * Límites de servicio
    * Métricas personalizadas
* Alarms:
    * OK
    * INSUFFICIENTE_DATA
    * ALARMA
* CloudWatch Logs:
    * Conjunto de logs a nivel cuenta/organización
    * Para instancias de EC2 se debe implementar el CloudWatch Agent
* AWS CloudTrail
* AWS Config:
    * Auditoría y registro de conformidad de los recursos de AWS
    * Ver el cumplimiento de un recurso a lo largo del tiempo

## AWS Systems Manager y OpsWorks

* AWS Systems Manager: 
    * Ayuda a gestionar sistemas EC2 y On-Premises a escala
    * Se instala mediante el System Manager Agent
    * Session Manager 
        * Iniciar Sesión en EC2 sin SSH
* Similar A System Manager
    * Utiliza Chef o Puppet

## AWS CloudFormation

* Stack Designer

## AWS Well Architected Framework

* Six Advantages:
    * Change CaPex for OpEx
    * Stop Guessing capacity
    * Stop spending maintaining Servers
    * Go Global in minutes
    * Masive Economies of scale
    * Agility

* Pillars:
    * Operacional Excellence
    * Security
    * Reliability
    * Performance Operations
    * Cost Optimization
    * Sustainability

## AWS Cloud Adoption Framework

* Perspectivas:
    * Comercial
    * Personas
    * Gobernanza
    * Plataforma
    * Seguridad 
    * Operaciones
