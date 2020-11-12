#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

animals = ["sheep","cows","pigs","chickens", "llamas", "cats"]

#for x in farms[0]["agriculture"]:
#    print(x)

farm = input("Select a farm by number 1: NE Farm, 2: W Farm, 3: SE Farm: ")

#for x in farms[int(farm)-1]["agriculture"]:
#    print(x)

for x in farms[int(farm)-1]["agriculture"]:
    if x in animals:
       print(x)