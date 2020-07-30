from selenium import webdriver
from  time import sleep as sleep


url = 'https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior.html'

PATH = 'C:\chromedriver.exe'
browser = webdriver.Chrome(PATH)

browser.get(url)

#sleep(5)

ids = browser.find_elements_by_xpath("//*[@href]")


try:
	for ii in ids:
	#print(ii.get_attribute('href'))
		if "propriedades" in ii.get_attribute('href'):
			print(ii.get_attribute('href'))
except:
	pass

sleep(5)

browser.close()