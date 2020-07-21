
# remember to download and install chromedriver
# https://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior.html'

PATH = 'C:\chromedriver.exe'
browser = webdriver.Chrome(PATH)

browser.get(url)
if  browser.find_element_by_id("#body-listado") is True:
    erro = browser.find_element_by_css_selector("#modalContent > div > button > i")
    erro.click()

prices = browser.find_elements(By.CLASS_NAME, "posting-location go-to-posting")
#span.posting-location.go-to-posting

#print(driver.page_source)

print(prices)

#time.sleep(20)

browser.quit()