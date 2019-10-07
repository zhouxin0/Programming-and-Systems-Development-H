#lab

#q1
import numpy as np
x=np.array([30,30,30,0])
print("original array")
print(x)
print(np.all(x)) #有0就返回false
print(np.any(x)) #都是0返回false
#q2
import numpy as np
x = np.array([45,67,23])
y = np.array([56,67,89])
print(np.greater(x,y))
print(np.greater_equal(x,y))
#what is the difference between greater_equal
print(np.less(x,y))
print(np.less_equal(x,y))
#q3 ask if it is right
import numpy as np
a = np.zeros(8)
b = np.ones(5)
c = np.ones(10)*5
print(a,b,c)
d = np.hstack((a,b,c))
print(d)
#q4
import numpy as np
x = np.array([23,45,11])
y = np.array([12,23,54])
z = np.array([29,19,34])
w = np.array([1,23,10])
all = np.vstack((x,y,z,w))
print(all)
u = np.array([2,0,2])
print(all+u)
#Write a Numpy program to add a vector v with values 2, 0, 2 to each row of a matrix m with values
#q5

t = np.ones((5,5))
print(t)
for x in range (1,4):
    for y in range (1,4):
      t[x][y]=25
      y=y+1
    x=x+1
print(t)
#q6

from pandas import DataFrame


import numpy as np
x = np.array([23,45,11,5])
y = np.array([23,5,1])
print(set(x)&set(y))
#q7
array2 = np.array([[3,5,1],[2,3,4],[9,1,5]])
array1 = np.array([[23,45,11],[12,23,54],[1,23,10]])
#print(array1,"\n",array2)
h_stack = np.hstack((array1,array2))
v_stack = np.vstack((array1,array2))
print(h_stack)
print(v_stack)
print(np.hsplit(array1,3))#按列数切开
print(np.vsplit(array2,3))#按行数切开

#q8-q13
#Sample DataFrame:

import numpy as np
import pandas as pd

assessment_results = {'name': ['Anastasia', 'Paul', 'Kathe', 'Joseph', 'Linda', 'Michael', 'Matt', 'Laurentine', 'Chirstian', 'Jonas'],
                      'score': [12.5, 10, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                      'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                      'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
frame = pd.DataFrame(assessment_results, index=labels)
print(frame)
print(frame['a':'c'])
print(frame[frame.attempts>2])
print(len(frame))
print(frame.columns.size)
frame1 = frame[frame.score>=14]
print(frame1[frame1.score<=20])
print(frame)

new_data={
    'Paul':'zhou'
}
frame.replace(new_data)
print(frame)

frame.loc['c','score']=11.5
print(frame)

print(DataFrame.mean(frame.score))

