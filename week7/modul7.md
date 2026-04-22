# Modul 7 - Socket Programming

Aplikasi jaringan umumnya terdiri dari dua program, yaitu klien dan server, yang berjalan pada sistem berbeda dan berkomunikasi melalui soket. Tugas utama pengembang adalah membuat kode untuk kedua program tersebut agar dapat saling bertukar data.Terdapat dua jenis aplikasi jaringan. Pertama, aplikasi terbuka yang mengikuti standar protokol seperti RFC, sehingga klien dan server dari pengembang berbeda tetap dapat berkomunikasi (contohnya browser Google Chrome dengan server Apache HTTP Server). Kedua, aplikasi proprietary yang menggunakan protokol tertutup, sehingga hanya dapat digunakan dalam sistem yang dikembangkan oleh pihak yang sama.Dalam pengembangannya, developer juga harus memilih antara TCP dan UDP. TCP bersifat andal dan berbasis koneksi, sedangkan UDP tidak berbasis koneksi dan tidak menjamin pengiriman data. Selain itu, penggunaan nomor port harus disesuaikan terutama jika menggunakan protokol standar.

Pemrograman soket UDP dan TCP diperkenalkan melalui contoh aplikasi sederhana menggunakan Python 3.11 Python dipilih karena lebih mudah dipahami, memiliki kode yang lebih ringkas, serta mampu menjelaskan konsep dasar soket dengan jelas dibandingkan bahasa lain seperti Java, C, atau C++.

## Program Socket dengan UDP
Pada bagian ini dibuat program client-server sederhana menggunakan UDP dan TCP. Komunikasi antar proses terjadi melalui soket, yang dianalogikan seperti pintu antara aplikasi dan protokol transport-layer. Pengembang hanya mengontrol aplikasi, sedangkan transport-layer dikendalikan oleh sistem.Dalam UDP sebelum data dikirim, proses pengirim harus menyertakan alamat tujuan yang terdiri dari alamat IP dan nomor port. Alamat ini digunakan untuk mengarahkan paket ke proses yang tepat di host tujuan. Selain itu, alamat sumber juga disertakan secara otomatis oleh sistem operasi.

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
________________________________________________________________________________________________________
## Program Socket dengan TCP
TCP (Transmission Control Protocol) merupakan protokol yang bersifat connection-oriented, sehingga sebelum pertukaran data terjadi, klien dan server harus membangun koneksi terlebih dahulu melalui proses three-way handshake. Koneksi ini menghubungkan soket klien dengan soket server menggunakan alamat IP dan nomor port masing-masing.Berbeda dengan UDP pada TCP pengirim tidak perlu menyertakan alamat tujuan setiap kali mengirim data karena koneksi sudah terbentuk. Klien berperan untuk memulai komunikasi sedangkan server harus dalam keadaan siap dengan menyediakan soket khusus (welcoming socket) untuk menerima permintaan koneksi.

Saat klien memulai koneksi, server akan membuat soket baru yang khusus digunakan untuk melayani klien tersebut. Soket awal hanya digunakan untuk menerima koneksi sedangkan komunikasi selanjutnya dilakukan melalui soket koneksi (connection socket), sehingga server dapat melayani banyak klien secara bersamaan.TCP menyediakan komunikasi yang andal, di mana data dikirim secara berurutan dan lengkap. Baik klien maupun server dapat saling mengirim dan menerima data. Contoh sederhana adalah klien mengirim pesan ke server, lalu server memprosesnya (misalnya mengubah huruf menjadi kapital) dan mengirimkannya kembali ke klien.

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