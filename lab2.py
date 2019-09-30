
# 1 day 9.30
'''



name=input("enter your name:")
num=int(input("enter the num:"))
if num<10:
     for i in range(num):
         print(name)
else:
      print("too high') #如何换行
      print("too high')
      print("too high')
'''
# 2
# exercise 2
'''
import re
total=0
i=1
for i in range(5):
    ask = input("if you want to add the number to the total:")
    x = re.search("yes" or "YES" or "Yes", ask)
    num = int(input("enter  a number:"))
    if(x):
     total = num + total
    else:
     total=total
i=i+1
print(total)
'''
#3
'''
direction=input("which direction you want to choose?:up or down")
if direction == "up":
    num=int(input("enter a number:")) #1-that number
   # num=num+1
    for i in range(1,num+1):
        print(i)
    i=i+1
elif direction == "down":
    num = int(input("enter a number:"))  # 1-that number
    i=20
    for i in range(20,num-1,-1):
        print(i)
else:
    print("i dont understand")
'''
'''
num = 5
print(num)
print(range(num))
for i in range(num):
    print(i)
'''
#4
'''
num = int(input("enter a number:"))
num_1 = int(input("enter another number:"))
num_total=num+num_1
ask=input("do you want to enter one more number:y or n")
while ask == "y":
    num_more=int(input("enter one more number:"))
    num_total=num_total+num_more
    ask = input("do you want to enter one more number:y or n")
if ask == "n":
      print(num_total)
else:
      print(num_total)
'''
#5
'''
comp=50
num = int(input("enter a number:"))
i=0
while num!=comp:
    if num > comp:
        print("too high")
        num = int(input("enter a number:"))
        i = i + 1
    else:
        print("too low")
        num = int(input("enter a number:"))
        i=i+1

print("good guess")
print("you have tried",i+1,"times")
'''
#6
'''
num = int(input("enter a number:"))
print(num,"bottles on the wall,fall one bottle")
ques=int(input("how many on the wall?:"))
while ques == num-1:
    print(num-1,"green bottles on the wall")
    print(num-1, "bottles on the wall,fall one bottle")
    num=num-1
    ques=int(input("how many on the wall?:"))
#ques!= num-1
print("wrong")
print("guess again")
ques = int(input("how many on the wall?:"))
'''

#problem1
'''
message = input("enter a message:")
while message != "":
    n = int(input("how many times?"))
    for i in range(n):
        print(message)
    break
    '''
#problem2
'''
line = input("enter a string: ")
is_palindrome = True
i = 0
while i < len(line)/2 and is_palindrome:
    i = i+1
    if line[i] != line[len(line) - i -1]:
        is_palindrome = False
if is_palindrome:
    print(line, "is a palindrome")
else:
    print(line,"is not a palindrome")
    '''
#problem3
#==判断 =赋值

#problem4
'''
import random
num= random.random()
print(num)
'''
#problem 5

#7
'''
def countnum():
    num=int(input("enter a number:"))
    return num
def count_func(num):#函数定义里面都是对象
    i=1
    for i in range(1,num+1):
        print(i)
        i=i+1
def main():
    num=countnum()
    count_func(num)# num is 参数
main()
'''
#8 不太会
#9
'''
import random
fruit_list=['orange','grape','banana','starwberry','melon']
print(random.choice(fruit_list))
'''
#__import__() 有问题
#10
'''
import random
user_input=input("enter heads or tails h or t?:")
comp_input=random.choice(["h","t"])
if user_input == comp_input:
    print("you win")
else:
    print('bad luck')
    print("the computer ramdomly select",comp_input)
'''
#11
'''
import random
our_list=[1,2,3,4,5]
#print(our_list)
user_input=int(input("pick a number form 1 to 5?:"))
comp_input=random.choice(our_list)
print(comp_input)
quit = True
while user_input == comp_input and  quit==True :
    print("well done")
    quit = False
if user_input < comp_input:
        print("your guess is low")
        our_list.remove(user_input)
        guess_again=input("pick another number form 1 to 5?:")
        if guess_again==comp_input:
            print("correct")
        else:
            print("you lose")
else:
        print("your guess is high")
        our_list.remove(user_input)
        guess_again=input("pick another number form 1 to 5?:")
        if guess_again==comp_input:
            print("correct")
        else:
            print("you lose")
'''
#12 failure
'''
import random
color_list=['orange','blue','pink','black','green']
text_list=['choose orange bro','choose blue','choose pink','choose black','choose green']
print(color_list)
user_input=input("pick a color from above?:")
comp_input=random.choice(color_list)
print(comp_input)
quit=True
while user_input != comp_input and quit==True :
    print("wrong")
    guess_again = input("pick another color from above?:")
    if user_input == comp_input:
      print("correct")
    else:
      print("take another chance")
print("well done")
quit=False





import random
color_list=['orange', 'blue', 'pink', 'black', 'green']
text_list=['choose orange bro', 'choose blue', 'choose pink', 'choose black', 'choose green']
print(random.choice(color_list))
'''
#13
'''
import turtle
turtle.circle(30, extent=None, steps=None)
turtle.mainloop()
'''
#14
'''
import turtle
import random
color_list=['orange', 'blue', 'pink', 'black', 'green','yellow']
turtle.begin_fill()
turtle.color(random.choice(color_list))  #画笔颜色
turtle.speed(10)        #画笔的速度范围为【1-10】
i = 1
while i <= 8 :
    turtle.forward(100) #向前移动100
    turtle.right(45)    #右转90度
    i = i+1             #循环变量加1
turtle.up()             #画笔抬起
turtle.end_fill()
turtle.mainloop()
'''
#15
'''
import turtle
import random
color_list=['orange', 'blue', 'pink', 'black', 'green','yellow']
number_lines=random.randint(1,10)
#length_lines=random.randint(20,100)
#color_lines=random.choice(color_list)
#angle_lines=random.randint(0,360)

print(number_lines)
for i in range(number_lines):
    turtle.pencolor(random.choice(color_list))
    turtle.forward(random.randint(20,100))
    turtle.right(random.randint(0,360))
turtle.mainloop()
'''
#16
'''
list_num=[111,222,333,444]
for num in list_num:
    print(num,'\n')
user_input=int(input("enter a 3-digit number:"))
if user_input in list_num:
    print("the position is ",list_num.index(user_input))
else:
    print("that is not in the list")
    '''
