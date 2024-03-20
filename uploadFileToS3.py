import boto3

session = boto3.session.Session(profile_name="default")
s3_client = session.client('s3')

bucket_name = 'naniwebsite'
local_file_path = 'p1.pdf'
s3_object_key = 'abc'

# Determine the content type
content_type = 'application/pdf'

# Upload the file to S3 with content type metadata
with open(local_file_path, 'rb') as file:
    s3_client.upload_fileobj(
        file,
        bucket_name,
        s3_object_key,
        ExtraArgs={'ContentType': content_type}
    )

print("File uploaded successfully to S3 bucket:", bucket_name)
