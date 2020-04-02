import mysql.connector
import sshtunnel

sshtunnel.TUNNEL_TIMEOUT = sshtunnel.SSH_TIMEOUT = 15.0
server = sshtunnel.open_tunnel(
    'ssh.pythonanywhere.com',
    ssh_username="bosal",
    ssh_password="kkddhh77887788@",
    remote_bind_address=('bosal.mysql.pythonanywhere-services.com', 3306),
    local_bind_address=('127.0.0.1', 22),
    debug_level='TRACE',
)

server.start()
db = mysql.connector.connect(
    user='bosal', password='kkddhh77887788@',
    host='127.0.0.1', port=server.local_bind_port,
    database='bosal$pj_db',
)
db.close()
server.stop()
