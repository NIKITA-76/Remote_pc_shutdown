import socket

socket_srver = socket.socket()

command = input('your command')
socket_srver.connect(('192.168.0.102', 9090))

socket_srver.send(command.encode())
