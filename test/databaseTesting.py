import numpy as np
import cv2
import csv
import boto3

access_key_id = 'AKIA6GG5DNG4Z44BCN2H'
secret_access_key = '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'

photo = 'opencv_frame_0.png'

region = "ap-southeast-1" 
client= boto3.client('rekognition',region_name="ap-southeast-1",
 aws_access_key_id= access_key_id,
 aws_secret_access_key= secret_access_key)  
with open(photo,'rb')as source_image:
    source_bytes= source_image.read()  
response= client.detect_labels(Image={'Bytes':source_bytes},
MaxLabels=10,
MinConfidence=95)
# print(response)

import io
import requests
from io import BytesIO
import pandas as pd
files = requests.get('https://docs.google.com/spreadsheets/d/1ZPL7sejPopQVya3lE6F4-E1nPxJgqXaZ80fM-Xh-cDI/export?format=csv&id=1ZPL7sejPopQVya3lE6F4-E1nPxJgqXaZ80fM-Xh-cDI&gid=0')
assert files.status_code == 200, 'Wrong status code'
data = files.content

# import data to dataframe
df = pd.read_csv(BytesIO(data), usecols=['Name','Type']) #unprocessed data
# print few rows
# print(df)
# object=response["Labels"][0]["Name"]
nrow,_ = df.shape
k=0
while k<len(response["Labels"]):
    object= response["Labels"][k]["Name"]
    # print(object)
    for i in range(0, nrow):
        name = df.iloc[i,0]
        if (str(name) == object):
            print(response["Labels"][k]["Name"])
            print(response["Labels"][k]["Confidence"], "%") 
            print(df['Type'][i]) 
    k += 1
