# Input 
nama = input("Masukkan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

# Menghitung nilai akhir
nilai_akhir = (nilai_tugas * 0.20) + (nilai_uts * 0.35) + (nilai_uas * 0.45)

# Output
print("\n===== HASIL PERHITUNGAN =====")
print("Nama Mahasiswa :", nama)
print(f"Nilai Akhir : {nilai_akhir:.2f}")