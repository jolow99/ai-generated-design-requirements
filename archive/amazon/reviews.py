from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def extract_record(item):
    # print("Item: ", item)
    print("Item: ", item)
    print("Item Type: ", type(item))
    title = item.find('a', {'data-hook': 'review-title'})
    print("Title:", title)
    # stars = item.find('i', {'data-hook': 'cmps-review-star-rating'})
    # print("Stars:", stars)
    # print("type Stars:", type(stars))
    # if stars: 
    #     rating = stars.find('span', {'class': 'a-icon-alt'}).text
    #     print(rating)
    #     print(type(rating))
    #     print("/n")
    # profile = item.find('span', 'a-profile-name').text.strip()
    # rating = item.find('div','a-row').text.strip()[len(profile):len(profile)+3]
    # title = item.find('a','a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold').text.strip()
    # review = item.find('span','a-size-base review-text review-text-content').text.strip()    
    # review_date = item.find('span','a-size-base a-color-secondary review-date').text.strip()
    # date = review_date[review_date.index('on')+3:]
    # result = (title, profile, date, rating,  product_size, verified_purchase, review)
    return None

def get_url(ASIN):
    template = 'https://www.amazon.com/product-reviews/{}/ref=cm_cr_getr_d_paging_btm_next_3?sortBy=recent'
    url = template.format(ASIN)
    url += '&pageNumber={}'
    return url

def main(ASIN):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    records = []
    url = get_url(ASIN)
    for page in range(1, 11):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-hook': 'review'})
        for item in results:
            record = extract_record(item)
            # if record:
            #     records.append(record)
        time.sleep(3)
    driver.close()
    
    # # save data to csv file
    # with open(ASIN +'.csv', 'w', newline='', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['Title', 'Profile', 'Date', 'Rating', 'ProductSize', 'Verified_Purchase', 'Review'])
    #     writer.writerows(records)

ASINs = {'B003UMHO8G'}
for ASIN in ASINs:
    main(ASIN)