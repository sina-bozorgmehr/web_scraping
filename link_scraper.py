#!/usr/bin/env python
# coding: utf-8

# In[8]:


# importing libraries

import requests
from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re
import csv


# getting the content of the "Current Estimates" webpage

url = 'https://www.census.gov/programs-surveys/popest.html'

content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, 'lxml')
print(soup)


# finding all the links and making all of them absolute URIs

link_list =[]
for link in soup.find_all('a', href=True):
    if link.get('href').startswith('#'):
        continue
    elif link.get('href').startswith('/'):
        link_list.append('https://www.census.gov'+link.get('href'))
    else:
        link_list.append(link.get('href'))
    
for link in link_list:
    print(link)
   

# making sure that all the retrieved links are relocating to a HTML page using RegEx.

pattern1 = re.compile(r'/[a-zA-Z0-9-]*$')
pattern2 = re.compile(r'.html$')
cleaned_link_list = []

for link in link_list:
    a = pattern1.search(link)
    b = pattern2.search(link)
    if a or b != None:
        cleaned_link_list.append(link)

for link in cleaned_link_list:
    print(link)

    
# removing the duplicate links

print("Number of links before removing the duplicates:\n",len(cleaned_link_list))

cleaned_link_list = list(set(cleaned_link_list))

print("Number of links after removing the duplicates:\n",len(cleaned_link_list))


# writing the links into a csv file

import csv

with open ('links.csv', 'w', newline ='') as csvfile:
    file_writer = csv.writer(csvfile, delimiter=',')
    for link in cleaned_link_list:
        file_writer.writerow([link])


# In[ ]:




