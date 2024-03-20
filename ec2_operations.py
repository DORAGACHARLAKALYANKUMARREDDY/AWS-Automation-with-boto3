import boto3

aws_management_console=boto3.session.Session(profile_name="default")
ec2_console=aws_management_console.client(service_name="ec2")

# response=ec2_console.stop_instances(
#     InstanceIds=['i-046408a20e4950d90']
# )

# response=ec2_console.start_instances(
#     InstanceIds=['i-046408a20e4950d90']
# )

# response=ec2_console.terminate_instances(
#     InstanceIds=['i-046408a20e4950d90']
# )