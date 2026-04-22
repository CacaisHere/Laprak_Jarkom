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
