# Build a simple web scraper with python.

import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.simpleweb.org/")


soup = BeautifulSoup(res.content, "html.parser")
search = soup.find("table", class_="mainContent")
content = search.find_all("p")

print(content)
