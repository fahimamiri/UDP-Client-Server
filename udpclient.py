from socket import *

serverName = '127.0.0.1'  # Server's IP address
serverPort = 12345         # Server's port number

clientSocket = socket(AF_INET, SOCK_DGRAM)

sentence = input('Input sentence to reverse: ')

clientSocket.sendto(sentence.encode(), (serverName, serverPort))

modifiedSentence, serverAddress = clientSocket.recvfrom(2048)

print('Reversed sentence from server:', modifiedSentence.decode())

clientSocket.close()
