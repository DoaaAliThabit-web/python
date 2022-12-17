import requests
from bs4 import BeautifulSoup as bs
import csv
from itertools import zip_longest

book_title = []
cover = []
price = []
shipping = []
Evaluation = []
Type = []
url = requests.get("https://www.amazon.eg/s?k=books+for+girls&i=stripbooks&crid=3B4D73BNWCD53&qid=1671261201&sprefix=books%2Cstripbooks%2C130&ref=sr_pg_1")
soup = bs(url.text, "html.parser")

book_titles = soup.find_all("span", {"class": "a-size-medium a-color-base a-text-normal"})
Cover_type = soup.find_all("a", {"class": "a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold"})
evaluation = soup.find_all("a", {"class": "a-popover-trigger a-declarative"})
The_price = soup.find_all("span", {"class": "a-offscreen"})
Shipping = soup.find_all("div", {"class": "a-row a-size-base a-color-secondary s-align-children-center"})
for i in range(len(book_titles)):
    book_title.append(book_titles[i].text)
    cover.append(Cover_type[i].text)
    price.append(The_price[i].text.replace("\u200f","").replace("\xa0",""))
    Evaluation.append(evaluation[i].text)
    Type.append("Book For Girls")
for i in range(len(Shipping)):
    shipping.append(Shipping[i].text.replace("احصل عليه غداً، 18 ديسمبر","").replace("احصل عليه الاثنين, 19 ديسمبر - الثلاثاء, 20 ديسمبر", "").replace("احصل عليه الثلاثاء, 20 ديسمبر - الأربعاء, 21 ديسمبر", "").replace("\u200f","").replace("\xa0",""))
print(Type)
file_list = [book_title, cover, price, shipping, Evaluation, Type]
doaa = zip_longest(*file_list)
with open("D:/Document.csv", "w", encoding="utf-8") as d:
    wr = csv.writer(d)
    wr.writerow(["Book Name", "Cover Type", "The Price", "Shipping", "Evaluation", "BooKs For...."])
    wr.writerows(doaa)
