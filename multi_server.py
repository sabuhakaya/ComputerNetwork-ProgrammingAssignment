# import socket module
from socket import *
from threading import Thread
# In order to terminate the program

def connector(connectionSocket):

    try:

        message = connectionSocket.recv(1024).decode()
        print(message)
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\n\n".encode())

        #Send the content of the requested file to the client
       #  for i in range(0, len(outputdata)):
       #      connectionSocket.send(outputdata[i].encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("404 Not Found\r\n".encode())
        #Close client socket
        connectionSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 12000
serverIp = gethostname()
print(gethostbyname(gethostname()))
serverSocket.bind((serverIp, serverPort))
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # soketi yeniden kullan

networkThreads=[]

while True:
    #Establish the connection
    serverSocket.listen(10)  # maksimum bağlanabilecek client sayısı
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    # Create a thread to service the received request
    newThread = Thread(target=connector, args=(connectionSocket,))
    newThread.start()
    networkThreads.append(newThread)

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data