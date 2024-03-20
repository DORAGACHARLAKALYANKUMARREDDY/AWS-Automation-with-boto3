import boto3
aws_management_console=boto3.session.Session(profile_name="default")
ec2_console=aws_management_console.resource(service_name="ec2",region_name='us-east-1')

#List all ebs volumes

# for each in ec2_console.volumes.all():
#     print(each.id,each.state)

a={'Name':'status','Values':['available']}
for each in ec2_console.volumes.filter(Filters=[a]):
    print(each.id,each.state)