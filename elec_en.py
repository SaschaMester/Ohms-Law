#! /usr/bin/python3 
# -*- coding: utf-8 -*-

########################################
############### Ohms-Law ###############
########################################

########################################
# (c) 2014 by Sascha Mester            #
# This program is free software.       #
# You can freely redistribute it       #
# under the terms of the               #
# GNU General Public License,          #
# version 3 or ( at your opinion)      #
# any later version, published by      #
# the Free Software Foundation.        #
########################################
# This program is published in the     #
# hope that it will be useful,         #
# but WITHOUT ANY WARRANTY, without    #
# even the implied warranty of         #
# MERCHANDIBILITY of FITNESS FOR A     #
# PARTICULAR PURPOSE. See the          #
# GNU GENERAL PUBLIC LICENSE for       #
# more details.                        #
########################################

from os import * # Used for clear screen
import string

def ourLicense():
  print("########################################")
  print("############### Ohms-Law ###############")
  print("########################################")
  print()
  print("########################################")
  print("# (c) 2014 by Sascha Mester            #")
  print("# This program is free software.       #")
  print("# You can freely redistribute it       #")
  print("# under the terms of the               #")
  print("# GNU General Public License,          #")
  print("# version 3 or ( at your opinion)      #")
  print("# any later version, published by      #")
  print("# the Free Software Foundation.        #")
  print("########################################")
  print("# This program is published in the     #")
  print("# hope that it will be useful,         #")
  print("# but WITHOUT ANY WARRANTY, without    #")
  print("# even the implied warranty of         #")
  print("# MERCHANDIBILITY of FITNESS FOR A     #")
  print("# PARTICULAR PURPOSE. See the          #")
  print("# GNU GENERAL PUBLIC LICENSE for       #")
  print("# more details.                        #")
  print("########################################")
  print("# Program continues within 6 seconds   #")
  print("########################################")
  wait(6)
  main()

def wait(N):
  system("sleep {}" . format(N))

def error():
  print("ERROR! The program would divide by 0, this is not possible")

def clear(): # Clear screen
  system("clear")

def end(): # Finish
  end_answer = input("Do you really want to quit? (Y/N) ")
  if len(end_answer) != 1:
    print("Only ONE letter!") 
    end()
  elif end_answer == "n" or end_answer == "N":
    main()



def cont(): # Ask if the user wants another calculation
  cont_answer = input("Do you want to continue? (Y/N) ")
  if len(cont_answer) != 1:
    print("Only ONE letter!")
    cont()
  elif cont_answer == "Y" or cont_answer == "y":
    main()
  else:
    end()

def voltage(): # Calculate voltage
  r = float(input("Enter resistance value: "))
  i = float(input("Enter current: "))
  u = r * i
  print ("The voltage value is {} Volts" . format(u))
  cont()

def resistance(): # Calculate resistance
  u = float(input("Enter voltage value: "))
  i = float(input("Enter current: "))
  if i == 0: # Avoid divide by zero 
    error()
    resistance()
  else:
    r = u / i
    print("The resistance value is  {} Ohms" . format(r))
    cont()

def current(): # Calculate current
  u = float(input("Enter voltage value: "))
  r = float(input("Enter resistance value: "))
  if r == 0: # Avoid divide by zero
    error()
    current()
  else:
    i = u / r
    print("The current is {} amps" . format(i))
    cont()

def main(): # Main menu
  clear()
  print("1. Calculate voltage (Ohm's Law)")
  print("2. Calculate current (Ohm's Law)")
  print("3. Calculate resistance (Ohm's Law)")
  print("4. Quit")
  print("5. License Information")
  choice = int(input("Your Choice: "))

  # Links the numbers to the calculating functions 
  if choice == 1:
    voltage()

  elif choice == 2:
    current()

  elif choice == 3:
    resistance()

  elif choice == 4:
    end()

  elif choice == 5:
    ourLicense()

  elif choice <1 or choice > 5: # Invalid Choice
    print ("Only numbers 1 - 5 allowed")
    print ("The program will continue in 3 seconds") # You can change this value in wait() method
    wait(3)
    main()

main()

