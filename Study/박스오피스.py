import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def PlayTrailerOnYoutube(name_of_movie):
    
    
    driver.get('https://www.youtube.com')
    time.sleep(1)

    input_element = driver.find_element_by_name("search_query")
    time.sleep(1)

    input_element.send_keys(name_of_movie + " 예고편")
    input_element.submit()
    time.sleep(1)

    continue_link = driver.find_elements_by_partial_link_text("예고편")
    continue_link[0].click()

def WatchMovieTrailer(movie_list):
    print("========== 박스오피스 현황 ==========")
    
    for i in range(len(movie_list)):
        print(f'{i+1}위 : {movie_list[i]}')
    
    selection = int(input("어떤 영화의 예고편을 보겠습니까? : "))

    if not 1 <= selection <= 10: print("잘못된 입력"); return
    else: PlayTrailerOnYoutube(movie_list[selection - 1])

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=영화'
res = requests.get(url).text
soup = BeautifulSoup(res, "html.parser")

movie_name = soup.select("ul.thumb_list > li > dl > dt > a")
grade = soup.select("dd > span.point_num")

chart = [movie_name[i].text for i in range(len(movie_name))]

driver = webdriver.Chrome("D:\PY\Python\Day 4\chromedriver.exe")
WatchMovieTrailer(chart)
