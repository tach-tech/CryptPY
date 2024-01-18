from pystyle import *
from os import system

import cryptpy

purple = Col.purple
white = Col.white

system('cls')
c = input(f"{purple}You want run ?: \n \n1) cmd program : 1\n2) gui program : 2\n \n => {white}")

cryptpy.cryptPY_cmd() if c == "1" else cryptpy.cryptPY_gui()