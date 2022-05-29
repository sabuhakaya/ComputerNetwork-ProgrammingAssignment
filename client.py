from http import client
from socket import *
import sys


if len(sys.argv) != 4:
    print("Wrong formatted there must be 3 parameter which is (server_ip, server_port, requested_file)")
    sys.exit(-1)
_, serverIP, serverPort, filename = sys.argv


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(10)
try:
    clientSocket.connect((serverIP, int(serverPort)))
    request_message = f"GET /{filename} HTTP/1.1\rHost: {gethostbyname(gethostname())}:{str(clientSocket.getsockname()[1])}\r\n\r\n"
    clientSocket.send(request_message.encode())
    
    response = clientSocket.recv(1024)
    print(response)

    fileData = clientSocket.recv(10000)
    print(fileData)
except Exception as e:
    raise(e)
finally:
    clientSocket.close()