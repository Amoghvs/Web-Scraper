# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:31:43 2020

@author: Amogh
"""

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

#grabbing the page
uClient=uReq(url)
page_html=uClient.read()
uClient.close()


#html parsing
page_soup=soup(page_html,"html.parser")

#header of the page
#page_soup.h1 
#page_soup.p
#age_soup.body.span


containers=page_soup.findAll("div",{"class":"item-container"})
containers[0]


container=containers[0]
#name=container.findAll("a",{"class":"item-title"})

out_filename = "graphics_cards.csv"
# header of csv file to be written
headers = "brand,product_name,shipping \n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)


for container in containers:
    brand_container=container.findAll("div",{"class":"item-branding"})
    brand= brand_container[0].a.img["title"]
    title_container=container.findAll("a",{"class":"item-title"})
    product_name=title_container[0].text

    shipping_container=container.findAll("li",{"class":"price-ship"})
    shipping=shipping_container[0].text.strip()

    print("brand: " + brand + "\n")
    print("product_name: " + product_name + "\n")
    print("shipping: " + shipping + "\n")

    f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")

f.close() 
