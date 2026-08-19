# Getting Started

## Core concepts

* You can create a lot of stacks and use them inside the App
* Every `Stack` has methods and APIs, the most important is `add_dependecy()`
* We can nest stacks
* CDK Stages allow to develop the same resources in several accounts.
* `Constructs` are the basic building blocks of AWS Cloud Development Kit
  * `L1`: `CfnBucket` to follow `AWS::S3::Bucket`
  * `L2`: `s3.Bucket`
  * `L3`: They are a complete pattern
* `Props` are the configuration objects for constructs

## About `L1` Constructs

This kind of constructs uses `Cfn` prefix to represent its low level, because it is so similar to `CloudFormation`. Please, aboid to use `L1` constructs.

## About `L2` Constructs

This is the best choice if you want to work with CDK, because they have the `L1` abstraction and a lot of methods to work with some important actions such `grant_access`.

## About `L3` Constructs

They are a common pattern following specific solutions, again, they follow a pattern.

If you want to learn more about the main differences between them, please check [this](https://www.youtube.com/watch?v=PzU-i0rJPGw&t=374s)
