
# i=0
# while i<10:
#     num=input()
#     try:
#         num=int(num)
#         break
#     except:
#         print("type integer number")
        
#     i=i+1
# print(num)
    
# i=0
# while True:
#     print("hello")
    
# letter=[1,2,3,4,5,6,7]
# for i in letter:
#     print(i)

# num=[1,2,3,4,4,5,6,7,8,9,3,4,5,6,767,8,98,532,45]
# print(max(num))
# list of numbers
# list1 = [10, 20, 4, 45, 99]
 
# # sorting the list
# list1.sort()
 
# # printing the last element
# print( list1[
# i=0
# def code():
#     while True:
#         ask=input("enter your number")
#         if ask=="done":
#             print("done")
#             break
#         else:
#             code()
#         break
# def new_code():
#     while True:
#         try:
#             code()
#             break
#         except:
#             print("invalid input")
#             n

# new_code()







# data=[
#     {"name":"lakshay","age":12,"new_age":16,"class":"ai"},
#     {"name":"qwerty","age":13,"new_age":16,"class":"qa"},
#     {"name":"hello","age":15,"new_age":16,"class":"cs"}
#     ]
# for var in data:
# # var=data[0]
#     # print(var)
#     dif=var["new_age"]-var["age"]
#     print(var["name"],":",dif)

# a="hello"
# b=a+"there"
# print(b)

# word = "bananaana"
# i = word.count("na")
# print(i)

# str='XMS-DPMS-Confidence: 0.878 '
# # print(type(str))
# colon=str.find(':')
# # print(colon)
# space=str.find(' ',colon)
# # print(space)
# num=str[space+1:]
# new=float(num)
# print(type(new))
# import os
# # pwd
# file=open("idea.txt")
# for line in file:
#     print(line.upper())
# list=[]
# # print(len(list[2]))
# list.append("book")
# print(list)




# list=list()
# def loop():
#     while True:
#         try:
#             int=input("enter your number: ")
#             int=float(int)
#         except:
#             print("wrong statemenet ")
#             loop()
#         if int == "done": break
        
#         num=list.append(int)
#     print(list)
#     avg=sum(list)/len(list)
#     print(avg)
# loop()

# list={"name":"lakshay","class":12,"age":15}
# a= [12345]
# a[0]=4
# print(a)
# (a,b) = ('hello','err')
# print(a)

# ('Adam' ,'eve') < ('Qwerty','abe')
# import re
# x= ' from hello@hello.in.com.lol remove this all thing'
# y= re.findall('^from (\S+@\S+)',x)
# print(y)


# import socket
# mysoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysoc.connect(('data.pr4e.org',80))
# cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# mysoc.send(cmd)

# while True:
#     data=mysoc.recv(512)
#     if  (len(data) < 1 ):
#         break
#     print(data.decode())
# mysoc.close()

# h=b"hello"

# print(type(h))
# import urllib.request,urllib.parse,urllib.error
# fhand=urllib.request.urlopen('https://priyaminfosystems.com/')
# for line in fhand:
#     print(line.decode().strip())

# import urllib.request,urllib.error,urllib.parse
# from bs4 import BeautifulSoup

# import json
# data='''{
#     "name":"lucky",
#     "phone":{
#         "service":"airtel",
#         "number":"+9192873723"
#     },
#     "email":{
#         "hide":"yes"
#     }
# }'''

# info=json.loads(data)
# print('name: ',info["name"])
# print("no: ", info["email"])
from time import sleep

x = 'hello world'

h = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'w', 'q', 'z', ' ']

z = 0
t = ""

while t != x:
    for i in h:
        if t == x:
            break
        print(t + i, end='\r')
        if i == x[z]:
            t += i
            z += 1
            sleep(0.3)
            break
        sleep(0.1)
        print(t)