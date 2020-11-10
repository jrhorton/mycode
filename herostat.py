#!/usr/bin/env python3

char_name = input("Which character do you want to know about? (Flash, Batman, Superman)? ")

char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence)? ")

stats = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

#print(stats["flash"]["speed"])

print(f"{char_name[0].upper() + char_name[1:]}'s {char_stat} is: {stats[char_name][char_stat]}.")
