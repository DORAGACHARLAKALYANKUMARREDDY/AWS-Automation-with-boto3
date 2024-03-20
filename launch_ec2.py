import boto3
 
aws_management_console = boto3.session.Session(profile_name="default")
ec2_console = aws_management_console.client('ec2')

response = ec2_console.run_instances(
    ImageId='ami-09d3b3274b6c5d4aa',#Corrected AMI ID
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)  
