# Seguridad en la nube

## Share Responsability Model

Check: https://aws.amazon.com/es/compliance/shared-responsibility-model/

* AWS: De la nube
* Cliente: En la nube

* Access: CLI, SDK, and Console
* Máximo dos Access Keys por usuario

## Gestión de Identidad y Acceso (IAM - Identity and Access Management)

¿Cómo sabemos que eres quien dices ser?

* AAA: 
    * Authenticate: 
        * IAM Username/Password
        * Access Key
        * MFA
        * Federation
    * Authorize:
        * IAM Policies 
    * Audit:
        * CloudTrail

### Principales de AWS

* Root 
* Users, groups, and roles
* Temporal Security Credentials