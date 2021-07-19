#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


response = requests.get('https://reliefweb.int/updates?advanced-search=%28PC188%29')
doc = BeautifulSoup(response.text, 'html.parser')


# In[3]:


articles = doc.select(".report.with-summary")
for article in articles:
    print("-----")
    print(article.select_one(".title").text)
    print(article.select_one(".content").text)
     


# In[6]:


articles = doc.select(".report.with-summary")

rows = []
for article in articles:
    print("-----")
    row = {}
    row['title'] = article.select_one(".title").text
    row['content'] = article.select_one(".content").text
    rows.append(row)
rows


# In[8]:


import pandas as pd

df = pd.DataFrame(rows)
df


# In[9]:


df.to_csv("emergency_reports.csv")


# In[ ]:




