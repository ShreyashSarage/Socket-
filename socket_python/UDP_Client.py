import socket

msgFromClient = "hello udp server"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("127.0.0.1",8080)
bufferSize = 1024

#create a udp socket at client side
UDPClinetSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#send to server using created UDP socket
UDPClinetSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClinetSocket.recvfrom(bufferSize)

msg = "message from server {}".format(msgFromServer[0])

print(msg)
UDPClinetSocket.close()