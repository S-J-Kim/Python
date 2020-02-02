from selenium import webdriver

driver = webdriver.Chrome(r'Day 9\예제\data\chromedriver.exe')

driver.get("http://www.opinet.co.kr")
driver.get('http://www.opinet.co.kr/searRgSelect.do')