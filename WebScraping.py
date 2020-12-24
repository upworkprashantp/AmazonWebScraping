from bs4 import BeautifulSoup
import time
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
from pync import Notifier

f = open('SourceCode/UserAgent.txt', 'r')
UserAgentID = f.read()
f.close()

f = open('SourceCode/StashID.txt', 'r')
StashID = f.read()
f.close()


#date and time imports
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(Fore.WHITE + current_time)

print(Fore.WHITE + 'AmazonWebScraper 1.0.0\n' + Fore.YELLOW + 'by AccendWeb\n')

print(Fore.WHITE + 'Welcome',StashID + '!')
print(Fore.YELLOW + '1. run')


main_menu = input(':')

if main_menu == ('1'):
    URLinput = input('insert url')
    while True:
        def StockChecker():
                #Amazon
            URL= URLinput
            headers = {"User-Agent": UserAgentID}
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content,'html.parser')
            title = soup.find(id="productTitle").get_text()
            stock = soup.find(id="availability").get_text()
            if 'Currently unavailable.' in stock:
                    print(Fore.GREEN + title.strip())
                    print(Fore.RED + "Currently unavailable, stock TBD")
                    
                            
                                
            if 'In stock on' in stock:
                price = soup.find(id="priceblock_ourprice").get_text()
                StockStrip = stock.strip()
                StockStriped = StockStrip.strip('Order it now.') 
                print(Fore.RED + StockStriped)
                        

                                        
                            
            if 'In stock.' in stock:
                price = soup.find(id="priceblock_ourprice").get_text()
                print(Fore.GREEN + title.strip())
                print(Fore.GREEN + price)
                  
                print(Fore.GREEN + stock.strip())
                Notifier.notify('item in stock', title='Stash')
                                

            if 'Only' in stock:
                print(Fore.GREEN + title.strip())
                print(Fore.RED +  stock.strip())
                Notifier.notify(stock.strip(), title='Stash')

            if '(more on the way)' in stock:
                print(Fore.GREEN + title.strip())
                print(Fore.RED + stock.strip())
                Notifier.notify(stock.strip(), title='Stash')

            if 'Available from these sellers.' in stock:
                print(Fore.GREEN + title.strip())
                print(Fore.RED + stock.strip())
        
        StockChecker()