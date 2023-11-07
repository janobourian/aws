# DynamoDB

## More information 

For more information please see the [documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) or check this [link](https://ddb.acloudfan.com/1.service-under-the-hood/)

## Introduction 

Item maximun size: 400 KB
Maximun amount of data stored in the partition: 10 GB

Item is divided in:
* Partition Key (a.k.a. Hash Key)
* Value (a.k.a. Item collection):
    * Sort Key (a.k.a. Range Key)

## Tools

* [NoSQL Workbench](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html)
* [Python 3](https://www.python.org/downloads/)
* [Boto 3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
* [Visual Studio Code](https://visualstudio.microsoft.com/vs/community/)
* [AWS Toolkit for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode)
* [Git](https://github.com/git-guides/install-git)
* [JRE](https://docs.oracle.com/javase/10/install/installation-jdk-and-jre-microsoft-windows-platforms.htm#JSJIG-GUID-96EB3876-8C7A-4A25-9F3A-A2983FEC016A)

## Commands examples

```bash
aws dynamodb list-tables --endpoint-url http://localhost:8000
```