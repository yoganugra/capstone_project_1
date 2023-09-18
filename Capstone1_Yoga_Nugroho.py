import os
os.system("clear")

# DATA DUMMY =========================
# Data-data di bawah ini adalah data dummy. Apabila ada kesamaan, itu murni merupakan ketidaksengajaan.

data_siswa = {
    'YG001':{'Nama'                 :'Muhammad Jaehyun',
             'Kelas'                :'12 IPA 1',
             'Rerata Nilai'         :92,
             'Nama Orang Tua/Wali'  :'Abdul Azis',
             'Kontak Orang Tua/Wali':'087851423695'},

    'YG002':{'Nama'                 :'Siti Nur Jennie',
            'Kelas'                 :'12 IPS 1',
            'Rerata Nilai'          :82,
            'Nama Orang Tua/Wali'   :'Eko Bagus',
            'Kontak Orang Tua/Wali':'085655030705'},

    'YG003':{'Nama'                 :'Abdul Taehyung',
            'Kelas'                 :'12 IPS 2',
            'Rerata Nilai'          :85,
            'Nama Orang Tua/Wali'   :'Nurul Qomari',
            'Kontak Orang Tua/Wali' :'087850605356'},

    'YG004':{'Nama'                 :'Sri Ningning',
            'Kelas'                 :'12 IPA 2',
            'Rerata Nilai'          :89,
            'Nama Orang Tua/Wali'   :'Ririn Agustina',
            'Kontak Orang Tua/Wali' :'085231770004'},

    'YG005':{'Nama'                 :'Nurul Jihyo',
            'Kelas'                 :'12 IPA 3',
            'Rerata Nilai'          :91,
            'Nama Orang Tua/Wali'   :'Zainul Arifin',
            'Kontak Orang Tua/Wali' :'087850032365'}
             }

lima_jurusan_saintek = (['Pendidikan Kedokteran',89.93],
                        ['Teknik Informatika',88.88], 
                        ['Ilmu Komputer', 88,88],
                        ['Farmasi',88.49], 
                        ['Keperawatan', 88.60])

lima_jurusan_soshum = (['Ilmu Komunikasi', 89.51],
                       ['Manajemen', 88.05],
                       ['Sastra Inggris', 84.94],
                       ['Akuntansi', 87.97],
                       ['Ilmu Psikologi', 89.52])

# KUMPULAN FUNGSI

# READ DATA ===========================
def menampilkanSemuaData():
    print('+' + '-'*114 + '+')
    print(f"| {'NIS':^6} | {'NAMA SISWA':^25} | {'KELAS':^8} | {'RERATA NILAI':^12} | {'NAMA ORANG TUA/WALI':^25} | {'KONTAK ORANG TUA/WALI':^21} |")   # NAMA KOLOM
    print('+' + '-'*114 + '+')
    # menampilkan semua data
    for key,value in data_siswa.items():
        print(f'| {key:^6} | {value["Nama"]:^25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} | {value["Nama Orang Tua/Wali"]:^25} | {value["Kontak Orang Tua/Wali"]:^21} |')
    # ketika items pada dict sudah kosong (terhapus semua)
    if len(data_siswa) == 0:
        print(f"|{'Tidak ada data murid tersimpan.':^114}|")
    print('+' + '-'*114 + '+')         

def menampilkanUrutanNilai():
    garisPembatas()
    print('1. Menampilkan nilai dari terbesar - terkecil')
    print('2. Menampilkan nilai dari terkecil - terbesar')
    garisPembatas()
    pilihan = input('Masukan pilihan: ')
    # nilai terbesar - terkecil (desc / reverse = True)
    if pilihan == '1':
        print('+' + '-'*62 + '+') 
        print(f'| {"NIS":^6} | {"Nama":<25} | {"Kelas":^8} | {"Rerata Nilai":^12} |') 
        print('+' + '-'*62 + '+')
        #sorted value menggunakan sorted dan lambda
        nilai_terurut = sorted(data_siswa.items(), key=lambda x:x[1]['Rerata Nilai'], reverse=True)
        for key,value in nilai_terurut:
            print(f'| {key:^6} | {value["Nama"]:<25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} |')

        if len(data_siswa) == 0:
            print(f"|{'Tidak ada data murid tersimpan.':^62}|")
        print('+' + '-'*62 + '+') 

    # nilai terkecil - terbesar (asc / reverse = False)
    elif pilihan == '2':
        print('+' + '-'*62 + '+') 
        print(f'| {"NIS":^6} | {"Nama":<25} | {"Kelas":^8} | {"Rerata Nilai":^12} |') 
        print('+' + '-'*62 + '+')
        nilai_terurut = sorted(data_siswa.items(), key=lambda x:x[1]['Rerata Nilai'], reverse=False)
        for key,value in nilai_terurut:
            print(f'| {key:^6} | {value["Nama"]:<25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} |')

        if len(data_siswa) == 0:
            print(f"|{'Tidak ada data murid tersimpan.':^62}|")
        print('+' + '-'*62 + '+') 
    
    else:
        garisPembatas()
        print(f"{'Pilih angka dari pilihan tersedia. Silakan ulangi.':^116}")
        garisPembatas()

def menampilkanUrutanNilaiRumpun():
    garisPembatas()
    print('1. Menampilkan nilai dari terbesar - terkecil rumpun IPA')
    print('2. Menampilkan nilai dari terkecil - terbesar rumpun IPA')
    print('3. Menampilkan nilai dari terbesar - terkecil rumpun IPS')
    print('4. Menampilkan nilai dari terkecil - terbesar rumpun IPS')
    garisPembatas()
    pilihan = input('Masukan pilihan: ')
    if pilihan == '1':
        print('+' + '-'*62 + '+') 
        print(f'| {"NIS":^6} | {"Nama":<25} | {"Kelas":^8} | {"Rerata Nilai":^12} |')
        print('+' + '-'*62 + '+')
        nilai_terurut = sorted(data_siswa.items(), key=lambda x:x[1]['Rerata Nilai'], reverse=True)
        for key,value in nilai_terurut:
            if value["Kelas"][3:-2] == 'IPA':
                print(f'| {key:^6} | {value["Nama"]:<25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} |')

        if len(data_siswa) == 0:
            print(f"|{'Tidak ada data murid tersimpan.':^62}|")
        print('+' + '-'*62 + '+') 

    elif pilihan == '2':
        print('+' + '-'*62 + '+') 
        print(f'| {"NIS":^6} | {"Nama":<25} | {"Kelas":^8} | {"Rerata Nilai":^12} |')
        print('+' + '-'*62 + '+')
        nilai_terurut = sorted(data_siswa.items(), key=lambda x:x[1]['Rerata Nilai'], reverse=False)
        for key,value in nilai_terurut:
            if value["Kelas"][3:-2] == 'IPA':
                print(f'| {key:^6} | {value["Nama"]:<25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} |')

        if len(data_siswa) == 0:
            print(f"|{'Tidak ada data murid tersimpan.':^62}|")
        print('+' + '-'*62 + '+') 
    
    elif pilihan == '3':
        print('+' + '-'*62 + '+')
        print(f'| {"NIS":^6} | {"Nama":<25} | {"Kelas":^8} | {"Rerata Nilai":^12} |')
        print('+' + '-'*62 + '+')
        nilai_terurut = sorted(data_siswa.items(), key=lambda x:x[1]['Rerata Nilai'], reverse=True)
        for key,value in nilai_terurut:
            if value["Kelas"][3:-2] == 'IPS':
                print(f'| {key:^6} | {value["Nama"]:<25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} |')

        if len(data_siswa) == 0:
            print(f"|{'Tidak ada data murid tersimpan.':^62}|")
        print('+' + '-'*62 + '+') 

    elif pilihan == '4':
        print('+' + '-'*62 + '+')
        print(f'| {"NIS":^6} | {"Nama":<25} | {"Kelas":^8} | {"Rerata Nilai":^12} |')
        print('+' + '-'*62 + '+')
        nilai_terurut = sorted(data_siswa.items(), key=lambda x:x[1]['Rerata Nilai'], reverse=False)
        # print(sorted_data)
        for key,value in nilai_terurut:
            if value["Kelas"][3:-2] == 'IPS':
                print(f'| {key:^6} | {value["Nama"]:<25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} |')
        if len(data_siswa) == 0:
            print(f"|{'Tidak ada data murid tersimpan.':^62}|")
        print('+' + '-'*62 + '+') 

    else:
        garisPembatas()
        print(f"{'Pilih angka dari pilihan tersedia. Silakan ulangi.':^116}")
        garisPembatas()

