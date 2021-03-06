
# remember to download and install chromedriver
# https://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options # trying to insert headers in webdriver to avoid cloudfare
#from selenium.webdriver.common import By
from  time import sleep as sleep
#import math
import pandas as pd
import datetime
import re




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
today = datetime.datetime.now().strftime("%d-%m-%y")

while True:

    
    page = 1

    #sleep(7)

    while page <= 3:
        sleep(3)
        browser.get("https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior-pagina-" + str(page)+ ".html")

        if page == 1:
            print('time to do the captcha')
            sleep(40) # Time to do the captcha
            
        page+=1
        print(page, total_pages, total)

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
            f = texto.split()
            for g in f:
                rua_list.append(g[-3])
                bairro_list.append(g[-2])
                cidade_list.append(g[-1])
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
            for s in site:
            #print(ii.get_attribute('href'))
                if "propriedades" in s.get_attribute('href'):
                    site_list.append(s.get_attribute('href'))
        except:
            pass

        data_anuncio = browser.find_elements_by_css_selector(".posting-features-container")
        for d in data_anuncio:
            da = d.text
            dat = re.sub("[a-zA-Zà-úÀ-Ú]", "", da)
            data = dat.strip()
            print(data, da, dat)
            if data is None or "":
                data_anuncio_list.append(today)
            else:
                #data_anuncio_list.append(datetime.datetime.now() + datetime.timedelta(days=int(data)))
                data_anuncio_list.append(data)


       


        print(len(endereco_list), 
              len(titulo_list), 
              len(precos_list), #react-posting-cards > div > div:nth-child(1) > div > div.second-column > div.posting-features-container > ul > li > i
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
df['data_anuncio'] = data_anuncio_list
df['data_pesquisa'] = today

#save the dataframe to .csv

df.to_csv("registros-do-dia-"+ today +".csv")

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