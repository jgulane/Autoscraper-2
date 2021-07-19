#!/usr/bin/env python
# coding: utf-8

# In[110]:


import requests
from bs4 import BeautifulSoup


# In[111]:


response = requests.get('https://reliefweb.int/updates?advanced-search=%28PC188%29')
doc = BeautifulSoup(response.text, 'html.parser')


# In[112]:


articles = doc.select(".report.with-summary")
for article in articles:
    print("-----")
    print(article.select_one(".title").text)
    print(article.select_one(".content").text)
     


# In[118]:


articles = doc.select(".report.with-summary")

for article in articles:
    print("-----")
    row = {}
    row['title'] = article.select_one(".title").text
    row['content'] = article.select_one(".content").text
    rows.append(row)
rows


# In[114]:


df = pd.DataFrame(rows)
df


# In[116]:


df.to_csv("emergency_reports.csv")


# In[ ]:




