import requests, bs4, folium, webbrowser, gmaps
import pandas as pd
from datetime import datetime
from haversine import haversine
from urllib.parse import urlencode, quote_plus, unquote

#전기차 충전소 운영정보 공공데이터 키 값, 필수 데이터값 입력
xmlUrl = 'http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList'

My_API_Key = unquote('your service key')
queryParams = '?' + urlencode(
    {
        quote_plus('ServiceKey') : My_API_Key, # 키값
        quote_plus('pageNo') : '1',            # 표시할 페이지 수(모든 데이터 비교하기 위해 한페이지에 모두 표시)
        quote_plus('numOfRows') : 1982         # 총 데이터 수 : 1982개
    }
)

response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')

rows = xmlobj.findAll('item')
columns = rows[0].find_all()
# 0 = 주유소 위치 string, 4 = stat, 8 = 위도, 9 = 경도

result_name = [] # 충전소 위치(string)
result_stat = [] # 충전 상태
goal = [] # 목적지 x,y 좌표
min1, min2, min3 = 1000000, 2000000, 3000000 # 두 지점 사이의 최솟값 1, 2, 3

# 구글맵으로 현 위치 좌표 불러옴
LOCATION_API_KEY = 'AIzaSyAUdKigcmQ314Ew7BlDD9ux2pxEE9PVSXg'
url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={LOCATION_API_KEY}'
data = {
    'considerIp': True,
}
result_now = requests.post(url, data)
start = (result_now.json()['location']['lat'], result_now.json()['location']['lng']) # 현위치

for i in range(1982): # -1982개까지 최종 출력 목록
    columns = rows[i].find_all()
    result_name.append(columns[0].text)
    if columns[4].text == '1': result_stat.append('충전가능')
    elif columns[4].text == '2' : result_stat.append('충전중')
    elif columns[4].text == '3' : result_stat.append('고장/점검')
    elif columns[4].text == '4' : result_stat.append('통신장애')
    elif columns[4].text == '5' : result_stat.append('통신미연결')
    else: result_stat.append('x')
    goal.append((float(columns[8].text), float(columns[9].text)))

# 5번째 충전소까지의 충전상태 비교 >> 현 위치로부터 가장 가까운 충전소 위치, 좌표, 충전상태 표시
result_count = []
second1, second2, second3 = 0, 0, 0
for i in range(1982):
    if result_stat[i] != '충전가능': continue
    else:
        if haversine(start, goal[i]) < min3:
            if haversine(start, goal[i]) < min2:
                if haversine(start, goal[i]) < min1:
                    min3 = min2
                    second3 = second2
                    min2 = min1
                    second2 = second1
                    min1 = haversine(start, goal[i])
                    second1 = i
                elif haversine(start, goal[i]) > min1:
                    min3 = min2
                    second3 = second2
                    min2 = haversine(start, goal[i])
                    second2 = i
            elif haversine(start, goal[i]) > min2:
                min3 = haversine(start, goal[i])
                second3 = i

else:
    print(result_name[second1])
    print(goal[second1])
    print(result_stat[second1])
    print(result_name[second2])
    print(goal[second2])
    print(result_stat[second2])
    print(result_name[second3])
    print(goal[second3])
    print(result_stat[second3])

