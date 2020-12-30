import pandas as pd
# import data to dataframe
df = pd.read_csv('./GreenAble - Trang tính1.csv') #unprocessed data
# print few rows
print(df.head())
# print(df)
object=response["Labels"][0]["Name"]
nrow,_ = df.shape
#display circles represent for patients
for i in range(0, nrow):
    name = df.iloc[i,0]
    if (str(name) == object):
        # print(response["Labels"][0]["Name"])
        # print(response["Labels"][0]["Confidence"], "%") 
        print(df['Type'][i]) 
    # else:
    #     print("Not given")