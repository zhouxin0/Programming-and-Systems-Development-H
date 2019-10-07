#Exercise: Find the area
print("1) Square")
print("2) Triangle")
import turtle
x=input("    enter a number:")
if x=="1":
    turtle.begin_fill()
    turtle.color("red")
    turtle.speed(10)
    i=1
    while i <=4:
        turtle.forward(100)
        turtle.right(90)
        i=i+1
    turtle.end_fill()
    turtle.done()
        #something wrong
else:
    import turtle
    turtle.color('red')
    turtle.circle(30)
    turtle.done()
#Exercise: Classifying Triangles
first=input("enter the first length:")
second=input("enter the second length:")
third=input("enter the third length:")
a=int(first)
b=int(second)
c=int(third)

if a+b>c and a+c>b and b+c>a:
   if a==b or b==c or a==c:
    if a==b==c:
      print("it is equilateral triangles")
    else:
      print("it is  isosceles")
   else:
    print("it is scalene")
else:
  print("not a triangle")

#Exercise: Name the shape
num=input("enter the number of sides:")
int_num=int(num)
if int_num>=3 or int_num < 10:
   print("it has",int_num,"sides")
else:
    print("wrong number")

#???Exercise: Vowel or Consonant
word = input("enter a word:")
import re
x=re.search("a"or"e"or"i"or"o"or"u"or"y",word[0])
if(x):
    if x=="y":
        print("somtimes")
    else:
        print("vowel")
else:
    print("consonant")

#Exercise: Even or Odd
num = int(input("enter a number"))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is odd".format(num))

#Exercise: Your age
age=input("how old are you?:")
if int(age)>=17:
  if int(age)>=18:
    print("you can vote")
  else:
    print("You can learn how to drive")
elif int(age) == 16:
  print("you can buy a lottery ticket")
else:
  print("You can go Trick-or-Treating")

#Exercise: Umbrella or no umbrella
answer=input("if it is raining?:")
import re
x=re.search("yes"or "YES"or"Yes",answer)
if(x):
  answer1=input("if it is windy?:")
  y=re.search("yes"or "YES"or"Yes",answer1)
  if(y):
    print("it is too cloudy to carry an umbrella")
  else:
    print("take an umbrella")
else:
  print("enjoy your day")

#Exercise: Pig Latin
word=input("enter a word:")
import re
x=re.search("a"or"e"or"i"or"o"or"u",word[0])
if(x):
  print(word[1:len(word)]+"ay")
else:
  print((word[0:len(word)])+("way"))

#Exercise: Upper or Lower case name
firstname=input("enter your first name:")
if len(firstname)<5:
  surname=input("enter your surname:")
  print(firstname+surname)
else:
  print(str.lower(firstname))


#Exercise: Length and Slicing
fav_song=input("enter the name of your favourite song?:")
length=len(fav_song)
print(length)
start_num=int(input("enter the start number:"))
end_num=int(input("enter the end number:"))
print(fav_song[start_num:end_num])

#Exercise: Day old Bread
n_oldbread=input("enter the number of old bread:")
n_newbread=input("enter the number of new bread:")
float(n_oldbread)
float(n_newbread)
price_new=3.49
discount_price=float(price_new)*0.40
price_old=discount_price
total=float(n_newbread)*price_new+float(n_oldbread)*price_old
print("the overall price is :","%.2f"%total,"pounds")



