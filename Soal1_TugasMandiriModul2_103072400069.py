import numpy as np

nama = []
nilai = []

while True:

    print("\n===== MENU =====")
    print("1. Input Data Mahasiswa")
    print("2. Tampilkan Array Nilai")
    print("3. Tampilkan Nilai Akhir")
    print("4. Analisis Nilai Kelas")
    print("5. Tampilkan 3 Nilai Tertinggi")
    print("6. Cari Data Mahasiswa")
    print("7. Update Nilai Mahasiswa")
    print("8. Hapus Mahasiswa")
    print("9. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":

        n = int(input("Jumlah mahasiswa: "))

        for i in range(n):

            print("\nMahasiswa ke-", i+1)

            nm = input("Nama: ")
            tugas = float(input("Nilai tugas: "))
            uts = float(input("Nilai UTS: "))
            uas = float(input("Nilai UAS: "))

            nama.append(nm)
            nilai.append([tugas, uts, uas])

        nilai = np.array(nilai)

    elif menu == "2":

        print("\nArray Nilai:")
        print(nilai)

    elif menu == "3":

        print("\nNilai Akhir Mahasiswa")

        for i in range(len(nama)):

            akhir = (0.3*nilai[i][0]) + (0.3*nilai[i][1]) + (0.4*nilai[i][2])

            print(nama[i], "=", round(akhir,2))

    elif menu == "4":

        nilai_akhir = []

        for i in range(len(nama)):

            akhir = (0.3*nilai[i][0]) + (0.3*nilai[i][1]) + (0.4*nilai[i][2])
            nilai_akhir.append(akhir)

        nilai_akhir = np.array(nilai_akhir)

        print("Rata-rata nilai akhir:", np.mean(nilai_akhir))
        print("Median nilai akhir:", np.median(nilai_akhir))

    elif menu == "5":

        nilai_akhir = []

        for i in range(len(nama)):

            akhir = (0.3*nilai[i][0]) + (0.3*nilai[i][1]) + (0.4*nilai[i][2])
            nilai_akhir.append(akhir)

        nilai_akhir = np.array(nilai_akhir)

        urut = np.argsort(nilai_akhir)[::-1]

        print("\n3 Nilai Tertinggi:")

        for i in range(3):

            idx = urut[i]
            print(nama[idx], "=", round(nilai_akhir[idx],2))

    elif menu == "6":

        cari = input("Masukkan nama mahasiswa: ")

        for i in range(len(nama)):

            if nama[i] == cari:

                print("Nama:", nama[i])
                print("Tugas:", nilai[i][0])
                print("UTS:", nilai[i][1])
                print("UAS:", nilai[i][2])

    elif menu == "7":

        cari = input("Masukkan nama mahasiswa: ")

        for i in range(len(nama)):

            if nama[i] == cari:

                tugas = float(input("Nilai tugas baru: "))
                uts = float(input("Nilai UTS baru: "))
                uas = float(input("Nilai UAS baru: "))

                nilai[i][0] = tugas
                nilai[i][1] = uts
                nilai[i][2] = uas

                print("Data berhasil diperbarui")

    elif menu == "8":

        cari = input("Masukkan nama mahasiswa yang dihapus: ")

        for i in range(len(nama)):

            if nama[i] == cari:

                nama.pop(i)
                nilai = np.delete(nilai, i, axis=0)

                print("Data berhasil dihapus")
                break

    elif menu == "9":

        print("Program selesai")
        break

    else:

        print("Menu tidak tersedia")