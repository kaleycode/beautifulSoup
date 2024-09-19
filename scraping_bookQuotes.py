from bs4 import BeautifulSoup
import requests

url = "https://bookroo.com/quotes/sherlock-holmes"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all('div', class_ = 'text-lg md:text-xl leading-[1.8] whitespace-pre-wrap break-words mb-4')
for quote in quotes:
    print(quote.text)
    print()
    print()
