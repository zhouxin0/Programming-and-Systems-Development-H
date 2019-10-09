import matplotlib.pyplot as plt

# plt.plot([1,2,3,4])
import pandas as pd

'''
plt.axis([0,5,0,20])
plt.title('my first plot')
plt.plot([1,2,3,4],[1,4,9,16],'ro')# what is the meaning of ro?
'''

import math
import numpy as np
'''
t = np.arange(0, 2.5, 0.1)  # 间隔为0.1,左闭右包,无2.5
print(t)
y1 = np.sin(math.pi * t)
y2 = np.sin(math.pi * t + math.pi / 2)
y3 = np.sin(math.pi * t - math.pi / 2)
plt.plot(t, y1, 'b*', t, y2, 'g^', t, y3, 'ys')  # what does b* g^ ys represent for?
plt.show()
'''
'''
plt.plot(t, y1, 'b--', t, y2, 'g', t, y3, "r-.")
plt.show()
#kwargs_keywords arguments
plt.plot([1,2,3,2,1,0,1,2,1,4],linewidth = 2.0)
plt.show()
plt.plot([1,2,3,2,1,0,1,2,1,4],linewidth = 5.0)
plt.show()
'''
'''
t = np.arange(0,5,0.1)
y1 = np.sin(2*np.pi*t)
y2 = np.cos(2*np.pi*t)
plt.subplot(211)   #first number-vertically,second number-horizontally,third which we direct commands
plt.plot(t,y1,'b-.')
#plt.subplot(212)   # when we comment this line the second figure cannot be seen 
#plt.plot(t,y2,'r--')
plt.show()
'''
'''
t = np.arange(0,1.,0.05) #what is the difference between 1. and 1
y1 = np.sin(2*np.pi*t)
y2 = np.cos(2*np.pi*t)
plt.subplot(121)   #first number-vertically,second number-horizontally,third which we direct commands
plt.plot(t,y1,'b-.')
plt.subplot(122)   # when we comment this line the second figure cannot be seen
plt.plot(t,y2,'r--')
plt.show()# 21横着排列  12竖着排列
#cant distinguish right or left
'''

