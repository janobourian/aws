# Create Static html site

If you need more information please check the next [link](https://adamtheautomator.com/host-a-website-on-aws-ec2/)

## Steps

```bash
sudo su
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
```