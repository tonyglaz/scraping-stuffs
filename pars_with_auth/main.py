from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

work = Session()

work.get("https://quotes.toscrape.com/", headers=headers)
response = work.get("https://quotes.toscrape.com/login", headers=headers)
soup = BeautifulSoup(response.text, "lxml")
token = soup.find("form").find("input").get("value")
data = {"csrf_token": token, "username": "petya", "password": "petyapass"}
result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)
print(result.text)

# как остановить парсинг данных когда неизвестно сколько у тебя страниц:
# result = soup.find_all("span", class_="text")
# author = soup.find_all("small", class_="author")
#     if len(result) != 0:
#
#     else:
#         break
