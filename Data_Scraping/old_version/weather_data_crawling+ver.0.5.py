from bs4 import BeautifulSoup
from selenium import webdriver
import time as t

page_url ='http://www.kma.go.kr/'
si_button = '//*[@id="weather-home-dong-selector"]/form/div[1]/a'
gu_button = '//*[@id="weather-home-dong-selector"]/form/div[2]/a'
dong_button = '//*[@id="weather-home-dong-selector"]/form/div[3]/a'


def button_click(xpath):
    button = browser.find_element_by_xpath(xpath)
    button.click()
    t.sleep(0.8)
    # 커서 웹 영역에 위치시키지 말기!!!! (자꾸 새로고침 되지 않게)

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# browser = webdriver.Chrome(r"C:\Users\user\Documents\Python\chromedriver.exe", chrome_options=options)
browser = webdriver.Chrome(r"C:\Users\user\Documents\Python\chromedriver.exe")
browser.get(page_url)
t.sleep(5)

button_click(si_button)
button_click('//*[@id="weather-home-dong-selector"]/form/div[1]/ul/a[7]')
button_click(gu_button)
button_click('//*[@id="weather-home-dong-selector"]/form/div[2]/ul/a[4]')
button_click(dong_button)
button_click('//*[@id="weather-home-dong-selector"]/form/div[3]/ul/a[6]')
button_click('//*[@id="btnFavView"]')
t.sleep(2)

soup = BeautifulSoup(browser.page_source, 'html.parser')
browser.close()
print(soup.select("div#weather-home-dong-forecast"))
