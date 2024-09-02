# Addition
# a = int(input("Enter the first number for addition:"))
# b = int(input("enter the second number for addition:"))
# print(f"sum: {a} + {b} = {a+b}")

# area of triangle
# a=int(input("enter the length of the base of the triangle:"))
# h=int(input("enter the height of the triangle:"))
# print(f"the area of the triangle is:{0.5*a*h}")


# Swap variable without swap() function
# firstVariable=input("enter the first variable:")
# secondVariable=input("enter the second variable:")
# print(f"Before swapping,a={firstVariable}  b={secondVariable}")
# firstVariable,secondVariable=secondVariable,firstVariable
# print(f"After swapping,a={firstVariable}  b={secondVariable}")


# generate random number
# import random
# print(f"Random number={random.randint(1,100)}")


# kilometer to miles
# dKilo=int(input("enter distance in kilometer:"))
# print(f"In miles {dKilo} km={dKilo*0.621371}")


# display calender
# import calendar
# year=int(input("enter year:"))
# month=int(input("enter month:"))
# cr=calendar.month(year, month)
# print(cr)


# solve quadratic equation
# print("enter the value of a,b,c of quadratic form(ax^2 + bx + c = 0)")
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if a==0:
#     print("re enter the value of a as it cant be zero")
#     a=int(input("a="))
# res1=(-b+((b**2-4*a*c)/(1/2)))/(2*a)
# res2=(-b-((b**2-(4*a*c))**(1/2)))/(2*a)
# print(f"the solution is either {res1} or {res2}")


# check is a number is positive, negative or zero.
# input=int(input("enter a number"))
# if input>0:
#     print("positive")
# elif input<0:
#     print("negavtive")
# else:
#     print("zero")


# check prime number
# input=int(input('enter a number:'))
# count= False
# if input==1 or input==0:
#     print("neither prime or composite")
# for item in range(2,input):
#     if input%item==0:
#         count= True
# if count==True:
#     print("it is a composite number")
# elif count==False and input!=0 and input!=1:
#     print("it is a prime number")


# find prime numbers in interval 1-10
# print("prime numbers in interval 1-10:")
# for num in range(2,10):
#     flag=False
#     i=2
#     while(i<num):
#         if num%i==0:
#             flag=True
#             break
#         else:
#             i+=1
#     if flag==True:            
#         pass
#     elif flag==False:
#         print(num)


# find factorial of a number
# fac1=1
# def fac(num):
#     global fac1
#     if num==1:
#         return fac1
#     else:
#         fac1*=num
#         return fac(num-1)
# inpu=int(input("enter number"))
# result=fac(inpu)   
# print(f"the factorial of {inpu} is {result}")    


# Multiplication table
# for num in range(1,11):
#     for item in range(1,11):
#         print(f"{num}*{item}={num*item}")
#     print("\n")


# Fibonacci series upto 15th term
# print("1\n1")
# def fibo(x,y,count):
#     i=x+y
#     print(i)
#     count+=1
#     if count<=15:
#         return fibo(y,i,count)
# fibo(1,1,3)


# Ckeck Armstrong number
# num=input("enter a number:")
# length=len(num)
# num=int(num)
# n=num
# arm=0
# while(n!=0):
#     arm=arm+((n%10)**length)
#     n=int(n/10)
# if arm==num:
#     print("armstrong")
# else:
#     print("not armstrong")  


# find Armstrong in interval
# for num in range(1, 2000):
#     num = str(num)
#     length = len(num)
#     num = int(num)
#     n = num
#     arm = 0
#     while n != 0:
#         arm = arm+((n % 10)**length)
#         n = int(n/10)
#     if arm == num:
#         print(num)


# x=[1,2,3,4,5]
# y=x
# y[0]=100
# print(x)  
# print(y) 


