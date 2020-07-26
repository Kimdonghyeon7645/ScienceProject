# ScienceProject
<img src="https://img.shields.io/github/languages/count/Kimdonghyeon7645/ScienceProject?style=flat-square"> <img src="https://img.shields.io/github/languages/top/Kimdonghyeon7645/ScienceProject?style=flat-square&logo=Python">

## 과학프로젝트, 날씨에 학교를 더하다

![화면](https://user-images.githubusercontent.com/48408417/79071603-98d46e80-7d17-11ea-9e33-9983a033374f.gif)

2019년 2학기말에 시작한 프로젝트 였는데, 이를 통해서 DB와 Django를 입문해 보았고, (제 장고로의 첫 작품입니다.)  
2020년 현재까지도 개인적으로 조금씩 코드를 리펙토링하거나, 괜찮은 기능을 추가하는 등 시도를 해보고 있습니다.  
<br>

## 버전

### ver1(2020-2-15) 개발목표에(제안서, 계획서) 맞는 웹을 개발하였습니다.
날씨정보중 등하교 날씨, 아침운동 시간의 날씨를 가져와, 그외의 날씨정보(온도, 기상상황, 미세먼지등등)과 함께  
그에맞는 피드백을 제공해주는(아침운동 확률을 예측해주는) 웹을 개발, 배포하였습니다.

> 조별 프로젝트로 진행했고, 브레인스토밍부터 개발 과정까지 노션을 활용하면서 과정들을 기재하고 공유했습니다. 
https://www.notion.so/Science_Project-9c3b5deffd7446eda3b27296d446757e

#### 개발목표와 제안서를 개인적으로 정리하면 아래와 같습니다.
```
개발목표 - 
우리학교의 등하교시간, 아침운동시간의 날씨정보와 날씨정보로 아침운동확률도 예측하는 웹사이트

개발기간 - 
2019년 12월 20일 ~ 2월 15일
개발단계 - 
1. 데이터 크롤링 프로그램 구현, mysql로 DB 구축 (동현, 수필, 두평, 19.12.20. ~ 20.1.4.) 
2. DB 서버 연동, 백엔드 프론트엔드 나뉘어 구현 (두평, 현호, 종근, 20.12.20. ~ 20.1.16.)
3. 프론트 백 연결 문제로 무산 (20.1.16 ~ 20.2.1.)
4. 장고로 웹 구현, 로컬서버로 프론트에 DB값 출력 성공 (20.2.2. ~ 20.2.7.)
5. 웹 디자인, 퍼블리싱 완료, 원격서버로 배포 완료, 프로젝트 끝! (20.2.8. ~ 20.2.15.)

(백 프론트상 연결이 도무지 안되고, 갈등으로 프론트가 잠수타버리는 바람에 데이터 크롤링파트인 저혼자 장고로 웹구현 하게 됬다는 슬픈 전설..)
```

### ver2(2020-4-1) 크롤링과 DB 업데이트 자동화로, 웹의 콘텐츠가 매일 갱신됩니다. 
3일간의 삽질 끝에 크롤링과 DB 자동 업데이트를 구현했습니다.  
앞으로 서버 갱신만 한달에 한번씩 확인해준다면(무료계정의 비애),  
매일매일 그날의 날씨에 맞는 정보를 제공합니다.  

### ver3(2020-4-30, 석가탄신일) 코드를 리펙토링해서 index.html 내용을 반의 반으로 최적화 했습니다. get 요청으로 웹 페이지가 변화합니다.
Django 와 웹에 대해서 학습한 이후에, 백엔드에서 폼의 get 요청을 받아서  
알맞은 페이지와 DB를 전송할 수 있게 했습니다.  
2일만에 쉽게 끝냈으며, 석가탄신일(4-30)에 문서로 내용을 정리하였습니다.
> 2803 줄 => 562 줄

### ver3.1(2020-5-5, 어린이날) 코드를 추가로 리펙토링 해서, index.html 의 내용을 거의 절반으로 다시 최적화 했습니다.  
반복되는 요소를 묶어서 장고의 템플릿 언어 {% for ~ in ~ %} 문으로 처리해 주었습니다.
> 562 줄 => 355 줄

### ver3.9(2020-5-7) 반응형 웹으로, 컴퓨터 ~ 타블렛 스크린에 맞는 화면을 지원합니다.
기본 컴퓨터 화면부터 ~ 600px 너비의 화면까지 화면에 맞는 레이아웃으로 지원하게 하였습니다.  
미디어 쿼리를 사용해서 기존 css 와 타블렛 스크린 css 를 분리했습니다. 
``` 자세한 내용은 결과 이미지를 참고 ```

### ver4(2020-5-7) 반응형 웹으로, 이제 휴대폰 ~ 타블렛 ~ 컴퓨터 모두의 화면을 지원합니다.
화면의 너비가 430px 이하인 휴대폰 화면에서도 이제 웹사이트의 콘텐츠를 확인할 수 있습니다.
``` 자세한 내용은 결과 이미지를 참고 ```

<br>  


## 결과

> 링크 : http://bosal.pythonanywhere.com/

#### PC 화면
<details>
  <summary>그외...</summary>
 
  <img src="/readme_img/1-1.png" width="550px" height="auto" title="메인컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
  <img src="/readme_img/1-2.png" width="550px" height="auto" title="세부정보컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
  <img src="/readme_img/1-3.png" width="550px" height="auto" title="시간별컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
  <img src="/readme_img/1-4.png" width="550px" height="auto" title="푸터" alt="프로젝트웹사이트캡처"></img><br/>
</details> 

#### 타블렛 화면
<img src="/readme_img/2-1.png" width="550px" height="auto" title="메인컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
 <details>
  <summary>그외...</summary>
 
  <img src="/readme_img/2-2.png" width="550px" height="auto" title="메인컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
  <img src="/readme_img/2-3.png" width="550px" height="auto" title="세부정보컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
  <img src="/readme_img/2-4.png" width="550px" height="auto" title="세부정보컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
  <img src="/readme_img/2-5.png" width="550px" height="auto" title="시간별컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
  <img src="/readme_img/2-6.png" width="550px" height="auto" title="푸터" alt="프로젝트웹사이트캡처"></img><br/>
</details> 

### 휴대폰 화면
<img src="/readme_img/3-1.jpg" width="550px" height="auto" title="메인컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
<details>
  <summary>그외...</summary>
 
  <img src="/readme_img/3-2.jpg" width="550px" height="auto" title="세부정보컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
  <img src="/readme_img/3-3.jpg" width="550px" height="auto" title="시간별컨텐츠_푸터" alt="프로젝트웹사이트캡처"></img><br/>
</details> 
<br> 

## 개발 노트

<details>
  <summary>ver 2 개발 노트</summary>
  
  ## ver 2, 크롤링, DB 업로드 자동화
  (2020.3.31.~4.2.)
  pythonanywhere의 database를 python script로 접근, db를 자동으로 업데이트 하는 코드 + 크롤링 자동화까지 개발에 종지부를 찍었습니다.
  
  친절하게도 pythonanywhere에서 스크립트 기능을 제공하는데,  
  불친절하게도 db 접근시 생기는 오류에 대해서 대충 명시해서, 삽질좀 했습니다.
  
  문제 해결과정(삽질)에 대해서 자세한 내용은, pythonanywhere_access/ 폴더를 참고하시면 되겠습니다. 
  
  
  ### 결과
  
  <img src="https://user-images.githubusercontent.com/48408417/79047064-65c6a800-7c4f-11ea-97f3-4f62ac262987.png" width="450px" height="auto" title="결과화면" alt="프로젝트웹사이트캡처"></img><br/>
</details>

<details>
  <summary>4월 6일자 노트</summary>
  
  ## backup?

  (2020-4-6)  
  정말 울뻔했습니다. git bash로 폴더들의 이름을 변경하려고 했는데, 뭐가 잘못됬는지, git mv 원래이름 새이름이 안됬습니다.  
  그래서 구글링으로 찾은 방법들을 실행하다가, 브런치를 삭제하는 명령어였나.? 왜그랬는지는 모르겠지만,     
  로컬에 있는 브런치를 삭제하고 원격으로 다시 받아올려는 생각이였는 가본데,   
  > git status
  
  하고 상태를 보니까 이상하게 폴더의 모든 파일이 삭제됬다 하는 겁니다.  
  그리고 git push 를 하려니까 아이디랑 비밀번호를 입력하라 하더라구요...  
  
  #### 그리고 나서 모든 파일이 삭제되었습니다 (이 원격 저장소안의 모든 폴더, 파일)
  
  머리속도 같이 하얘졌고, git reset 으로 복구는 안됬습니다.  
  (당연하게도 로컬저장소로 복구해봤자 원격저장소는 복구 할 수 없는데,)  
  그땐 머리가 굳어서 git reset 을 했는데 원격저장소가 왜 그대론가 슬펐습니다.  
  
  정말 1시간동안 정말 울뻔했지만, 어떻게든 맨탈을 잡고, 저장소 복구에 성공했습니다.
  
  > https://jupiny.com/2019/03/19/revert-commits-in-remote-repository/  
  정말 감사합니다
  
  덕분에 깃허브의 공포의 쓴맛을 오랜만에 만났고, 더욱이 지식이 늘었습니다.   
  그리고 다음부터 모르는 건, 특히 아이디와 비번을 입력해야 되는 것은 함부로 안할 것 같습니다. ^^;;
</details>


<details>
  <summary>ver 4 개발 노트</summary>

  ## ver 4. 반응형 웹 구현
  (2020-5-6 ~ 2020-5-7)

  <img src="/readme_img/3-1.png" width="550px" height="auto" title="메인컨텐츠" alt="프로젝트웹사이트캡처"></img><br/>
  솔직히 처음 웹을 만들었을때, 친구나 가족에게 자랑할려고 링크를 SNS로 보내는데, 하나같이 깨진다고 하더라구요.  
  생각해보니까 맨처음 만들때 반응형으로 웹을 안만들었던 것이였습니다.. 

  근데 뭐 css 에서 미디어 쿼리 이용해서 스타일만 적용해주면 되니까 처음에는 별 생각없이,  
  css 코드를 수정하러 갔는데... 

  가관이였습니다. 심지어 html 에서 style 속성도 있고 선택자가 중복되는 css도 있고...
  일단 간략하게 반응형 웹 구현을 마치고, 다음번에는 html 에서 style 속성값을 모두 css로 옮기고 코드를 정리하는,  
  리펙토링을 다시한번 해봐야 겠습니다.
</details> 
<br>

## 참고(Reference)

- 파이썬을 통한 웹페이지 크롤링 살펴보기 :  https://www.youtube.com/watch?v=7_IEdMv9eFE  

사실상 이분(이진석코치) 영상으로, 장고해볼까 고민하게 됬고, 입문하게 되었습니다. 사실상 이 영상이 크롤링만 하던 제가 장고와 웹개발까지 입문하게 된 계기가 되었습니다.

- 꿈 많은 사람의 이야기(티스토리 블로그) : https://lsjsj92.tistory.com/category/python-django

장고로 DB 연동부터 웹 페이지 연결까지, 솔직히 2003 에러도 죽어라 만났었는데, 결국 장고로 웹을 구현할 때 까지 이 블로그의 장고 설명글을 중심으로 공부했습니다. 

- 스텍 오버플로우 : https://stackoverflow.com/questions/5922563/unicodedecodeerror-at-utf8-codec-cant-decode-bytes/5922583#5922583

사실상 개발할 때 거의 절반 이상은 스텍 오버플로우에서 오류를 수정하는데만 힘썼습니다. 몇십개의 페이지를 들락날락 하고, 인내심의 한계에도 견디는 게 결국 프로젝트에서 가장 필요한 능력이였던 것 같습니다.
