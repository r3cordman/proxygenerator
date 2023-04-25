import random

jumlah_kode = int(input("Jumlah proxy yang ingin digenerate ? : "))
nama_file = input("Masukan nama file : ")
kode_list = []

for i in range(jumlah_kode):
    angka1 = str(random.randint(1, 2))
    angka2 = str(random.randint(1, 30)).zfill(2)
    angka3 = str(random.randint(1, 2))
    angka4 = str(random.randint(1, 30)).zfill(2)
    angka5 = str(random.randint(1, 5))
    angka6 = str(random.randint(1, 29)).zfill(random.choice([1, 2]))
    angka7 = str(random.randint(1, 5))
    angka8 = str(random.randint(1, 29)).zfill(random.choice([1, 2]))
    kode = angka1 + angka2 + "." + angka3 + angka4 + "." + angka5 + angka6 + "." + angka7 + angka8 + ":" + str(random.randint(1, 1399)).zfill(4)
    kode_list.append(kode)

for kode in kode_list:
    print(kode)

with open(nama_file + ".txt", "w") as file:
    for kode in kode_list:
        file.write(kode + "\n")

print("Proxy berhasil digenerate dan disimpan dengan nama file " + nama_file + ".txt")
