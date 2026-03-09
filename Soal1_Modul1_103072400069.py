def kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False

tahun = int(input("Masukkan tahun: "))
hasil = kabisat(tahun)

if hasil:
    print("Tahun", tahun, "adalah tahun kabisat")
else:
    print("Tahun", tahun, "bukan tahun kabisat")