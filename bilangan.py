print("====================================")
print(" MENTUKAN BILANGAN GENAP DAN GANJIL")
print("====================================")

awal = int(input("Masukan bilangan Awal   :"))
akhir = int(input("Masukan bilangan Akhir :"))

x = []
y = []

for i in range(awal,akhir):
    if i%2 == 0:
        x.append(i)
    if i%2 == 1:
        y.append(i)
print(f"Angka bilangan Genap  : {x}")
print(f"Angka bilangan Ganjil : {y}")