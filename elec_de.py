#! /usr/bin/python3 
from os import * # Wird benötigt für die Bildschirmlöschfunktion


def fehler(): # Fehlermeldung bei Division durch 0
  print("FEHLER! Es würde eine Division durch 0 passieren, dies jedoch ist nicht möglich")

def clear(): # Bildschirm löschen
  system("clear")

def ende(): # Programm beenden
  quit

def fortsetzen(): # Fragen, ob weitere Berechnung durchgeführt werden soll
  cont = input("Weitere Rechnung durchführen? (J/N) ")
  if cont == "j" or cont == "J":
    clear()
    main()
  else:
    clear()
    ende()

def spannung(): # Spannungswert berechnen
  r = float(input("Bitte Widerstandswert eingeben: "))
  i = float(input("Bitte Stromstärke eingeben: "))
  u = r * i
  print ("Der Spannungswert beträgt {} Volt" . format(u))
  fortsetzen()

def widerstand(): # Widerstandswert berechnen
  u = float(input("Bitte Spannungswert eingeben: "))
  i = float(input("Bitte Stromstärke eingeben: "))
  if i == 0: # Division durch 0 verhindern
    fehler()
    widerstand()
  else:
    r = u / i
    print("Der Widerstandswert beträgt {} Ohm" . format(r))
    fortsetzen()

def ampere(): # Stromstärke berechnen
  u = float(input("Bitte Spannungswert eingeben: "))
  r = float(input("Bitte Widerstandswert eigeben: "))
  if r == 0: # Division durch 0 verhindern
    fehler()
    ampere()
  else:
    i = u / r
    print("Die Stromstärke beträgt {} Ampère" . format(i))
    fortsetzen()

def main(): # Hauptmenü
  print("1. Spannung berechnen (Ohmsches Gesetz)")
  print( "2. Stromstärke berechnen (Ohmsches Gesetz)")
  print( "3. Widerstand berechnen (Ohmsches Gesetz)")
  print( "4. Programm beenden")
  print( "5. Bildschirm löschen")
  auswahl = int(input("Ihre Auswahl: "))

  # Eingabe auswerten
  if auswahl == 1:
    spannung()

  elif auswahl == 2:
    ampere()

  elif auswahl == 3:
    widerstand()

  elif auswahl == 4:
    ende()

  elif auswahl == 5:
    clear()

  elif auswahl <1 or auswahl  > 5: # Was passiert bei Eingabe von ungültigen Werten? 
    print ("Bitte nur Zahlen von 1 - 5")
    main()

main()

