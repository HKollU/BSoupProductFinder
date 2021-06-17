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
				webbrowser.open_new(URL)
				getIt = page.text
	
				f = open('output.html','wt',encoding='utf-8')
				f.write(getIt)
				print(getIt)
				quit()

	if AMD in URL:
		browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
		browser.execute_script("console.log('mkay')")
		quit()
browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
browser.get('https://www.amd.com/en/direct-buy/5458372800/us')
browser.execute_script('javascript:(async () => { s=document.createElement(\'script\'); s.innerHTML=(await (await fetch(`https://gist.githubusercontent.com/sebast1an99/ca41e69a0fcb3f6c1cceb0bc05668e6e/raw/amd.js?v=${new Date().getTime()}`)).text()); document.body.appendChild(s); })()')
print('Title: %s' % browser.title)
