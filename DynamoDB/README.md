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
* [Course Repository](https://github.com/acloudfan/DynamoDB-For-Architects)

## Commands examples

```bash
aws dynamodb list-tables --endpoint-url http://localhost:8000
```

Create Table

```bash
aws dynamodb create-table --table-name  test --attribute-definitions AttributeName=PK,AttributeType=S AttributeName=SK,AttributeType=S  --key-schema AttributeName=PK,KeyType=HASH AttributeName=SK,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --endpoint-url http://localhost:8000
```

Add items

```bash
aws dynamodb put-item --table-name test --item "{\"PK\": {\"S\": \"doe@example.com\"}, \"SK\": {\"S\": \"John Doe\"}, \"Age\": {\"N\": \"31\"}}" --endpoint-url http://localhost:8000

aws dynamodb put-item --table-name  test --item "{\"PK\": {\"S\": \"doe@example.com\"}, \"SK\": {\"S\": \"Jane Doe\"}, \"Age\": {\"N\": \"28\"}}" --endpoint-url   http://localhost:8000
```

Read All Items

```bash
aws dynamodb scan --table-name  test --endpoint-url http://localhost:8000
```

Get specific items

```bash
aws dynamodb get-item  --table-name test --key "{\"PK\": {\"S\": \"doe@example.com\"}, \"SK\": {\"S\": \"John Doe\"}}" --endpoint-url   http://localhost:8000
```

Delete Table

```bash
aws dynamodb delete-table --table-name  test --endpoint-url   http://localhost:8000
```

## Fundamentals 

### Storage And Charges

* Charged for amount of storage
* Charged for number of Read and Write
* Charged for other features.

Storage Classes:
* Standard
* Standard - IA

RRU means Read Request Unit: 4KB chunks of data
Strongly consistent read: IO operations in primary partition (1 RRU)
Eventually consistent read: IO operations in secondary partition (0.5 RRU)

WRU means Write Request Unit: 1KB chunks of data

RCU means Read Capacity Unit
WRU means Write Capacity Unit

Maximun numbers of reads/second: 
* 3000 Strongly consistent reads of 4KB chunks
* 6000 Eventually consistent reads of 4KB chunks

Maximun numbers of writes/second:
* 1000 writes of 1KB chunks