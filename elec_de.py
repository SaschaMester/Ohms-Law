#!/usr/bin/python3

#
#  Copyright (C) 2014  Sascha Mester
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#  Menu by Christian Hausknecht, the original source code of
#  Christian Hausknecht's "simplemenu" is included

"""
    ~~~~~~~~~~~~~
    simplemenu.py
    ~~~~~~~~~~~~~

    Very simple approach to implement a generic, but easy to use menu system
    with basic Python data types.
    
    Each menu consists of this tuple (or list) structure:
    
        (
            ("text to be shown", <function object>),
            ("another item text", <another function object>),
            (..., ...),
            ...
        )
        
    To be more generic, each 'callable' can be used as second argument.
    
    The user can choose via an computed index, which action should be
    triggered by the core function `handle_menu`.

    This is esspecially written for beginners, so there is no magic like
    `functools.partial` or some closures to create demo functions.

    .. moduleauthor:: Christian Hausknecht <christian.hausknecht@gmx.de>
"""


#
# Some little demo functions that does not have any sensefull functionality.
# We just need something that "does" something
#

from os import *
import string
import sys

def lizenz():
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
  print("# In 6 Sekunden geht's weiter          #")
  print("########################################")
  print("# Das Menü ist das \"simplemenu\" von  #")
  print("# Christian Hausknecht. Der Original-  #")
  print("# Quellcode hierfür liegt dem          #")
  print("# Git-Repo bei                         #")
  print("########################################")
  
  wait(6)
  main()

def wait(N):
  system("sleep {}" . format(N)) 

def fehler(): # Fehlermeldung bei Division durch 0
  print("FEHLER! Es würde eine Division durch 0 passieren, dies jedoch ist nicht möglich")

def clear(): # Bildschirm löschen
  system("clear")

def spannung(): # Spannungswert berechnen
  r = float(input("Bitte Widerstandswert eingeben: "))
  i = float(input("Bitte Stromstärke eingeben: "))
  u = r * i
  print ("Der Spannungswert beträgt {} Volt" . format(u))

def widerstand(): # Widerstandswert berechnen
  u = float(input("Bitte Spannungswert eingeben: "))
  i = float(input("Bitte Stromstärke eingeben: "))
  if i == 0: # Division durch 0 verhindern
    fehler()
    widerstand()
  else:
    r = u / i
    print("Der Widerstandswert beträgt {} Ohm" . format(r))

def ampere(): # Stromstärke berechnen
  u = float(input("Bitte Spannungswert eingeben: "))
  r = float(input("Bitte Widerstandswert eigeben: "))
  if r == 0: # Division durch 0 verhindern
    fehler()
    ampere()
  else:
    i = u / r
    print("Die Stromstärke beträgt {} Ampère" . format(i))

#
# Core functions of our simple menu system
#
    
def print_menu(menu):
    """
    Function that prints our menu items. It adds an numeric index to each
    item in order to make that the choosebale index for the user.
    
    :param menu: tuple with menu definition
    """
    for index, item in enumerate(menu, 1):
        print("{}  {}".format(index, item[0]))

        
def get_user_input(menu):
    """
    This function implements a simple user input with validation. As the
    input data should match with existing menu items, we check, if the value
    is valid.

    :param menu: tuple with menu definition
    
    :returns: int
    """
    while True:
        try:
            choice = int(input("Ihre Wahl?: ")) - 1
            if 0 <= choice < len(menu):
                return choice
            else:
                raise IndexError
        except (ValueError, IndexError):
            print("Bitte nur Zahlen aus dem Bereich 1 - {} eingeben".format(
                                                                    len(menu)))


def handle_menu(menu):
    """
    Core function of our menu system. It handles the complete process of
    printing the menu, getting the user input and calling the corresponding
    function.
    
    :param menu: tuple with menu definition
    """
    while True:
        print_menu(menu)
        choice = get_user_input(menu)
        menu[choice][1]()

    
def main():
    # just some demonstration menu structure:
    menu = (
        ("Spannung berechnen(Ohmsches Gesetz)", spannung),
        ("Stromstärke berechnen (Ohmsches Gesetz)", ampere),
        ("Widerstand berechnen (Ohmsches Gesetz)", widerstand),
        ("Lizenzinformation", lizenz),
        ("Beenden", lambda: sys.exit(0))
    )
    
    # run the menu-"handler" :-)
    handle_menu(menu)


if __name__ == "__main__":
    main()
