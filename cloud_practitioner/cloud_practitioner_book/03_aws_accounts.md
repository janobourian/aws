# Exploring AWS Accounts, Multi-Accounts Strategy and AWS Organizations

## AWS Environment

* Multiple Accounts:
    * Sandbox
    * Development
    * UAT/Testing
    * Production

* Benefits:
    * Administrative isolation between workloads
    * Limit visibility and discoverability of workloads
    * Isolation of security and identity management
    * Isolation of recovery or audit accounts

## AWS Landing Zone

* It will be deprecated, use AWS Control Tower instead

## AWS Control Tower

* Creation of an AWS Organizations and multi-account setup
* Identity and access management with AWS Single Sign-On (SSO) default directory services
* Account Federation using SSO
* Centralized logging using AWS CloudTrail and AWS Config

## AWS Organizations

* Key concepts:
    * It is a free service
    * OUs: Organizations Units
    * SCP: Service Control Policies

* Core AWS OUs:
    * Infrastructure services account:
        * Amazon Machine Images (AMIs)
    * Security Services:
        * Identity and Access Management

1.- A
2.- A
3.- A, B
4.- A
5.- A
6.- A -> B
7.- C -> B