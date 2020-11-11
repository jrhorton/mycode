#!/usr/bin/env python3
## create file object in "r"ead mode
x = input("What file do you want to open?: ")
configfile = open(str(x), "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)
print(len(configlist))

## Always close your file
configfile.close()

