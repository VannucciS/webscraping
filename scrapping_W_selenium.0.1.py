
# remember to download and install chromedriver
# https://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options # trying to insert headers in webdriver to avoid cloudfare
#from selenium.webdriver.common import By
from  time import sleep as sleep
import math
import pandas as pd
from datetime import datetime




url = 'https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior.html'

PATH = 'C:\chromedriver.exe'
#browser = webdriver.Chrome(PATH)



"""
The follow part came from this website:
http://allselenium.info/how-to-setup-user-agent-in-python-selenium-webdriver/
"""
#get user agent from the chrome browser
#agent = browser.execute_script("return navigator.userAgent")
#print(agent)
#print(browser.execute_script("return navigator.userAgent"))

# User agent setup in chrome
opts = Options()
opts.add_argument("user-agent=[user=agent string]")
browser = webdriver.Chrome(options = opts, executable_path = PATH)
agent = browser.execute_script("return navigator.userAgent")


browser.get(url)
sleep(7)
total = browser.find_element_by_css_selector("#react-result-title > h1 > b").text
total_pages = round(int(total.replace('.','')) / 20)


df = pd.DataFrame(columns = ['local', 'lista', 'precos', 'resumo', 'site', 'data_pesquisa'])

local_list = []
lista_list = []
precos_list = []
description_list = []
    #site_list = []

while True:

    
    page = 1

    #sleep(7)

    while page < 5:
        sleep(5)
        browser.get("https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior-pagina-" + str(page)+ ".html")

        if page == total_pages:
            print('time to do the captcha')
            sleep(30) # Time to do the captcha
            
        page+=1
        print(page, total_pages, total)

        try:
            browser.find_element_by_css_selector("#modalContent > div > button > i").click()
        except:
            pass
        

        local = browser.find_elements_by_tag_name(".posting-location go-to-posting")
        for l in local:
            local_list.append(l.text)
        lista = browser.find_elements_by_tag_name("h2")
        for li in lista:
            lista_list.append(li.text)
        precos = browser.find_elements_by_css_selector(".posting-price-container > div.posting-price > div > span > b")
        for p in precos:
            precos_list.append(p.text)
        description = browser.find_elements_by_css_selector(".posting-description")
        for d in description:
            description_list.append(d.text)
        #site = browser.find_elements_by_css_selector("#react-posting-cards") #arrumar



        print(len(lista_list), len(precos_list), len(description_list), len(local_list))


        # Ir para a proxima pagina
        
    
        
    else:
        print("erro")
        print(page, total_pages, total)
        break

#react-result-title > h1 > b
#from list to dataframe
df['local'] = local_list
df['lista'] = lista_list
df['precos'] = precos_list
df['data_pesquisa'] = datetime.now().strftime("%d-%m-%y")

#save the dataframe to .csv
dia = datetime.now().strftime("%d-%m-%y")
df.to_csv("registros-do-dia-"+ dia +".csv")

"""
for index, l in enumerate(lista):
    print (index, l.text)
    


for index, l in enumerate(price):
    print (index, l.text)
      

for l in list:
    print(l.find_element_by_tag_name("h2").text)
#span.posting-location.go-to-posting

#print(driver.page_source)

print(prices)
"""




browser.quit()