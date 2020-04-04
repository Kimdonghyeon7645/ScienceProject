# pythonanywhere 원격 db 연결
<a href="https://github.com/Kimdonghyeon7645/ScienceProject/issues/3">연결되는 이슈 (바로가기)</a>

### 서버에서 스크립트로, 매일마다 서버의 db를 업데이트 하는 코드를 작성하기 위해서,

맨 처음으로 pythonanywhere 원격 db를 파이썬 코드로 연결하고, 업로드 하는 과정이 필요하다.

<details>
  <summary><b> error 도장깨기의 흔적... (누르면 펼쳐져요) </b></summary>
  
  ### 2020-3-31
  
  ```
  2020-03-31 13:28:08,610| ERROR   | Secsh channel 0 open FAILED: open failed: Administratively prohibited
  2020-03-31 13:28:08,610| ERROR   | Could not establish connection from ('127.0.0.1', 2460) to remote side of the tunnel
  Traceback (most recent call last):
    File "C:/PycharmProjects/과학 프로젝트/ssh access-test 2.py", line 30, in <module>
      database=f'{user_name}${database_name}',
    File "C:\PycharmProjects\과학 프로젝트\venv\lib\site-packages\mysql\connector\__init__.py", line 179, in connect
      return MySQLConnection(*args, **kwargs)
    File "C:\PycharmProjects\과학 프로젝트\venv\lib\site-packages\mysql\connector\connection.py", line 95, in __init__
      self.connect(**kwargs)
    File "C:\PycharmProjects\과학 프로젝트\venv\lib\site-packages\mysql\connector\abstracts.py", line 716, in connect
      self._open_connection()
    File "C:\PycharmProjects\과학 프로젝트\venv\lib\site-packages\mysql\connector\connection.py", line 207, in _open_connection
      self._do_handshake()
    File "C:\PycharmProjects\과학 프로젝트\venv\lib\site-packages\mysql\connector\connection.py", line 99, in _do_handshake
      packet = self._socket.recv()
    File "C:\PycharmProjects\과학 프로젝트\venv\lib\site-packages\mysql\connector\network.py", line 243, in recv_plain
      raise errors.InterfaceError(errno=2013)
  mysql.connector.errors.InterfaceError: 2013: Lost connection to MySQL server during query
  ```
  
  와 같은 오류로 삽질...
  
  문제는 문법오류에 있었던것 같음,
  그래도 해결이 안되던데, 문제는 인자값중 호스트, 포트 번호가 이상했었음.
  추가로 로컬 호스트 번호는 localhost 대신 127.0.0.1 을 이용해야함.
  
  > 참고
  https://www.pythonanywhere.com/forums/topic/10934/  
  https://www.pythonanywhere.com/forums/topic/26949/  
  https://andromedarabbit.net/ssh-%EC%A0%91%EC%86%8D%EC%9D%B4-%EC%9E%90%EA%BE%B8-%EB%81%8A%EA%B2%A8%EC%84%9C-%EC%A7%9C%EC%A6%9D%EB%82%A0-%EB%95%8C/
  
  > 사실 이게 뭔문젠지 몰라서, ssh 연결에 대해서 (포트 바인딩등) 공부하고, /etc/ssh/sshd_config 설정에서 삽질.
  
  
  ***
  
  ### 2020-4-1
  
  현재 timed out 에러에 걸리는 문제에 봉착.
  
  ```
  ssh.pythonanywhere.com port 22: Connection timed out
  ```
  
  접근방식의 문제인 것을 판단. 
  
  > 참고  
  https://www.pythonanywhere.com/forums/topic/7558/  
  https://www.pythonanywhere.com/forums/topic/26949/  
  https://github.com/pahaz/sshtunnel/blob/master/Troubleshoot.rst  
  https://www.pythonanywhere.com/forums/topic/13928/  
  
  특히 pythonanywhere 에서 디버깅할 때 활용할 test code를 링크 걸어줘서,
  https://github.com/pahaz/sshtunnel/blob/master/Troubleshoot.rst  
  https://help.pythonanywhere.com/pages/AccessingMySQLFromOutsidePythonAnywhere/  
  
  문제 원인을 파악하는데, (물론 몇십시간을 삽질하는데에도) 유용하게 사용함.
  
  비밀번호 오류등 인자값을 잘못 넘기면, 접근이 꼬여서 에러가 나는데, 
  pythonanywhere에서 이럴경우 연속적인 연결시도로 암호를 해독하는 것을 방지하기 위해 액세스를 거부.
  (1번은 몰라도, 두번 접근에 오류를 되면 액세스가 일시적으로 거부됨.)
  
  > 참고 : https://www.pythonanywhere.com/forums/topic/7558/
  
  그래서 액세스가 거부된 상태에서 접근을 하면, 접속이 안되다가 결국 timed out 오류가 뜸.
  (대신 한두시간 뒤에 액세스 거부가 풀림)
  
  이에 대해 신중하게 코드를 고쳐서 시도하면 될듯.
  
  ***
  
  ### 2020-4-2
  하루종일 삽질하다가 이제야 원인 분석,
  
  > https://www.pythonanywhere.com/forums/topic/11396/
  
  2일동안 한 것을 허무하게 만드는 한문단...
  
  ```
  Ah, that would explain it. 
  PythonAnywhere MySQL servers aren't directly accessible from the public Internet, for security. 
  As you have a paid account, you can access your server indirectly using an SSH tunnel
  -- there's documentation on how to do that here.
  ```
  
  요약하자면, 보안상의 문제때문에 로컬 머신에서 PythonAnywhere MySQL servers에 접근할 수 없다...   
  유료계정일 경우에만 ssh tunnel을 이용해서 간접적으로 접근할 수 있었다.
  
  허무했지만 일단 이유를 찾았으니까 pythonanywhere 콘솔로 스크립트 파일을 돌렸는데,  
  얼마지나지 않아서 뒷통수를 맞았따...
  
  > https://www.pythonanywhere.com/forums/topic/15007/
  
  보안상의 문제때문에 스크립트 pythonanywhere 상에서 함부로 다른 링크에 접근하는 것이 불가능 했다...   
  이또한 무료계정에만 해당되며, 유료계정은 이런 제한없이 링크에 접근할 수 있다. 
  
  이때문에 크롤링으로 requests.get(url) 하는 부분에서 뜬금없는 403에러가 나타났다....
  
  ---
  
  그래도 알아보니, white list라고 무료계정에서 pythonanywhere 상으로 접근할 수 있는 링크 리스트를 제공하며,    
  원한다면 white list 에 없는 링크를 추가해달라고 요청할 수 있는 것을 알아냈다.
  
  > white list 링크 : https://www.pythonanywhere.com/whitelist/
  
  대신에 아무 링크나 추가해줄수 있는 것이 아니고, 공용, 공식 api 같은 것만 추가할 수 있다고 했다.    
  그래서 영어 실력을 모두 짜내서, (구글 번역기로) 포럼 + 피드백에 요청을 보냈다.  
  
  -> 애초에 유료 계정이였으면 이런 저런 오류 하나없이 접근할 수 있었다는 사실이 드러났다...   
  -> 근데 무료계정으로 pythonanywhere를 악용할 수 있기에 이런 제한은 이해가 된다. 
  
  이제 남은것은 답변을 기다리거나(포럼을 참고하면 1~2일 정도에 답변이 오는걸 알수 있었다),   
  white list에 이미 있는 날씨 사이트로 새로운 스크립트 파일을 작성한다든지(크롤링부터 DB업로드 코드를 새로 짜야된다.),   
  ㄴ 시도해 봤는데 크롤링 부분에서 셀레니움, requests와 header설정까지 추가했는데도 접근에 에러가 뜬다... 보류...  
  
  크롤링 자동화는 포기하고, DB업로드만 스크립트로 자동으로 하기로 목표를 변경하거나,
  ㄴ 이럴 경우엔 안하니만 못할 수도 있다. 애초에 크롤링한 파일을 만드는 것이 수동이라면 원래랑 다를께 없기에...
  
  등이 있다.  
  (주변에 웹 전문가가 정말 있었으면 좋았을 것같다...)
  
  ***
  
  일단 너무 많이 시간을 썼으니까 보류하고,  
  밀렸던 파이썬, 웹 문법 정리와 과제, 블로그 포스팅을 해야겠다. (아맞다 토익공부)
  (2020-4-2)
  
</details>  

***

## 해결 2020-4-2

결국 해결했다. 포럼에서 관리자가 당일에 답변해줬고, 다행이 미숙한 영어실력으로 피드백을 보낸것을  
이해해서 화이트리스트에 내가 원하는 링크 1개를 추가했다.  

다만 다른 하나는 api를 이용하지 않으면 안된다고 했다. (한번더 물어봤는데 안된다한다.)

그래도 그부분은 서브콘텐츠 정보를 크롤링해오는 링크였기에, 임시방편으로 대처하고 스크립트를 수정하고  
정상실행까지 여러번 디버깅했더니, 결국 정상종료, DB엔 정상 업데이트가 됬다.

와...

크롤링, DB 업데이트 자동화는 그렇게 끝났다.

***

