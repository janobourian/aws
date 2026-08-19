# VPC

## VPC FlowLog

* Is a way to catch the flow in/outbound you VPC through CloudWatch
* Steps to apply:
  * You have to create the Virtual private Cloud
  * Create a public subnet
  * Create a private subnet
  * Create a route table and associate it with the public subnet
  * Create a route table and associate it with the private subnet
  * Associate the public route table with the Internat Gateway
  * Create the log group
  * Create the role from VPC Flow Logs to Cloudwatch
    * Create the role with Trust Relationship
    * Add the permissions
  * Create the VPC Flow Logs in the VPC
