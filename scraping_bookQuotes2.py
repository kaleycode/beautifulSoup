from bs4 import BeautifulSoup
import requests
url = "https://murder-mayhem.com/sherlock-holmes-quotes"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all('p')
for quote in quotes:
    print(quote.text)
    print()
