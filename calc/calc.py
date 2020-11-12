#!/usr/bin/env python3

print("Welcome to the handy dandy calculator")

def add(num1,num2):
    return(num1+num2)

def sub(num1,num2):
    return(num1-num2)

def mult(num1,num2):
    return(num1*num2)

def div(num1,num2):
    return(num1/num2)

list1 = ["+","-","*","/"]

esc = ""

while esc != "Q":
    oper = ""

    while True:
        try:
            x1 = float(input("What is the first number?: "))
            break
        except:
            print("We need a number!")

    while oper not in list1:
        oper = input("What do you want to do? +, -, *, / : ")
        if oper not in list1:
            print("We need one of these....  +, -, *, / ")

    while True:
        try:
            x2 = float(input("What is the second number?: "))
            break
        except:
            print("We need a number!")

    while oper == "/" and x2 == 0:
        while True:
            try:
                x2 = float(input("You should know better than to try to divide by 0! Enter a new number, you potato: "))
                break
            except:
                print("We need a number!")
            break

    if oper == "+":
        res = (add(x1,x2))
    elif oper == "-":
        res = (sub(x1,x2))
    elif oper =="*":
        res = (mult(x1,x2))
    elif oper == "/":
        res = (div(x1,x2))

    if res.is_integer():
        print(int(res))
    else:
       print(res)

    esc = input("Enter Q to quit, or enter any key to continue ").upper()

print("Goodbye")




