nilaiMahasiswa = []


def inputMahasiswa():
        print('***Tambah Data***')
        print('-'*13,'/')
        nim = int(input('Masukkan Nomor Induk Mahasiswa : '))
        nama = input('Masukkan Nama Mahasiswa : ')
        tugas =int(input('Masukkan Nilai Tugas Mahasiswa : '))
        uts = int(input('Masukkan Nilai UTS mahasiswa : '))
        uas = int(input('Masukkan Nilai UAS mahasiswa : '))
        akhir = tugas * 0.3 + uts * 0.35 + uas * 0.35 

        newMahasiswa = {'nim' : nim,'nama' : nama,'tugas' : tugas ,'uts' : uts,'uas' : uas ,'akhir' :akhir}
        nilaiMahasiswa.append(newMahasiswa)
    
def menampilkanData():
        print('***Menampilkan Data***')
        print('-'*13,'/')
        
        if len(nilaiMahasiswa) > 0 :
            print('='*78)
            print('|    NIM    |    Nama    |    Tugas    |    UTS    |    UAS    |     Akhir    |')
            print('='*78)
            for mahasiswa in nilaiMahasiswa :
                print(f'''|    {mahasiswa['nim']}    |    {mahasiswa['nama']}    |    {mahasiswa['uts']}    |    {mahasiswa['uas']}    |    {mahasiswa['akhir']}    |''')
                print('-'*78)
            print('='*78)
        else :
            print('='*78)
            print('|    no    |    Nama    |    Tugas    |    UTS    |    UAS    |     Akhir    |')
            print('='*78)
            print('                              TABEL BELUM DIISI                               ')
            print('='*78)

def mengupgradeData():
    print('***Ubah Data Mahasiswa***')
    print('-'*13, '/')
    if len(nilaiMahasiswa) == 0:
        print('Data mahasiswa kosong, tidak ada yang dapat diubah.')
        return
    
    nim = int(input('Masukkan NIM mahasiswa yang ingin diubah: '))
    for mahasiswa in nilaiMahasiswa:
        if mahasiswa['nim'] == nim:
            print('Data ditemukan:')
            print(f"Nama: {mahasiswa['nama']}, Tugas: {mahasiswa['tugas']}, UTS: {mahasiswa['uts']}, UAS: {mahasiswa['uas']}, Akhir: {mahasiswa['akhir']:.2f}")
            print('''
            Pilih data yang ingin diubah:
            1. Nama
            2. Nilai Tugas
            3. Nilai UTS
            4. Nilai UAS
            5. Semua Data
            ''')
            pilihan = input('Masukkan pilihan (1-5): ')
            
            if pilihan == '1':
                mahasiswa['nama'] = input('Masukkan nama baru: ')
            elif pilihan == '2':
                mahasiswa['tugas'] = int(input('Masukkan nilai tugas baru: '))
            elif pilihan == '3':
                mahasiswa['uts'] = int(input('Masukkan nilai UTS baru: '))
            elif pilihan == '4':
                mahasiswa['uas'] = int(input('Masukkan nilai UAS baru: '))
            elif pilihan == '5':
                mahasiswa['nama'] = input('Masukkan nama baru: ')
                mahasiswa['tugas'] = int(input('Masukkan nilai tugas baru: '))
                mahasiswa['uts'] = int(input('Masukkan nilai UTS baru: '))
                mahasiswa['uas'] = int(input('Masukkan nilai UAS baru: '))
            else:
                print('Pilihan tidak valid.')

            # Hitung ulang nilai akhir
            mahasiswa['akhir'] = mahasiswa['tugas'] * 0.3 + mahasiswa['uts'] * 0.35 + mahasiswa['uas'] * 0.35
            print('Data berhasil diperbarui.')
            return
    print(f'Data dengan NIM {nim} tidak ditemukan.')


def menampilkanDetailData():
    print('***Cari Data Mahasiswa***')
    print('-' * 13, '/')
    if len(nilaiMahasiswa) == 0:
        print('Data mahasiswa kosong.')
        return

    nim = int(input('Masukkan NIM mahasiswa yang ingin dicari: '))
    for mahasiswa in nilaiMahasiswa:
        if mahasiswa['nim'] == nim:
            print('Data ditemukan:')
            print(f"NIM: {mahasiswa['nim']}")
            print(f"Nama: {mahasiswa['nama']}")
            print(f"Nilai Tugas: {mahasiswa['tugas']}")
            print(f"Nilai UTS: {mahasiswa['uts']}")
            print(f"Nilai UAS: {mahasiswa['uas']}")
            print(f"Nilai Akhir: {mahasiswa['akhir']:.2f}")
            return
    print(f'Data dengan NIM {nim} tidak ditemukan.')



def menghapusData():
    print('***Hapus Data Mahasiswa***')
    print('-' * 13, '/')
    if len(nilaiMahasiswa) == 0:
        print('Data mahasiswa kosong, tidak ada yang dapat dihapus.')
        return

    nim = int(input('Masukkan NIM mahasiswa yang ingin dihapus: '))
    for mahasiswa in nilaiMahasiswa:
        if mahasiswa['nim'] == nim:
            nilaiMahasiswa.remove(mahasiswa)
            print(f'Data dengan NIM {nim} berhasil dihapus.')
            return
    print(f'Data dengan NIM {nim} tidak ditemukan.')
    
while True : 
    print('menu')
    print('''
    1. Tambah Data 
    2. Ubah Data 
    3. Tampilkan Data 
    4. Cari Data
    5. Menghapus Data
    ''')

    userInput = input("Pilih Daftar Menu : ")
    if userInput == '1':
        inputMahasiswa()
    elif userInput == '2':
        mengupgradeData()     
    elif userInput == '3':
       menampilkanData() 
    elif userInput == '4':
        menampilkanDetailData()
    elif userInput == '5':
        menghapusData()
    else :
        print('Terimakasih!')