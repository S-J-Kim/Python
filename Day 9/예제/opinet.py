from selenium import webdriver

driver = webdriver.Chrome(r'Day 9\예제\data\chromedriver.exe')

driver.get("http://www.opinet.co.kr")
driver.find_element_by_css_selector("#gnb_0_0").click()