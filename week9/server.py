from socket import *
import sys

# membuat TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM) #pakai tcp socket

# membuat server socket
serverPort = 6789 #server berjalan pada port 6789
serverSocket.bind(('', serverPort))#menghungkan socket ke port dengan alamat ip kosong
serverSocket.listen(1)#server socket siap menerima koneksi
print("Server ready on port", serverPort)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#server lagi nunggu koneksi masuk
    try:
        # terima pesan dari client
        message = connectionSocket.recv(1024).decode()#menerima data dari browse dengan ukuran maksimum 1024 byte, dan mendekodekannya menjadi string
        print("Request:", message)  #menampilkan pesan yang diterima dari client (request HTTP) di konsol server

        # ambil nama file yang diminta
        filename = message.split()[1]
        # buka file yang diminta
        f = open(filename[1:]) 
        outputdata = f.read()#membaca isi file yang telah dibuka dan menyimpannya dalam variabel outputdata. Isi file ini nantinya akan dikirim kembali ke client sebagai respons HTTP.

        # mengirimkan HTTP response header
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())#mengirimkan respon http ke browser
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())#mengirimkan header HTTP tambahan yang menunjukkan jenis konten 
    
        # mengirimkan isi file ke client    
        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # mengirimkan HTTP response header untuk file yang tidak ditemukan
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())

        connectionSocket.send("""
        <html>
        <head><title>404 Not Found</title></head>
        <body><h1>404 File Not Found</h1></body>
        </html>
        """.encode())

        #tutup koneksi dengan client
        connectionSocket.close()

# tutup server socket
serverSocket.close()
sys.exit()