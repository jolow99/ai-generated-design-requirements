import requests
from bs4 import BeautifulSoup
import pandas as pd 

# Using Selenium
data = open('DS.html','r', encoding ="utf-8")
soup = BeautifulSoup(data, 'html5lib')

table = soup.find_all('a', attrs={'class': 'js-gtm-product-click'})

links = []
stoplinks = ["https://www.delonghi.com/en/kg521-m-dedica-electric-coffee-grinder/p/KG521.M"]

for row in table:
    link = "https://www.delonghi.com" + row.get('href')
    if link not in stoplinks and link not in links:
        links.append(link)

# Write to CSV file by creating a dataframe
df = pd.DataFrame({"links": links})
df.to_csv("links2.csv", index=False)

