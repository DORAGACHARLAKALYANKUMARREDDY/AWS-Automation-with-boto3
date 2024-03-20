import boto3

# Create a session
aws_management_console = boto3.session.Session(profile_name="default")


# Use the session to create a client for the desired service (IAM in this case)
iam_client = aws_management_console.client('iam')
# Now you can use the client to interact with IAM
print('printing via client object')
response = iam_client.list_users()
for each_user in response['Users']:
    print(each_user['UserName'])
    
    
iam_resource =aws_management_console.resource('iam')
print('printing via resource object')
for each in iam_resource.users.all():
    print(each.name)
