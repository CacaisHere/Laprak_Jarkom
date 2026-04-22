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