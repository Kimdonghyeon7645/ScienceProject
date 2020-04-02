import sshtunnel

sshtunnel.SSH_TIMEOUT = sshtunnel.TUNNEL_TIMEOUT = 5.0


server = sshtunnel.open_tunnel(
    'ssh.pythonanywhere.com',
    ssh_username="bosal",
    ssh_password="kkddhh77887788@",
    remote_bind_address=('bosal.mysql.pythonanywhere-services.com', 3306),
    local_bind_address=('127.0.0.1', 22),
    debug_level='TRACE',
)

server.start()
print(server.local_bind_port)  # show assigned local port
server.stop()

"""
정상종료
출력결과 : 22

# 단기간에 여러번 실행할 경우 timed out과 함께 접근 할 수 없음.
"""
