from bs4 import BeautifulSoup
import requests

s1 = '30'    # 대전광역시 = 30
s2 = {'대덕구': '230', '동구': '110', '서구': '170', '유성구': '200', '중구': '140'}
s3 = {'대화동': '52000',
      '덕암동': '57000',
      '목상동': '58000',
      '법1동': '60000',
      '법2동': '61000',
      '비래동': '53300',
      '석봉동': '56000',
      '송촌동': '54300',
      '신탄진동': '55000',
      '오정동': '51000',
      '중리동': '54600',
      '회덕동': '52500',
      '가양1동': '62000',
      '가양2동': '63000',
      '대동': '58500',
      '대청동': '72500',
      '산내동': '74000',
      '삼성동': '69500',
      '성남동': '66500',
      '신인동': '54500',
      '용운동': '56000',
      '용전동': '64000',
      '자양동': '59000',
      '중앙동': '51500',
      '판암1동': '55100',
      '판암2동': '55200',
      '홍도동': '67000',
      '효동': '53000',
      '가수원동': '59000',
      '가장동': '57000',
      '갈마1동': '58100',
      '갈마2동': '58200',
      '관저1동': '59600',
      '관저2동': '59700',
      '괴정동': '56000',
      '기성동': '60000',
      '내동': '57500',
      '도마1동': '52000',
      '도마2동': '53000',
      '둔산1동': '63000',
      '둔산2동': '64000',
      '둔산3동': '66000',
      '만년동': '65000',
      '변동': '54000',
      '복수동': '51000',
      '용문동': '55000',
      '월평1동': '58600',
      '월평2동': '58700',
      '월평3동': '58800',
      '정림동': '53500',
      '탄방동': '55500',
      '관평동': '60000',
      '구즉동': '58000',
      '노은1동': '54600',
      '노은2동': '54700',
      '노은3동': '54800',
      '신성동': '55000',
      '온천1동': '53000',
      '온천2동': '54000',
      '원신흥동': '61000',
      '전민동': '57000',
      '진잠동': '52000',
      '대사동': '63000',
      '대흥동': '57500',
      '목동': '55000',
      '문창동': '60500',
      '문화1동': '72000',
      '문화2동': '73000',
      '부사동': '64000',
      '산성동': '74000',
      '석교동': '62000',
      '오류동': '67000',
      '용두동': '65500',
      '유천1동': '70000',
      '유천2동': '71000',
      '은행선화동': '53500',
      '중촌동': '56000',
      '태평1동': '68000',
      '태평2동': '69000'
      }

for gu in s2.keys():
    for dong in s3.keys():
        for day in ['0', '1', '2']:
            page_url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3020055000'
            page_html = requests.get(page_url)
            page_soup = BeautifulSoup(page_html.text, 'html.parser')
            print(page_soup.text)
