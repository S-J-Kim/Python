import googlemaps
import pandas as pd

criminal_police = pd.read_csv(r'Day 9\예제\data\02. crime_in_Seoul.csv', thousands='.', encoding='euc-kr')
gmaps_key = "##########################"  # 발급받은 API KEY 입력
gmaps = googlemaps.Client(key=gmaps_key)

station_name = []

for name in criminal_police['관서명']: # 중부서 -> 서울중부경찰서 
    station_name.append('서울' + name[:-1] + '경찰서')
    
station_address = []
station_lat = [] #latitude
station_lng = [] #longitude

for name in station_name:
    tmp=gmaps.geocode(name, language='ko')
    station_address.append(tmp[0].get("formatted_address"))
    
    tmp_loc = tmp[0].get("geometry")
    
    station_lat.append(tmp_loc['location']['lat'])
    station_lng.append(tmp_loc['location']['lng'])
    
    print(f'{name} --> {tmp[0].get("formatted_address")}')
