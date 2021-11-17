sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.38.165.12', 9090))
sock.connect(('127.0.0.1', 9090))

#msg = input()
msg = "Hi!"
sock.send(msg.encode())
msg = input()
while len(msg) != 0:
    sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
    data = sock.recv(1024)
    if msg == 'exit':
        sock.close()
        break
    print(data.decode())
    msg = input()
