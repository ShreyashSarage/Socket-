import socket

HOST = "127.0.0.1"  #the server's hostname or ip address
PORT = 8080

# message = input("enter mesage")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"hello world!!")
    data = s.recv(1024)

print(f"sended {data!r}")