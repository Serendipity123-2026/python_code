import csv

import requests
from lxml import html

url = "http://localhost:63342/pythonProject/Chapter%204/resources/%E4%B9%A6%E5%9F%8E.html?_ijt=drfr9iacnl9fv2jfeqn4270kci&_ij_reload=RELOAD_ON_SAVE"

response = requests.get(url, timeout=60)
response.encoding = "utf-8"
document = html.fromstring(response.text)

# book_list = document.xpath("//*[@id=\"book_list\"]/tbody/tr")
# for book_messages in book_list:
#     book_name = book_messages.xpath("./td[@class='name']/a/text()")
#     print(book_name)
#     # book_author =

#
# book_message_list = []
# book_message_list.append(book_name)
# book_message_list.append(book_author)
# book_message_list.append(book_publish)
# book_message_list.append(book_year)
# book_message_list.append(book_price)
# book_message_list.append(book_type)
# book_message_list.append(content_list)
# print(book_message_list)
def main():

    book_name = document.xpath("//td[@class='name']/a/text()")

    book_author = document.xpath("//*[@id=\"book_list\"]/tbody/tr/td[2]/text()")

    book_publish = document.xpath("//*[@id=\"book_list\"]/tbody/tr/td[3]/text()")

    book_year = document.xpath("//*[@id=\"book_list\"]/tbody/tr/td[4]/text()")

    book_price = document.xpath("//*[@id=\"book_list\"]/tbody/tr/td[5]/text()")

    book_type = document.xpath("//*[@id=\"book_list\"]/tbody/tr/@data-cate")

    content_list = []
    content_url = document.xpath("//td[@class='name']/a/@href")
    for lianjie in content_url:
        book_content = url + lianjie
        content_list.append(book_content)

    with open("E:\AI智能应用开发\code\The first stage\pythonProject\Chapter 4\data/messages.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["字段", "类型", "说明"])
        writer.writeheader()
        writer.writerow({"字段": "书名", "类型": "str", "说明": book_name})
        writer.writerow({"字段": "作者", "类型": "str", "说明": book_author})
        writer.writerow({"字段": "出版社", "类型": "str", "说明": book_publish})
        writer.writerow({"字段": "出版年", "类型": "int", "说明": book_year})
        writer.writerow({"字段": "价格", "类型": "float", "说明": book_price})
        writer.writerow({"字段": "分类", "类型": "str", "说明": book_price})
        writer.writerow({"字段": "详情", "类型": "str", "说明": content_list})


if __name__ == '__main__':
    main()
