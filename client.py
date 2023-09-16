import socket

socket_srver = socket.socket()

command = input('your command')
socket_srver.connect(('10.137.84.60', 9090))

socket_srver.send(command.encode())