def menampilkanDataTertentu():
    nis_siswa = input('Masukan NIS\t\t\t: ').upper()
    garisPembatas()
    print(f'Berikut data siswa dengan NIS {nis_siswa}: ')
    if nis_siswa in data_siswa.keys():
        print('+' + '-'*114 + '+')
        print(f"| {'NIS':^6} | {'NAMA SISWA':^25} | {'KELAS':^8} | {'RERATA NILAI':^12} | {'NAMA ORANG TUA/WALI':^25} | {'KONTAK ORANG TUA/WALI':^21} |")   # NAMA KOLOM
        print('+' + '-'*114 + '+')
        for key, value in data_siswa.items():
            if key == nis_siswa:
                print(f'| {key:^6} | {value["Nama"]:^25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} | {value["Nama Orang Tua/Wali"]:^25} | {value["Kontak Orang Tua/Wali"]:^21} |')
                print('+' + '-'*114 + '+') 
        if len(data_siswa) == 0:
            print(f"| {'Tidak ada data murid tersimpan.':^114}|")
            print('+' + '-'*114 + '+') 
        
    else:
        garisPembatas()
        print(f'{"Siswa dengan NIS {} tidak terdaftar. Silakan periksa kembali dan masukan ulang.".format(nis_siswa):^116}')
        garisPembatas()

# CREATE DATA ==========================
def menambahkanData():
    print('+' + '-'*114 + '+') 
    print(f'''{'Baca intruksi di bawah ini sebelum menambahkan data: ':^116}
{('+' + '-'*114 + '+')}
1.  Format penulisan NIS adalah ['YG' + 3 angka]. Contoh: YG001.
2.  NIS yang diinput tidak boleh merupakan NIS yang sudah ada.
3.  Nama lengkap harus diinput sesuai dengan akta kelahiran, dengan panjang maksimal 25 karakter.
    Apabila nama terdiri lebih dari 25 karakter, silakan lakukan penyingkatan dan penggunaan akronim.
4.  Kelas siswa harus diinput dengan format [kelas (spasi) jurusan (spasi) angka]. Contoh: 12 IPA 1.
5.  Rerata nilai merupakan bilangan bulat rerata nilai dari semester 1 - 5. 
    Mohon direratakan dan dibulatkan ke bawah terlebih dahulu sebelum diinput.
6.  Nama lengkap orang tua / wali siswa harus diinput dengan ketentuan sama seperti menginput nama lengkap siswa.
7.  Nomor telepon orang tua / wali yang diinput harus merupakan nomor aktif yang dapat dihubungi.
{('+' + '-'*114 + '+')}
Apabila sudah dibaca dengan cermat, silakan lanjutkan mengisi isian di bawah ini.
''')
    while True:
        nis_siswa_baru              = input('Masukan NIS siswa\t\t\t\t\t: ').upper()
 
        # kondisi yang harus terpenuhi

        # NIS harus gabungan angka & huruf
        if nis_siswa_baru.isalpha() or nis_siswa_baru.isnumeric():
            garisPembatas()
            print(f"{'Format penulisan NIS: YG [spasi] 3 karakter angka (contoh: YG001)':^116}")
            garisPembatas()
            continue

        # NIS harus diawali 'YG'
        elif nis_siswa_baru[0:2] != 'YG':
            garisPembatas()
            print(f"{'NIS harus diawali dengan YG':^116})")
            garisPembatas()
            continue

        # NIS harus memiliki panjang karakter tepat di angka 5. Karena diasumsikan sekolah ini hanya bisa menampung maksimal 999 siswa aktif
        elif len(nis_siswa_baru) < 5 or len(nis_siswa_baru) > 5:
            garisPembatas()
            print(f"{'NIS harus terdiri dari lima karakter, gabungan dari 2 huruf (YG) dan 3 angka yang mengikuti kedua huruf tersebut':^116}")
            garisPembatas()
            continue

        # Jika NIS bukan merupakan duplikat, lanjutkan tahap pengisian
        elif nis_siswa_baru not in data_siswa.keys():
            while True:
                nama_siswa_baru             = input('Masukan nama lengkap siswa\t\t\t\t: ').title()
                # kondisi yang harus terpenuhi

                # Nama hanya boleh berisikan alphabet
                nama_salah = False
                for karakter in nama_siswa_baru:
                    if karakter.isdigit():
                        nama_salah = True

                if nama_salah:
                    garisPembatas()
                    print(f"{'Nama harus berupa kumpulan huruf yang dipisahkan dengan spasi. Tolong masukan nama sesuai dengan akta kelahiran.':^116}")
                    garisPembatas()
                    continue        

                # Nama tidak boleh berisikan kumpulan
                elif nama_siswa_baru.isspace():
                    garisPembatas()
                    print(f"{'Nama harus berupa kumpulan huruf yang dipisahkan dengan spasi. Tolong masukan nama sesuai dengan akta kelahiran.':^116}")
                    garisPembatas()
                    continue

                # Nama tidak boleh kosong
                elif len(nama_siswa_baru) == 0:
                    garisPembatas()
                    print(f"{'Nama tidak boleh kosong.':^116}")
                    garisPembatas()
                    continue

                # Nama tidak boleh memiliki panjang karakter lebih dari 25
                elif len(nama_siswa_baru) > 25:
                    garisPembatas()
                    print(f"{'Nama terlalu panjang. Silakan lakukan penyingkatan dan penggunaan akronim.':^116}")
                    garisPembatas()
                    continue  
                # Jika syarat sudah terpenuhi, lanjutkan pengisian
                else:
                    break
                
            while True:    
                kelas_siswa_baru            = input('Masukan kelas siswa\t\t\t\t\t: ').upper()
                # kondisi yang harus terpenuhi

                # Format penulisan kelas harus (kelas(10-12) [spasi] rumpun(IPA/IPS) [spasi] angka)
                if kelas_siswa_baru[0:2].isalpha() or kelas_siswa_baru[0:2].isspace() or int(kelas_siswa_baru[0:2]) not in (10,11,12) or kelas_siswa_baru[3:6] not in ('IPA','IPS') or len(kelas_siswa_baru) < 7:
                    garisPembatas()
                    print(f"{'Format penulisan kelas: kelas(10-12) [spasi] rumpun(IPA/IPS) [spasi] angka. Contoh: 12 IPA 2':^116}")
                    garisPembatas()
                    continue

                # Karakter terakhir pada kolom kelas, harus berupa angka
                elif not kelas_siswa_baru[-1].isdigit():
                    garisPembatas()
                    print(f"{'Format penulisan kelas: kelas(10-12) [spasi] rumpun(IPA/IPS) [spasi] angka. Contoh: 12 IPA 2':^116}")
                    garisPembatas()

                # Panjang karakter kelas harus tepat 7. Diasumsikan setiap kelas pada tiap rumpunnya hanya bisa menampung 9 kelas
                elif len(kelas_siswa_baru) < 8 or len(kelas_siswa_baru) > 8:
                    garisPembatas()
                    print(f"{'Angka kelas melebihi jumlah kelas yang ada. Mohon perhatikan kembali':^116}") 
                    garisPembatas()     
                # Jika syarat sudah terpenuhi, lanjutkan pengisian
                else:
                    break

            while True:
                rerata_nilai_baru           = input('Masukan rerata nilai siswa\t\t\t\t: ')
                # kondisi yang harus terpenuhi

                # Rerata nilai harus merupakan bilangan bulat. Jika bukan, dibulatkan ke bawah terlebih dahulu
                if not rerata_nilai_baru.isdigit():
                    garisPembatas()
                    print(f"{'Rerata nilai harus berupa bilangan bulat. Silakan bulatkan ke bawah':^116}")
                    garisPembatas()
                    continue
                # Jika syarat sudah terpenuhi, lanjutkan pengisian
                else:
                    break

            while True:
                nama_ortu_wali_siswa_baru   = input('Masukan nama lengkap orang tua / wali siswa\t\t: ').title()
                # kondisi yang harus terpenuhi

                # Nama hanya boleh berisikan alphabet
                nama_salah = False
                for karakter in nama_ortu_wali_siswa_baru:
                    if karakter.isdigit():
                        nama_salah = True

                if nama_salah:
                    garisPembatas()
                    print(f"{'Nama harus berupa kumpulan huruf yang dipisahkan dengan spasi. Tolong masukan nama sesuai dengan akta kelahiran.':^116}")
                    garisPembatas()
                    continue 
                
                # Nama tidak boleh memiliki panjang karakter lebih dari 25
                elif len(nama_ortu_wali_siswa_baru) > 25:
                    garisPembatas()
                    print(f"{'Nama terlalu panjang. Silakan lakukan penyingkatan dan penggunaan akronim.':^116}")
                    garisPembatas()
                    continue 

                # Nama tidak boleh kosong
                elif len(nama_ortu_wali_siswa_baru) == 0:
                    garisPembatas()
                    print(f"{'Nama tidak boleh kosong.':^116}")
                    garisPembatas()
                    continue

                # Nama tidak boleh berisikan kumpulan spasi
                elif nama_ortu_wali_siswa_baru.isspace():
                    garisPembatas()
                    print(f"{'Nama harus berupa kumpulan huruf. Tolong masukan nama sesuai dengan akta kelahiran.':^116}")
                    garisPembatas()
                    continue
                # Jika syarat sudah terpenuhi, lanjutkan pengisian
                else:
                    break

            while True:    
                kontak_ortu_wali_siswa_baru = input('Masukan nomor telepon aktif orang tua / wali siswa\t: ')
                panjang_nomor_kontak        = len(kontak_ortu_wali_siswa_baru)
                maksimal_nomor              =  13
                # kondisi yang harus terpenuhi

                # Kontak harus merupakan kumpulan angka
                if not kontak_ortu_wali_siswa_baru.isdigit():
                    garisPembatas()
                    print(f"{'Nomor kontak harus berupa kumpulan angka':^116}")
                    garisPembatas()
                    continue

                # Panjang kontak tidak boleh lebih dari 13
                elif panjang_nomor_kontak > maksimal_nomor:
                    garisPembatas()
                    print(f"{'Jumlah maksimal angka pada nomor telepon adalah 13 digit. Tolong masukan nomor yang valid.':^116}")
                    garisPembatas()
                    continue

                # Panjang kontak tidak kurang dari 11
                elif panjang_nomor_kontak < 11:
                    garisPembatas()
                    print(f"{'Jumlah minimal angka pada nomor telepon adalah 11 digit. Tolong masukan nomor yang valid.':^116}")
                    garisPembatas()
                    continue

                # Kontak diasumsikan harus nomor telepon di Indonesia, dimulai dengan 08
                elif kontak_ortu_wali_siswa_baru[0:2] != '08':
                    garisPembatas()
                    print(f"{'Nomor telepon harus dimulai dengan 08':^116}")
                    garisPembatas()
                    continue
                # Jika syarat sudah terpenuhi, lanjutkan pengisian
                else:
                    break

            # Setelah semua isian benar, maka masukan data ke dalam data dummy (dict)
            while True:
                print('-'*116)
                print(f'''{"REKAPITULASI INPUT DATA BARU":^116}
nama            : {nama_siswa_baru}
kelas           : {kelas_siswa_baru}
rerata nilai    : {rerata_nilai_baru}
nama ortu/wali  : {nama_ortu_wali_siswa_baru}
kontak ortu/wali: {kontak_ortu_wali_siswa_baru}''')

                print('-'*116)
                konfirmasi_penambahan = input("Apakah Anda yakin akan menambahkan data? (ya/tidak):  ").lower()
                print('-'*116)
                # konfirmasi penambahan
                if konfirmasi_penambahan == 'ya':
                    data_siswa[nis_siswa_baru] = {'Nama'                    : nama_siswa_baru,
                                                  'Kelas'                   : kelas_siswa_baru,
                                                  'Rerata Nilai'            : int(rerata_nilai_baru),
                                                  'Nama Orang Tua/Wali'     : nama_ortu_wali_siswa_baru,
                                                  'Kontak Orang Tua/Wali'   : kontak_ortu_wali_siswa_baru}
                    garisPembatas()
                    print(f"{'Data berhasil ditambahkan!':^116}")
                    garisPembatas()
                    menampilkanSemuaData()
                    print('\n')
                    break
                elif konfirmasi_penambahan == 'tidak':
                    garisPembatas()
                    print(f"{'Data tidak ditambahkan.':^116}")
                    garisPembatas()
                    break
                else:
                    garisPembatas()
                    print(f"{'Masukan antara ya dan tidak. Silakan ulangi.':^116}")
                    garisPembatas()
                    continue
            break
                    
        # Jika NIS merupakan duplikat
        else:
            garisPembatas()
            print(f"{'NIS sudah ada! Periksa ulang NIS dan silakan input kembali.':^116}")
            garisPembatas()
            continue
        
