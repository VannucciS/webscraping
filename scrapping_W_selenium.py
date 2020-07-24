
# remember to download and install chromedriver
# https://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common import By
import time
#import pandas as pd


url = 'https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior.html'

PATH = 'C:\chromedriver.exe'
browser = webdriver.Chrome(PATH)

browser.get(url)


"""

"""
while True:
    local = []
    lista = []
    precos = []
    resumo = []
    site = []

    time.sleep(5)

    if browser.find_element_by_css_selector("#modalContent > div > button > i"):
        browser.find_element_by_css_selector("#modalContent > div > button > i").click()
    

    local = browser.find_elements_by_tag_name(".posting-location go-to-posting")
    lista = browser.find_elements_by_tag_name("h2")
    precos = browser.find_elements_by_css_selector(".posting-price-container > div.posting-price > div > span > b")
    resumo = browser.find_elements_by_css_selector(".posting-info-container > div > ul > li:nth-child(1) > b")
    site = browser.find_elements_by_css_selector("#react-posting-cards")

    print(len(lista), len(precos), len(resumo), len(site), len(local))

    if browser.find_element_by_xpath("/html/body[@id='body-listado']/div[@id='modal-hide-elements']/main/div[@id='main-layout-container']/div[@id='react-paging']/div[@class='paging']/ul/li[@class='pag-go-next']/a"):
        browser.find_element_by_xpath("/html/body[@id='body-listado']/div[@id='modal-hide-elements']/main/div[@id='main-layout-container']/div[@id='react-paging']/div[@class='paging']/ul/li[@class='pag-go-next']/a").click() #next page

    else:
        break





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
