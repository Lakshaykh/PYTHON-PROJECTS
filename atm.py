#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pyttsx3 as py
import random as rd
import string as s

def change_pin():
    pin=rd.randint(3000,5000)
    song=py.init()
    song.say("enter the your pin")
    print("Your pin : ",pin)
    new_pin=int(input("enter ur old pin: "))
    if pin==new_pin:
        global new_p
        new_p=input("enter ur new pin: ")
        song=py.init()
        song.say("your pin have been change succesfully")
        print("your pin has been successfully......")
    else:
        print("Old pin does not match...")
        
def pin_show():
    song=py.init()
    song.say(f"your new pin is {new_p}")
    print("Your new pin: ",new_p)

    
def captcha():
    rand=s.ascii_uppercase+ s.ascii_lowercase + s.digits + "!@#$%^&*"
    z=rd.sample(rand,5)
    z="".join(z)
    return(z)
store=captcha()

global balanace
balance=50000
def withdraw():
    global balance
    song=py.init()
    song.say("enter the amount you want to withdraw")
    amount=int(input("enter the amount you want to witdraw"))
    if amount<balance:
        balance=balance-amount
        print("net balance is :",balance)
    elif amount>balance:
        print("insufficient balance")
    
def deposit():
    global balance
    song=py.init()
    song.say("enter the amount you want to deposit")
    song.runAndWait()
    amount=int(input("enter the amount you want to deposit"))
    balance=balance+amount
    song.say(f"thank you for depositing {amount} ")
    print("net balance is :",balance)
    song.say(f"now your net balance is {balance}")
    

def check():
             
    song=py.init()
    song.say(f"your balance is {balance} ")
    print("net balance is :",balance)

def menu():
    song=py.init()
    song.say("please select one option")
    print("for withdraw press 1")
    print("for deposit press 2")
    print("for check press 3")
    print("for change pin press 4")
    print("for see your pin press 5")
    menu=int(input("enter your choice"))
    if menu==1:
        withdraw()
    elif menu==2:
        deposit()
    elif menu==3:
        check()
    elif menu==4:
        change_pin()
    elif menu==5:
        pin_show()
    else:
        print("wrong choice")
        
def user():
    for i in range(3):
        song=py.init()
        song.say('please enter your username ')
        song.runAndWait()
        print("lakshay")
        username=input("enter your username: ")
        if (username=="lakshay"):
            song=py.init()
            song.say('enter your password ')
            song.runAndWait()
            print("qwerty")
            password=input("eneter your password: ")
            if (password=="qwerty"):
                song=py.init()
                song.say('enter your captcha ')
                song.runAndWait()
                print(store)
                cap=input("enetr your captcha :")
                if (cap==store):
                    song=py.init()
                    song.say('enter your pin ')
                    song.runAndWait()
                    print("2022")
                    pin=input("eneter your pin")
                    if pin.isdigit()==True:
                        if pin=="2022" :
                            menu()
                        else:
                            print("wrong pin")
                    else:
                        print("invalid pin")
                else:
                    print("wrong captcha")
            else:
                print("wrong password")
        else:
            print("wrong username")

       
        
song=py.init()
song.say("hello sir how may i help you")
song.runAndWait()
user()


       
                
            
               
        
            
    
    


# 

# In[ ]:




