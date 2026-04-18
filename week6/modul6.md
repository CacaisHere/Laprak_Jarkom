# Jawaban Modul 6

## Jawablah pertanyaan-pertanyaan berikut dengan menganalisis paket yang tertangkap pada trace tcp- ethereal-trace-1.
1. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien (sumber) untuk
mentransfer file ke gaia.cs.umass.edu? Cara paling mudah menjawab pertanyaan ini adalah
dengan memilih sebuah pesan HTTP dan meneliti detail paket TCP yang digunakan untuk
membawa pesan HTTP tersebut.
![soal1](asset/jawab1.png)
>jawab :

_____________________________________________________________________________________________________________________
2. Apa alamat IP dari gaia.cs.umass.edu? Pada nomor port berapa ia mengirim dan menerima
segmen TCP untuk koneksi ini?
![soal1](asset/jawab2.png)
>jawab :

_____________________________________________________________________________________________________________________
## Dasar TCP : Jawablah beberapa pertanyaan berikut untuk segmen TCP:
1. Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara
komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga
teridentifikasi sebagai segmen SYN?
![soal1](asset/soal1.png)
>jawab :

_____________________________________________________________________________________________________________________
2. Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien
sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK?
Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen
sehingga teridentifikasi sebagai segmen SYNACK?
![soal1](asset/soal2.png)
>jawab :

_____________________________________________________________________________________________________________________
3. Berapa nomor urut segmen TCP yang berisi perintah HTTP POST? Perhatikan bahwa untuk
menemukan perintah POST, Anda harus menelusuri content field milik paket di bagian
bawah jendela Wireshark, kemudian cari segmen yang berisi "POST" di bagian field DATAnya.
![soal1](asset/)
>jawab :

_____________________________________________________________________________________________________________________
4. Anggap segmen TCP yang berisi HTTP POST sebagai segmen pertama dalam koneksi TCP.
Berapa nomor urut dari enam segmen pertama dalam TCP (termasuk segmen yang berisi
HTTP POST)? Pada jam berapa setiap segmen dikirim? Kapan ACK untuk setiap segmen
diterima? Dengan adanya perbedaan antara kapan setiap segmen TCP dikirim dan kapan
acknowledgement-nya diterima, berapakah nilai RTT untuk keenam segmen tersebut?
Berapa nilai EstimatedRTT setelah penerimaan setiap ACK? (Catatan: Wireshark memiliki
fitur yang memungkinkan Anda untuk memplot RTT untuk setiap segmen TCP yang dikirim.
Pilih segmen TCP yang dikirim dari klien ke server gaia.cs.umass.edu pada jendela "daftar paket yang ditangkap". Kemudian pilih: Statistics->TCP Stream Graph- >Round Trip Time
Graph).
![soal1](asset/soal4.png)
>jawab :

_____________________________________________________________________________________________________________________
5. Berapa panjang setiap enam segmen TCP pertama?
![soal1](asset/soal5.png)
>jawab :

_____________________________________________________________________________________________________________________
6. Berapa jumlah minimum ruang buffer tersedia yang disarankan kepada penerima dan
diterima untuk seluruh trace? Apakah kurangnya ruang buffer penerima pernah
menghambat pengiriman?
![soal1](asset/soal6.png)
>jawab :

_____________________________________________________________________________________________________________________
7. Apakah ada segmen yang ditransmisikan ulang dalam file trace? Apa yang anda periksa (di
dalam file trace) untuk menjawab pertanyaan ini?
![soal1](asset/soal7.png)
>jawab :

_____________________________________________________________________________________________________________________
8. Berapa banyak data yang biasanya diakui oleh penerima dalam ACK? Dapatkah anda
mengidentifikasi kasus-kasus di mana penerima melakukan ACK untuk setiap segmen yang
diterima?![soal1](asset/soal8.png)
>jawab :

_____________________________________________________________________________________________________________________
9. Berapa throughput (byte yang ditransfer per satuan waktu) untuk sambungan TCP?
Jelaskan bagaimana Anda menghitung nilai ini.
![soal1](asset/soal9.png)
>jawab :

_____________________________________________________________________________________________________________________
## Jawalah beberapa pertanyaan berikut menggunakan segmen TCP pada trace paket tcp-etherealtrace-1 di http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip .

1. Gunakan alat plotting Time-Sequence-Graph (Stevens) untuk melihat grafik nomor urut
berbanding waktu dari segmen yang dikirim oleh klien ke server gaia.cs.umass.edu.
Dapatkah Anda mengidentifikasi di mana fase “slow start” TCP dimulai dan berakhir, dan
pada bagian mana algoritma ”congestion avoidance” mengambil alih? Berikan komentar
tentang bagaimana data yang diukur berbeda dari perilaku ideal TCP yang telah kita pelajari.
![soal1](asset/soal9.png)
>jawab :

_____________________________________________________________________________________________________________________
2. Jawablah kedua pertanyaan di atas untuk trace yang Anda dapatkan ketika Anda
mengirimkan file dari komputer ke gaia.cs.umass.edu.
![soal1](asset/soal9.png)
>jawab :

_____________________________________________________________________________________________________________________