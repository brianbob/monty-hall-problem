#!/usr/bin/env python

import os
import random

path = "database.txt"
database = open(path, "r+")
stays = switches = line_num = 0

if os.stat(path).st_size > 0 :
  # read the results from the file
  for line in database.readlines():
    line_num += 1
    # Line 2 is stays
    if (line_num == 2) :
      stays = line
    # LIne 3 is failures
    if (line_num == 3) :
      switches = line
  # end for loop
# end if statement

# Re-open the file for writing so that it is overwritten.
database = open(path, 'w')

print("There is a prize behind on of these three doors...")
print("   [1]   [2]   [3]")
door = input("What door is the prize behind? ")

print("you picked door #" + str(door))

# write the results to the file
database.write("Results file. Line 2 is stays, 3 is switches \n")
database.write(stays)
database.write(switches)
database.close()
