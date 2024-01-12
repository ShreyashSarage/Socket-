import socket

host = "127.0.0.1"
port = 8080

def start_client():
    with socket.socket() as client_socket:
        try:
            client_socket.connect((host,port))
            print("connected to server. type 'BYE' to exit.")

            while True:
                message = input("enter a message:")
                client_socket.sendall(message.encode())

                if message.upper() == 'BYE':
                    print("exciting client")
                    break

                data = client_socket.recv(2048)
                print(data.decode('utf-8'))

        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            print("closing the client")
            client_socket.close()

if __name__ == '__main__':
    start_client()