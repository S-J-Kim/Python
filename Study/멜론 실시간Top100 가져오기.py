import MySQLdb
import requests
from bs4 import BeautifulSoup

# 멜론은 user-agent를 변경해서 써야 parsing이 가능
headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57'}

url = "https://www.melon.com/chart/index.htm"
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res, "lxml")

song_name = soup.select("#lst50 > td > div > div > div.ellipsis.rank01 > span > a")
artist_name = soup.select("#frm > div > table > tbody > tr > td > div > div > div.ellipsis.rank02")
album_name = soup.select("#lst50 > td > div > div > div.ellipsis.rank03 > a")

for i in range(len(artist_name)):
    artist_name[i] = artist_name[i].select("div > a")
    for j in range(len(artist_name[i])):
        artist_name[i][j] = artist_name[i][j].text


for i in range(len(song_name)):
    song_name[i] = song_name[i].text
    
for i in range(len(album_name)):
    album_name[i] = album_name[i].text

for i in range(len(artist_name)):
    artist_name[i] = ', '.join(artist_name[i])

for i in range(len(album_name)):
    print(f'{song_name[i]} / {artist_name[i]} / {album_name[i]}')

# con = MySQLdb.connect(host='localhost', port=3306, db='mydb', user='root', passwd='root', use_unicode=True, charset='utf8')
# c = con.cursor()

# for i in range(len(song_name)):
#     data = [i, song_name[i], artist_name[i], album_name[i]]
#     c.execute("""INSERT INTO chart200122 VALUES (%s, %s, %s, %s);""", data)

# con.commit()
