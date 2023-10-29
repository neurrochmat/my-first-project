# Membuat kamus (dictionary) untuk menyimpan data siswa dan hobi mereka
data_siswa = {}

# Fungsi untuk menambahkan data siswa dan hobi
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    hobi = input("Masukkan hobi siswa: ")
    data_siswa[nama] = hobi
    print("Data siswa telah ditambahkan.")

# Fungsi untuk mencari hobi siswa berdasarkan nama
def cari_hobi():
    nama = input("Masukkan nama siswa yang ingin dicari hobi nya: ")
    if nama in data_siswa:
        print(f"{nama} memiliki hobi {data_siswa[nama]}.")
    else:
        print(f"{nama} tidak ditemukan dalam database.")

# Fungsi untuk menampilkan semua data siswa dan hobi mereka
def tampilkan_semua():
    print("Data Siswa dan Hobi:")
    for nama, hobi in data_siswa.items():
        print(f"{nama}: {hobi}")

# Loop utama untuk interaksi dengan program
while True:
    print("\nMenu:")
    print("1. Tambah Data Siswa")
    print("2. Cari Hobi Siswa")
    print("3. Tampilkan Semua Data")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        cari_hobi()
    elif pilihan == "3":
        tampilkan_semua()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang valid.")
