import pymysql
conn = pymysql.connect(host='10.156.147.199', user='dupang', passwd='1234', db='mysql', charset='utf8')
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='kkddhh77887788@', db='mysql', charset='utf8')
# conn : 연결 객체

cur = conn.cursor()
# cur : 커서 객체

cur.execute("SHOW databases;")
cur.execute("USE dupang_db")
cur.execute("SHOW tables;")
cur.execute("INSERT INTO test_v1 (title, kind, profile) VALUES (%s, %s, %s)", ('임베디드', '+', '보안'))

# cur.execute("SHOW databases;")
# cur.execute("USE ppap")
# cur.execute("CREATE table v0 ( pp VARCHAR(20), PRIMARY KEY(pp) ); ")
# cur.execute("INSERT INTO v0 (pp) VALUES (%s)", ('돼라'))
conn.commit()
cur.close()
conn.close()
