import pymysql
import sshtunnel

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com', 22),
    ssh_username="bosal",
    ssh_password="kkddhh77887788@",
    remote_bind_address=('bosal.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    port = tunnel.local_bind_port
    db_connection = pymysql.connect(
        host='bosal.mysql.pythonanywhere-services.com', port=port, db='bosal$pj_db', user='bosal',
        password='')
    db_connection.close()
