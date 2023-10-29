penerima_beasiswa = []

while True:
    nama = input("Masukkan nama siswa: ")
    nim = input("Masukkan NIM siswa: ")
    ipk = float(input("Masukkan ipk terbaru: "))
    pendapatan_orang_tua = int(input("Masukkan pendapatan orang tua: "))

    nilai_minimal = float(3.00)
    pendapatan_maximal = 1000000

    if ipk >= nilai_minimal and pendapatan_orang_tua <= pendapatan_maximal:
        penerima_beasiswa.append({'nama': nama, 'nim': nim})

    lanjutkan = input(
        "Apakah Anda ingin menginput data siswa lainnya? (ya/tidak): ")
    if lanjutkan.lower() != 'ya':
        break
if len(penerima_beasiswa) > 0:
    print("Daftar siswa yang mendapat beasiswa:")
    for siswa in penerima_beasiswa:
        print(f"Nama: {siswa['nama']}, NIM: {siswa['nim']}")
else:
    print("Tidak ada siswa yang mendapat beasiswa.")
