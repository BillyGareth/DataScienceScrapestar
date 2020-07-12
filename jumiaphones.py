from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request

url="https://www.jumia.co.ke/smartphones/"

req=Request(url, headers={"User-Agent":"Mozilla/5.0"})

webpage=urlopen(req).read()

page_soup = soup(webpage,"html.parser")

containers = page_soup.findAll("div",{"class":"info"})

filename = "phoneprices.csv"
f = open(filename,"w")
headers="pro_name,price\n"
f.write(headers)


for container in containers:
	item_name=page_soup.findAll("h3","name")
	pro_name = item_name[0].text
	print(pro_name)

	pricing=page_soup.findAll("div","prc")
	price=pricing[0].text
	print(price)

	#reduction=page_soup.findAll("div","tag_dsct_sm")
	#discount=reduction[0].text
	#print("pro_name: " + pro_name)
	#print("price: " + price)

	f.write(pro_name.replace(",","|") + "," + price + "\n")

f.close()



#For looping through pages

for i in range(1, 907):     #Number of pages plus one
    url = "http://www.pga.com/golf-courses/search?page={}&searchbox=Course+Name&searchbox_zip=ZIP&distance=50&price_range=0&course_type=both&has_events=0".format(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")   #Can use whichever parser you prefer




import csv
import requests 
from bs4 import BeautifulSoup
url = "http://www.pga.com/golf-courses/search?searchbox=Course+Name&searchbox_zip=ZIP&distance=50&price_range=0&course_type=both&has_events=0"

s = requests.Session()
r = s.get(url)



