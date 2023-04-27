from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

pages = requests.get(url)
pages.text
soup = BeautifulSoup(pages.text, 'lxml')
soup.div
print(soup)