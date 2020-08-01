
# remember to download and install chromedriver
# https://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options # trying to insert headers in webdriver to avoid cloudfare
#from selenium.webdriver.common import By
from  time import sleep as sleep
#import math
import pandas as pd
from datetime import datetime
#from parsel import Selector




url = 'https://www.wimoveis.com.br/imoveis-aluguel-distrito-federal-goias.html'

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


"""
You can save the current cookies as a python object using pickle. For example:

import pickle
import selenium.webdriver 

driver = selenium.webdriver.Firefox()
driver.get("http://www.google.com")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))


and later to add them back:

import pickle
import selenium.webdriver 

driver = selenium.webdriver.Firefox()
driver.get("http://www.google.com")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)







"""

browser.get(url)
browser.get_cookies()

sleep(5)
total = browser.find_element_by_css_selector("#react-result-title > h1 > b").text
total_pages = round(int(total.replace('.','')) / 20)
#html = browser.page_source

df = pd.DataFrame(columns = ['titulo', 'caracteristicas', 'precos', 'endereco','rua', 'bairro', 'cidade','data_anuncio', 'link','data_pesquisa'])

endereco_list = []
titulo_list = []
precos_list = []
caracteristicas_list = []
cidade_list = []
bairro_list = []
rua_list = []
site_list = []
data_anuncio_list=[]

print(total_pages)

while True:    
    page = 1

    
    while page <= total_pages:
        
        browser.get("https://www.wimoveis.com.br/imoveis-aluguel-distrito-federal-goias-pagina-" + str(page)+ ".html")
        sleep(5)

        if page == 1:
            print('You have 40 seconds to captcha')
            sleep(10) # Time to do the captcha
            print("You have 30 seconds...")
            sleep(10)
            print("You have 20 seconds...")
            sleep(10)
            print("You have 10 seconds...")
            sleep(10)
            print("You're time is over...")
        page+=1
        
        try:
            browser.find_element_by_css_selector("#modalContent > div > button > i").click()
        except:
            pass
        

        endereco = browser.find_elements_by_xpath("//*[@class='posting-location go-to-posting']") #'Rua T 53 , Setor Marista, Goiânia'
        for e in endereco:
            if e is None:
                endereco_list.append(0)
            else:
                endereco_list.append(e.text)
                """
                texto = e.text
                print(texto)
                f = texto.split(",", maxsplit = 2)
                print(f)
                rua_list.append(f[0])
                cidade_list.append(f[1])
                """
        titulo = browser.find_elements_by_tag_name("h2") #'Sobrado Comercial Marista'
        for li in titulo:
            titulo_list.append(li.text)
        
        precos = browser.find_elements_by_css_selector(".posting-price-container > div.posting-price > div > span > b") #'R$ 5.500'
        for p in precos:
            precos_list.append(p.text)
        
        caracteristicas = browser.find_elements_by_xpath("//*[@class='main-features go-to-posting']") #'587 m² área total 221 m² área útil 0 Quartos 3 Banheiros 2 Vagas
        for d in caracteristicas:
            caracteristicas_list.append(d.text)
        

        site = browser.find_elements_by_xpath("//*[@href]")
        try:
            for ii in site:
                if "propriedades" in ii.get_attribute('href'):
                    site_list.append(ii.get_attribute('href'))
        except:
            pass


       


        print(len(endereco_list), 
              len(titulo_list), 
              len(precos_list), 
              len(caracteristicas_list),
              len(cidade_list),
              len(bairro_list),
              len(rua_list),
              len(site_list))


        # Ir para a proxima pagina
        
    
        
    else:
        print("erro")
        print(page, total_pages, total)
        break

#react-result-title > h1 > b
#from list to dataframe
df['titulo'] = titulo_list
df['endereco'] = endereco_list
df['precos'] = precos_list
df['caracteristicas'] = caracteristicas_list
"""
df['rua'] = rua_list
df['cidade'] = cidade_list
df['bairro'] = bairro_list
"""
df['link'] = site_list
df['data_pesquisa'] = datetime.now().strftime("%d-%m-%y")

#save the dataframe to .csv
dia = datetime.now().strftime("%d-%m-%y")
df.to_csv("registros-do-dia-"+ dia +".csv")

print("Bye, bye...")
browser.quit()