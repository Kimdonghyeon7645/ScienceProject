## pythonanywhere 원격 db 연결
<a href="https://github.com/Kimdonghyeon7645/ScienceProject/issues/3">연결되는 이슈</a>

#### 서버에서 스크립트로, 매일마다 서버의 db를 업데이트 하는 코드를 작성하기 위해서,

맨 처음으로 pythonanywhere 원격 db를 파이썬 코드로 연결하고, 업로드 하는 과정이 필요하다.

<details>
  <summary>error 도장깨기의 흔적...</summary>
  
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
  
  
</details>  

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

***

### 얼렁뚱땅이지만, 현위치

비밀번호 오류등 인자값을 잘못 넘기면, 접근이 꼬여서 에러가 나는데, 
pythonanywhere에서 이럴경우 연속적인 연결시도로 암호를 해독하는 것을 방지하기 위해 액세스를 거부.

> 참고 : https://www.pythonanywhere.com/forums/topic/7558/

그래서 액세스가 거부된 상태에서 접근을 하면, 접속이 안되다가 결국 timed out 오류가 뜸.
(대신 한두시간 뒤에 액세스 거부가 풀림)

이에 대해 신중하게 코드를 고쳐서 시도하면 될듯.

***
