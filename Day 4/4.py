# 웹 사이트 접속 후 검색하기, 페이지 열기
# -*- coding: utf-8 -*-

import time
from selenium import webdriver

# Chrome WebDriver를 이용해 Chrome을 실행한다.
driver = webdriver.Chrome("chromedriver.exe")

# www.google.com으로 이동한다.
driver.get("https://www.youtube.com")
time.sleep(4)

# html element 이름이 "q"인 것을 찾는다. (검색창)
input_element = driver.find_element_by_name("q")
time.sleep(1)

# 검색창에 "www.ngle.co.kr"을 입력한다.
input_element.send_keys("멜론 1월 1주차")
time.sleep(1)

# 검색 내용을 보낸다.
input_element.submit()
time.sleep(1)

# 검색된 내용 중 링크 텍스트에 "THE BEST BUSINESS PLAN" 이 포함된 것을 찾는다.
continue_link = driver.find_element_by_partial_link_text("1월")
time.sleep(1)

# 해당 링크를 클릭한다.
continue_link.click()
time.sleep(3)

driver.quit()
