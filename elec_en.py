#! /usr/bin/python3 
from os import *

def clear():
  system("clear")
  main()

def end():
  quit

def voltage():
  r = float(input("Enter resistance value: "))
  i = float(input("Enter current: "))
  u = r * i
  print ("The voltage value is {} Volts" . format(u))
  main()

def resistance():
  u = float(input("Enter voltage value: "))
  i = float(input("Enter current: "))
  r = u / i
  print("The resistance value is  {} Ohms" . format(r))
  main()

def current():
  u = float(input("Enter voltage value: "))
  r = float(input("Enter resistance value: "))
  i = u / r
  print("The current is {} amps" . format(i))
  main()

def main():
  print("1. Calculate voltage (Ohm's Law)")
  print("2. Calculate current (Ohm's Law)")
  print("3. Calculate resistance (Ohm's Law)")
  print("4. Quit")
  print("5. Clear Screen")
  choice = int(input("Your Choice: "))

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

  elif choice <1 or choice > 5:
    print ("Only numbers 1 - 5 allowed")
    main()

main()

