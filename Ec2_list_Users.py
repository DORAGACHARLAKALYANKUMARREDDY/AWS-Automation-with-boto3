import boto3

# Create a session without specifying a profile name
aws_management_console = boto3.session.Session(profile_name="default")

# Use the session to create a client for the desired service (EC2 in this case)
ec2_console = aws_management_console.client(service_name="ec2")

# Now you can use the client to interact with EC2
result = ec2_console.describe_instances()['Reservations']
for each_instance in result:
    for value in each_instance['Instances']:
        print(value['InstanceId'])
