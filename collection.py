from bs4 import BeautifulSoup

import os
import pandas as pd

d = {'title': [], 'price': [], 'link': []}

for  file in os.listdir("data"):
    try:
    
     with open(f"data/{file}") as f:
        html_doc = f.read()
        
     soup = BeautifulSoup(html_doc, 'html.parser')
     t = soup.find("h2")
     l = soup.find("a")
     p = soup.find("span", attrs = {"class": "a-price-whole"})
     title = t.get_text()
     link = "https://amazon.in/" + l['href']
     price = p.get_text()
    
    
    
     d["title"].append(title)
     d["price"].append(price)
     d["link"].append(link)
     
    except Exception as e:
        print(e)
         
    
    
df= pd.DataFrame(data=d)
df.to_csv("data.csv")

    