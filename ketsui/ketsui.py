import pandas as pd

ketsui = pd.read_csv("ketsui.csv")

def roomnumber(number: int, malti: int=1):
    try:
        number_sam = ketsui[ketsui["roomnumber"] == number]
        number_sam = number_sam[number_sam["maltinumber"] == malti]
        return [str(number_sam["roomnumber"].iloc[-1]),str(number_sam["roomname"].iloc[-1]),str(number_sam["ketsuimessage"].iloc[-1])]
    except:
        return "number・numberの値がおかしい可能性があります"

def number(number: int):
    try:
        number_sam = ketsui[ketsui["indexnumber"] == number]
        return [str(number_sam["roomnumber"].iloc[-1]),str(number_sam["roomname"].iloc[-1]),str(number_sam["ketsuimessage"].iloc[-1])]
    except:
        return "number・numberの値がおかしい可能性があります"

# import random

# for i in range(10):
#     print(number(random.randrange(1, 26, 1))[2])