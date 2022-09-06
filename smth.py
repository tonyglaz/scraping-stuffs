import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}


def get_url():
    for count in range(1, 8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"  # отправляем запрос на сайт и получаем html код count-страницы каталога с отварами
        response = requests.get(url,
                                headers=headers)  # отправляем запрос на сайт и получаем html код count-страницы каталога с отварами (в response лежит ответ сайта)
        soup = BeautifulSoup(response.text,
                             "lxml")  # lxml - анализатор html кода помогающий парсить наш response,в переменную soup получили уже обработанный html код страницы
        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")  # получили список всех карт на странице

        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url
            # name = i.find("h4", class_="card-title").text.strip()
            # price = i.find("h5").text
            # url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get(
            #     "src")  # метод get - получить содержимое атрибута
            #
            # print(name + '\n' + price + '\n' + url_img + '\n\n')


def run_function():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)  # запрос отдельно на каждую карту товара
        soup = BeautifulSoup(response.text,
                             "lxml")
        data = soup.find("div", class_="card mt-4 my-4")
        name = data.find("h3", class_="card-title").text
        price = data.find("h4").text
        text = data.find("p", class_="card-text").text
        url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
        yield name, price, text, url_img
