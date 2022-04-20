from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.delonghi.com/en/products/coffee/c/coffee?q=%3Arelevance%3Aseries%3AMagnifica%2BEvo%3Aseries%3AVertuoNext%3Aseries%3ADedica%3Aseries%3AManual%2Bespresso%2Bmakers%3Aseries%3AFilter%2Bcoffee%2Bmakers%3Aseries%3AMagnifica%2BS%3Aseries%3AAutomatic%2Bcoffee%2Bmakers%3Aseries%3ADinamica%2BPlus%3Aseries%3AIcona%2BVintage%3Aseries%3AMagnifica%3Aseries%3APrimaDonna%2BSoul%3Aseries%3ACombi%2Bcoffee%2Bmakers%3Aseries%3ADinamica%3Aseries%3AMagnifica%2BS%2BSmart%3Aseries%3AGran%2BLattissima%3Aseries%3AIcona%2B%2526%2BDedica%2BMetallics%3Aseries%3ALa%2BSpecialista%3Aseries%3ALattissima%2BOne%3Aseries%3APerfecta%2BEvo%3Aseries%3APrimaDonna%2BElite%3Aseries%3APerfecta%2BDeluxe%3Aseries%3APrimaDonna%2BClass%3Aseries%3AActive%2BLine%3Aseries%3AEletta%3Aseries%3AEletta%2BCappuccino%2BEvo%3Aseries%3ALattissima%2BPro"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

ScrollNumber = 10
for i in range(1,ScrollNumber):
    driver.execute_script("window.scrollTo(1,50000)")
    time.sleep(3)

file = open('DS.html', 'w',encoding="utf-8")
file.write(driver.page_source)
file.close()

driver.close()