#17
'''
import re
our_list=[]
our_list.append(input("add a name:"))
our_list.append(input("add a name:"))
our_list.append(input("add a name:"))
quit=True
while quit==True:
    ques = input("if you want to add another:")
    x=re.search('yes'or 'YES'or'Yes',ques)
    if(x):
         our_list.append(input("add a name:"))
    else:
        print("how many people are there in the list?",len(our_list))
        quit=False
print(our_list)
'''
#18
'''
food={}
for i in range(5):
    food[i]=input("enter your favourite food:")
print(food)
del_user=int(input("which one you want to delete?enter the number:"))
del food[del_user]
print(food)

food_1=sorted(food) #maybe something wrong? only return nums
print(food_1)
'''
#19
'''
country_tuple=('china','uk','us','sweden','iceland')
print(country_tuple)
user=input("enter a country name?:")
#display the index number
print(country_tuple.index(user))
user_1=int(input("enter a number from 0 to 4?:"))
print(country_tuple[user_1])
'''
#20
'''
from array import*
integers=array("i",[])
i=0
for i in range(0,5):
    newvalue=int(input("enter a number:"))
    integers.append(newvalue)
    i=i+1
print(integers)
integers=sorted(integers)
print(integers)
integers.reverse()
print(integers)
'''
#21
'''
import random
from array import*
naa=array("i",[])
i=0
for i in range(0,5):
    newvalue = random.randint(0,100)
    naa.append(newvalue)
    print(naa[i])
    i=i+1
'''
#22
'''
from array import*
integers=array("i",[])
i=0
for i in range(0,3):
    newvalue=int(input("enter a number:"))
    integers.append(newvalue)
    i=i+1
print(integers)
import random
from array import*
naa=array("i",[])
j=0
for j in range(0,5):
    newvalue = random.randint(0,100)
    naa.append(newvalue)
    i=i+1
print(naa)
integers.extend(naa)
print(integers)#new integers
new=sorted(integers) #有什么作用么
print(new)
for i in range(len(new)):
    print(new[i])
'''
#23
'''
from array import*
nums=array("i",[])
i=0
for i in range(0,5):
    newvalue=int(input("enter a number:"))
    nums.append(newvalue)
    i=i+1
print(nums)
newnums=sorted(nums)
print(newnums)
select=int(input('select one number from above:'))
nums.remove(select)
print(nums)
newArray=("i",[select])
print(newArray)
'''
#24
'''
from array import*
nums=array("i",[])
i=0
for i in range(0,5):
    newvalue=int(input("enter a number:"))
    nums.append(newvalue)
    i=i+1
print(nums)

quit=True
select=int(input('select one number from above:'))
while quit==True:
    if select in nums:
        print("position",nums.index(select))
        quit = False
    else:
        select=int(input('select one number from above:'))
'''
#25
'''
from array import*
nums=array("f",[66.77,33.55,76.34,45.44,45.49])
user=int(input("enter a whole num between 2 and 5:"))
quit=True
while quit==True:
    if user<2 or user>5:
      print("error")
      user = int(input("enter a whole num between 2 and 5:"))
      quit =True
    else:
        i=0
        for i in range(0,5):
            nums[i]=nums[i]/user
            zhou=nums[i]
            print('%.2f'%zhou)
            i=i+1
            quit =False
'''
#26
'''
new_list=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(new_list)
user_row=int(input("select one row:"))
user_col=int(input("select one col:"))
print(new_list[user_row][user_col])
'''
#27
'''
new_list=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(new_list)
user_row=int(input("select one row:"))
#user_col=int(input("select one col:"))
print(new_list[user_row])
user_row1=int(input("enter one value:"))
new_list[user_row].append(user_row1)
print(new_list[user_row])
'''
#28
'''
import re
new_list=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(new_list)
user_row=int(input("select one row that you want to display:"))
print(new_list[user_row])
user_col=int(input("select one col:"))
print(new_list[user_row][user_col])
ask=input("if you want to change the value?:")
y=re.search('yes'or'Yes'or'YES',ask)
if(y):
        new_list[user_row][user_col]=int(input("enter a value you like to replace:"))
        print(new_list)
else:
        print(new_list)

'''
'''
user_row1=int(input("enter one value:"))
new_list[user_row].append(user_row1)
print(new_list[user_row])
'''
#29
