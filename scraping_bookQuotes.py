from bs4 import BeautifulSoup
import requests
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.goodreads.com/work/quotes/7492217-the-complete-sherlock-holmes")
elem = driver.find_element(By.NAME, "q")

soup = BeautifulSoup(response.text, 'html.parser')

print(response.status_code)

'''for quote in quotes:
    print(quote.text) '''



#quotes = soup.find_all("div", attrs={"class" : "quoteText"})
#print(quotes)

#div class = "quoteText"