# UPDATE DATA ==========================

def merubahData():
    while True:
        rubah_nis_siswa = input('Masukan NIS siswa yang ingin diubah datanya: ').upper()
        if rubah_nis_siswa in data_siswa.keys():
            print('+' + '-'*114 + '+')
            print(f"| {'NIS':^6} | {'NAMA SISWA':^25} | {'KELAS':^8} | {'RERATA NILAI':^12} | {'NAMA ORANG TUA/WALI':^25} | {'KONTAK ORANG TUA/WALI':^21} |")   # NAMA KOLOM
            print('+' + '-'*114 + '+')
            for key, value in data_siswa.items():
                if key == rubah_nis_siswa:
                    print(f'| {key:^6} | {value["Nama"]:^25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} | {value["Nama Orang Tua/Wali"]:^25} | {value["Kontak Orang Tua/Wali"]:^21} |')
                    print('+' + '-'*114 + '+') 

            print('''Data apa yang mau diubah?
1. Nama
2. Kelas
3. Rerata Nilai
4. Nama Orang Tua / Wali
5. Kontak Orang Tua / Wali
6. Kembali ke menu merubah data''')
            pilih_ubah = input('Masukan pilihan: ')
            while True:
                if pilih_ubah   == '1':
                    nama_baru = input('Masukan nama baru: ').title()
                    nama_salah = False
                    for karakter in nama_baru:
                        if karakter.isdigit():
                            nama_salah = True
                    if nama_salah:
                        garisPembatas()
                        print(f"{'Nama harus berupa kumpulan huruf. Tolong masukan nama sesuai dengan akta kelahiran.':^116}")
                        garisPembatas()
                        continue
                    elif nama_baru == data_siswa[rubah_nis_siswa]['Nama']:
                        garisPembatas()
                        print(f"{'Nama sudah ada!':^116}")
                        garisPembatas()
                        continue
                    elif nama_baru.isspace():
                        garisPembatas()
                        print(f"{'Nama harus berupa kumpulan huruf. Tolong masukan nama sesuai dengan akta kelahiran.':^116}")
                        garisPembatas()
                        continue
                    elif len(nama_baru) > 25:
                        garisPembatas()
                        print(f"{'Nama terlalu panjang. Silakan lakukan penyingkatan dan penggunaan akronim.':^116}")
                        garisPembatas()
                        continue         
                    elif len(nama_baru) == 0:
                        garisPembatas()
                        print(f"{'Nama tidak boleh kosong.':^116}")
                        garisPembatas()
                        continue
                    else:
                        garisPembatas()
                        print(f"{'Rubah data dari {} jadi {}?'.format(data_siswa[rubah_nis_siswa]['Nama'],nama_baru):^116}")
                        garisPembatas()
                        konfirmasi_perubahan = input('Ubah data?(ya/tidak): ').lower()
                        if konfirmasi_perubahan == 'tidak':
                            garisPembatas()
                            print(f"{'Tidak ada perubahan data.':^116}")
                            garisPembatas()
                        elif konfirmasi_perubahan == 'ya':
                            data_siswa[rubah_nis_siswa]['Nama'] = nama_baru
                            print('+' + '-'*114 + '+')
                            print(f"| {'NIS':^6} | {'NAMA SISWA':^25} | {'KELAS':^8} | {'RERATA NILAI':^12} | {'NAMA ORANG TUA/WALI':^25} | {'KONTAK ORANG TUA/WALI':^21} |")   # NAMA KOLOM
                            print('+' + '-'*114 + '+')
                            for key, value in data_siswa.items():
                                if key == rubah_nis_siswa:
                                    print(f'| {key:^6} | {value["Nama"]:^25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} | {value["Nama Orang Tua/Wali"]:^25} | {value["Kontak Orang Tua/Wali"]:^21} |')
                                    print('+' + '-'*114 + '+')
                            garisPembatas() 
                            print(f"{'Data berhasil diubah.':^116}")
                            garisPembatas()
                            break
                        else:
                            garisPembatas()
                            print(f'{"Masukan antara ya atau tidak. Silakan ulangi.":^116}')
                            garisPembatas()
                            break
                    break


                elif pilih_ubah == '2':
                    kelas_baru = input('Masukan kelas baru: ').upper()
                    if kelas_baru == data_siswa[rubah_nis_siswa]['Kelas']:
                        garisPembatas()
                        print(f"{'Siswa sudah di kelas tersebut!':^116}")
                        garisPembatas()
                    elif kelas_baru[0:2].isalpha() or kelas_baru[0:2].isspace() or int(kelas_baru[0:2]) not in (10,11,12) or kelas_baru[3:6] not in ('IPA','IPS') or len(kelas_baru) < 7:
                        garisPembatas()
                        print(f"{'Format penulisan kelas: kelas(10-12) [spasi] rumpun(IPA/IPS) [spasi] angka. Contoh: 12 IPA 2':^116}")
                        garisPembatas()
                        continue
                    elif not kelas_baru[-1].isdigit():
                        garisPembatas()
                        print(f"{'Format penulisan kelas: kelas(10-12) [spasi] rumpun(IPA/IPS) [spasi] angka. Contoh: 12 IPA 2':^116}")
                        garisPembatas()
                        continue
                    elif len(kelas_baru) < 8 or len(kelas_baru) > 8:
                        garisPembatas()
                        print(f"{'Angka kelas melebihi jumlah kelas yang ada. Mohon perhatikan kembali.':^116}") 
                        garisPembatas()
                        continue  
                    else:
                        garisPembatas()
                        print(f"{'Rubah data dari {} jadi {}?'.format(data_siswa[rubah_nis_siswa]['Kelas'],kelas_baru):^116}")
                        garisPembatas()
                        konfirmasi_perubahan = input('Ubah data?(ya/tidak): ').lower()
                        if konfirmasi_perubahan == 'tidak':
                            garisPembatas()
                            print(f"{'Tidak ada perubahan data.':^116}")
                            garisPembatas()
                        elif konfirmasi_perubahan == 'ya':
                            data_siswa[rubah_nis_siswa]['Kelas'] = kelas_baru
                            print('+' + '-'*114 + '+')
                            print(f"| {'NIS':^6} | {'NAMA SISWA':^25} | {'KELAS':^8} | {'RERATA NILAI':^12} | {'NAMA ORANG TUA/WALI':^25} | {'KONTAK ORANG TUA/WALI':^21} |")   # NAMA KOLOM
                            print('+' + '-'*114 + '+')
                            for key, value in data_siswa.items():
                                if key == rubah_nis_siswa:
                                    print(f'| {key:^6} | {value["Nama"]:^25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} | {value["Nama Orang Tua/Wali"]:^25} | {value["Kontak Orang Tua/Wali"]:^21} |')
                                    print('+' + '-'*114 + '+') 
                            garisPembatas()
                            print(f"{'Data berhasil diubah.':^116}")
                            garisPembatas()
                        else:
                            garisPembatas()
                            print(f'{"Masukan antara ya atau tidak. Silakan ulangi.":^116}')
                            garisPembatas()
                            break
                    break

                elif pilih_ubah == '3':
                    rerata_nilai_baru = input('Masukan rerata nilai baru: ')
                    if not rerata_nilai_baru.isdigit():
                        garisPembatas()
                        print(f"{'Rerata nilai harus berupa angka.':^116}")
                        garisPembatas()
                        continue
                    elif int(rerata_nilai_baru) == data_siswa[rubah_nis_siswa]['Rerata Nilai']:
                        garisPembatas()
                        print(f"{'Rerata nilai sama dengan sebelummya!':^116}")
                        garisPembatas()
                        continue
                    else:
                        garisPembatas()
                        print(f"{'Rubah data dari {} jadi {}?'.format(data_siswa[rubah_nis_siswa]['Rerata Nilai'],rerata_nilai_baru):^116}")
                        garisPembatas()
                        konfirmasi_perubahan = input('Ubah data?(ya/tidak): ').lower()
                        if konfirmasi_perubahan == 'tidak':
                            print('d')
                            garisPembatas()
                            print(f"{'Tidak ada perubahan data.':^116}")
                            garisPembatas()
                        elif konfirmasi_perubahan == 'ya':
                            data_siswa[rubah_nis_siswa]['Rerata Nilai'] = rerata_nilai_baru
                            print('+' + '-'*114 + '+')
                            print(f"| {'NIS':^6} | {'NAMA SISWA':^25} | {'KELAS':^8} | {'RERATA NILAI':^12} | {'NAMA ORANG TUA/WALI':^25} | {'KONTAK ORANG TUA/WALI':^21} |")   # NAMA KOLOM
                            print('+' + '-'*114 + '+')
                            for key, value in data_siswa.items():
                                if key == rubah_nis_siswa:
                                    print(f'| {key:^6} | {value["Nama"]:^25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} | {value["Nama Orang Tua/Wali"]:^25} | {value["Kontak Orang Tua/Wali"]:^21} |')
                                    print('+' + '-'*114 + '+') 
                            garisPembatas()
                            print(f"{'Data berhasil diubah.':^116}")
                            garisPembatas()
                        else:
                            garisPembatas()
                            print(f'{"Masukan antara ya atau tidak. Silakan ulangi.":^116}')
                            garisPembatas()
                            break      
                    break

                elif pilih_ubah == '4':
                    nama_ortu_wali_baru     = input('Masukan nama orang tua / wali baru: ').title()
                    nama_salah = False
                    for karakter in nama_ortu_wali_baru:
                        if karakter.isdigit():
                            nama_salah = True
                    if nama_salah:
                        garisPembatas()
                        print(f"{'Nama harus berupa kumpulan huruf. Tolong masukan nama sesuai dengan akta kelahiran.':^116}")
                        garisPembatas()
                        continue
                    elif nama_ortu_wali_baru == data_siswa[rubah_nis_siswa]['Nama Orang Tua/Wali']:
                        garisPembatas()
                        print(f"{'Nama orang tua/wali masih sama!':^116}")
                        garisPembatas()
                    elif nama_ortu_wali_baru.isspace():
                        garisPembatas()
                        print(f"{'Nama harus berupa kumpulan huruf. Tolong masukan nama sesuai dengan akta kelahiran.':^116}")
                        garisPembatas()
                        continue
                    elif len(nama_ortu_wali_baru) > 25:
                        garisPembatas()
                        print(f"{'Nama terlalu panjang. Silakan lakukan penyingkatan dan penggunaan akronim.':^116}")
                        garisPembatas()
                        continue          
                    elif len(nama_ortu_wali_baru) == 0:
                        garisPembatas()
                        print(f"{'Nama tidak boleh kosong.':^116}")
                        garisPembatas()
                        continue
                    else:
                        garisPembatas()
                        print(f"{'Rubah data dari {} jadi {}?'.format(data_siswa[rubah_nis_siswa]['Nama Orang Tua/Wali'],nama_ortu_wali_baru):^116}")
                        garisPembatas()
                        konfirmasi_perubahan = input('Ubah data?(ya/tidak): ').lower()
                        if konfirmasi_perubahan == 'tidak':
                            garisPembatas()
                            print(f"{'Tidak ada perubahan data':^116}")
                            garisPembatas()
                        elif konfirmasi_perubahan == 'ya':
                            data_siswa[rubah_nis_siswa]['Nama Orang Tua/Wali'] = nama_ortu_wali_baru
                            print('+' + '-'*114 + '+')
                            print(f"| {'NIS':^6} | {'NAMA SISWA':^25} | {'KELAS':^8} | {'RERATA NILAI':^12} | {'NAMA ORANG TUA/WALI':^25} | {'KONTAK ORANG TUA/WALI':^21} |")   # NAMA KOLOM
                            print('+' + '-'*114 + '+')
                            for key, value in data_siswa.items():
                                if key == rubah_nis_siswa:
                                    print(f'| {key:^6} | {value["Nama"]:^25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} | {value["Nama Orang Tua/Wali"]:^25} | {value["Kontak Orang Tua/Wali"]:^21} |')
                                    print('+' + '-'*114 + '+') 
                            garisPembatas()
                            print(f"{'Data berhasil diubah.':^116}")
                            garisPembatas()
                        else:
                            garisPembatas()
                            print(f'{"Masukan antara ya atau tidak. Silakan ulangi.":^116}')
                            garisPembatas()
                            break      
                    break

                elif pilih_ubah == '5':
                    kontak_ortu_wali_baru   = input('Masukan kontak orang tua / wali baru: ')
                    maksimal_nomor          = 13
                    panjang_nomor_kontak    = len(kontak_ortu_wali_baru)

                    if kontak_ortu_wali_baru == data_siswa[rubah_nis_siswa]["Kontak Orang Tua/Wali"]:
                        garisPembatas()
                        print(f"{'Nomor kontak orang tua/wali masih sama!':^116}")
                        garisPembatas()
                        continue
                    elif not kontak_ortu_wali_baru.isdigit():
                        garisPembatas()
                        print(f"{'Nomor kontak harus berupa kumpulan angka.':^116}")
                        garisPembatas()
                        continue
                    elif panjang_nomor_kontak > maksimal_nomor:
                        garisPembatas()
                        print(f"{'Jumlah maksimal angka pada nomor telepon adalah 13 digit. Tolong masukan nomor yang valid.':^116}")
                        garisPembatas()
                        continue
                    elif panjang_nomor_kontak < 11:
                        garisPembatas()
                        print(f"{'Jumlah minimal angka pada nomor telepon adalah 11 digit. Tolong masukan nomor yang valid.':^116}")
                        garisPembatas()
                        continue
                    elif kontak_ortu_wali_baru[0:2] != '08':
                        garisPembatas()
                        print(f"{'Nomor telepon harus dimulai dengan 08.':^116}")
                        garisPembatas()
                        continue
                    else:
                        garisPembatas()
                        print(f"{'Rubah data dari {} jadi {}?'.format(data_siswa[rubah_nis_siswa]['Kontak Orang Tua/Wali'],kontak_ortu_wali_baru):^116}")
                        garisPembatas()
                        konfirmasi_perubahan = input('Ubah data?(ya/tidak): ').lower()
                        if konfirmasi_perubahan == 'tidak':
                            garisPembatas()
                            print(f"{'Tidak ada perubahan data.':^116}")
                            garisPembatas()
                        elif konfirmasi_perubahan == 'ya':
                            data_siswa[rubah_nis_siswa]["Kontak Orang Tua/Wali"] = kontak_ortu_wali_baru
                            print('+' + '-'*114 + '+')
                            print(f"| {'NIS':^6} | {'NAMA SISWA':^25} | {'KELAS':^8} | {'RERATA NILAI':^12} | {'NAMA ORANG TUA/WALI':^25} | {'KONTAK ORANG TUA/WALI':^21} |")   # NAMA KOLOM
                            print('+' + '-'*114 + '+')
                            for key, value in data_siswa.items():
                                if key == rubah_nis_siswa:
                                    print(f'| {key:^6} | {value["Nama"]:^25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} | {value["Nama Orang Tua/Wali"]:^25} | {value["Kontak Orang Tua/Wali"]:^21} |')
                                    print('+' + '-'*114 + '+') 
                            garisPembatas()
                            print(f"{'Data berhasil diubah.':^116}")
                            garisPembatas()
                        else:
                            garisPembatas()
                            print(f'{"Masukan antara ya atau tidak. Silakan ulangi.":^116}')
                            garisPembatas()
                            break      
                    break

                elif pilih_ubah == '6':
                    break

                else:
                    garisPembatas()
                    print(f"{'Masukan nomor dari pilihan yang tersedia. Silakan Ulangi':^116}")
                    garisPembatas()
                    break
            break

        else:
            garisPembatas()
            print(f"{'Tidak ada siswa dengan NIS {}. Silakan cek dan ulangi.'.format(rubah_nis_siswa):^116}")
            garisPembatas()
            continue

