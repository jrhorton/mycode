#!/usr/bin/env python3
def calc(num1,num2,func):
    print(num1+func+num2)

while True:
    try:
        x1 = float(input("What is the first number?: "))
        break
    except:
        print("We need a number!")

while True:
    try:
        x2 = float(input("What is the second number?: "))
        break
    except:
        print("We need a number!")

while True:
    try:
        func = input("What do you want to do? +, -, *, / : ") in ["+","-","*","/"]
        break
    except:
        print("We need one of these....  +, -, *, / ")


calc(x1,x2,func)



