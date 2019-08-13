import pandas as pd
import numpy as np
import time
from  scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
# dt=pd.read_csv(r'F:\Python_run\convert.csv',header=None,parse_dates=[5])#parse_dates=[5]表示将[5]指定为时间，
                                                                         # 这样也已经改变了[5]的数据类型，其value值也就是时间戳
dt=pd.read_csv(r'C:\Users\Administrator\Desktop\jupyter-notebook\data5.csv')
dt['datatime']=0
for index,row in dt.iterrows():
    # print(row)
    # break
    dt.loc[index,'datatime']=time.mktime(time.strptime(row[2], "%Y/%m/%d %H:%M"))
    # print dt['datatime']
    # print row[5].value
# dt[9]=dt['datatime']
# print(dt.head(10))
dt.to_csv(r'F:\h\data5.csv',index=None,header=None)