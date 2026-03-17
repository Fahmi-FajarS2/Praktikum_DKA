import numpy as np
import random

nama = []
kode = []
data = []

n = int(input("Masukkan jumlah pelanggan: "))

for i in range(n):
    print("\nData pelanggan ke-", i+1)

    nm = input("Nama pelanggan: ")
    belanja = int(input("Total belanja: "))
    transaksi = int(input("Jumlah transaksi: "))

    kd = "UND-" + str(random.randint(1000,9999))

    nama.append(nm)
    kode.append(kd)
    data.append([belanja, transaksi])

data = np.array(data)

print("\nDATA PELANGGAN")
for i in range(n):
    print(kode[i], "-", nama[i], "-", data[i])

# rata-rata belanja
rata = np.mean(data[:,0])
print("Rata-rata total belanja =", rata)

print("\nPelanggan Prioritas (belanja > rata-rata)")
prioritas = []

for i in range(n):
    if data[i][0] > rata:
        print(nama[i])
        prioritas.append(i)

# menentukan slot undian
slot = []

for i in range(n):

    if data[i][1] >= 3:   # minimal 3 transaksi

        s = 0

        if data[i][0] < 300000:
            s = 1
        elif data[i][0] <= 700000:
            s = 2
        else:
            s = 3

        if i in prioritas:
            s = s + 2

        for j in range(s):
            slot.append(i)

# memilih pemenang
pemenang = []

while len(pemenang) < 2:

    pilih = random.choice(slot)

    if pilih not in pemenang:
        pemenang.append(pilih)

print("\nPEMENANG UNDIAN")
for i in pemenang:
    print(nama[i], "-", kode[i])

# pencarian kode
cari = input("\nMasukkan kode undian yang dicari: ")

for i in range(n):
    if kode[i] == cari:
        print("Nama:", nama[i])
        print("Total Belanja:", data[i][0])
        print("Jumlah Transaksi:", data[i][1])