import boto3
import botocore

BUCKET_NAME = 'my-bucket00103' # replace with your bucket name
KEY = 'uploadedimage.jpg' # replace with your object key
newKey = 'downloadedimage.jpg'
s3 = boto3.resource('s3')
mys3 = boto3.client('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, newKey)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise