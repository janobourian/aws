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