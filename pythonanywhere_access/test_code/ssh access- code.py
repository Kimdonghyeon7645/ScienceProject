import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 22))
s.listen(1)
s.close()

"""
local bind port 가 수신권한이 있는지 확인하는 코드

정상종료
"""