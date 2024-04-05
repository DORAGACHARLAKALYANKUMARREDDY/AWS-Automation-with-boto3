import boto3

def create_s3_bucket(bucket_name):
    try:
        s3_client=boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def delete_s3_bucket(bucket_name):
    try:
        s3_client = boto3.client('s3')
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting bucket: {e}")

if __name__ == "__main__":
    bucket_name = 'nani15'

    create_s3_bucket(bucket_name)

    # delete_s3_bucket(bucket_name)
