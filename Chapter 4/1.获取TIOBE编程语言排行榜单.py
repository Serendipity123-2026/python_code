# 导入 requests包
import requests
from lxml import html
# 定义爬取数据的网页路径
url = "https://www.tiobe.com/tiobe-index"

# 使用 requests发送 http请求  请求方式：get
response = requests.get(url)

document = html.fromstring(response.text)

# 获取表头信息
table_header = document.xpath("//table[@id='top20']/thead/tr/th/text()")
print(table_header)

# 获取列表信息
form_list = document.xpath("//table[@id='top20']/tbody/tr")
for form in form_list:
    form_list_message = form.xpath("./td/text()")
    print(form_list_message)