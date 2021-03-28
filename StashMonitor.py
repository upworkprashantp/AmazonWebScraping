
import os
from colorama import Fore , Back , Style
import time 
import requests
from bs4 import BeautifulSoup
import smtplib
from pync import Notifier
import sys
import subprocess
import re
import urllib
import webbrowser
from datetime import datetime
from getpass import getpass

#make an algorithm which reads all the link from the files

#tracking sites
AmazonItems = ["https://www.amazon.co.uk/Xbox-RRT-00007-Smeeries-X/dp/B08H93GKNJ/ref=sr_1_5?dchild=1&keywords=xbox&qid=1608378501&sr=8-5"
,"https://www.amazon.co.uk/Xbox-RRT-00007-Series-X/dp/B08GD9MNZB/ref=sr_1_5?dchild=1&keywords=xbox&qid=1608378501&sr=8-5&th=1",
"https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_3?dchild=1&keywords=playstation&qid=1608378578&sr=8-3",
"https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H97NYGP/ref=sr_1_3?dchild=1&keywords=playstation&qid=1608378578&sr=8-3&th=1",
"https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H99878P/ref=sr_1_3?dchild=1&keywords=playstation&qid=1608378578&sr=8-3&th=1"]

CurrysItems = ["https://www.currys.co.uk/gbuk/gaming/console-gaming/consoles/microsoft-xbox-series-x-1-tb-10203371-pdt.html"]


#current time
now = datetime.now()
current_time = now.strftime("\n%H:%M:%S")
print(Fore.WHITE + current_time)

#loading config files
f = open('config/StashID.txt', 'r')
StashID = f.read()
f.close()

f = open('config/UserAgent.txt', 'r')
UserAgentID = f.read()
f.close()

f = open('config/manual.txt', 'r')
HelpManual = f.read()
f.close()

f = open('config/NameID.txt', 'r')
NameID = f.read()
f.close()





print(Fore.WHITE+ 'AmazonWebScraper 1.0.0')


#login sequence +  hides password in terminal 
password = getpass()

if password == StashID:
    print(Fore.GREEN + 'User logged in\n')
    Login = True
else:
    print(Fore.RED + 'denied')
    f = open('config/ErrorLog.txt', 'a')
    f.write(current_time)
    f.write('\nInvalid Login credentials\n')
    f.close()
    PasswordReset = input('do you want to change your password y/n ')
    
    
    if PasswordReset == ('y'):
        print('unavailable')
        sys.exit()
    else:
        sys.exit()

if Login == False:
    sys.exit()

