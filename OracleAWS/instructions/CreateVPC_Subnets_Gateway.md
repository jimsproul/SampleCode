# Create VPC, Subnets and Gateway

In account select VPC service

### Create VPC

**Region** us-east-1

**Name** co-vpc-01

**CIDR** 10.1.0.0/16

### Create Subnets

Creating subnets for all availability zones

#### For each AZ

In this example setting up for AZs 1a, 1b and 1c

**Name** co-subnet-az#

**VPC** co-vpc-01

**AZ** Select one 

**Subnet CIDR** 10.1.#.0/24 where # is sequence of subnet

### Create Internet Gateway

**Name** co-gateway-01

Then attach to VPC

**Attach to** co-vpc-01

