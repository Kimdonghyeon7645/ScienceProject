# -*- coding: utf-8 -*-
import pymysql
from bs4 import BeautifulSoup
import requests


pms = []
url2 = 'https://www.airkorea.or.kr/web/dustForecast?pMENU_NO=113'
html2 = requests.get(url2)
soup2 = BeautifulSoup(html2.text, 'html.parser')
contents2 = soup2.select("dl.forecast.MgT50")
for content2 in contents2:
    cols = content2.select("table.st_2 tbody tr")
    try:
        big_pm = cols[1].select("td")[6].text
    except IndexError:
        big_pm = '-999'
    # 미세먼지
    try:
        small_pm = cols[2].select("td")[6].text
    except IndexError:
        small_pm = '-999'
    # 초미세먼지
    pm = [big_pm, small_pm]
    pms.append(pm)


data = []
num = 1
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3020055000'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
contents = soup.select('data')
x = soup.find('x').text
y = soup.find('y').text
update_time = soup.find('tm').text[:-2]
now_hour = int(update_time[6:8])
for content in contents:
    hour = content.find('hour').text
    # 현재 시간 (3시간 간격, ex> 3, 6, 9, ...)
    today_plus_numder = content.find('day').text
    # 오늘(현재 날짜)로 부터 몇 일뒤(+) 인지 날짜 값 (오늘이면 0일뒤므로 = 0)
    temp = content.find('temp').text
    # 현재 온도 (섭씨 ℃)
    day_high_temp = content.find('tmx').text
    # 현재 날짜의 최고 온도 (오늘은 구하지 않음, -999)
    day_low_temp = content.find('tmn').text
    # 현재 날짜의 최저 온도 (오늘은 구하지 않음, -999)
    sky_state = content.find('sky').text
    # 현재 하늘의 상태, 구름의 정도 1~4로 표현(1:맑음, 2:구름적음, 3:구름많음, 4:흐림)
    weather_state = content.find('pty').text
    # 현재 기상현상 상태, 0: 맑음, 1: 비, 2: 진눈개비, 3: 눈, 4: 소나기
    weather_korean = content.find('wfkor').text
    # 현재 기상현상 상태 통틀어서 한글로
    rain_persent = content.find('pop').text
    # 현재 비올 확률 (백분위, %)
    expect_rain_6h = content.find('r06').text
    # 6시간 뒤까지의 예상 강수량
    expect_rain_12h = content.find('r12').text
    # 12시간 뒤까지의 예상 강수량
    expect_snow_6h = content.find('s06').text
    # 6시간 뒤까지의 예상 적설량
    expect_snow_12h = content.find('s12').text
    # 12시간 뒤까지의 예상 적설량
    wind_speed = str(round(float(content.find('ws').text), 2))
    # 현재 풍속
    wind_way = content.find('wd').text
    # 현재 풍향(8분위, ex> 0: 북, 2: 동, 4: 남, 6: 서)
    wind_korean = content.find('wden').text
    # 현재 풍향 한글로
    humi = content.find('reh').text
    # 현재 습도 (백분위, %)
    hour_data = [num, x, y, update_time, str(int(today_plus_numder)*24+int(hour)-now_hour), hour, temp,
                 day_high_temp, day_low_temp, sky_state, weather_state, weather_korean, rain_persent,
                 expect_rain_6h, expect_rain_12h, expect_snow_6h, expect_snow_12h, wind_speed, wind_way, wind_korean,
                 humi, pms[int(today_plus_numder)][0], pms[int(today_plus_numder)][1]]
    num += 1
    data.append(hour_data)

# conn = pymysql.connect(host='10.156.147.199', user='dupang', passwd='1234', db='mysql', charset='utf8')
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='kkddhh77887788@', db='mysql', charset='utf8')

cur = conn.cursor()
state = input("데이터 베이스 구축이 처음입니까? \n(그렇다면 y, 이미 데이터 베이스 구축을 실행했다면 y를 제외한 아무키를 입력하세요) "
              ": ")
# state = 'd'

if state is 'y':
    cur.execute("CREATE DATABASE project_data_DB;")
    cur.execute("USE project_data_DB")
    cur.execute(
        "CREATE TABLE data ( num TINYINT, x TINYINT, y TINYINT, update_time INT, time_ahead TINYINT, hour TINYINT, "
        "temp SMALLINT, day_high_temp SMALLINT, day_low_temp SMALLINT, sky_state TINYINT, weather_state TINYINT, "
        "weather_korean VARCHAR(6), rain_persent TINYINT, "
        "expect_rain_6h FLOAT, expect_rain_12h FLOAT, expect_snow_6h FLOAT, expect_snow_12h FLOAT, "
        "wind_speed FLOAT, wind_way TINYINT, wind_text CHAR(4), humi TINYINT, "
        "big_PM VARCHAR(6), small_PM VARCHAR(6), PRIMARY KEY(num) );")
    cur.executemany("INSERT INTO data (num, x, y, update_time, time_ahead, hour, temp, day_high_temp, day_low_temp, "
                    "sky_state, weather_state, weather_korean, rain_persent, expect_rain_6h, expect_rain_12h, "
                    "expect_snow_6h, expect_snow_12h, wind_speed, wind_way, wind_text, humi, big_PM, small_PM) "
                    "VALUES "
                    "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    data)
    conn.commit()
else:
    cur.execute("USE project_data_DB")

    for num in range(0, 18):
        cur.execute("USE project_data_DB")
        cur.execute("UPDATE data SET x = %s, y = %s, update_time = %s, time_ahead  = %s, hour = %s, temp = %s, "
                    "day_high_temp = %s, day_low_temp = %s, sky_state = %s, weather_state = %s, weather_korean = %s, "
                    "rain_persent = %s, expect_rain_6h = %s, expect_rain_12h = %s, expect_snow_6h = %s, "
                    "expect_snow_12h = %s, wind_speed = %s, wind_way = %s, wind_text = %s, humi = %s, "
                    "big_PM = %s, small_PM = %s WHERE num=%s",
                    (data[num][1], data[num][2], data[num][3], data[num][4], data[num][5],
                     data[num][6], data[num][7], data[num][8], data[num][9], data[num][10], data[num][11],
                     data[num][12], data[num][13], data[num][14], data[num][15],
                     data[num][16], data[num][17], data[num][18], data[num][19], data[num][20],
                     data[num][21], data[num][22], int(data[num][0]))
                    )
        conn.commit()
cur.close()
conn.close()
