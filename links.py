import requests
from bs4 import BeautifulSoup
import pandas as pd 

# series = {
#     "Magnifica Evo": "https://www.delonghi.com/en/products/coffee/c/coffee?q=%3Arelevance%3Aseries%3AMagnifica%2BEvo",
#     "VertuoNext": "https://www.delonghi.com/en/products/coffee/c/coffee?q=%3Arelevance%3Aseries%3AVertuoNext",
#     "Dedica": "https://www.delonghi.com/en/products/coffee/c/coffee?q=%3Arelevance%3Aseries%3ADedica",
#     "Manual espresso makers": "https://www.delonghi.com/en/products/coffee/c/coffee?q=%3Arelevance%3Aseries%3AManual%2Bespresso%2Bmakers",
#     "Clessidra Filter coffee makers": "https://www.delonghi.com/en/products/coffee/c/coffee?q=%3Arelevance%3Aseries%3AFilter%2Bcoffee%2Bmakers",
# }


url = "https://www.delonghi.com/en/products/coffee/c/coffee?q=%3Arelevance%3Aseries%3AMagnifica%2BEvo%3Aseries%3AVertuoNext%3Aseries%3ADedica%3Aseries%3AManual%2Bespresso%2Bmakers%3Aseries%3AFilter%2Bcoffee%2Bmakers%3Aseries%3AMagnifica%2BS%3Aseries%3AAutomatic%2Bcoffee%2Bmakers%3Aseries%3ADinamica%2BPlus%3Aseries%3AIcona%2BVintage%3Aseries%3AMagnifica%3Aseries%3APrimaDonna%2BSoul%3Aseries%3ACombi%2Bcoffee%2Bmakers%3Aseries%3ADinamica%3Aseries%3AMagnifica%2BS%2BSmart%3Aseries%3AGran%2BLattissima%3Aseries%3AIcona%2B%2526%2BDedica%2BMetallics%3Aseries%3ALa%2BSpecialista%3Aseries%3ALattissima%2BOne%3Aseries%3APerfecta%2BEvo%3Aseries%3APrimaDonna%2BElite%3Aseries%3APerfecta%2BDeluxe%3Aseries%3APrimaDonna%2BClass%3Aseries%3AActive%2BLine%3Aseries%3AEletta%3Aseries%3AEletta%2BCappuccino%2BEvo%3Aseries%3ALattissima%2BPro"

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
