import csv
import os.path

import requests
from lxml import html

def get_book_info_url(book_info_url):
    response = requests.get(book_info_url)
    response.encoding = "utf-8"
    doc = html.fromstring(response.text)

    book_name = doc.xpath("//*[@id=\"content_inner\"]/article/div[1]/div[2]/h1/text()")
    # print(book_name)

    book_price = doc.xpath("//*[@id=\"content_inner\"]/article/div[1]/div[2]/p[1]/text()")
    # print(book_price)

    book_description = doc.xpath("//*[@id=\"content_inner\"]/article/p/text()")
    # print(book_description)

    book_message = {
        "书名": book_name[0].strip() if book_name else None,
        "价格": book_price[0].strip() if book_name else None,
        "简介": book_description[0].strip() if book_name else None
    }

    return book_message


def save_book_messages(book_messages):
    if not os.path.exists("./data"):
        os.makedirs("./data")

    with open("./data/book_messages.csv", "w",encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["书名", "价格","简介"])
        writer.writeheader()
        writer.writerows(book_messages)

def main():

    url = "https://books.toscrape.com/"

    response = requests.get(url)

    document = html.fromstring(response.text)
    # print(document)

    # name = document.xpath("//*[@id=\"default\"]/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a/text()")
    # print(name)

    # 获取图书列表信息
    books_list = document.xpath("//*[@id=\"default\"]/div/div/div/div/section/div[2]/ol/li")
    # print(books_list)

    book_messages = []

    # 遍历图书列表中的的每一本书的 url信息
    for book in books_list:
        book_url = book.xpath("./article/div[1]/a/@href")
        # print(book_url)
        # 拼接网址 获取到每本书额详情页面路径
        book_info_url = url + book_url[0]
        # print(book_info_url)

        book_info = get_book_info_url(book_info_url)
        book_messages.append(book_info)
        # print(book_info)

        save_book_messages(book_messages)

if __name__ == '__main__':
    main()
