# Virtual Private Cloud

Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways. You can also create a hardware virtual private network (VPN) connection between your corporate data center and your VPC and leverage the AWS cloud as an extension of your corporate data center.

## VPC Endpoints

A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not require public IP addresses to communicate with resources in the service. Traffic between your VPC and the other service does not leave the Amazon network.

### Interface Endpoints (Powered by Private Link)

An interface endpoint is an elastic network interface with a private IP address that serves as an entry point for traffic destined to a supported service.

Features:

* Provisions an ENI as an entry point
* Supports most AWS services
* $ per hour + $ per GB of data processed

### Gateway Endpoints

A gateway endpoint is a gateway that you specify as a target for a route in your route table for traffic destined to a supported AWS service.

Features:

* Provision a gateway and must be used as a target in route table (does not use security group)
* Supports both S3 and DynamoDB
* Free
