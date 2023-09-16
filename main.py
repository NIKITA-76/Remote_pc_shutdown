import socket
import subprocess



new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_socket.bind(('192.168.0.102', 9090))
new_socket.listen()


conn, add = new_socket.accept()


client = (conn.recv(1024).decode())
print(client)
while True:
    if client == '1':
        subprocess.call(['cmd.exe', '/c', 'shutdown /h'])
        print(' ' + client)

