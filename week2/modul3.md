# Laporan Modul 3

Pada modul kali ini saya akan mempraktikan beberapa aspek dari protokol HTTP (Hypertext Transfer Protocol).Beberapa hal yang akan diamati antara lain interaksi dasar antara metode GET dan response, format pesan HTTP, proses pengambilan file HTML berukuran besar, pengambilan file HTML yang memiliki objek tertanam (embedded objects), serta mekanisme autentikasi dan keamanan pada HTTP.

## Basic HTTP GET/response interaction
Untuk memulai eksplorasi terhadap protokol HTTP, pertama bisa mengakses sebuah file HTML yang sangat sederhana. File tersebut berukuran kecil dan tidak memiliki objek yang disematkan (embedded objects). Langkah-langkah yang dilakukan dalam percobaan ini adalah sebagai berikut:

1. Membuka web browser yang akan digunakan untuk mengakses halaman web.
2. Mengakses alamat berikut melalui browser: http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html. ingat harus berupa HTTP nanti akan muncul seperti gambar dibawah ini.

![1](assets/image/2.png)

3. Setelah halaman berhasil ditampilkan, proses pengambilan paket pada Wireshark dihentikan.

![1](assets/image/1.png)