#text and title and grid
'''
plt.axis([0,5,0,20])#先x轴后y轴
plt.title('my first plot',fontsize = 20, fontname = 'Times New Roman')
plt.xlabel("counting",color='gray')
plt.xlabel("square values",color='gray')
plt.text(1,1.5,'first')
plt.text(2,4.5,'second')
plt.text(3,9.5,'third')
plt.text(4,16.5,'fourth')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.grid(True)
plt.legend(['first series'],loc = 8)#reference the list in ppt
plt.show()
plt.savefig('my_chart.png') #there is a picture which is blank.
'''
# page12 of data visualization 跳过了
#color code P13
'''
x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(3*x)/x
plt.plot(x,y3,color='r',linestyle='--',linewidth=5)
plt.plot(x,y,'k--',linewidth=3)# 黑线 和 红色线重合
plt.plot(x,y2,'g-.')#green 点线
plt.show()
'''
'''
import pandas as pd
import numpy as np
data = {'series1':[1,3,4,3,5],
        'series2':[2,4,5,2,4],
        'series3':[3,2,3,1,3]
}
df=pd.DataFrame(data)
print(df)
x = np.arange(5)
plt.axis([0,5,0,7])
plt.plot(x,df)
plt.legend(data,loc=2) #loc=2 右上角 legend 参数1 data 参数2 放置的位置
#plt.legend(['first series'],loc = 8)
plt.show()
'''
#histograms
'''
import matplotlib.pyplot as plt
import numpy as np
pop = np.random.randint(0,100,100)
print(pop)
n,bins,patches = plt.hist(pop)
plt.show()
print(pop[pop>95])
'''
#bar chart
'''
index= np.arange(5)#这里[0,1,2,3,4]就不行,why?
values1 = [5,7,3,4,6]
plt.bar(index,values1)
plt.xticks(index+0.4,['a','b','c','d','e'])
plt.show()
#what is the difference between the two?
'''
'''
index= np.arange(5)
values1 = [5,7,3,4,6]
std1 = [0.8,1,0.4,0.9,1.3]
plt.title('my bar chart')
plt.barh(index,values1,xerr=std1,error_kw={'ecolor':'0.1',"capsize":6},alpha=0.7,label='first')
plt.yticks(index+0.4,['a','b','c','d','e'])
plt.legend(loc=2)
plt.show()

index = np.arange(5)
values1 = [5,7,3,4,6]
values2 = [6,6,4,5,7]
values3 = [5,6,5,4,6]
bw= 0.3
plt.axis([0,8,0,5])
plt.title('multiseries bar chart',fontsize=20)
plt.barh(index,values1,bw,color='b')
plt.barh(index+bw,values2,bw,color='g')
plt.barh(index+2*bw,values3,bw,color='r')
plt.yticks(index+1.5*bw,['a','b','c','d','e'])
plt.show()
'''
#page 24
'''
data = {'series1':[1,3,4,3,5],
        'series2':[2,4,5,2,4],
        'series3':[3,2,3,1,3]
}
df= pd.DataFrame(data)
df.plot(kind = 'barh',stacked= True)
plt.show()
'''
'''
#page 26 other bar chart
x0 = np.arange(8)
y1 = np.array([1,3,4,6,4,3,2,1])
y2 = np.array([1,2,5,4,3,3,2,1])
plt.ylim(-7,7)
plt.bar(x0,y1,0.9,facecolor='r')
plt.bar(x0,y2,0.9,facecolor='b')
plt.xticks(())
plt.grid(True)
for x,y in zip(x0,y1):
    plt.text(x+0.4,y+0.05,'%d'%y,ha='center',va='bottom')
for x,y in zip(x0,y2):
    plt.text(x+0.4,-y-0.05,'%d'%y,ha='center',va='top')
plt.show()
print(x0)#something goes wrong???
'''
'''
labels = ['nokia','samsung','huawei','apple','motorola']
values = [10,20,34,56,45]
colors = ['yellow','red','gray','orange','green']
explode = [0,0.5,0,0,0]
plt.title('pie chart')
plt.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,
        autopct = '%1.1f%%',startangle = 180)
plt.axis('equal')
plt.show()

'''
'''
data = {'series1':[1,3,4,3,5],
        'series2':[2,4,5,2,4],
        'series3':[3,2,3,1,3]
}
df=pd.DataFrame(data)
df['series1'].plot(kind='pie',figsize=(4,2))
plt.show()

'''
'''
N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area =(30*np.random.rand(N)**2)
plt.scatter(x,y,s=area,c=colors,alpha=0.5)
plt.show()
#29页 有程序跳过了




categories = ('cat1','cat2','cat3')
data = {'days':np.random.randint(120,size=100),
        'category':np.random.choice(categories,100),
        'values':100.0*np.random.random_sample(100)}
df = pd.DataFrame(data)
print(df)
df.describe()
df.boxplot(by='category',
           column=['values'],
           grid=False)
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import csv
'''
filename='sitka_weather_07-2014.csv'
with open('document.csv','r')as file:
    #1.创建阅读器对象
    reader=csv.reader('document.csv')
    #2.读取文件头信息
    header_row=next(reader)
    #3.保存最高气温数据
    month_number=[]
    for row in reader:
        #4.将字符串转换为整型数据
        month_number.append(int(row[1]))
    print(month_number)
'''
'''
df = pd.read_csv('document.csv',index_col=['month_number','total_profit'])
profitlist = df ['total_profit'].tolist()
monthlist = df ['month_number'].tolist()
plt.plot(monthlist,profitlist,label="zhou")
plt.axis([0,12,100000,500000])
plt.title('company profit per month')
plt.xlabel('profit dollar',color='gray')
plt.xlabel('month number',color='gray')
plt.plot(x='month_number',y='total_profit')
plt.show()
'''