# PREDIKSI SNBP =========================
def prediksi_jurusan():
    while True:
        nis_siswa = input('Masukan NISmu: ').upper()
        if nis_siswa in data_siswa.keys():
            print('+' + '-'*114 + '+')
            print(f"| {'NIS':^6} | {'NAMA SISWA':^25} | {'KELAS':^8} | {'RERATA NILAI':^12} | {'NAMA ORANG TUA/WALI':^25} | {'KONTAK ORANG TUA/WALI':^21} |")   # NAMA KOLOM
            print('+' + '-'*114 + '+')
            for key, value in data_siswa.items():
                if key == nis_siswa:
                    print(f'| {key:^6} | {value["Nama"]:^25} | {value["Kelas"]:^8} | {value["Rerata Nilai"]:^12} | {value["Nama Orang Tua/Wali"]:^25} | {value["Kontak Orang Tua/Wali"]:^21} |')
                    print('+' + '-'*114 + '+') 
        else:
            garisPembatas()
            print(f"{'Periksa kembali NISmu!':^116}")
            garisPembatas()
            continue

        while True:
            # ketika siswa merupakan bagian dari kelas IPA
            if data_siswa[nis_siswa]["Kelas"][3:-2] == 'IPA':
                print(f'Karena kamu merupakan bagian dari kelas {data_siswa[nis_siswa]["Kelas"][3:-2]}, maka pilihan jurusan SNBPmu harus bagian dari ILMU EKSAKTA/SAINTEK.')
                print('Berikut beberapa jurusan yang bisa kamu prediksi: ')
                # menampilkan lima jurusan saintek
                for index,i in enumerate(lima_jurusan_saintek):
                    print(f'{index + 1}. {i[0]}')

                pilih_jurusan = input("Masukan pilihanmu: ")
                if pilih_jurusan in ('1','2','3','4','5'):
                    print(f'Nilaimu\t\t\t\t: {data_siswa[nis_siswa]["Rerata Nilai"]}')
                    print(f'Nilai minimal pilihan jurusanmu\t: {lima_jurusan_saintek[int(pilih_jurusan) - 1][1]}')
                    # Menampilkan selisih
                    if data_siswa[nis_siswa]["Rerata Nilai"] > lima_jurusan_saintek[int(pilih_jurusan) - 1][1]:
                        garisPembatas()
                        print(f'{"Pertahankan! Nilaimu lebih besar {} dari prediksi.".format(round(data_siswa[nis_siswa]["Rerata Nilai"] - lima_jurusan_saintek[int(pilih_jurusan) - 1][1],2)):^116}')
                        garisPembatas()
                    elif data_siswa[nis_siswa]["Rerata Nilai"] == lima_jurusan_saintek[int(pilih_jurusan) - 1][1]:
                        garisPembatas()
                        print(f'{"Tingkatkan! Nilaimu sama dengan nilai dari prediksi, dengan selisih.":^116}')
                        garisPembatas()
                    else:
                        garisPembatas()
                        print(f'{"Nilaimu {} lebih kecil dari prediksi. Silakan lakukan konsultasi lanjutan di BK.".format(round(lima_jurusan_saintek[int(pilih_jurusan) - 1][1] - data_siswa[nis_siswa]["Rerata Nilai"],2)):^116}')
                        garisPembatas()
                else:
                    garisPembatas()
                    print(f"{'Masukan pilihan yang tersedia. Jika tidak ada, bawa semua berkas dan konsultasikan langsung ke BK.':^116}")
                    garisPembatas()
                    break

                prediksi_lagi = input('Prediksi pilihan lain? (ya/tidak): ' ).lower()
                if prediksi_lagi == 'ya':
                    continue
                elif prediksi_lagi == 'tidak':
                    break
                else:
                    garisPembatas()
                    print(f"{'Masukan pilihan antara ya atau tidak. Silakan ulangi':^116}")
                    garisPembatas()
                    break

            # ketika siswa merupakan bagian dari kelas IPS
            elif data_siswa[nis_siswa]["Kelas"][3:-2] == 'IPS':
                print(f'Karena kamu merupakan bagian dari kelas {data_siswa[nis_siswa]["Kelas"][3:-2]}, maka pilihan jurusan SNBPmu harus bagian dari ILMU SOSIAL/SOSHUM.')
                print('Berikut beberapa jurusan yang bisa kamu prediksi: ')
                # menampilkan lima jurusan soshum
                for index,i in enumerate(lima_jurusan_soshum):
                    print(f'{index + 1}. {i[0]}')

                pilih_jurusan = input("Masukan pilihanmu: ")
                if pilih_jurusan in ('1','2','3','4','5'):
                    print(f'Nilaimu\t\t\t\t: {data_siswa[nis_siswa]["Rerata Nilai"]}')
                    print(f'Nilai minimal pilihan jurusanmu\t: {lima_jurusan_soshum[int(pilih_jurusan) - 1][1]}')
                    # Menampilkan selisih
                    if data_siswa[nis_siswa]["Rerata Nilai"] > lima_jurusan_soshum[int(pilih_jurusan) - 1][1]:
                        garisPembatas()
                        print(f'{"Pertahankan! Nilaimu lebih besar {} dari prediksi.".format(round(data_siswa[nis_siswa]["Rerata Nilai"] - lima_jurusan_soshum[int(pilih_jurusan) - 1][1],2)):^116}')
                        garisPembatas()
                    elif data_siswa[nis_siswa]["Rerata Nilai"] == lima_jurusan_soshum[int(pilih_jurusan) - 1][1]:
                        garisPembatas()
                        print(f'{"Tingkatkan! Nilaimu sama dengan nilai dari prediksi, dengan selisih.":^116}')
                        garisPembatas()
                    else:
                        garisPembatas()
                        print(f'{"Nilaimu {} lebih kecil dari prediksi. Silakan lakukan konsultasi lanjutan di BK.".format(round(lima_jurusan_soshum[int(pilih_jurusan) - 1][1] - data_siswa[nis_siswa]["Rerata Nilai"],2)):^116}')
                        garisPembatas()
                else:
                    garisPembatas()
                    print(f"{'Masukan pilihan yang tersedia. Jika tidak ada, bawa semua berkas dan konsultasikan langsung ke BK.':^116}")
                    garisPembatas()
                    break

                prediksi_lagi = input('Prediksi pilihan lain? (ya/tidak): ' ).lower()
                if prediksi_lagi == 'ya':
                    continue
                elif prediksi_lagi == 'tidak':
                    break
                else:
                    garisPembatas()
                    print(f"{'Masukan antara ya atau tidak. Silakan ulangi.':^116}")
                    garisPembatas()
                    break
        break

