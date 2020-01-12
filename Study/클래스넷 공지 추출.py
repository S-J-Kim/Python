from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd


path='D:\PY\Python\Study\drv.exe'
driver = webdriver.Chrome(path)
driver.get("http://www.hongik.ac.kr/login.do?Refer=https://cn.hongik.ac.kr/")

identifier = 'B611033'
password = '9712qwer##'

driver.implicitly_wait(5)

my_id = driver.find_element_by_name("USER_ID")
my_pw = driver.find_element_by_name("PASSWD")

my_id.send_keys(identifier)
my_pw.send_keys(password)

driver.find_element_by_xpath('\
    /html/body/div/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/table/tbody/tr/td[2]/div/form/div/div/div[2]/button' ).click()
    
driver.get("https://cn.hongik.ac.kr/stud/include/main.jsp")
notices = driver.find_elements_by_tag_name("#notice > ul > li > a")
date = driver.find_elements_by_tag_name("#notice > ul > li > span")


for i in range(len(notices)):
    notices[i] = notices[i].text
    date[i] = date[i].text

noti_data = {'notice': notices, 'date': date}
df = pd.DataFrame(noti_data, columns=noti_data.keys())

excel_writer = pd.ExcelWriter("클래스넷 공지목록.xlsx", engine='xlsxwriter')
df.to_excel(excel_writer, index=False)
excel_writer.save()

