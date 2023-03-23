from bs4 import BeautifulSoup
import requests


site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, "html.parser")

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

print(temperatura)
print(soup.title.string)
