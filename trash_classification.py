
import numpy as np
import cv2


cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)


cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

import csv
import boto3

access_key_id = 'AKIA6GG5DNG4Z44BCN2H'
secret_access_key = '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'

i = 0
for i in expression_list:
    pass
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

import pandas as pd
df = pd.read_csv('database.csv')
# print few rows
# print(df)
object=response["Labels"][0]["Name"]
nrow,_ = df.shape
#display circles represent for patients
for i in range(0, nrow):
    name = df.iloc[i,0]
    if (str(name) == object):
        print(response["Labels"][0]["Name"])
        print(response["Labels"][0]["Confidence"], "%") 
        print(df['Type'][i]) 
    # else:
    #     print("Not given")