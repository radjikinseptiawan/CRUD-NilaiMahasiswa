nilaiMahasiswa = []

while True : 
    print('menu')
    print('''
    1. Tambah Data 
    2. Ubah Data 
    3. Tampilkan Data 
    4. Cari Data
    ''')

    userInput = input("Pilih Daftar Menu : ")
    if userInput == '1':
        print('*Tambah Data*')
        print('-'*13,'/')
        nim = int(input('Masukkan Nomor Induk Mahasiswa : '))
        nama = input('Masukkan Nama Mahasiswa : ')
        tugas =int(input('Masukkan Nilai Tugas Mahasiswa : '))
        uts = int(input('Masukkan Nilai UTS mahasiswa : '))
        uas = int(input('Masukkan Nilai UAS mahasiswa : '))
        akhir = tugas * 0.3 + uts * 0.35 + uas * 0.35 

        newMahasiswa = {'nim' : nim,'nama' : nama,'tugas' : tugas ,'uts' : uts,'uas' : uas ,'akhir' :akhir}
        nilaiMahasiswa.append(newMahasiswa)
    elif userInput == '2':
          print('Ubah Data')
          nilaiMahasiswa
    elif userInput == '3':
        print('Menampilkan Data')
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
    
    elif userInput == '4':
        print('Hapus Data')
    else :
        print('Terimakasih!')