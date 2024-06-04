print("|==============================|")
print("|Program Menampilkan Kalender  |")
print("|==============================|")

import calendar

tahun = int(input("Masukan Tahun :"))
bulan = int(input("Masukan Bulan :"))
print()

print(calendar.month(tahun,bulan))
