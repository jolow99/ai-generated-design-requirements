import requests
from bs4 import BeautifulSoup
import csv
import os 
import pandas as pd 
 
# reading CSV file as dataframe and convert to list
df = pd.read_csv("links.csv")
links = df['links'].tolist()
stoplinks = ["https://www.delonghi.com/en/ec9355-bm-la-specialista-prestigio-manual-espresso-maker/p/EC9355.BM"]

for url in links: 
    print("Current URL:", url)
    model = url.split('/')[-1]
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    data, labels, values = {"model": model}, [], []
    
    if url not in stoplinks: 
        table = soup.find('div', attrs={'class': 'del-simple-css-accordion__content-desktop'})
    else: 
        # hot-fix for one product
        table = soup.find_all('div', attrs={'class': 'del-simple-css-accordion__content-desktop'})[1]

    for label in table.findAll('span', attrs = {'class':"del-pdp__specifications__single__label"}):
        if label.string == "Dimensions (wxdxh-mm) without filter holder" or label.string == "Dimensions (wxdxh)": 
            label.string = "Dimensions (wxdxh) (mm)"
        if label.string == "Pump pressure":
            label.string = "Pump pressure (bar)"
        if label.string == "Max cup height (mm)":
            label.string = "Maximum cup height (mm)"
        labels.append(label.string)
    for value in table.findAll('span', attrs = {'class':"del-pdp__specifications__single__value"}):
        if value.string != None: 
            print("Value:",value)
            values.append(value.string.strip())
        else: 
            print("Value:",value)
            energy_class = value.i["class"][-1]
            energy_class_label = energy_class[-1]
            print(energy_class_label)
            values.append(energy_class_label)
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