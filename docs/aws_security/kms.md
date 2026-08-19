# KMS - Key Management Service

## Encryption in flight

* Data is encrypted before sending and decrypted after receiving (TLS/SSL)
* TLS certificates help with encryption (HTTPS)
* Encryption in flight ensures no MITM

## Encryption at rest (Server side encryption)

* Data is encrypted when stored on disk
* AWS KMS (Key Management Service) is used to manage encryption keys
* The encryption / decryption keys must be managed somewhere, and the server must have access to it

## Client-side encryption

* Data is encrypted before sending to the server and decrypted after receiving from the server

## KMS | Info

* AWS Encryption service
* Fully integrated with IAM for authorization
* KMS is a regional service (not global)
* Able to audi KMS Key usage using CloudTrail

## KMS | Types

* KMS Keys is the new name of KMS Customer Master Key
* Symmetric (AES-256 keys)
  * Single encryption key that is used to Encrypt and Decrypt
  * You never get access to the KMS Key unencrypted
* Asymmetric (RSA and ECC keys)
  * Public (Encrypt) and Private Key (Decrypt) pair
  * Used for Encrypt/Decrypt, or Sign/Verify operations
  * The public key is downloadable, but you cannot access the Private Key unencrypted
  * Use case: encryption outside of AWS by users who cannot call the KMS API
* Types:
  * AWS Owned Key
  * AWS Managed Key
  * Customer Managed Key created
  * Customer Managed Key imported
* Automatic Key rotation:
  * AWS-managed KMS Key: automatic every 1 year
  * Customer-managed Key: automatic and on-demand
  * Imported: only manual rotation possible using alias
* Key policies:
  * Default
    * Created if you do not provide a specific KMS Key Policy
    * Complete access to the key to the root user = entire AWS account
  * Custom
    * Define users, roles that can access the KMS Key
    * Define who can administer the key
    * Useful for cross-account access of your KMS Key

## Working with snapshots

* Create snapshot with you CMK
* Attach KMS policy to allow cross-account access
* Share the encrypted snapshot
* Create a copy of the snapshot encrypted with CMK
* Create a volume from the snapshot

## KMS | multi-region keys
