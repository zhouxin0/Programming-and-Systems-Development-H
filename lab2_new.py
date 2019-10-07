#from solutions
#8 12 29 30 from teacher's solutions

#question 12

import random

color = random.choice(['red','blue','green','white','pink'])
print("select from above")
tryagain=True
while tryagain == True:
    theirchoice = input("enter a color:")
    theirchoice = theirchoice.lower()
    if color ==  theirchoice:
        print("well done")
        tryagain = False
    else:
        if color == "red":
            print("i think it is red")
        elif color == "blue":
            print("i think it is blue")
        elif color == "green":
            print("i think it is green")
        elif color == "white":
            print("i like white")
        elif color == "pink":
            print("i like pink very much")

#question29
list = {}
for i in range(0,4):
    name = input("enter your name:")
    age = int(input("enter your age:"))
    shoe = int(input('enter your shoe size:'))
    list[name] = {"age":age,"shoe size":shoe}
for name in list:
    print((name),list[name]["age"])

#question30
list = {}
for i in range(0,4):
    name = input("enter your name:")
    age = int(input("enter your age:"))
    shoe = int(input('enter your shoe size:'))
    list[name] = {"age":age,"shoe size":shoe}
getrid = input("who do you want to remove from the list?:")
del list[getrid]

for name in list:
    print((name),list[name]["age"],list[name]["shoe size"])

#question8
def add_name():
    name = input("enter a new name:")
    names.append(name)
    return names
def change_name():
    num = 0
    for x in names:
        print(num,x)
        num=num+1
        select_num=int(input("enter the number of name you want to change"))
        name = input("enter new name:")
        names[select_num] = name
        return names
def delete_name():
    num=0
    for x in names:
        print(num,x)
        num=num+1
    select_num = int(input("enter the number of the name you want to delete:"))
    del names[select_num]
    return names
def view_names():
    for x in names:
        print(x)
    print()
def main():
    again = "y"
    while again == "y":
        print('''
        1)add a name
        2)change a name
        3)delete a name
        4)view a name
        5)quit
        ''')
        selection = int(input("what do you want to do?"))
        if selection == 1:
            names = add_name()
        elif selection == 2:
            names = change_name()
        elif selection == 3:
            names = delete_name()
        elif selection == 4:
            names = view_names()
        elif selection == 5:
            again = "n"
        else:
            print("incorrect option:")
        data=(names,again)
names=[]
main()
# something wrong when change names














