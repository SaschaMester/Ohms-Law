#! /usr/bin/python3 

def ende():
  quit

def spannung():
  r = int(input("Bitte Widerstandswert eingeben: "))
  i = int(input("Bitte Stromstärke eingeben: "))
  u = r * i
  print ("Der Spannungswert beträgt {} Volt" . format(u))
  main()

def widerstand():
  u = int(input("Bitte Spannungswert eingeben: "))
  i = int(input("Bitte Stromstärke eingeben: "))
  r = u / i
  print("Der Widerstandswert beträgt {} Ohm" . format(r))
  main()

def ampere():
  u = int(input("Bitte Spannungswert eingeben: "))
  r = int(input("Bitte Widerstandswert eigeben: "))
  i = u / r
  print("Die Stromstärke beträgt {} Ampère" . format(i))
  main()

def main():
  print("1. Spannung berechnen (Ohmsches Gesetz)")
  print( "2. Stromstärke berechnen (Ohmsches Gesetz)")
  print( "3. Widerstand berechnen (Ohmsches Gesetz)")
  print( "4. Programm beenden")
  auswahl = int(input("Ihre Auswahl: "))

  if auswahl == 1:
    spannung()

  elif auswahl == 2:
    ampere()

  elif auswahl == 3:
    widerstand()

  elif auswahl == 4:
    ende()
  elif auswahl <1 or auswahl  > 4:
    print ("Bitte nur Zahlen von 1 - 4")
    main()

main()

