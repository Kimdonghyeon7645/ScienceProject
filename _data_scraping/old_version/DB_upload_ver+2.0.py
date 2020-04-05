# -*- coding: utf-8 -*-
"""
ver.3 : 장소를 대전광역시 구(대표하는 동)으로 5가지 위치 추가
"""
import pymysql
from bs4 import BeautifulSoup
import requests


def num_change(x):
    return {'좋음': '1', '보통': '2', '나쁨': '3', '매우나쁨': '4'}.get(x, 'NoneData')


def gu_numbering(x):
    return {'유성구': '1', '서구': '2', '중구': '5', '동구': '3', '대덕구': '4'}.get(x, 'NoneData')


pms = []
url2 = 'https://www.airkorea.or.kr/web/dustForecast?pMENU_NO=113'
html2 = requests.get(url2)
soup2 = BeautifulSoup(html2.text, 'html.parser')
contents2 = soup2.select("dl.forecast.MgT50")
for content2 in contents2:
    cols = content2.select("table.st_2 tbody tr")
    try:
        big_pm = num_change(cols[1].select("td")[6].text)
    except IndexError:
        big_pm = 'NoneData'
    # 미세먼지
    try:
        small_pm = num_change(cols[2].select("td")[6].text)

    except IndexError:
        small_pm = 'NoneData'
    # 초미세먼지
    pm = [big_pm, small_pm]
    pms.append(pm)


all_data = []
num = 1
urls = ['http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3020055000',  # 유성구 (신성동)
        'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3017059700',  # 서구 (관저동)
        'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3014074000',  # 중구 (산성동)
        'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3023060000',   # 대덕구 (법동)
        'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3011062000'   # 동구 (가양동)
        ]

for url in urls:
    data = []
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    gu = soup.find('title').text.split(' ')[-3]
    area = gu_numbering(gu)
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
        weather_english = content.find('wfen').text    # 알파벳 대문자는 오류남
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
        hour_data = [num, area, x, y, update_time, str(int(today_plus_numder) * 24 + int(hour) - now_hour), hour, temp,
                     day_high_temp, day_low_temp, sky_state, weather_state, weather_english, rain_persent,
                     expect_rain_6h, expect_rain_12h, expect_snow_6h, expect_snow_12h, wind_speed, wind_way,
                     wind_korean,
                     humi, pms[int(today_plus_numder)][0], pms[int(today_plus_numder)][1]]
        num += 1
        data.append(hour_data)
    all_data.append(data)


# conn = pymysql.connect(host='10.156.147.210', user='jong', passwd='1234', db='mysql', charset='utf8')
# conn = pymysql.connect(host='10.156.147.199', user='dupang', passwd='1234', db='mysql', charset='utf8')
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='kkddhh77887788@', db='mysql', charset='utf8')

cur = conn.cursor()
state = input("데이터 베이스 구축이 처음입니까? \n(그렇다면 y, 이미 데이터 베이스 구축을 실행했다면 y를 제외한 아무키를 입력하세요) "
              ": ")
# state = 'd'

if state is 'y':
    cur.execute("CREATE DATABASE project_data_db;")
    cur.execute("USE project_data_DB")
    cur.execute(
        "CREATE TABLE data ( num TINYINT, gu VARCHAR(4), x TINYINT, y TINYINT, update_time INT, time_ahead TINYINT, "
        "hour TINYINT, temp SMALLINT, day_high_temp SMALLINT, day_low_temp SMALLINT, sky_state TINYINT, "
        "weather_state TINYINT, weather_eng VARCHAR(20), rain_persent TINYINT, "
        "expect_rain_6h FLOAT, expect_rain_12h FLOAT, expect_snow_6h FLOAT, expect_snow_12h FLOAT, "
        "wind_speed FLOAT, wind_way TINYINT, wind_text CHAR(4), humi TINYINT, "
        "fine_dust VARCHAR(10), small_fine_dust VARCHAR(10), PRIMARY KEY(num) );")
    for data in all_data:
        cur.executemany(
            "INSERT INTO data(num, gu, x, y, update_time, time_ahead, hour, temp, day_high_temp, day_low_temp, "
            "sky_state, weather_state, weather_eng, rain_persent, expect_rain_6h, expect_rain_12h, "
            "expect_snow_6h, expect_snow_12h, wind_speed, wind_way, wind_text, humi, fine_dust, small_fine_dust) "
            "VALUES "
            "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            data)
        conn.commit()
else:
    cur.execute("USE project_data_DB")

    for data in all_data:
        for hour_data in data:
            cur.execute("USE project_data_DB")
            cur.execute(
                "UPDATE data SET gu = %s, x = %s, y = %s, update_time = %s, time_ahead  = %s, hour = %s, temp = %s,"
                " day_high_temp = %s, day_low_temp = %s, sky_state = %s, weather_state = %s, weather_eng = %s, "
                "rain_persent = %s, expect_rain_6h = %s, expect_rain_12h = %s, expect_snow_6h = %s, "
                "expect_snow_12h = %s, wind_speed = %s, wind_way = %s, wind_text = %s, humi = %s, "
                "fine_dust = %s, small_fine_dust = %s WHERE num=%s",
                (hour_data[1], hour_data[2], hour_data[3], hour_data[4], hour_data[5],
                 hour_data[6], hour_data[7], hour_data[8], hour_data[9], hour_data[10], hour_data[11],
                 hour_data[12], hour_data[13], hour_data[14], hour_data[15],
                 hour_data[16], hour_data[17], hour_data[18], hour_data[19], hour_data[20],
                 hour_data[21], hour_data[22], hour_data[23], int(hour_data[0]))
                )
            conn.commit()
cur.close()
conn.close()
