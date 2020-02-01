from selenium import webdriver
import time

driver = webdriver.Chrome(r"Day 9\예제\data\chromedriver.exe")
driver.get("https://nid.naver.com/")

# 매크로 실행 시 마우스 포커스를 이동하면 안된다. 좌표가 달라짐

# driver.save_screenshot(r'Day 9\예제\naver1.png')

# xpath = """//*[@id="account"]/div/a/i"""

# driver.find_element_by_xpath(xpath).click()

elem_login = driver.find_element_by_id("id")
elem_login.clear()
elem_login.send_keys("hedro458")

elem_login = driver.find_element_by_id("pw")
elem_login.clear()
elem_login.send_keys("9712qwer@@")

time.sleep(2)

login_xpath = '//*[@id="log.login"]'
driver.find_element_by_xpath(login_xpath).click()

driver.get("http://mail.naver.com")

