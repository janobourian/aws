# CDK Overview

If you are lookig for more information about CDK you cand check and follow the official documentation [AWS Documentation](https://docs.aws.amazon.com/cdk/v2/guide/home.html)

The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework to define your cloud application resources using familiar programming languages. It allows you to model and provision your cloud application resources using code, making it easier to manage and automate infrastructure deployment.

With AWS CDK, you can use languages like TypeScript, JavaScript, Python, Java, and C# to define your cloud infrastructure. The CDK provides a high-level object-oriented abstraction over AWS CloudFormation, allowing you to work with constructs that represent AWS resources and services.

The key features of AWS CDK include:

1. **Infrastructure as Code**: Define your cloud infrastructure using code, enabling version control, collaboration, and automation.
2. **Constructs**: Use pre-built constructs that represent AWS resources, making it easier to create resources and reusable code.
3. **Multi-language Support**: Choose from multiple programming languages to define your infrastructure, allowing you to work in a language you are comfortable with.
4. **Integration with AWS Services**: Seamlessly integrate with various AWS services and leverage their capabilities.
5. **Deployment Automation**: Use the CDK CLI to deploy your infrastructure changes automatically, reducing manual effort and potential errors.
6. **Extensibility**: Create custom constructs and share them with the community, fostering collaboration and code reuse.

AWS CDK is particularly useful for developers and DevOps teams who want to streamline the process of defining and deploying cloud infrastructure. It simplifies the management of complex infrastructure setups and promotes best practices in infrastructure design and deployment.

To get started with AWS CDK, you can follow these steps:

1. Install the AWS CDK CLI: You can install the AWS CDK CLI using npm

```bash
npm install -g aws-cdk
```

1. Create a new CDK project: Use the CDK CLI to create a new project

```bash
cdk init app --language typescript
```

1. Define your infrastructure: Use the programming language of your choice to define your cloud resources using constructs
2. Deploy your infrastructure: Use the CDK CLI to deploy your infrastructure changes to AWS

```bash
cdk deploy
```

1. Monitor and manage your infrastructure: Use the AWS Management Console or AWS CLI to monitor and managed your deployed resources.
2. Clean up resources: When you no longer need the resources, you can use the CDK CLI to destroy them

```bash
cdk destroy
```

For more detailed information and examples, you can refer to the official AWS CDK documentation and explore the various constructs and features available in the framework.

## Important resources

* [Awesome CDK](https://github.com/kalaiser/awesome-cdk)
* [aws-cdk-examples](https://github.com/aws-samples/aws-cdk-examples)
* [AWS CDL Immersion Day Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/10141411-0192-4021-afa8-2436f3c66bd8/en-US)
* [aws-cdk-library](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk/README.html)
* [aws-cdk-python-reference](https://docs.aws.amazon.com/cdk/api/v2/python/)
* [CDK dev](https://cdk.dev)
* [CDK for Terraform](https://developer.hashicorp.com/terraform/cdktf)
* [CDK Patterns](https://cdkpatterns.com)
* [Construct Hub](https://constructs.dev)
