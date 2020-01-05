# 환율 계산 크롤링

from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("div.head_info > span.value").string
print("USD/KRW = ", price)
