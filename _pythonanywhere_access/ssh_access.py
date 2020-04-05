import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('ssh.pythonanywhere.com',
               username="bosal",
               password="kkddhh77887788@",
               allow_agent=False,
               look_for_keys=False,
               timeout=5.0)

"""
paramiko 를 사용해서 SSH 연결을 테스트 하는 코드,
<정상실행됨>
"""
