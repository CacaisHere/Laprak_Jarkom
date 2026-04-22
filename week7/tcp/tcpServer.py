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
