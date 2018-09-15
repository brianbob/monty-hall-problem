#!/usr/bin/env python

import os
from random import randint

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

doors = [1, 2, 3]
prize = randint(0,2)
doors.pop(prize);
print(doors);
exit(1);

# Re-open the file for writing so that it is overwritten.
database = open(path, 'w')

print("There is a prize behind on of these three doors...")
print("   [1]   [2]   [3]")
door = input("What door is the prize behind? ")

print("you picked door #" + str(door))

# write the results to the file
database.write("Results file. Line 2 is stays, 3 is switches, line 4 is switches that turned out to be right, and line 5 is stays that turned out to be right. \n")
database.write(stays)
database.write(switches)
database.write(switches_right)
database.write(stays_right)
database.close()