def Main():
    print(Fore.GREEN + 'Welcome back', NameID + '!')
    print(Fore.YELLOW+ '0.  settings')
    print(Fore.RED + '1. run')

    start_menu = input(':')

    if start_menu == ('0'):
        print(Fore.GREEN + '0. change user agent')
        print(Fore.RED + '1. help manual')
        settings_menu = input(':')
    
             

        if settings_menu == ('0'):
            NewUserAgent = str(input('insert new user agent'))
            f = open('config/UserAgent.txt', 'a')
            f.truncate(0)
            f.write(NewUserAgent)
            f.close()
            print(Fore.GREEN + 'user agent changed')
            time.sleep(2)
            Main()
            
        
        if settings_menu == ('1'):
            print(Fore.GREEN + HelpManual)
            print(Fore.RED + '0. back')
            help_menu = input(':')

            if help_menu == ('0'):
                Main()






        if settings_menu == ("1"):
            print(Fore.YELLOW + 'Xbox Series X')
            print(Fore.YELLOW + "Xbox Series S")
            print(Fore.YELLOW + "PS5 ")
            print(Fore.YELLOW + "PS5 Digital Edition")
            print(Fore.RED + '0. back')
            tracking_menu = input(':')

            if tracking_menu == ('0'):
                Main()


        
    if start_menu == ('1'):
        print('\nstarting..\n')
        
     
        while True:
            def StockChecker():
                #Instock prompt
                InStock = 0 
                XboxSeriesX = 0 
                XboxSeriesS = 0
                PS5Console = 0
                PS5Digital = 0 
                XboxSeriesXnd = 0

                #Amazon
                try:
                    URL= AmazonItems[0]
                    headers = {"User-Agent": UserAgentID}
                    page = requests.get(URL, headers=headers)
                    soup = BeautifulSoup(page.content,'html.parser')
                    title = soup.find(id="productTitle").get_text()
                    stock = soup.find(id="availability").get_text()
                except ConnectionError:
                    print(Fore.RED + 'the server has stopped you from connecting, please refrain from restarting program frequently')
                    print(Fore.YELLOW + 'if you think this is an error/bug, please contact us')
                    f = open('config/ErrorLog.txt', 'w')
                    f.write('ConnectionError: SSL Error')
                    f.close()
                    sys.exit()
                
                
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
                    webbrowser.open(AmazonItems[0])
                    print(Fore.GREEN + stock.strip())
                    Notifier.notify('item in stock', title='Stash')
                    InStock+=1
                    XboxSeriesX+=1
                    
                   
                    
                if 'Only' in stock:
                    print(Fore.GREEN + title.strip())
                    print(Fore.RED +  stock.strip())
                    Notifier.notify(stock.strip(), title='Stash')
                    InStock+=1
                    XboxSeriesX+=1
                    
                    
                    

                if '(more on the way)' in stock:
                    print(Fore.GREEN + title.strip())
                    print(Fore.RED + stock.strip())
                    Notifier.notify(stock.strip(), title='Stash')

                if 'Available from these sellers.' in stock:
                    print(Fore.GREEN + title.strip())
                    print(Fore.RED + stock.strip())

                URL= AmazonItems[1]
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
            
                    webbrowser.open(AmazonItems[1])
                    
                    
                    print(Fore.GREEN + stock.strip())
                    Notifier.notify('item in stock', title='Stash')
                    InStock+=1
                    XboxSeriesS+=1
                    

                if 'Only' in stock:
                            print(Fore.GREEN + title.strip())
                            print(Fore.RED +  stock.strip())
                            Notifier.notify(stock.strip(), title='Stash')
                            InStock+=1
                            XboxSeriesS+=1
                           
                          
                if '(more on the way)' in stock:
                        print(Fore.GREEN + title.strip())
                        print(Fore.RED + stock.strip())
                        Notifier.notify(stock.strip(), title='Stash')
                
                if 'Available from these sellers.' in stock:
                    print(Fore.GREEN + title.strip())
                    print(Fore.RED + stock.strip())
                    

                URL= AmazonItems[2]
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
                    
                    webbrowser.open(AmazonItems[2])
        
                    print(Fore.GREEN + stock.strip())
                    Notifier.notify('item in stock', title='Stash')
                    InStock+=1
                    PS5Console+=1
                    
                   

                if 'Only' in stock:
                            print(Fore.GREEN + title.strip())
                            print(Fore.RED +  stock.strip())
                            Notifier.notify(stock.strip(), title='Stash')
                            InStock+=1
                            PS5Console+=1
                           
                           

                if '(more on the way)' in stock:
                        print(Fore.GREEN + title.strip())
                        print(Fore.RED + stock.strip())
                        Notifier.notify(stock.strip(), title='Stash')

                if 'Available from these sellers.' in stock:
                    print(Fore.GREEN + title.strip())
                    print(Fore.RED + stock.strip())

                URL= AmazonItems[3]
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
                
                    webbrowser.open(AmazonItems[3])
                    print(Fore.GREEN + stock.strip())
                    Notifier.notify('item in stock', title='Stash')
                    InStock+=1
                    PS5Digital+=1
                    
                    
                        

                if 'Only' in stock:
                            print(Fore.GREEN + title.strip())
                            print(Fore.RED +  stock.strip())
                            Notifier.notify(stock.strip(), title='Stash')
                            InStock+=1
                            PS5Digital+=1
                            
                           
                if '(more on the way)' in stock:
                        print(Fore.GREEN + title.strip())
                        print(Fore.RED + stock.strip())
                        Notifier.notify(stock.strip(), title='Stash')

                if 'Available from these sellers.' in stock:
                    print(Fore.GREEN + title.strip())
                    print(Fore.RED + stock.strip())

        
                
                
                URL= CurrysItems[0]
                headers = {"User-Agent": UserAgentID}
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content,'html.parser')
                stock = soup.find(id="product-actions").get_text()
                titleRaw = soup.find("h1", {"class": "page-title nosp"})
                titleFormat = str(titleRaw)
                pattern = "<span>(.*?)</span>\n</h1>"
                title = re.search(pattern, titleFormat).group(1)
                
                if 'Sorry this item is out of stock' in stock:
                    print(Fore.GREEN + title.strip())
                    print(Fore.RED + 'item is out of stock')
                else:
                    print(Fore.GREEN + title.strip())
                    print(Fore.GREEN + 'item is in stock\n') 
                    webbrowser.open(AmazonItems[4])
                    InStock+=1
                    XboxSeriesXnd+=1
                    
                 

                print(Fore.YELLOW + 'Only', InStock,'is in stock')

                
                #collective
                if XboxSeriesX == 1:
                    print(Fore.LIGHTCYAN_EX + AmazonItems[0])
                else:
                    pass

                if XboxSeriesS == 1:
                    print(Fore.LIGHTCYAN_EX + AmazonItems[1])
                else:
                    pass

                if PS5Console == 1:
                    print(Fore.LIGHTCYAN_EX + AmazonItems[2])
                else:
                    pass

                if PS5Digital == 1:
                    print(Fore.LIGHTCYAN_EX + AmazonItems[3])
                else:
                    pass

                if XboxSeriesXnd == 1:
                    print(Fore.LIGHTCYAN_EX + CurrysItems[0])
                else:
                    pass
                



                


                
                

        
               


            StockChecker()    
Main()    
           
        
def something()
    oprint
        