# DELETE DATA =======================
def menghapusData():
    menampilkanSemuaData()
    hapus_data = input('Masukan NIS siswa yang ingin dihapus: ').upper()
    if hapus_data in data_siswa.keys():
        print('+' + '-'*114 + '+')
        print(f"| {'NIS':^6} | {'NAMA SISWA':^25} | {'KELAS':^8} | {'RERATA NILAI':^12} | {'NAMA ORANG TUA/WALI':^25} | {'KONTAK ORANG TUA/WALI':^21} |")   # NAMA KOLOM
        print('+' + '-'*114 + '+') 
        for key,value in data_siswa.items():
            if hapus_data == key:
                print(f'| {key:^6} | {data_siswa[key]["Nama"]:^25} | {data_siswa[key]["Kelas"]:^8} | {data_siswa[key]["Rerata Nilai"]:^12} | {data_siswa[key]["Nama Orang Tua/Wali"]:^25} | {data_siswa[key]["Kontak Orang Tua/Wali"]:^21} |')
                print('+' + '-'*114 + '+') 
        while True:
            konfirmasi_hapus = input('Apakah anda yakin ingin menghapus data siswa ini (ya/tidak)?: ').lower()
            if konfirmasi_hapus   == 'ya':
                del data_siswa[hapus_data]
                garisPembatas()
                print(f"{'Siswa dengan NIM {} berhasil dihapus.'.format(hapus_data):^116}")
                garisPembatas()
                break
            elif konfirmasi_hapus == 'tidak':
                garisPembatas()
                print(f"{'Tidak ada data terhapus.':^116}")
                garisPembatas()
                break
            else:
                garisPembatas()
                print(f"{'Masukan antara ya atau tidak. Silakan ulangi.':^116}")
                garisPembatas()
    else:
        garisPembatas()
        print(f"{'Tidak ada siswa dengan NIS {}. Silakan periksa kembali daftar NIS dan ulangi'.format(hapus_data):^116}")
        garisPembatas()

