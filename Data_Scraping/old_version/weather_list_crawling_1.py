# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

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
    wind_speed = content.find('ws').text
    # 현재 풍속
    wind_way = content.find('wd').text
    # 현재 풍향(8분위, ex> 0: 북, 2: 동, 4: 남, 6: 서)
    wind_korean = content.find('wden').text
    # 현재 풍향 한글로
    humi = content.find('reh').text
    # 현재 습도 (백분위, %)

    print("\n현재 시간: ", hour,
          "\n오늘로 부터 몇일 뒤: ", today_plus_numder,
          "\n현재 온도: ", temp,
          "\n최고 온도: ", day_high_temp,
          "\n최저 온도: ", day_low_temp,
          "\n하늘 상황: ", sky_state,
          "\n기상 상황: ", weather_state,
          "\n기상 상황 한글: ", weather_korean,
          "\n예상 강수 확률: ", rain_persent,
          "\n예상 강수량(6시간): ", expect_rain_6h,
          "\n예상 강수량(12시간): ", expect_rain_12h,
          "\n예상 적설량(6시간): ", expect_snow_6h,
          "\n예상 적설량(12시간): ", expect_rain_12h,
          "\n풍속: ", wind_speed,
          "\n풍향: ", wind_way,
          "\n풍향 한글: ", wind_korean,
          "\n습도: ", humi
          )
