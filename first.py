# variable-myVariable
# class-MyClass
# method-my_method

# print(a,b)

# customer={
#     "name":"swta",
#     "age":19
# }

# print(customer)

# number={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"foue",
#    "5":"five",
#     "6":"six",
#     "7":"seven",
#     "8":"eight",
#     "9":"nine",
#     "0":"zero"
# }
# final=""
# answer=input("phone:")
# for digit in answer:
#     final+=" " + number[digit]
# print(final)

# string slicing and string not changeable
# name = "ram122"
# print((name[0:3]))

# multiline string
# name="""haha
# hehe"""
# print(name)

# list can contain multiple types of datatypes
# number=[3,2,"sweta"]
# print(number[2])

# tuples
# example = (2,3,4)
# print(example)

# set support integer, string,tuple and doesnt show duplicate. can use duplicate value but doesnt show while printing
# a={1,4,"sweta",5,7}
# print(a)

# dictionary
# person={
#     "name":"ram",
#     "hobbies":[
#         "reading book",
#         "watching football",
#     ],
#     "friend":[
#         {
#         "name":"shyam",
#         "hobbies":[
#             "playing football",
#             "guitar"
#         ],
#     }]
# }
# print(person["friend"][0]["hobbies"][1][3])

# type casting of tuple into list to modify elements of tuple
# example=(1,2,3)
# example=list(example)
# example[1]=5
# example=tuple(example)
# print(example)

# use of operator
# a,b=5,7
# a+=1
# print(a)

# comparison operator
# a=7.01
# b=7
# print(not(a==b))


# do homework
# x= int(input("enter first number:"))
# y=int(input("enter second number:"))
# task=int(input("""operations:
# 1.sum
# 2.subtraction
# 3.division
# 4.multiplication
# Click thier respective serial number for the operation
# """))
# if task==1:
#     print(x+y)
# elif task==2:
#     print(x-y)
# elif task==3:
#     print(x/y)
# elif task==4:
#     print(x*y)
# else:
#     print("wrong input")

# loop while
# i=1
# while i<=3:
#     if i==3:
#         break
#     print(i)
#     i+=1

# membership operator "in"
# people={
#     "Ram",
#     "shyam",
#     1
# }
# for index,person in enumerate(people):
#     print(f'hello {index} {person}')

# i=[1,2,3,4,5,6,7,8,9]
# total=len(i)
# ll=[]
# for item in i:
#     if item==i[total-1]:
#         break
#     if item+i[total-1]==10:
#         ll.append((item,i[total-1]))
#         total-=1
# print(ll)

# def person(name,age,gender):
#     print(f"hello i am {name}. age={age} and gender={gender}")
# person(name="ram",age=9,gender="female")

# def sum(x,y):
#     print(x+y)
# def diff(x,y):
#     print(x-y)
# def multiply(x*y):
#     print(x*y)
# def div(x,y):
#     print(x/y)
# input1=int(input("enter a number:"))
# input2=int(input("enter another number:"))
# input=print("enter what you wanna do. 1.sum 2.difference 3.multiply 4.division")
# if input==1:
#     sum(input1,input2)
# if input2==0 and input==4:
#     print("cant perform division.")

# elif input==2:
#     diff(input1,input2)
# elif input==3:
#     multiply(input1,input2)
# elif input==4:
#     div(input1,input2)
# else:
#     print("wrong input")

# def num(*nums):
#     print(nums)
#     total=0
#     for n in nums:
#         total+=n
#     print(total)
# num(1,3,5)

# dictionary parameter & arguments
# def person(**i):
#     print(f" hello {i['name']} age={i['age']}")
# person(name="ram",age=9)

# import sys
# print(sys.version)

# i=3
# if i==2:
#     print("true")
# print("2")

# hw2
# num=int(input("enter a number:"))
# i=1
# def multiplication(num):
#      print(f"{num}*{i}={num*i}")

# while i<=10:
#     multiplication(num)
#     i+=1
# reply=input("do u wan to continue(y/n):")
# if reply==y:
#     num=int(input("enter a number:"))
#     while i<=10:
#     multiplication(num)
#     i+=1
# else:
#     exit
# hw1
# input1=[]
# i=0
# s=''
# def greetings(name):
#     print(f"Hello! {name}. A warm welcome to you.")
# print("enter 10 names:")
# for item in range(10):
#     s=input(f"{item +1}. ")
#     input1.append(s)
# reply=input("do you want greetings(y/n)").lower()
# if reply=='y':
#     i=int(input("enter the index of name whose greeting you want:"))
#     greetings(input1[i-1])
# elif reply=='n':
#     exit
# else:
#     print("wrong input")


# limit=int(input("enter a limit"))
# start=int(input("enter a starting number:"))
# def num(n,limit):
#      print(n)
#      if n==limit:
#       return
#      num(n+1,limit)
# num(start,limit)

# lamda function

# def sum(a,b):
#     return a+b

# a,b parameter and return a+b
# su=lambda a,b:a+b
# print(su(1,2))

# def multi(a):
#     return lambda n:a*n
# pass1 = multi(2)
# input2=int(input("enter limit:"))
# print(pass1(input2))

# def up(text1):
#     return text1.upper()
# def low(text2):
#     return text2.lower()
# def final(fun):
#     setter=fun("hello namaste")
#     print(setter)
# final(up)
# final(low)

# decorator
# def head(func):
#     def middle():
#         print("hello")
#         func()
#     return middle
# def subj():
#     print("wrapped")
# rej=head(subj)
# rej()

# def deco(func):
#     def inner(a,b):
#         if a==b:
#             print("equal")
#             return
#         return func(a,b)
#     return inner
# @deco
# def ordinary(a,b):
#     print(a/b)
# ordinary(2,2)
# ordinary(2,3)

