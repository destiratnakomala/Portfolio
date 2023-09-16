# Final-Project-RMT-020
# <center> <b> Analisis Marketing Bank untuk Memprediksi klien yang akan Subscribe Deposit Berjangka<br>

Dataset : `Bank Customer Data in VietNam`

HuggingFace: [`Bank-Marketing-Term-Deposit-prediction`](https://huggingface.co/spaces/destiratnakomala/Bank-Marketing-Term-Deposit)

Model 1: [Main Model](https://github.com/destiratnakomala/Final-Project-FTDS-020/blob/main/Bank-Marketing-Term-Deposit/01_Main_desti_ratna_komala.ipynb)

Model 2: [Model Neural Network](https://github.com/destiratnakomala/Final-Project-FTDS-020/blob/main/Bank-Marketing-Term-Deposit/02_sub_desti_ratna_komala.ipynb)


### Objective
Sebuah bank di VietNam ingin memaksimalkan biaya pemasaran untuk produk deposito berjangka. Namun, pihak bank kesulitan dalam menentukan klien mana yang akan berlangganan pada produk tersebut. Oleh karena itu, dibutuhkan pemodelan untuk mengindentifikasi hal tersebut berdasarkan perilaku dan informasi data diri masing-masing pelanggan agar upaya pemasaran dapat lebih terarah dan efisien.

### Dataset Information

Dataset ini merupakan pemasaran yang dilakukan secara langsung via telepon (phone calls) oleh Bank VietNam, terdiri dari 42639 baris dan 16 kolom. Fitur target (term_deposit) menunjukkan apakah seorang klien akan berlangganan pada produk deposito berjangka atau tidak. Fitur target tersebut bernilai **0 : tidak berlangganan (not_subscribe)** dan **1 : berlangganan (subscribe)**.

Berikut adalah deskripsi dari masing-masing fitur pada dataset `Bank Customer in VietNam`

|Feature|Deskripsi|
|------|-------|
|ID|Nomor id client bank|
|age|Usia client bank|
|job|Jenis pekerjaan client bank|
|marital|status pernikahan client bank|
|education|tingkat pendidikan client bank||
|default|status apakah client bank pernah gagal bayar (default) kartu kredit?||
|housing|status apakah client bank mempunyai cicilan rumah?||
|loan|status apakah client bank mempunyai hutang pribadi?||
|balance|Jumlah saldo yang dimiliki client bank||
|month|Bulan terakhir client bank dihubungi|
|day|hari terakhir client bank dihubungi|
|duration|durasi kontak terakhir bank terhadap client|
|campaign| jumlah kontak yang telah dilakukan selama melakukan kampanye marketing|
|pdays|jumlah hari kontak terakhir setelah client dihubungi oleh tim marketing bank
|previous|jumlah kontak yang dilakukan sebelum tim marketing bank menghubungi client ini
|term_deposit|Status apakah client akan berlangganan tabungan berjangka (term_deposit) atau tidak?



Sehingga, dapat dikategorikan manjadi:

- **Data Klien Bank**

         'ID', 'age', 'marital', 'education', 'job', 'default', 'housing', 'loan', 'balance'


- **Kontak terakhir klien terhadap tim pemasaran**

       'day','month','duration','pdays', 'previous', 'campaign'



- **Status Deposito Berjangka**
        'term_deposit'

# Kesimpulan 

**Berdasarkan pemodelan** yang telah dilakukan, model tuning XGBoosting merupakan model terbaik dalam memprediksi apakah customer akan berlangganan deposito berjangka atau tidak. Dengan tingkat akurasi hingga 88%, tingkat klasifikasi sebesar 89% dan tingkat kesalahan prediksi yang sangat rendah sebesar 7%.

**Berdasarkan fiturnya**, klien yang memiliki cicilan rumah (**housing loan**) dan hutang pribadi(**personal loan**) menjadi indikator paling penting apakah seorang klien akan berlangganan deposito berjangka atau tidak.
Selain itu, pekerjaan **jobs**, status pernikahan **marital** dan durasi tim marketing memasarkan produk bank kepada klien **duration** menjadi faktor penting dalam menentukan apakah seorang klien akan berlangganan deposito berjangka atau tidak.


**Rekomendasi Strategi Pemasaran:**

- Melakukan Survei Target
    
  Menanyakan secara langsung/melakukan survei mendalam kepada klien yang telah bergabung dan yang akan bergabung dengan bank Anda. Berikan hadiah/kartu voucher sebagai reward telah mengisi survei dengan lengkap. Pastikan seluruh klien mengisi alasan mereka bergabung dengan bank Anda dan alasan mengapa mereka meninggalkan bank mereka sebelumnya. Berdasarkan hal tersebut, buatlah strategi bisnis yang sesuai dengan kebutuhan klien.

- Memberikan Penawaran sesuai data demografik

  Menggunakan informasi publik seperti tren produk, pendapatan per demografik, dan tingkat konsumerisasi pada lingkungan tersebut. Tawarkan produk-produk yang sedang trending pada klien dengan tingkat konsumerisasi yang tinggi. Untuk klien yang sudah berkeluarga, tawarkan bonus-bonus yang berhubungan dengan produk rumah tangga. Target utama pemasaran sebaiknya untuk klien dengan nilai `balance` yang tinggi. Karena semakin besar saldo yang dimiliki klien, semakin besar kemungkinan klien tersebut akan berlangganan deposito berjangka.

- Tingkatkan Kualitas Customer Service

  Customer service merupakan wajah yang mencerminkan kualitas suatu bank. Kehilangan klien akan lebih mahal ketimbang mempertahankan klien, oleh karena itu pemberian pelayanan terbaik dari pihak bank sangat perlu diutamakan. Buatlah strategi bagaimana supaya orang-orang yang sudah menjadi klien dapat tetap bertahan dan setia dengan bank Anda. Variasikan layanan yang ditawarkan kepada klien. Pastikan selalu mengecek perkembangan klien Anda dan berikan solusi yang menguntungkan kedua belah pihak jika klien tersebut memiliki masalah finansial.

- Taktik lainnya:
  - Bekerjasama dengan perusahaan/bank lain
  - Pemasaran sebaiknya dilakukan berdasarkan perilaku belanja klien
  - Lakukan pemasaran melalui medio online/onsite/via telepon
  - Highlight cerita-certa sukses klien
  






