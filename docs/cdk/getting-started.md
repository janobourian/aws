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