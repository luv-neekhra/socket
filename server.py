import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('waiting for connections...')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Connected With', addr, name)

    hi= 'Welcome ' + name


    c.send(bytes(hi , 'utf-8'))

    while True:
        msg = c.recv(1024).decode()
        print(f'Message received from client: {msg}')
        rep = input('Your response: ')
        c.send(rep.encode())

    c.close()