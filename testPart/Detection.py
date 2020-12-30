import csv
import boto3

access_key_id = 'AKIA6GG5DNG4Z44BCN2H'
secret_access_key = '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'

photo = 'opencv_frame_0.png'
label_counter = 0
region = "ap-southeast-1"
client= boto3.client('rekognition',region_name="ap-southeast-1",
 aws_access_key_id= access_key_id,
 aws_secret_access_key= secret_access_key)  
with open(photo,'rb')as source_image:
    source_bytes= source_image.read()  
response= client.detect_labels(Image={'Bytes':source_bytes},
MaxLabels=10,
MinConfidence=95)
print(response)
