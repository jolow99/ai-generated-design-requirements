import requests
from bs4 import BeautifulSoup
import csv
import os 
import pandas as pd 
 
# reading CSV file as dataframe and onvert to list
df = pd.read_csv("links.csv")
links = df['links'].tolist()

for url in links: 
    print("Current URL:", url)
    model = url.split('/')[-1]
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    data, labels, values = {"model": model}, [], []
    table = soup.find('div', attrs={'class': 'del-simple-css-accordion__content-desktop'})
    for label in table.findAll('span', attrs = {'class':"del-pdp__specifications__single__label"}):
        labels.append(label.string)
    for value in table.findAll('span', attrs = {'class':"del-pdp__specifications__single__value"}):
        values.append(value.string.strip())
    for i in range(len(labels)):
        data[labels[i]] = values[i]

    # Create directory if it does not eixst
    if not os.path.exists('consolidated'):
        os.makedirs('consolidated')

    # Create csv file 
    with open(f'consolidated/{model}.csv', 'w', newline='') as f:
        w = csv.DictWriter(f,data.keys())
        w.writeheader()
        w.writerow(data)
        
    print("Done with", model)
    print("")