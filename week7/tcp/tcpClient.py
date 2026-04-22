from socket import *

serverName = "localhost"
serverPort = 12000
 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
#send message ke server
sentence = input("input lowercase sentence: ")
clientSocket.send(sentence.encode())
#receive message dari server
modifiedSentence = clientSocket.recv(2048)
print("From Server: ", modifiedSentence.decode())
clientSocket.close()