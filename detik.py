print("*"*44)
print(" KONVERSI DETIK MENJADI JAM : MENIT : DETIK")
print("*"*44)

detik_awal = int(input("Masukan nilai awal detik :"))
jam = int(detik_awal//3600)
menit = int(detik_awal - (jam * 3600))//60

detik = (detik_awal - (jam*3600)-(menit*60))
print(str(jam) + " JAM " + str(menit) + " MENIT " + str(detik) + " DETIK ")