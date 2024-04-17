from socket import *

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

serverPort = 12345
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', serverPort))

print('UDP server is ready to receive')

while True:
    sentence, clientAddress = serverSocket.recvfrom(2048)
    sentence = sentence.decode()

    print('Received sentence from client:', sentence)

    reversed_sentence = reverse_sentence(sentence)

    serverSocket.sendto(reversed_sentence.encode(), clientAddress)
    print('Reversed sentence sent to client:', reversed_sentence)
