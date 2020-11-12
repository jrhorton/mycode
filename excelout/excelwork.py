#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel
import getpass
from datetime import datetime

# Request data from user
def get_ip_data():
    input_k1 = input("\nWhat is the first thing called? ")
    input_ip = input(f"\nWhat is the {input_k1}? ")
    input_k2 = input("\nWhat is the second thing called? ")
    input_driver = input(f"What is the {input_k2}? ")
    d = {input_k1: input_ip, input_k2: input_driver,"User": getpass.getuser,"DateTime": datetime.now() }
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}] {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")


# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue, or \
    enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break
i
filename = input("\nWhat is the name of the *.xls file? ")
print(mylistdict)
pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")

