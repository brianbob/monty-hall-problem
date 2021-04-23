#!/usr/bin/env python

import random

opened_door = 0

# Create our door options
prize = random.randint(1,3)
doors = {'1': 0 , '2': 0, '3': 0 }

for key,value in doors.items():
    if prize == int(key):
        doors[key] = 'prize'
    else:
        doors[key] = 'goat'



print("There is a prize behind on of these three doors...")
print("   [1]   [2]   [3]")

# Get the user's door choice
first_choice = input("What door is the prize behind? ")
print("you picked door #" + str(first_choice))


for key,value in doors.items():
    if first_choice == key:
        pass
    else:
        if value == 'goat':
            opened_door = key
            continue


print("There is a goat behind door # " + str(opened_door))


# Ask the user if they want to switch
switch = input("Do you want to switch your pick from door #" + str(first_choice) + "? If so pick a door ")

print(f"The door you picked contains a {doors[switch]}")
