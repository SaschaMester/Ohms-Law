#! /usr/bin/python3 

def ende():
  quit

def spannung():
  r = int(input("Enter resistance value: "))
  i = int(input("Enter current: "))
  u = r * i
  print ("The voltage value is {} Volts" . format(u))
  main()

def widerstand():
  u = int(input("Enter voltage value: "))
  i = int(input("Enter current: "))
  r = u / i
  print("The resistance value is  {} Ohms" . format(r))
  main()

def ampere():
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
    spannung()

  elif auswahl == 2:
    ampere()

  elif auswahl == 3:
    widerstand()

  elif auswahl == 4:
    ende()
  elif auswahl > 4:
    print ("Bitte nur Zahlen von 1 - 4")
    main()
  else:
    print("FEHLER! Programm wird abgebrochen")
    quit

main()