def menghapusSemuaData():
    garisPembatas()
    print('Catatan: data yang akan dihapus tidak dapat dipulihkan!')
    garisPembatas()
    konfirmasi_hapus = input('Hapus semua data siswa (ya/tidak)?: ').lower()
    if konfirmasi_hapus   == 'ya':
        data_siswa.clear()
        garisPembatas()
        print(f"{'Semua data berhasil dihapus.':^116}")
        garisPembatas()
    elif konfirmasi_hapus == 'tidak':
        garisPembatas()
        print(f"{'Tidak ada data terhapus.':^116}")
        garisPembatas()
    else:
        garisPembatas()
        print(f"{'Masukan antara ya atau tidak. Silakan ulangi.':^116}")
        garisPembatas()

# PEMBATAS ==========================
def garisPembatas():
    print('+' + '-'*114 + '+')
# ===================================

# ===================================
# MAIN PROGRAM
while True:
    # HEADER SELAMAT DATANG
    print('+' + '-'*114 + '+')
    print(f"|{'Selamat Datang di':^114}|")
    print(f"|{'Database SMA Swasta Yoga Nugroho':^114}|")
    print('+' + '-'*114 + '+')
    
    # ENTRANCE
    garisPembatas()
    print(f"|{'1. Masuk sebagai siswa':114}|")
    print(f"|{'2. Masuk sebagai wali kelas':114}|")
    print(f"|{'3. Keluar':114}|")
    garisPembatas()
    identifikasi_pengguna = input('Masukan pilihan: ')

    if identifikasi_pengguna == '1':
    # MENU UTAMA - SISWA
        if len(data_siswa) != 0:
            while True:
                print('\n')
                garisPembatas()
                print(f"|{'MENU UTAMA - SISWA':^114}|")
                garisPembatas()
                menu = input('''Daftar Menu
1. Menampilkan datamu
2. Menampilkan urutan nilai dari semua siswa
3. Menampilkan urutan nilai dari semua siswa berdasarkan rumpun
4. Memprediksi nilai untuk persiapan SNBP
5. Kembali
6. Keluar dari program
Pilih menu yang diinginkan: ''') 
                if menu   == '1':
                    menampilkanDataTertentu()
                elif menu == '2':
                    menampilkanUrutanNilai()
                elif menu == '3':
                    menampilkanUrutanNilaiRumpun()
                elif menu == '4':
                    prediksi_jurusan()
                elif menu == '5':
                    break
                elif menu == '6':
                    garisPembatas()
                    print(f"|{'Terimakasih':^114}|")
                    garisPembatas()
                    exit()
                else:
                    garisPembatas() 
                    print(f'{"Pilihan yang kamu pilih tidak valid. Silakan ulangi dan masukan angka dari pilihan yang tersedia.":^116}')
                    garisPembatas() 
                    continue
        else:
            menampilkanSemuaData()
            garisPembatas()
            print(f"{'Tidak ada data tersimpan. Silakan laporkan pada wali kelasmu!':^116}")
            garisPembatas()           
            print('\n')

    elif identifikasi_pengguna == '2':
    # MENU UTAMA - WALI KELAS
        while True:
            print('\n')
            garisPembatas()
            print(f"|{'MENU UTAMA - WALI KELAS':^114}|")
            garisPembatas()
            menu = input('''Daftar Menu
1. Menampilkan data siswa
2. Menambah data siswa
3. Merubah data siswa
4. Memprediksi nilai untuk persiapan SNBP
5. Menghapus data siswa
6. Kembali
7. Keluar dari program
Pilih menu yang diinginkan: ''') 

        # MENU 1. READ
            if menu == '1':
                if len(data_siswa) != 0:
                    while True:
                        print('\n')
                        garisPembatas()
                        print(f"|{'MENU MENAMPILKAN DATA':^114}|")
                        garisPembatas()
                        
                        menu_tambahan_1 = input('''Daftar Menu
1. Semua data siswa
2. Semua data siswa berdasarkan urutan nilai
3. Semua data siswa berdasarkan rumpun
4. Semua data siswa berdasarkan NIS tertentu
5. Kembali ke menu utama
Pilih menu yang diinginkan: ''')
                        if menu_tambahan_1   == '1':
                            menampilkanSemuaData()
                        elif menu_tambahan_1 == '2':
                            menampilkanUrutanNilai()
                        elif menu_tambahan_1 == '3':
                            menampilkanUrutanNilaiRumpun()
                        elif menu_tambahan_1 == '4':
                            menampilkanDataTertentu()
                        elif menu_tambahan_1 == '5':
                            break
                        else:
                            garisPembatas()
                            print(f"{'Pilih angka dari pilihan tersedia, silakan pilih kembali.':^116}")
                            garisPembatas()
                            continue
                else:
                    menampilkanSemuaData()
                    garisPembatas()
                    print(f"{'Tidak ada data tersimpan. Silakan tambahkan data terlebih dahulu':^116}")
                    garisPembatas()

        # MENU 2. CREATE
            elif menu == '2':
                while True:
                    print('\n')
                    garisPembatas()
                    print(f"|{'MENU MENAMBAHKAN DATA':^114}|")
                    garisPembatas()

                    menu_tambahan_2 =  input('''Daftar Menu
1. Menambahkan data siswa baru
2. Kembali ke menu awal
Pilih menu yang diinginkan: ''')
                    if menu_tambahan_2   == '1':
                        menambahkanData()
                    elif menu_tambahan_2 == '2':
                        break
                    else:
                        garisPembatas()
                        print(f"{'Pilih angka dari pilihan tersedia, silakan pilih kembali.':^116}")
                        garisPembatas()
                        continue

        # MENU 3. UPDATE
            elif menu == '3':
                if len(data_siswa) != 0:
                    while True:  
                        print('\n')                                                       
                        garisPembatas()                 
                        print(f"|{'MENU MERUBAH DATA':^114}|")
                        garisPembatas() 

                        menu_tambahan_3 = input('''Daftar Menu
1. Merubah data siswa
2. Kembali ke menu awal
Pilih menu yang diinginkan: ''')
                        if menu_tambahan_3   == '1':
                            menampilkanSemuaData()
                            merubahData()
                        elif menu_tambahan_3 == '2':
                            break
                        else:
                            garisPembatas()
                            print(f"{'Pilih angka dari pilihan tersedia, silakan pilih kembali.':^116}")
                            garisPembatas()
                            continue
                else:
                    menampilkanSemuaData()
                    garisPembatas()
                    print(f"{'Tidak ada data tersimpan. Silakan tambahkan data terlebih dahulu':^116}")
                    garisPembatas()
                                            
        # MENU 4. MEMPREDIKSI SNBP
            elif menu == '4':
                if len(data_siswa) != 0:
                    prediksi_jurusan()
                else:
                    menampilkanSemuaData()
                    garisPembatas()
                    print(f"{'Tidak ada data tersimpan. Silakan tambahkan data terlebih dahulu':^116}")
                    garisPembatas()

        # MENU 5. DELETE
            elif menu == '5':
                if len(data_siswa) != 0:
                    while True:
                        print('\n')                                
                        garisPembatas()                
                        print(f"|{'MENU MENGHAPUS DATA':^114}|")
                        garisPembatas()

                        menu_tambahan_5 = input('''Daftar Menu
1. Hapus data siswa
2. Hapus semua data siswa
3. Kembali ke menu utama
Pilih menu yang diinginkan\t: ''')
                        if menu_tambahan_5   == '1':
                            menghapusData()
                        elif menu_tambahan_5 == '2':
                            menghapusSemuaData()
                            break
                        elif menu_tambahan_5 == '3':
                            break
                        else:
                            garisPembatas()
                            print(f"{'Pilih angka dari pilihan tersedia, silakan pilih kembali.':^116}")
                            garisPembatas()
                            continue
                else:
                    menampilkanSemuaData()
                    garisPembatas()
                    print(f"{'Tidak ada data tersimpan. Silakan tambahkan data terlebih dahulu':^116}")
                    garisPembatas()

        # MENU 6. KEMBALI KE ENTRANCE
            elif menu == '6':
                break

        # MENU 7. EXIT
            elif menu == '7':
                garisPembatas()
                print(f"|{'Terimakasih':^114}|")
                garisPembatas()
                exit()

        # Selain pilihan menu 1 - 7
            else:
                garisPembatas() 
                print(f'{"Pilihan yang kamu pilih tidak valid. Silakan ulangi dan masukan angka dari pilihan yang tersedia.":^116}')
                garisPembatas() 

    elif identifikasi_pengguna == '3':
        garisPembatas()
        print(f"|{'TERIMA KASIH':^114}|")
        garisPembatas()
        break

    else:
        garisPembatas() 
        print(f'{"Pilihan yang kamu pilih tidak valid. Silakan ulangi dan masukan angka dari pilihan yang tersedia.":^116}')
        garisPembatas() 