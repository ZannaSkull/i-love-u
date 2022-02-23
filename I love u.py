import time 
import ctypes
from termcolor import colored
import os
from os import system, name

ctypes.windll.kernel32.SetConsoleTitleW("Your Title")

VivaLaPatata = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
VivaLaPatata()

EZ=("I love U <3")
for i in range (0, 6969):
     print(colored(EZ,'magenta',))
     time.sleep(0.1)
