import requests
from bs4 import BeautifulSoup
import csv
import os 

urls = [
    "https://www.delonghi.com/en/ecam21-117-sb-magnifica-s-bean-to-cup-coffee-machines/p/ECAM21.117.SB"
    "https://www.delonghi.com/en/ecam22-110-sb-magnifica-s-automatic-coffee-maker/p/ECAM22.110.SB",
    "https://www.delonghi.com/en/ecam22-110-b-magnifica-s-automatic-coffee-maker/p/ECAM22.110.B",
    "https://www.delonghi.com/en/ecam21-117-b/p/ECAM21.117.B", 
    ]
for url in urls: 
    model = url.split('/')[-1]
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    data = {}
    labels = []
    values = []
    table = soup.find('div', attrs={'class': 'del-simple-css-accordion__content-desktop'})
    for label in table.findAll('span', attrs = {'class':"del-pdp__specifications__single__label"}):
        labels.append(label.string)
    for value in table.findAll('span', attrs = {'class':"del-pdp__specifications__single__value"}):
        values.append(value.string.strip())
    for i in range(len(labels)):
        data[labels[i]] = values[i]

    if not os.path.exists('output'):
        os.makedirs('output')

    filename = f'output/{model}.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['specification', 'data'])
        w.writeheader()
        for k, v in data.items():
            w.writerow({'specification': k, 'data': v})