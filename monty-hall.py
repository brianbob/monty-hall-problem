#!/usr/bin/env python

import os
import random

path = "database.txt"
database = open(path, "r+")
stays = switches = switches_right = stays_right = line_num = 0

if os.stat(path).st_size > 0 :
  # read the results from the file
  for line in database.readlines():
    line_num += 1
    # Line 2 is stays
    if (line_num == 2) :
      stays = int(line)
    # Line 3 is stays
    if (line_num == 3) :
      switches = int(line)
    # Line 4 is switches that were correct
    if (line_num == 4) :
      switches_right = int(line)
    # Line 5 is stays that were right
    if (line_num == 5) :
      stays_right = int(line)
  # end for loop
# end if statement

# calculate total (for use in percentages)
total_rounds = stays + switches

# Create our door options
doors = [1, 2, 3]

# Pick a door at random to be the 'prize door'
prize = random.choice(doors)

print("There is a prize behind on of these three doors...")
print("   [1]   [2]   [3]")

# Get the user's door choice
first_choice = input("What door is the prize behind? ")
print("you picked door #" + str(first_choice))

# Give the user the option to switch
# Fist tho, remove the prize door from our list of options
doors.pop(prize-1)

# If the user didn't pick the prize door, make sure the door they choice is
# removed from the options
if first_choice != prize :
  doors.pop(first_choice-1)

# Pick a goat door that is not the prize door and is not the user's pick.
goat = random.choice(doors)
#remove the goat door from the list of options.
doors.pop(goat-1)
print("There is a goat behind door # " + str(goat))

# get the last door number.
last = doors.pop()
# Ask the user if they want to switch
switch = input("Do you want to switch your pick from door #" + str(first_choice) + " to door #" + str(last) + "? (y/n)")

# @todo compute results
# @todo log results

# Re-open the file for writing so that it is overwritten.
database = open(path, 'w')
# write the results to the file
database.write("Results file. Line 2 is stays, 3 is switches, line 4 is switches that turned out to be right, and line 5 is stays that turned out to be right. \n")
database.write(stays)
database.write(switches)
database.write(switches_right)
database.write(stays_right)
database.close()
