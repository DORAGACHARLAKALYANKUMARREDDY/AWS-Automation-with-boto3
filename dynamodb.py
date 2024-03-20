import boto3

# Create a Boto3 client for CloudFormation
cloudformation_client = boto3.client('cloudformation')
template_body = """
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyDynamoDBTable": {
      "Type": "AWS::DynamoDB::Table",
      "Properties": {
        "TableName": "exampleTable",
        "AttributeDefinitions": [
          {
            "AttributeName": "MyPartitionKey",
            "AttributeType": "S"
          }
        ],
        "KeySchema": [
          {
            "AttributeName": "MyPartitionKey",
            "KeyType": "HASH"
          }
        ],
        "ProvisionedThroughput": {
          "ReadCapacityUnits": 5,
          "WriteCapacityUnits": 5
        }
      }
    }
  }
}
"""

# Create the CloudFormation stack
stack_name = 'DynamoDBStack'
response = cloudformation_client.create_stack(
    StackName=stack_name,
    TemplateBody=template_body,
    TimeoutInMinutes=5,
    Capabilities=['CAPABILITY_IAM']
)

print("Stack creation response:", response)
