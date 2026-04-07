# Laporan Praktikum modul 4

### Nslookup
1. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP
server tersebut?
![nslookup](asset/jwb1.png)
>jawaban:
 disini saya mencoba mencari ip dari website www.tokopedia.com dan IP yang dihasilkan adalah 23.40.63.199

______________________________________________________________________________________________________________
2.  Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa.
![nslookup](asset/jwb2.png)
>jawaban :

_______________________________________________________________________________________________________________
3. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! Mail
melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya?
![nslookup](asset/jwb3.png)

### Tracing DNS dengan Wireshark
Selanjutnya, jawab beberapa pertanyaan berikut:
1. Cari pesan permintaan DNS dan balasannya. Apakah pesan tersebut dikirimkan melalui UDP
atau TCP?
>jawab :

_______________________________________________________________________________________________________________
2. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasannya?
>jawab :

_______________________________________________________________________________________________________________
3. Pada pesan permintaan DNS, apa alamat IP tujuannya? Apa alamat IP server DNS lokal anda
(gunakan ipconfig untuk mencari tahu)? Apakah kedua alamat IP tersebut sama?
>jawab :

_______________________________________________________________________________________________________________
4. Periksa pesan permintaan DNS. Apa “jenis” atau ”type” dari pesan tersebut? Apakah pesan
permintaan tersebut mengandung ”jawaban” atau ”answers”?
>jawab :

_______________________________________________________________________________________________________________
5. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau ”answers” yang terdapat di
dalamnya? Apa saja isi yang terkandung dalam setiap jawaban tersebut?
>jawab :

_______________________________________________________________________________________________________________
6. Perhatikan paket TCP SYN yang selanjutnya dikirimkan oleh host Anda. Apakah alamat IP
pada paket tersebut sesuai dengan alamat IP yang tertera pada pesan balasan DNS?
>jawab :

_______________________________________________________________________________________________________________
7. Halaman web yang sebelumnya anda akses (http://www.ietf.org) memuat beberapa
gambar. Apakah host Anda perlu mengirimkan pesan permintaan DNS baru setiap kali ingin
mengakses suatu gambar?
