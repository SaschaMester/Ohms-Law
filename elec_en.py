#! /usr/bin/python3 

def end():
  quit

def voltage():
  r = int(input("Enter resistance value: "))
  i = int(input("Enter current: "))
  u = r * i
  print ("The voltage value is {} Volts" . format(u))
  main()

def resistance():
  u = int(input("Enter voltage value: "))
  i = int(input("Enter current: "))
  r = u / i
  print("The resistance value is  {} Ohms" . format(r))
  main()

def current():
  u = int(input("Enter voltage value: "))
  r = int(input("Enter resistance value: "))
  i = u / r
  print("The current is {} amps" . format(i))
  main()

def main():
  print("1. Calculate voltage (Ohm's Law)")
  print("2. Calculate current (Ohm's Law)")
  print("3. Calculate resistance (Ohm's Law)")
  print("4. Quit")
  auswahl = int(input("Your Choice: "))

  if auswahl == 1:
    voltage()

  elif auswahl == 2:
    current()

  elif auswahl == 3:
    resistance()

  elif auswahl == 4:
    end()
  elif auswahl > 4:
    print ("Only numbers 1 - 4 allowed")
    main()
  else:
    print("ERROR! Program will cancel")
    quit

main()

