import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
import json

data = json.dumps({
    "id": 99,
    "startx": 77,
    "starty": 467.2,
    "goalx": 365,
    "goaly": 684.6
})

sock.sendto(data.encode(), ("192.168.1.136", 2525))

received = sock.recv(1024)
data = json.loads(received.decode())

print data