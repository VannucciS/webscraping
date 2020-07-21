# html clues to scrappy - span data-price - to find the price of the place
# to find the location - <span class="posting-location go-to-posting">
# <span> Setor Habitacional Jardim Botânico, Brasília</span>
# date of publication of the ad - <li><i class="icon-g icon-g-fecha-publicado">
# features - <ul class="main-features go-to-posting">
# webpage https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior.html
# https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior-pagina-2.html


from bs4 import BeautifulSoup as soup
import requests


url = "https://www.wimoveis.com.br/casas-aluguel-distrito-federal-goias-ordem-publicado-maior.html"

#scraper = cloudscraper.create_scraper(browser='chrome', interpreter = 'nodejs', recaptcha ={ 'provider':'anticaptcha', 'api_key':'your_anticaptcha_api_key'}) # returns a cloudscraper instance
#scraper.get(url).text

session = requests.Session()
headers =  {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "pt-BR,pt;q=0.9"
    }


req = session.get(url, headers = headers)
req.raise_for_status()
print(len(req.text))
