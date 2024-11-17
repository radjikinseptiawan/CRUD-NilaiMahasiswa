contacts = [{
    'name' : 'Ari',
     'nomorTelp' : '0871267888'
},{
    'name' : 'Dina',
    'nomorTelp' : '087677776'
}]

# print kontak ari
for contact in contacts:
    if contact['name'] == 'Ari':
        print(contact['name'])
        print(contact['nomorTelp'])

# tambah kontak baru 
contacts.append({
    'name' : 'Riko',
    'nomorTelp' : '081944320881'
})

# Mengubah Kontak Dina
for contact in contacts :
    if contact['name'] == 'Dina':
        contact['nomorTelp'] ='088999776'
        print('berhasil mengupgrade contact!')

# Menampilkan semua nama
print('='*32)
print('    Nama     |||     Nomor    ')
print('='*32)

for contact in contacts:
    print(f'''     {contact["name"]}     |||     {contact["nomorTelp"]}     ''')

print('='*32)


# Menghapus kontak Dina
del contacts[1]

print('Kontak  berhasil di perbarui')
print('='*32)
print('    Nama     |||     Nomor    ')
print('='*32)

for contact in contacts:
    print(f'''     {contact["name"]}     |||     {contact["nomorTelp"]}     ''')

print('='*32)
