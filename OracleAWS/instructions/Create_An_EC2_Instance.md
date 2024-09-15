## Create an EC2 instance

Go to EC2 Dashboard

Click ==Launch Instance==

**Name** co-ec2-01

**Select** Amazon Linux AMI

**Instance Type** t2.large

Create key pair if needed (see below)

In ==Network settings== set VPC to ==co-vpc-01== and subnet ==co-subnet-1a==

**Auto-assign public IP** Enable

**Create security group** selected

**Security group name** co-sg-01 **type** ssh **Source type** My IP

**Configure storage section**

**root volume** 10GiB

**Add volumes** 2 EBS 30 GiB volumes

In ==Advanced pane== set Delete on termination on root volume to ==Yes==

Click ==Launch instance==