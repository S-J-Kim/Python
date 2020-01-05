# 웹 사이트 접속하기
import webbrowser

naver_search_url = 'https://search.naver.com/search.naver?query='  # 네이버 기본 검색 주소
daum_seacrh_url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q='
nate_search_url = 'https://search.daum.net/nate?thr=sbma&w=tot&q='
google_search_url = 'https://www.google.com/#q='

search_url = [naver_search_url, daum_seacrh_url, nate_search_url, google_search_url]
search_list = ["이천 쌀", "이천 반도체", "이천 도자기", "이천 복숭아"]

i = 0

for url in search_url:
    for word in search_list:
        if search_list[i] == word:
            webbrowser.open_new(url + word)
    i += 1

'''
for url, keyword in zip(search_url, search_list): 
    webbrowser.open(url + keyword)
'''
