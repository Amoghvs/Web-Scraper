# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:50:16 2020

@author: Amogh
"""

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
import re


#url="https://www.futurelearn.com/courses?filter_category=open&filter_course_type=open&filter_availability=started&all_courses=1"
#grabbing the page
#uClient=uReq(url)
#page_html=uClient.read()
#uClient.close()

from urllib.request import Request, urlopen

req = Request('https://www.futurelearn.com/courses?filter_category=open&filter_course_type=open&filter_availability=started&all_courses=1', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()


#html parsing
page_soup=soup(webpage,"html.parser")


containers=page_soup.findAll("div",{"class":"m-card Container-wrapper_GWW4X Container-grey_3ORsI"})
containers[0]
len(containers)



container=containers[0]
container

extracted_records = []
for container in containers:
    university_container=container.findAll("div",{"class":"label-wrapper_1cWTL"})
    university=university_container[0].span.text
    
    title_container=container.findAll("div",{"class":"Title-wrapper_3GPPt"})
    title=title_container[0].h4.text

    desc_container=container.findAll("p",{"class":"text-wrapper_osDIP text-mediumGrey_iJRmO text-sBreakpointSizexsmall_1urEo text-sBreakpointAlignmentleft_1CA1S text-isRegular_1-QX9"})
    desc=desc_container[0].text
       
    for div in container.findAll("div", text=re.compile('..week.')):
        #print(div.text)
        dur=div.text  
    for div2 in container.findAll("div", text=re.compile('. hrs per week$')):
        #print(div2.text)
        eff=div2.text  
    for div3 in container.findAll("div", text=re.compile("^Free digital upgrade$|^Included in Unlimited$|^Premium course$")):
        #print(div3.text)   
        price=div3.text
        
    record={
         'University':university,
         'Title':title,
         'Description':desc,
         'Duration':dur,
         'Effort':eff,
         'Cost':price
         }   
    extracted_records.append(record)
#print(extracted_records)
    

with open('data.json', 'w') as outfile:
    json.dump(extracted_records, outfile)
 

    