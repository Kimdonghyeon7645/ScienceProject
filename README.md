# ScienceProject
## 과학프로젝트, 날씨에 학교를 더하다

2019년 2학기말에 시작한 프로젝트 였고, 5인 프로젝트입니다.
  #### 조별프로젝트기에 노션을 이용해서 소통했고, 브레인 스토밍과 개발 과정까지 공유했습니다.
  https://www.notion.so/Science_Project-9c3b5deffd7446eda3b27296d446757e
  
### 2020-4-1) 크롤링과 ssh활용한 DB 업로드 자동화를 개발하고 있습니다.
자세한 내용은 <a href="#versionUp">아랫 부분에서 덧붙였습니다.</a>

***
### 개발목표 - 
우리학교의 등하교시간, 아침운동시간의 날씨정보와 날씨정보로 아침운동확률도 예측하는 웹사이트

### 개발기간 - 
2019년 12월 20일 ~ 2월 15일
### 개발단계 - 
1. 데이터 크롤링 프로그램 구현, mysql로 DB 구축 (동현, 수필, 두평, 19.12.20. ~ 20.1.4.) 
2. DB 서버 연동, 백엔드 프론트엔드 나뉘어 구현 (두평, 현호, 종근, 20.12.20. ~ 20.1.16.)
3. 프론트 백 연결 문제로 무산 (20.1.16 ~ 20.2.1.)
4. 장고로 웹 구현, 로컬서버로 프론트에 DB값 출력 성공 (20.2.2. ~ 20.2.7.)
5. 웹 디자인, 퍼블리싱 완료, 원격서버로 배포 완료, 프로젝트 끝! (20.2.8. ~ 20.2.15.)

(백 프론트상 연결이 도무지 안되고, 갈등으로 프론트가 잠수타버리는 바람에 데이터 크롤링파트인 저혼자 장고로 웹구현 하게 됬다는 슬픈 전설..)
***
## 실제 웹 링크 - 
http://bosal.pythonanywhere.com/
### 웹 캡쳐 -
<img src="/readme_img/1.png" width="450px" height="auto" title="메인컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
<img src="/readme_img/2.png" width="450px" height="auto" title="세부정보컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
<img src="/readme_img/3.png" width="450px" height="auto" title="시간별컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
<img src="/readme_img/4.png" width="450px" height="auto" title="푸터" alt="프로젝트웹사이트캡처"></img><br/>

(pythonanywhere를 활용했으며, 프로젝트로 처음 장고와 원격배포를 해봤기에 많이 어리숙합니다.
버전업한다면, DB업데이트가 수동이 아닌 자동으로 되게하며, 반응형 웹으로 구현할 예정입니다.)

***

## ver 2, 크롤링, DB 업로드 자동화<a name="versionUp"></a>
(2020.3.31.~)
pythonanywhere의 database를 python script로 접근, db를 자동으로 업데이트 하는 코드 + 크롤링 자동화까지 개발중입니다.  
친절하게도 pythonanywhere에서 스크립트 기능을 제공하는데,  
불친절하게도 db 접근시 생기는 오류에 대해서 대충 명시해서, 구글링으로 스텍오버플로우등을 찾아다니며 삽질하고 있습니다. 

` 혼자이면서, sshtunnel모듈과 ssh연결의 기본지식이 없다 보니까 많이 애먹고 있습니다;; `

2일간 하루종일 매달릴 시간이 있어서, 현재 문제 원인을 알았습니다.   
(문법 오류는 고쳤고, 잘못된 접근으로 인한 pythonanywhere에서의 차단과 그때문에 timed out이 뜨는것 같습니다.)

> 크게 도움된 문헌 : https://www.pythonanywhere.com/forums/topic/7558/

그외의 문제 해결과정에 대해서 자세한 내용은, pythonanywhere_access/ 폴더를 참고하시면 되겠습니다. 

<a href="https://github.com/Kimdonghyeon7645/ScienceProject/tree/master/pythonanywhere_access">바로가기</a>
