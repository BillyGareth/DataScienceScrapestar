from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request

url="https://www.jumia.co.ke/smartphones/"

req=Request(url, headers={"User-Agent":"Mozilla/5.0"})

webpage=urlopen(req).read()

page_soup = soup(webpage,"html.parser")

containers = page_soup.findAll('div', class_ = "-paxs row _no-g _4cl-3cm-shs")

for althecontainers in containers:
	product_label = containers.article.a.div.h3["name"]
	print(product_label)