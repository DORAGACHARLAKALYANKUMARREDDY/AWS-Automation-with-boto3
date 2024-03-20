import boto3

# Create a Boto3 client for CloudFormation
cloudformation_client = boto3.client('cloudformation')

# Define the CloudFormation template
template_body = """
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyVPC": {
      "Type": "AWS::EC2::VPC",
      "Properties": {
        "CidrBlock": "10.0.0.0/16",
        "EnableDnsSupport": "true",
        "EnableDnsHostnames": "true",
        "Tags": [
          { "Key": "Name", "Value": "MyVPC" }
        ]
      }
    },
    "PublicSubnet": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "VpcId": { "Ref": "MyVPC" },
        "CidrBlock": "10.0.0.0/24",
        "AvailabilityZone": "us-east-1a",
        "MapPublicIpOnLaunch": "true",
        "Tags": [
          { "Key": "Name", "Value": "PublicSubnet" }
        ]
      }
    },
    "RouteTable": {
      "Type": "AWS::EC2::RouteTable",
      "Properties": {
        "VpcId": { "Ref": "MyVPC" },
        "Tags": [
          { "Key": "Name", "Value": "MyRouteTable" }
        ]
      }
    },
    "PublicRoute": {
      "Type": "AWS::EC2::Route",
      "DependsOn": "InternetGatewayAttachment",
      "Properties": {
        "RouteTableId": { "Ref": "RouteTable" },
        "DestinationCidrBlock": "0.0.0.0/0",
        "GatewayId": { "Ref": "InternetGateway" }
      }
    },
    "InternetGateway": {
      "Type": "AWS::EC2::InternetGateway",
      "Properties": {
        "Tags": [
          { "Key": "Name", "Value": "InternetGateway" }
        ]
      }
    },
    "InternetGatewayAttachment": {
      "Type": "AWS::EC2::VPCGatewayAttachment",
      "Properties": {
        "VpcId": { "Ref": "MyVPC" },
        "InternetGatewayId": { "Ref": "InternetGateway" }
      }
    },
    "SSHSecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupDescription": "Allow SSH access",
        "VpcId": { "Ref": "MyVPC" },
        "SecurityGroupIngress": [
          {
            "IpProtocol": "tcp",
            "FromPort": "22",
            "ToPort": "22",
            "CidrIp": "0.0.0.0/0"
          }
        ]
      }
    }
  }
}
"""

# Create the CloudFormation stack
stack_name = 'MyVPCStack'
response = cloudformation_client.create_stack(
    StackName=stack_name,
    TemplateBody=template_body,
    TimeoutInMinutes=5,
    Capabilities=['CAPABILITY_IAM']
)

print("Stack creation response:", response)