# def deco(func):
#     def wrapper():
#         print("#"*10)
#         print("*"*10)
#         func()
#         print("*"*10)
#         print("#"*10)
#     return wrapper
# @deco
# def hello():
#     print("sweta")
# @deco
# def hi():
#     print("namaste")
# hello()
# hi()

# def deco(func):
#     def wrapper():
#         print("#"*10)
#         print("*"*10)
#         func()
#         print("*"*10)
#         print("#"*10)
#     return wrapper
# def star(func):
#     def wrappe():
#         print("*"*10)
#         func()
#         print("*"*10)
#     return wrappe
# def hello():
#     print("sweta")
# deco(hello)()
# star(hello)()

# def hi():
#     print("namaste")
# deco(hi)()

# registration
# +
# login global variable


# credential = {}


# def registration():
#     global credential
#     print(
#         """
# welcome to our system!
# registration process will start now."""
#     )
#     credential["name"] = input("enter your full name:")
#     credential["uname"] = input("enter your username:")
#     credential["age"] = int(input("enter your age"))
#     credential["password"] = input("enter your password:")
#     print(f"registration completed! now you({credential['uname']}) are registered.")
#     view_detail = input("do you want to view your detail?(y/n)").lower()
#     if view_detail == "y":
#         print(
#             f"Name:{credential['name']}\nAge:{credential['age']}\nusername:{credential['uname']}"
#         )


# def login():
#     name = input("enter username:")
#     password = input("enter password:")
#     if name == credential["uname"] and password == credential["password"]:
#         print("You have successfully logged in!")
#         exit()
#     else:
#         print("WRONG USERNAME OR PASSWORD. TRY AGAIN!")


# print(f"1.registration\n2.Exit")
# action = int(input(f"click the respective number of action you want to perform:"))
# while action == 1 or action == 2:
#     if action == 1:
#         registration()
#         jump = input("do u want to login?(y/n)").lower()
#         if jump == "y":
#             while True:
#                 login()
#         else:
#             break
#     elif action == 2:
#         break
#     else:
#         print("wrong input")

# class House:
#     window = 10
#     color = "white"
#     door = 2


# ram_ghar = House()


# sweta_ghar = House()
# sweta_ghar.door = 6
# print(ram_ghar.color)
# ram_ghar.color = "red"
# print(ram_ghar.color)


# class House:
#     color = "red"
#     door = 1

#     def set_color(self, color):
#         self.color = color

#     def get_color(self):
#         return self.color


# new_house = House()
# print(new_house.get_color())
# new_house.set_color("black")
# print(new_house.get_color())


# single inheritance, multilevel,multiple
# class grandfather:
#     house = "grand hotel"


# class father(grandfather):
#     bike = "honda"


# class mother:
#     jewelry = "gold"


# class child(father, mother):
#     console = "ps5"


# child1 = child()
# print(child.jewelry)

# magic method=constructor

# class Person(object):
#     def __init__(self, name):
#         self.name = name


#     def __str__(self):
#         return self.name


# ram =Person("ram")
# print(ram)

# class Person:
#     def __init__(self,age):
#         self.age=age
#     def __lt__(self,other):
#         return self.age<other.age
# ram=Person(18)
# shyam=Person(7)
# print(ram<shyam)


# class grand:
#     house="lux"
#     def __init__(self):
#         print(self.house)


# class father(grand):
#     car="bmw"
#     def __init__(self):
#         print(self.car)

# class mother:
#     clothe="vest"

# class child(father,mother):
#     console="ps5"
#     def __init__(self):
#         super().__init__()
#         print(self.console)

# obj=child()
# print(obj)

# class A:
#     x=0
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         return self.x+other.x
# obj=A(3)
# ob=A(4)
# print(obj+ob)


# from abc import ABC, abstractmethod

# class Computer(ABC):
#     @abstractmethod
#     def process(self,app):
#         pass
#     def run(self,app):
#         self.process(app)


# class Person(Computer):
#     def process(self,app):
#         print(app)
# obj=Person()
# obj.run("meet")


# encapsulation,private__,protected_,public(default nothing needed to do)
# class Person:
#     def __init__(self,email,password,number):
#         self.email=email
#         self.__password=password
#         self._number=number
#     def setv(self,password):
#         self.__password=password
#     def getv(self):
#         return self.__password

# obj=Person("sww@gmail.com","2345",234)
# print(obj.getv())
# obj.setv("456")
# print(obj.getv())


# exception handling
# try:
#     first=int(input("enter a number:"))
#     second=int(input("enter another number:"))
#     div=first/second
#     print(div)
# except ZeroDivisionError:
#     print("enter another value non zero.")
# except ValueError:
#     print("only enter integer.")
# except Exception as e:
#     print(f"something went wrong:{e}")


# import example-> used to access functions,variables of another file
# from file_name import function_name as r
# from file_name1 import Similar_function_name as Another_name,variable_name
#
# print(r(2,3))

# with open("name.txt") as f:
#     r = f.read()

#     for i in r:
#         print(i)

# user input ask file.txt filename ask,exist xa vane ask another name .ask for input. show files in directory. ask for file or folder delete.
# file_name="sweta"
# open(file_name,'x')

# first
# num=[34,15,88,2]
# small=num[0]
# for item in num:
#     if item < small:
#         small=item
# print(small)

# second
# num = [34, -345, -1, 100]
# small = num[0]
# for item in num:
#     if item < small:
#         small = item
# print(small)


x = ['a', 3]
for item in x:
    if type(item) == str:
        print("hi")
    else:
        print("hello")
