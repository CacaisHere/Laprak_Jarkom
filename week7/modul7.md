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