import requests,sys,webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
URL = 'https://www.newegg.com/p/1HJ-0113-00008?Item=9SIAGDWD026815&quicklink=true'
AMD = 'https://www.amd.com/en/direct-buy/5458372800/us'
if len(sys.argv) > 1:
        URL = sys.argv[1] 
if URL != AMD :
        while True:
                page = requests.get(URL)
                soup = BeautifulSoup(page.content,'html.parser')
                results = soup.find(id='ProductBuy')
                themessage = results.find_all('button',class_='btn btn-primary btn-wide')
                for themessage in themessage:
                        text_elem = themessage.text
                        title = themessage.title
                        print(text_elem)
                        if 'Add' in text_elem:
                                print('STOCK FOUND!: ' + URL)
                                #webbrowser.open_new(URL)
                                getIt = page.text
                                getIt = getIt.replace('Homall 60 Inch Gaming Desk PC Computer Desk Large Desktop Home Office Table T-shaped Frame Gamer Workstation with Full Desk Mouse Pad, Gaming Handle Rack, Cup Holder and Head Set Rack (Black) - Newegg.com','    Hello world, Joel   ')	
                                	
                                with open('output.html','w+',encoding='utf-8') as f:
                                    f.write(getIt)
                                    for i in range(0,100):
                                        print(getIt[i], end="")
                                quit()
