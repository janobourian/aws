# Deployment

Deployments:

* In-place deployment
* Blue/green deployment: Separate the versions at once
* Canary deployment: Deploy only for a few users before to scale
* Linear deployment: shift the traffic using the current time
* All-at-once deployment

Remember:

* Amazon ECS and AWS Lambda allows all deployments strategies
* Amazon EC2 and on-premises only allows In-place and sometimes Blue/green

AWS Elastic BeanStalk

* All-at-once
* Rolling
* Rolling with additional batch
* Immutable
* Traffic splitting

In general, AWS Elastic Beanstalk wants to preserve the EC2 instance instead of overwritte the current EC2 instance.
