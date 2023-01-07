import boto3

# create s3 client
myS3 = boto3.client('s3')

# list s3 bucket
myBuckets = myS3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in myBuckets['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)