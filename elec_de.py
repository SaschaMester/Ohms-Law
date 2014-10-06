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

from os import * # Wird benötigt für die Bildschirmlöschfunktion
import string

def wait():
  system("sleep 3") # Wartezeiten sind hier zu ändern

def fehler(): # Fehlermeldung bei Division durch 0
  print("FEHLER! Es würde eine Division durch 0 passieren, dies jedoch ist nicht möglich")

def clear(): # Bildschirm löschen
  system("clear")

def ende(): # Programm beenden
  end_antwort = input("Wirklich beenden? (J/N) ")
  if len(end_antwort) == 1:
    if end_antwort == "n" or end_antwort == "N":
      main()
  else:
    print ( "Bitte nur ein Buchstabe!" )
    ende()



def fortsetzen(): # Fragen, ob weitere Berechnung durchgeführt werden soll
  cont = input("Weitere Rechnung durchführen? (J/N) ")
  if len(cont) != 1:
    print("Bitte nur EIN Buchstabe!")
    fortsetzen()
  elif cont == "j" or cont == "J":
    main()
  else:
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
  auswahl = 1
  clear()
  print("1. Spannung berechnen (Ohmsches Gesetz)")
  print( "2. Stromstärke berechnen (Ohmsches Gesetz)")
  print( "3. Widerstand berechnen (Ohmsches Gesetz)")
  print( "4. Programm beenden")
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

  elif auswahl <1 or auswahl  > 4: # Was passiert bei Eingabe von ungültigen Werten? 
    print("Bitte nur Zahlen von 1 - 4 eingeben.")
    print("Programm setzt in 3 Sekunden fort") 
    # Die Wartezeit ist in der Methode wait() zu ändern
    wait()
    main()

main()

