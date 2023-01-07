import boto3

# create s3 client
myS3 = boto3.client("s3")

# Get a list of all bucket names from the response
myBuckets = myS3.list_buckets()
buckets = [bucket["Name"] for bucket in myBuckets["Buckets"]]

# get file from local storage
# filename = "file.txt"
filename = "image.jpg"
newFilename = "uploadedimage.jpg"
# bucket_name = buckets[0]
bucket_name = 'my-bucket00103'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.

myS3.upload_file(filename, bucket_name, newFilename)

# Print out the bucket list
# print("Bucket List: %s" % buckets)
