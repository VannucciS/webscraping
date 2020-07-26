from selenium import webdriver
from time import sleep

url = 'http://selenium.dunossauro.live/aula_05.html'

PATH = 'C:\chromedriver.exe'
browser = webdriver.Chrome(PATH)
  
browser.get(url)

def envia(nome,email,senha, telefone):
    browser.find_element_by_name("nome").send_keys(nome)
    browser.find_element_by_name("email").send_keys(email)
    browser.find_element_by_name("senha").send_keys(senha)
    browser.find_element_by_name("telefone").send_keys(telefone)
    browser.find_element_by_name("btn").click()

sleep(5)

envia("joao","joao@gmail.com", "123456", "2345678")


#browser.close()
