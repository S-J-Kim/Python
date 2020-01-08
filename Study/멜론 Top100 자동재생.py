# 웹 사이트 접속 후 검색하기, 페이지 열기
# -*- coding: utf-8 -*-

import time
import datetime
from selenium import webdriver

# Chrome WebDriver를 이용해 Chrome을 실행한다.
driver = webdriver.Chrome("D:\PY\Python\Day 4\chromedriver.exe")

# www.youtube.com으로 이동한다.
driver.get("https://www.youtube.com")
time.sleep(1)

# html element 이름이 "search_query"인 것을 찾는다. (검색창)
input_element = driver.find_element_by_name("search_query")
time.sleep(1)

# 오늘 날짜를 계산한다
d = str(datetime.datetime.now().day)  
m = str(datetime.datetime.now().month)
query = m + '월' + d + '일 멜론'
query2 = m + '월' + d

# 검색창에 "{month}월 {day}일 멜론"을 입력한다.
input_element.send_keys(query)
#ime.sleep(1)

# 검색 내용을 보낸다.
input_element.submit()
time.sleep(1)

# 검색된 내용 중 링크 텍스트에 "{month}월 {day}일" 이 포함된 것을 찾는다.
continue_link = driver.find_element_by_partial_link_text(query2)
#time.sleep(1)

# 해당 링크를 클릭한다.
continue_link.click()

