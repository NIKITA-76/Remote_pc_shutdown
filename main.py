import socket

new_socket = socket.socket()
new_socket.bind(('localhost', 50))
new_socket.listen()

conn, add = new_socket.accept()

client = (conn.recv(1024).decode())
print(client + 'Есть контакт')

