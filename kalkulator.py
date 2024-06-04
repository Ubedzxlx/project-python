print("="*30)
print('''
      Kalkulator Sederhana 
       Operasi Matematika
''')
print("="*30)
print('''
      1. Penjumlahan (+)
      2. Pengurangan (-)
      3. Perkalian   (*)
      4. Pembagian   (/)
''')
print("="*30)

operasi = input("Pilih Operasi (1/2/3/4) :")
angka1  = float(input("Masukan angka pertama :"))
angka2  = float(input("Masukan angka kedua   :"))
print("="*30)

if operasi == "1":
    print("User Memilih Operasi Penjumlahan")
elif operasi == "2":
    print("User Memilih Operasi Pengurangan")
elif operasi == "3":
    print("User Memilih Operasi Perkalian")
elif operasi == "4":
    print("User Memilih Operasi Pembangian")
else:
    print("Program Valid!")

if operasi == "1":
    hasil = angka1 + angka2
    print(f"Hasil dari {angka1} + {angka2} = {hasil:.2f}")
elif operasi == "2":
    hasil = angka1 - angka2
    print(f"Hasil dari {angka1} - {angka2} = {hasil:.2f}")
elif operasi == "3":
    hasil = angka1 * angka2
    print(f"Hasil dari {angka1} * {angka2} = {hasil:.2f}")
elif operasi == "4":
    if angka2 != 0:      
        hasil = angka1 / angka2
        print(f"Hasil dari {angka1} / {angka2} = {hasil:.2f}")
    else:
        print("Error pembagian dengan 0 tidak di perbolehkan!")
else:
    print("Program Valid!")
    
