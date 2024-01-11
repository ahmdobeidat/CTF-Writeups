from pwn import *
import json
HOST = 'socket.cryptohack.org'
PORT = 11112

req = {
    "buy": "flag"
}
def json_recv():
    line = s.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    s.sendline(request)

s = remote(HOST, PORT)
data = s.recvline()
#print(data)
data = s.recvline()
#print(data)
json_send(req)
data = s.recvline()
#print(data)
data = s.recvline()
#print(data)
flag = dict(json_recv())['flag']
print("Flag: ", end='')
print(flag)
