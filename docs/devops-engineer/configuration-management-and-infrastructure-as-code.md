# Domain 2 Configuration Management and IaC

## Service Catalog

AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures.

### Key Features

- Users that are new to AWS have too many options, and may create stacks that are not compliant / in line with th rest of the organization
- Administrators can create standardized products that are pre-approved for use
- Some users just want a quick self-service portal to launch a set of authorized products pre-defined by admins
- Includes: virtual machines, databases, storage options, etc....
- Enter AWS Service Catalog!
- Admins create portfolios of products (CloudFormation templates) that are approved for use
- Helps with governance, compliance, and consistency
- Can give user access to launching products without requiring deep AWS knowledge
- Integration with self-service portals such as Service Now
- Cycle:
    - Admins Tasks:
        - Product -> Portfolio -> Control
    - User Tasks:
        - Product List -> Launch -> Provisioned Products

### Service Catalog - Stack Set Constraints

- Allow you to configure Product deployment options using CloudFormation StackSets
- Accounts: identify AWS accounts where you want to create products
- Regions: identify AWS regions where you want to deploy to (with Order)
- Permissions: IAM StackSet Administrator Role to manage target AWS accounts

### Service Catalog - Launch Constraints

- IAM Role assigned to a Product which allows a user to launch, update, or terminate a product with minimal IAM permissions.
- Example: end user has access only to Service Catalog, all other permissions required are attached to the Launch Constraint IAM Role
- IAM Role must have the following permissions:
    - CloudFormation (Full Access)
    - AWS Services in the CloudFormation template
    - S3 Bucket which contains the CloudFormation template (ReadAccess)

```json
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "cloudformation:CreateStack",
            "cloudformation:DeleteStack",
            "cloudformation:DescribeStackEvents",
            "cloudformation:GetTemplateSummary",
            "cloudformation:SetStackPolicy",
            "cloudformation:ValidateTemplate",
            "cloudformation:UpdateStack",
            "ec2:*",
            "servicecatalog:*",
            "sns:*"
        ],
        "Resource": "*"
    },
    {
        "Effect": "Allow",
        "Action": [
            "s3:GetObject"
        ],
        "Resource": [
            "arn:aws:s3:::<bucket_name>",
            "arn:aws:s3:::<bucket_name>/*"
        ],
        "Condition": {
            "StringEquals": {
                "s3:ExistingObjectTag/ServiceCatalogProduct": "true"
            }
        }
    }
    ]
}
```

### Service Catalog - Continuous Delivery Pipeline (Syncing with CodeCommit)

- Developer: push `product-a.yml`
- CodeCommit: in `mapping.yml` invoke Lambda
- Lambda checkout CloudFormation templates 
- Lambda update/create Product
- Service Catalog has the Product A