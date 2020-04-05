# -*- coding: utf-8 -*-
"""
과학 프로젝트는 과학이다.
조별 프로젝트도 과학이다.
(걍 이럴꺼면 개인 프로젝트라고 했지 하....)
"""
import sshtunnel
import mysql.connector


# -*- 크롤링 끝, pythonanywhere 원격 DB 업로드 시작 -*-

database_name = "pj_db"
user_name = 'bosal'
user_password = 'kkddhh77887788@'
pythonanywhereDatabaseHostname = 'bosal.mysql.pythonanywhere-services.com'

sshtunnel.SSH_TIMEOUT = sshtunnel.TUNNEL_TIMEOUT = 5.0


with sshtunnel.SSHTunnelForwarder(
    'ssh.pythonanywhere.com',
    ssh_username=user_name, ssh_password=user_password,
    remote_bind_address=(pythonanywhereDatabaseHostname, 3306),
    local_bind_address=('127.0.0.1', 22),
) as tunnel:
    connection = mysql.connector.connect(
        user=user_name, password=user_password,
        host='127.0.0.1', port=tunnel.local_bind_port,
        database=f'{user_name}${database_name}',
    )
    connection.close()
