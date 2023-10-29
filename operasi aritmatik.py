print("pilihan: ")
print("pilihan 1: makan")
print("pilihan 2: minum")

pilihan = input("pilihan (1/2): ")

if pilihan == 1:
    print("pilih makanan: ")
    print("1. nasi")
    print("2. roti")
    makan = input("pilih (1/2   )")
    if makan == 1:
        print("silahkan ambil di rice cooker")
    elif makan == 2:
        print("silahkan ambil di meja makan")
        
if pilihan == 2:
    print("Pilih minuman: ")
    print("1. air putih")
    print("2. teh")
    minum = input("Pilih (1/2): ")
    if minum == 1:
        print("silahkan ambil di galon")
    elif minum == 2:
        print("silahkan ambil di teko")