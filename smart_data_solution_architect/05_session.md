# Almacenamiento

* Almacenamiento:
    * Bloque:
        * Se cambia sólo un bloque
    * Archivo
        * Se cambia sólo un bloque
    * Objecto
        * Se cambia todo el objeto

* Información relevante al almacenamiento:
    * Durabilidad
    * Disponibilidad
    * Seguridad
    * Costo
    * Escalabilidad
    * Rendimiento
    * Integración

## Amazon Elastic Block Store (EBS)

* Instance Storage: Almacenamiento Efímero
* Amazon EBS: Para cargas de trabajo con uso intensivo de transacciones y rendimiento
* Snapshots: Copias incrementales o para mover volúmenes de una AZ a otra
* Se conecta a las instancias mientras se ejecuta, pero no está en el mismo servidor
* Sólo se monta una instancia a la vez (Pero existe la posibilidad si sólo se utiliza un tipo de instancia específico)
* Están enlazados a una zona de disponibilidad específica:
    * Para mover se debe crear una instantánea
* Son una memoria USB
* Free tier: 30GB de SSD o magnético al mes
* Puedes controlar el comportamiento de EBS cuando se finaliza una instancia EC2
* Se factura por toda la capacidad provisionada
* Se puede escalar de manera automática, pero no se puede reducir la capacidad
* Casos de uso:
    * Conservar el volumen raíz cuando se termina la instancia

### Snapshot

* Es más barato mover EBS
* Se puede crear una papelera de reciclaje para conservar instantáneas
* Restauración rápida de instantáneas

### Amazon Data LifeCycle Manager

* Automatizar la creación
* Programar copias de seguridad
* Utilizar etiquetas de recursos
* No se puede usar para administrar instantáneas o AMI creadas fuera de DLM
* No se puede usar para administrar AMI respaldadas por el almacé de instancias