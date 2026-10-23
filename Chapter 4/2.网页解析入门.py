import requests
from lxml import html

with open("resources/书城.html", "r", encoding="utf-8") as f:
    file_txt = f.read()


document = html.fromstring(file_txt)

list_a= document.xpath("//table/tbody/tr")
for list in list_a:
    item = list.xpath("./td/text()")

    print(item)