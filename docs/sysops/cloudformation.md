# SysOps Administrator Associate Course

* Is a declarative way of outlining your AWS Infrastructure, for any resources. 
* You have a visual way to view your CloudFormation on Infrastructure Composer

* Benefits:
    * Infrastructure as code
    * Cost:
        * Each resources within the stack is tagged
        * You can estimate the costs of your resources using the CloudFormation template
        * Savings strategy: In Dev, you could automation deletion of templates at 5PM and recreated at 8AM, safely
    * Productivity:
        * Ability to destroy and re-create an infraestructure on the cloud on the fly
    * Separation of concern: 
        * create many stacks for many apps
    * Do not re-invent the wheel

* How CloudFormation Works
    * Template -> Upload -> S3 Bucket -> AWS CloudFormation -> Create -> Stack -> Create -> AWS Resources

* Deploying CloudFormation Templates
    * Manual Way
    * Automated way

* Building Blocks
    * Template's Components
        * AWS Template Format Version
        * Description
        * Resources
        * Parameters 
        * Mappings 
        * Outputs
        * Conditional
    * Template's Helpers
        * References 
        * Functions

## CloudFormation for SysOps

* General information: https://docs.aws.amazon.com/cloudformation/
* Technical and specific information: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/introduction.html


### Create

```yml
---
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone: us-east-1a
      ImageId: ami-0ff8a91507f77f867
      InstanceType: t2.micro
```

### Update

```yml
---
Parameters:
  SSHSecurityGroupDescription:
    Type: String
    Default: Security Group for SSH access via port 22
    Description: This is a Security Group to work in CloudFormation

  SecurityGroupDescription:
    Type: String
    Default: Security Group for MyEC2Instance
    Description: This is a Security Group to work in CloudFormation

Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone: us-east-1a
      ImageId: ami-0ff8a91507f77f867
      InstanceType: t2.micro
      SecurityGroups:
        - !Ref SSHSecurityGroup
        - !Ref ServerSecurityGroup
    
  MyEIP:
    Type: AWS::EC2::EIP
    Properties:
      InstanceId: !Ref MyEC2Instance
  
  SSHSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: !Ref SSHSecurityGroupDescription
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 0.0.0.0/0
  
  ServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: !Ref SecurityGroupDescription
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '80'
          ToPort: '80'
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 192.168.1.1/32
```

You can check the Replace operation in very CloudFormation update and you can check the terminate configuration for every resource created. 

### Resources

* The only Mandatory Field
* Can I create a dynamic number of resources?
  * Yes, you can by using CloudFormation Macros and Transform
  * It it not in the scope of this course
* Is every AWS Service supported?
  * Almost. Only a select few niches are not there yet
  * You can work around that using CloudFormation Custom Resources

```yaml
Resources:
  MyCustomResource:
    Type: 'AWS::EC2::Instance'
    Properties:
      AvailabilityZone: us-east-1a
      ImageId: ami-0ff8a91507f77f867
      InstanceType: t2.micro
```

### Parameters

* Parameters are a way to provide inputs to your AWS CloudFormation template
* They are important to know about if
  * You want to reuse your templates across the company
  * Some inputs can not be determined ahead of time
* Parameter are extremely powerful, controlled and can prevent errors from happening in your templates, thanks to types.

* When should you use a Parameter?
  * Ask yourself this:
    * Is this CloudFormation resources configuration likely to change in the future?
    * If so, make it a parameter
  * You won't have to re-upload a template to change its content

* Settings
  * Type
    * String
    * Number
    * CommaDelimiedList
    * List<Number>
    * AWS-Specific Parameter
      * to help catch invalid values - match against existing values in the AWS account
    * List<AWS-Specific Parameter>
    * SSM Parameter
      * get parameter value from SSM Parameter Store
  * Description
  * ConstaintDescription (string)
  * Min/MaxLength
  * Min/MaxValue
  * Default
  * AllowedValues (array)
  * AllowedPattern (regex)
  * NoEcho (boolean)

* AllowedValues (availables values)

```yml
Parameters:
  InstanceType:
    Description: Choose an EC2 instance type
    Type: String
    AllowedValues:
      - t2.micro
      - t2.small
      - t2.medium
    Default: t2.micro

Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !Ref InstanceType
      ImageId: ami-0c02fb55956c7d316
```

* NoEcho (not show the value)

```yml
Parameters:
  DBPassword:
    Description: The database admin password
    Type: String
    NoEcho: true

Resources:
  MyDBInstance:
    Type: AWS::RDS::DBInstance
    Properties:
      DBInstanceClass: db.t2.micro
      AllocatedStorage: 20
      Engine: mysql
      MasterUsername: admin
      MasterUserPassword: !Ref DBPassword
      DBInstanceIdentifier: mydbinstance
```

* Parameter references
  * The `Fn::Ref` function can be leveraged to reference parameters
  * In `YAML` we have the shortcut `!Ref` 

```yml
Resources:
  DBSubnet1:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVPC
```

#### Pseudo Parameters

* These can be used at any time and are enabled by default
* Important pseudo parameters:
  * AWS::AccountId
  * AWS::Region
  * AWS::StackId
  * AWS::StackName
  * AWS::NotificationARNs
  * AWS::NoValue