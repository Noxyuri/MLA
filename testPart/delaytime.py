import cv2
import time

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
img_counter = 0
frame_set = []
start_time = time.time()

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if time.time() - start_time >= 5: #<---- Check if 5 sec passed
        img_name = "opencv_frame_0.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        start_time = time.time()
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
        import pandas as pd
        # import data to dataframe
        df = pd.read_csv('GreenAble - Trang tính1.csv') #unprocessed data
        # print few rows
        # print(df.head())

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
