import socket

c = socket.socket()

c.connect(('localhost', 9999))

name = input('Enter Your Name : ')
c.send(bytes(name , 'utf-8'))

print((c.recv(1024).decode()))

while True:
    msg = input('Enter your message: ')
    c.send(msg.encode())

    rep = c.recv(1024).decode()
    print(f'Received from server: {rep}')
