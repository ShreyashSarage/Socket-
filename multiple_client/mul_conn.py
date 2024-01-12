import socket
from _thread import *

host = '127.0.0.1'
port = 8080

def client_handler(connection):
    connection.send(str.encode('You are now connected to the replay server.......Type BYE to stop'))
    while True:
        try:
            data = connection.recv(2048)
            if not data:
                break
            message = data.decode('utf-8')
            if message == 'BYE':
                break
            reply = f'Server:{message}'
            connection.sendall(str.encode(reply))
        except ConnectionResetError:
            break
    connection.close()

def accept_connections(ServerSocket):
    client,address = ServerSocket.accept()
    print('Connected to: '+ address[0]+':'+str(address[1]))
    start_new_thread(client_handler,(client, ))

def start_service(host,port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host,port))
    except socket.error as e:
        print(str(e))
        return
    
    print(f'Server is listening on port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)

start_service(host,port)