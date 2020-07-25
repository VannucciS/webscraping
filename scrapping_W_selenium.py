
# remember to download and install chromedriver
# https://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common import By
from  time import sleep as sleep
import math
#import pandas as pd

"""
Now I have to try to find a way to avoid cloudfare...
""""

url = 'https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior.html'

PATH = 'C:\chromedriver.exe'
browser = webdriver.Chrome(PATH)
browser.get(url)
total = browser.find_element_by_css_selector("#react-result-title > h1 > b").text
total_pages = round(int(total.replace('.','')) / 20)

while True:
    local = []
    lista = []
    precos = []
    resumo = []
    site = []

    sleep(5)

    try:
        browser.find_element_by_css_selector("#modalContent > div > button > i").click()
    except:
        pass
    

    local = browser.find_elements_by_tag_name(".posting-location go-to-posting")
    lista = browser.find_elements_by_tag_name("h2")
    precos = browser.find_elements_by_css_selector(".posting-price-container > div.posting-price > div > span > b")
    resumo = browser.find_elements_by_css_selector(".posting-info-container > div > ul > li:nth-child(1) > b")# arrumar
    site = browser.find_elements_by_css_selector("#react-posting-cards") #arrumar

    print(len(lista), len(precos), len(resumo), len(site), len(local))


    # Ir para a proxima pagina
    page = 1
    while page < total_pages:
        browser.get("https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior-pagina-" + str(page)+ ".html")
        page+=1
        print(page, total_pages, total)
        sleep(10)
    else:
        print("erro")
        print(page, total_pages, total)
        break

#react-result-title > h1 > b



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
