# -*- coding: utf-8 -*-
"""
과학 프로젝트는 과학이다.
조별 프로젝트도 과학이다.
(걍 이럴꺼면 개인 프로젝트라고 했지 하....)
"""
from bs4 import BeautifulSoup
import requests
import sshtunnel
import mysql.connector


def num_change(x):
    return {'좋음': '1', '보통': '2', '나쁨': '3', '매우나쁨': '4'}.get(x, 'NoneData')


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
header = []
num = 1
urls = [
    'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3020055000',  # 유성구 (신성동)
    'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3017059700',  # 서구 (관저동)
    'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3014074000',  # 중구 (산성동)
    'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3023060000',   # 대덕구 (법동)
    'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3011062000'   # 동구 (가양동)
]

for url in urls:  # 유성구, 서구, 중구, 대덕구, 동구순
    gu_data = []
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    # header 행
    if not header:
        n = str(1)  # 헤더 테이블 행 번호
        update_year = soup.find('tm').text[:4]
        update_month = soup.find('tm').text[4:6]
        update_date = soup.find('tm').text[6:8]
        update_time = soup.find('tm').text[8:-2]
        header = [n, update_year, update_month, update_date, update_time]

    contents = soup.select('data')
    for content in contents:
        hour = content.find('hour').text  # 현재 시간 (3시간 간격, ex> 3, 6, 9, ...)
        day_num = int(content.find('day').text)
        time_difference = str(int(hour) - int(update_time) + int(day_num)*24)  # 시간 차이
        temp = content.find('temp').text  # 현재 온도 (섭씨 ℃)
        day_high_temp = content.find('tmx').text  # 현재 날짜의 최고 온도 (오늘은 구하지 않음, -999)
        day_low_temp = content.find('tmn').text  # 현재 날짜의 최저 온도 (오늘은 구하지 않음, -999)
        sky_state = content.find('sky').text  # 현재 하늘의 상태, 구름의 정도 1~4로 표현(1:맑음, 2:구름적음, 3:구름많음, 4:흐림)
        weather_state = content.find('pty').text  # 현재 기상현상 상태, 0: 맑음, 1: 비, 2: 진눈개비, 3: 눈, 4: 소나기
        weather_english = content.find('wfen').text  # 현재 기상현상 상태 통틀어서 한글로
        rain_persent = content.find('pop').text  # 현재 비올 확률 (백분위, %)
        expect_rain_6h = content.find('r06').text  # 6시간 뒤까지의 예상 강수량
        expect_rain_12h = content.find('r12').text  # 12시간 뒤까지의 예상 강수량
        expect_snow_6h = content.find('s06').text  # 6시간 뒤까지의 예상 적설량
        expect_snow_12h = content.find('s12').text  # 12시간 뒤까지의 예상 적설량
        wind_speed = str(round(float(content.find('ws').text), 2))  # 현재 풍속
        wind_way = content.find('wd').text  # 현재 풍향(8분위, ex> 0: 북, 2: 동, 4: 남, 6: 서)
        wind_korean = content.find('wden').text  # 현재 풍향 한글로
        humi = content.find('reh').text  # 현재 습도 (백분위, %)
        hour_data = [
            str(num), time_difference, hour, temp, day_high_temp, day_low_temp, sky_state, weather_state, weather_english,
            rain_persent, expect_rain_6h, expect_rain_12h, expect_snow_6h, expect_snow_12h, wind_speed, wind_way,
            wind_korean, humi, pms[int(day_num)][0], pms[int(day_num)][1]
        ]
        num += 1
        gu_data.append(hour_data)

    all_data.append(gu_data)

# -*- 크롤링 끝, pythonanywhere 원격 DB 업로드 시작 -*-

database_name = "pj_db"
user_name = 'bosal'
user_password = 'kkddhh77887788@'
pythonanywhereDatabaseHostname = 'bosal.mysql.pythonanywhere-services.com'

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    'ssh.pythonanywhere.com',
    ssh_username=user_name, ssh_password=user_password,
    remote_bind_address=(pythonanywhereDatabaseHostname, 3306),
    local_bind_address=('127.0.0.1', 22),
) as tunnel:
    connection = mysql.connector.connect(
        user=user_name, password=user_password,
        host='127.0.0.1', port=tunnel.local_bind_port,
        database=f'{user_name}${database_name}',
    )
    cur = connection.cursor()
    # header 테이블 업데이트
    cur.execute(
        "UPDATE header SET update_year = %s, update_month = %s, update_date = %s, update_time = %s"
        " WHERE num = %s", (header[1], header[2], header[3], header[4], header[0])
    )
    # 구별로 테이블 업데이트
    for index, gu_data in enumerate(all_data):
        for hour_data in gu_data:
            cur.execute(
                f"UPDATE gu_{index} SET time_difference = %s, hour = %s, temp = %s, day_high_temp = %s, day_low_temp = "
                f"%s, sky_state = %s, weather_state = %s, weather_eng = %s, rain_persent = %s, expect_rain_6h = %s, "
                f"expect_rain_12h = %s, expect_snow_6h = %s, expect_snow_12h = %s, wind_speed = %s, wind_way = %s, "
                f"wind_text = %s, humi = %s, fine_dust = %s, small_fine_dust = %s WHERE num = %s",
                (
                    hour_data[1], hour_data[2], hour_data[3], hour_data[4], hour_data[5],
                    hour_data[6], hour_data[7], hour_data[8], hour_data[9], hour_data[10], hour_data[11],
                    hour_data[12], hour_data[13], hour_data[14], hour_data[15],
                    hour_data[16], hour_data[17], hour_data[18], hour_data[19], int(hour_data[0])
                )
            )
            connection.commit()
    cur.close()
    connection.close()
