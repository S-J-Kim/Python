from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

opt = Options()
opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")

path='D:\PY\Python\Study\drv.exe'
driver = webdriver.Chrome(chrome_options=opt, executable_path=path)
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

noti = driver.find_elements_by_class_name("no_loading")
print(noti)