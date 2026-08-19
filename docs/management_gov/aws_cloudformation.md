# CloudFormation

* Is a declarative way of outlining your AWS Infrastructure for any resources
* You can apply save strategies
* Automated generation of Diagram for your templates.
* Declarative programming
* Stacks for network, stacks for applications, and so on
* Deleting a stack deletes every single artifact that was created by CloudFormation
* Deploying CloudFormation Templates
  * Manual way
  * Using AWS CLI
* Templates has Tags:
  * stack-id
  * logical-id
  * stack-name

## Components

* AWSTemplateFormatVersion - "2010-09-09"
* Description
* Resources (MANDATORY)
* Parameters - the dynamic inputs for your template
* Mappings - the static variables for your template
* Outputs - references to what has been created
* Conditionals - list of conditions to perform resource creation

## Helpers

* References
* Functions
