from getpass import getpass
import colorama
from colorama import Fore
import subprocess
import os
import sys
from datetime import datetime
import re
import urllib
import webbrowser
from getpass import getpass
import requests
import time



print(Fore.GREEN + 'Welcome, create an account to start')
time.sleep(1)

NameID = input('What is your name?')
CreateStashID = input('create your stash ID' + Fore.RED + '(this will be used for logging in):')

CreateUserAgent = input(Fore.GREEN + 'input your user agent(search my user agent)')

#creating user files
file = open('SourceCode/StashID.txt', 'a')
file.write(CreateStashID)
file.close()


file = open('SourceCode/UserAgent.txt', 'a')
file.write(CreateUserAgent)
file.close()

file = open('SourceCode/NameID.txt', 'a')
file.write(NameID)
file.close()

time.sleep(2)
print(Fore.YELLOW + 'installing configuration files')
time.sleep(2)
print(Fore.YELLOW + 'creating user account')
time.sleep(2)
print(Fore.GREEN +  'setup complete!')
