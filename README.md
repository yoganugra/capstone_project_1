# Capstone Project Modul 1, Programming Fundamental - CRUD Project

## Diunggah sebagai capstone project module 1, Job Connector Data Science and Machine Learning - Purwadhika.

Program ini dirancang untuk siswa, terutama siswa kelas 12 semester 1, dan wali kelas masing-masing kelasnya.

Data dummy yang digunakan pada program ini adalah:
1. Lima Nomor Induk Siswa (NIS) dengan masing masing NIS berisikan:
    a. Nama Lengkap
    b. Kelas
    c. Rerata Nilai
    d. Nama Orang Tua/Wali
    e. Kontak Orang Tua/Wali
2. Lima jurusan saintek beserta passing gradenya untuk SNBP
3. Lima jurusan soshum beserta passing gradenya untuk SNBP

——————————————————————————————————————————————————————————————
Ketentuan data dummy yang digunakan pada program ini adalah:
1. NIS                    : sebagai primary key
2. Nama                   : Nama lengkap pemilik NIS
3. Kelas                  : Kelas dimana pemilik NIS belajar
4. Rerata Nilai           : Rerata nilai pemilik NIS dari kelas 10 semester 1 sampai kelas 12 semester 1 (5 semester)
5. Nama Orang Tua/Wali    : Nama orang tua/wali untuk dilakukan konsultasi mengenai perkembangan belajar di sekolah
6. Kontak Orang Tua/Wali  : Nomor handphone orang tua/wali untuk dilakukan komunikasi mengenai perkembangan belajar di sekolah, termasuk layak/tidaknya mendapatkan KIP-K.

——————————————————————————————————————————————————————————————
Program ini terdiri dari fitur utama dengan beberapa sub-fitur di dalamnya.

Untuk siswa sebagai user, hanya dapat mengakses fitur Read. Dimana, sub-fitur di dalamnya berisikan:
1. Menampilkan data siswa tersebut
2. Menampilkan urutan nilai dari semua siswa
3. Menampilkan urutan nilai dari semua siswa berdasarkan rumpun
4. Memprediksi nilai untuk persiapan SNBP

Untuk wali kelas sebagai user, dapat mengakses semua fitur pada program ini. Fitur tersebut berisikan:
1. Create (Menambah data siswa)
Menu Create terdiri dari penambahan siswa baru, dengan ketentuan:
  a. Menambahkan NIS sebagi primary-key
  b. Menambahkan nama lengkap siswa
  c. Menambahkan kelas siwa
  d. Menambahkan rerata nilai siswa
  e. Menambahkan nama orang tua/wali siswa
  f.  Menambahkan kontak orang tua/wali siswa
2. Read (Menampilkan data siswa)
Menu Read terdiri dari menampilkan data siswa, yang terdiri dari beberapa sub-fitur, yaitu:
  a. Menampilkan semua data siswa
  b. Menampilkan semua data siswa berdasarkan urutan nilai
  c. Menampilkan data siswa berdasarkan rumpun
  d. Menampilkan data siswa berdasarkan NIS tertentu
3. Memprediksi nilai untuk persiapan SNBP
Fitur tambahan ini membandingkan nilai siswa dengan nilai passing grade lima jurusan yang dipilih secara acak sebagai data dummy untuk tiap-tiap rumpun. 
4. Update (Merubah data siswa)
Menu Update terdiri dari merubah data siswa yang sudah ada, dengan ketentuan NIS harus sudah terdapat pada program ini, kemudian user dapat memilih untuk merubah:
  a. Nama lengkap siswa
  b. Kelas siwa
  c. Rerata nilai siswa
  d. Nama orang tua/wali siswa
  e.  Kontak orang tua/wali siswa
5. Delete (Menghapus data siswa)
Menu Delete terdiri dari penghapusan data yang sudah ada, yang terdiri dari beberapa sub-fitur, yaitu:
  a. Menghapus data siswa dengan NIS tertentu
  b. Menghapus seluruh data siswa
Setelah dilakukan penghapusan seluruh data, maka semua fitur, keculi fitur update, tidak dapat dijalankan.
——————————————————————————————————————————————————————————————
