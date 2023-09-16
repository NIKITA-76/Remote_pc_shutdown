import socket

new_socket = socket.socket()
new_socket.bind(('localhost', 50))
new_socket.listen()

print('Запустились')
nam