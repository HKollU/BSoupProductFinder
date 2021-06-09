import requests,sys,webbrowser
from bs4 import BeautifulSoup

URL = 'https://www.newegg.com/p/1HJ-0113-00008?Item=9SIAGDWD026815&quicklink=true'
if len(sys.argv) > 1:
        URL = sys.argv[1] 

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
                        webbrowser.open_new(URL)
                        quit()

