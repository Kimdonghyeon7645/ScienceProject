## pythonanywhere 원격 db 연결

#### 서버에서 스크립트로, 매일마다 서버의 db를 업데이트 하는 코드를 작성하기 위해서,

맨 처음으로 pythonanywhere 원격 db를 파이썬 코드로 연결하고, 업로드 하는 과정이 필요하다.
이에대해서 현재는 

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

와 같은 오류로 삽질하는 중이다. 

pythonanywhere 포럼과 가이드, 스텍 오버플로우에서도 해결되지 않는 것 보면 일이 큰것 같다.
(무엇보다 기본지식이 없는 것이 가장 큰 문제다.)
