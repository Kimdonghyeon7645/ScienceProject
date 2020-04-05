# -*- coding: utf-8 -*-
import pymysql
from bs4 import BeautifulSoup
import requests

data = []
num = 1
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3020055000'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
contents = soup.select('data')
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

    hour_data = [num, str(int(today_plus_numder)*24+int(hour)), hour, temp, day_high_temp, day_low_temp, sky_state,
                 weather_state, weather_korean, rain_persent, expect_rain_6h, expect_rain_12h, expect_snow_6h,
                 expect_snow_12h, wind_speed, wind_way, wind_korean, humi]
    num += 1
    data.append(hour_data)

# conn = pymysql.connect(host='10.156.147.199', user='dupang', passwd='1234', db='mysql', charset='utf8')
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='kkddhh77887788@', db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute("CREATE DATABASE project_data_DB;")
cur.execute("USE project_data_DB")
cur.execute("CREATE TABLE data ( num TINYINT, time_ahead TINYINT, hour TINYINT, temp SMALLINT, "
            "day_high_temp SMALLINT, day_low_temp SMALLINT, sky_state TINYINT, weather_state TINYINT, "
            "weather_korean VARCHAR(6), rain_persent TINYINT, "
            "expect_rain_6h FLOAT, expect_rain_12h FLOAT, "
            "expect_snow_6h FLOAT, expect_snow_12h FLOAT, "
            "wind_speed FLOAT, wind_way TINYINT, wind_text CHAR(4), humi TINYINT, PRIMARY KEY(num) );")
cur.executemany("INSERT INTO data (num, time_ahead, hour, temp, day_high_temp, day_low_temp, sky_state, weather_state, "
                "weather_korean, rain_persent, expect_rain_6h, expect_rain_12h, expect_snow_6h, expect_snow_12h, "
                "wind_speed, wind_way, wind_text, humi) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
conn.commit()
cur.close()
conn.close()
