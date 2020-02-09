from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

# 여러개의 파일과 폴더를 처리하기 위해 재귀호출을 사용
# 이미 처리한 파일인지 확인하기 위해 변수 선언 (dictionary)
proc_files = {}

# HTML 내부의 링크를 추출한다
def enum_links(html, base):
    soup = BeautifulSoup(html, "lxml")
    links = soup.select('link[rel="stylesheet"]')  # CSS
    links += soup.select("a[href]")  # 링크속성
    
    result = []

    # href 속성을 추출하고, 링크를 절대경로로 변환
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)

    return result

# 파일을 다운로드하고 저장
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath):  # 만약 대상이 폴더라면 index.html
        savepath += "index.html"
        
    savedir = os.path.dirname(savepath)
    
    # 대상 모두가 다운로드 되었는지 확인
    if os.path.exists(savepath):
        return savepath
    
    # 다운로드할 폴더를 생성
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)

    # 파일 다운로드 : 예외처리
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1)
        return savepath

    except:
        print("download failed : ", url)
        return None

# HTML 분석하고 다운로드하기
def analyze_html(url, root_url):
    savepath = download_file(url)
    
    if savepath is None:
        return
    if savepath in proc_files:
        return  # 이미 처리한 파일인 경우 아무것도 안함

    proc_files[savepath] = True
    print('analyze html : ', url)

    # 링크 추출
    html = open(savepath, "r", encoding='utf-8').read()
    links = enum_links(html, url)

    for link_url in links:
        # 링크가 루트 이외의 다른 경로인 경우 무시
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url):
                continue
        
        # 만약 HTML일 경우
        if re.search(r'.(html|htm)$', link_url):
            # 재귀적으로 HTML 파일 분석하기
            analyze_html(link_url, root_url)
            continue

        # 기타 파일인 경우
        download_file(link_url)

if __name__ == "__main__":
    # url에 있는 모든 파일들 다운로드하기
    url = 'https://docs.python.org/ko/3.8/library/'
    analyze_html(url, url)

        