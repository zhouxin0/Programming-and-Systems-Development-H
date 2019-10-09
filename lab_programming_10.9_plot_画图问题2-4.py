#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:51:31 2019

@author: marco
"""

#question2
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import csv
df = pd.read_csv('fdata.csv')
print(df)
#df=pd.dataframe
date = df ['Date'].tolist()
open = df ['Open'].tolist()
high = df ['High'].tolist()
low = df ['Low'].tolist()
close = df ['Close'].tolist()

plt.plot(date,open,color='red')
'''
plt.plot(date,high,color='yellow')
plt.plot(date,low,color='green')
plt.plot(date,close,color='black')
plt.xlabel('date',color='red')
plt.ylabel('amount',color='green')
'''

data={'open':open,'high':high,'low':low,'close':close}
df = pd.DataFrame(data)
plt.plot(date,df)
plt.legend(data,loc=2)
print(data)

plt.show()

#question3
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import csv
df = pd.read_csv('fdata.csv')
print(df)
#df=pd.dataframe
date = df ['Date'].tolist()
open = df ['Open'].tolist()
high = df ['High'].tolist()
low = df ['Low'].tolist()
close = df ['Close'].tolist()

l_open,=plt.plot(date,open,color='red',linewidth=0.5)
l_high,=plt.plot(date,high,color='yellow',linewidth=1)
l_low,=plt.plot(date,low,color='green',linewidth=2)
l_close,=plt.plot(date,close,color='black',linewidth=3)
plt.xlabel('date',color='red')
plt.ylabel('amount',color='green')
plt.legend(handles = [l_open,l_high,l_low,l_close,], labels = ['open', 'high','low','close'], loc = 'best')
'''
data={'open':open,'high':high,'low':low,'close':close}
df = pd.DataFrame(data)
plt.plot(date,df)
plt.legend(data,loc=2)
'''

plt.show()

#question4
x=np.arange(10,20,2)
y=np.arange(10,20,2)
plt.axis([10,30,10,40])#先x轴后y轴
plt.xlabel('x-axis',color='black')
plt.ylabel('y-axis',color='black')
plt.plot()
print(x)
