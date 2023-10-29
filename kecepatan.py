jarak_km = int(input("masukan jarak: "))
jarak_m = jarak_km * 1000
jam = int(input("masukan jam: "))
menit = int(input("masukan menit: "))
detik = int(input("masukan detik: "))
waktu = (jam * 3600) + (menit * 60) + detik
kecepatan = jarak_m / waktu
print(f"Kecepatan mobil adalah {round(kecepatan)} m/s")