# Modul 7 - Socket Programming

## Program Socket dengan UDP
1. UDP SERVER (udp-server.py)

```python
from socket import *

#membuat socket untuk server
serverPort=8080
serverSocket =socket(AF_INET,SOCK_DGRAM)

#menghubungkan (bind)
serverSocket.bind(
    #tuple
    ('',serverPort)
)

print("[SERVER] server siap digunakan")

#dijanlan selama running bernilai true

while True:
    message, clientAddress =  serverSocket.recvfrom(2048)
   # message yang diterima = 1010100010
    decodeMessage = message.decode()

    if decodeMessage.lower()== "exit":
        print("[SYSTEM] server telah diberhentikan")
        running = False
        continue

    modifiedMessage = decodeMessage.upper()
    print("[SYSTEM] diterima dari ",clientAddress, "message : ",decodeMessage)

    #mengirim ke client
    serverSocket.sendto(
        modifiedMessage.encode(),
        clientAddress
    )

serverSocket.close()
print("[SYSTEM] socket server telah ditutup")
```

2. UDP CLIENT (udp-client.py)
``` python
# import semua method yang ada disocket
from socket import *

#ke kampus,kost,rumah =
serverName = "localhost"
serverPort = 8080  #port kpneksi 

clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("> ")

    if message.lower() == "exit":
        clientSocket.sendto(
            message.encode(),
            (serverName, serverPort)
        )
        print("[SYSTEM] Keluar dari program")
        running = False
        continue

    clientSocket.sendto(
        message.encode(),
        (serverName, serverPort)
    )

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("[SYSTEM] Pesan dari:", serverAddress)
    print(modifiedMessage.decode())

clientSocket.close()
print("[SYSTEM] Koneksi telah ditutup")
```

## Program Socket dengan TCP
1. TCP CLIENT (tcpClient.py)
``` python
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
```
1. TCP SERVER (tcpServer.py)
```python
from socket import *

serverName = "localhost"
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print("[SERVER] server siap menerima koneksi dari client")

try :
    while True:
        try :
            connectionSocket, addr = serverSocket.accept()
            print("[SYSTEM] koneksi diterima dari:", addr)

            sentence = connectionSocket.recv(2048).decode()
            print("[SYSTEM] pesan diterima:", sentence)

            modifiedSentence = sentence.upper()
            connectionSocket.send(modifiedSentence.encode())
            print("[SYSTEM] pesan dikirim ke client:", modifiedSentence)

            connectionSocket.close()

        except timeout:
            continue
except KeyboardInterrupt:
    print("\n[SYSTEM] server dihentikan oleh pengguna")

finally :
    serverSocket.close()
```