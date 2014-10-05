#! /usr/bin/python3 
from os import * # Used for clear screen

def error():
  print("ERROR! The program would divide by 0, this is not possible")

def clear(): # Clear screen
  system("clear")
  main()

def end(): # Finish
  quit

def voltage(): # Calculate voltage
  r = float(input("Enter resistance value: "))
  i = float(input("Enter current: "))
  u = r * i
  print ("The voltage value is {} Volts" . format(u))
  main()

def resistance(): # Calculate resistance
  u = float(input("Enter voltage value: "))
  i = float(input("Enter current: "))
  if i == 0: # Avoid divide by zero 
    error()
    resistance()
  else:
    r = u / i
    print("The resistance value is  {} Ohms" . format(r))
    main()

def current(): # Calculate current
  u = float(input("Enter voltage value: "))
  r = float(input("Enter resistance value: "))
  if r == 0: # Avoid divide by zero
    error()
    current()
  else:
    i = u / r
    print("The current is {} amps" . format(i))
    main()

def main(): # Main menu
  print("1. Calculate voltage (Ohm's Law)")
  print("2. Calculate current (Ohm's Law)")
  print("3. Calculate resistance (Ohm's Law)")
  print("4. Quit")
  print("5. Clear Screen")
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
    clear()

  elif choice <1 or choice > 5: # Invalid Choice
    print ("Only numbers 1 - 5 allowed")
    main()

main()

