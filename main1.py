import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.goldtraders.or.th/DailyPrices.aspx")

def checkNA(price,r):
    if price == "n/a":
        x = price ="0"
        return x
    else:
        x = price = td1[r].text[0:2]+td1[r].text[3:]
        return float(x)

soup = BeautifulSoup(r.content,"lxml")
ta1 = soup.find_all("table")
td1 = ta1[2].find_all("td")

#ทองคำแท่ง 96.5%
g1buy = td1[2].text#ราคารับซื้อ บาทละ
g1sale = td1[3].text#ราคาขาย บาทละ
g1b = checkNA(g1buy,2)
g1s = checkNA(g1sale,3)

#ทองรูปพรรณ 96.5%
g2buy = td1[6].text#ราคารับซื้อ บาทละ
g2sale = td1[7].text#ราคาขาย บาทละ
g2b = checkNA(g2buy,6)
g2s = checkNA(g2sale,7)

#วันที่
from datetime import datetime
da = soup.find("span",id="DetailPlace_lblAsDate")
str_stamp = da.text
datetime_obj = datetime.strptime(str_stamp, '%d/%m/%Y').date()
date = str(datetime_obj)

print("this is data of gold price" + date,g1b,g1s,g2b,g2s)
