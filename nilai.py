print("="*38)
print(" NILAI AKHIR MAHASISWA")
print("="*38)

nama = input("Masukan Nama anda\t:")
nim = input("Masukan Nim anda\t:")
matkul = input("Masukan Mata Kuliah\t:")
semester = input("Semester berapa ?\t:")

tugas = float(input("Masukan Nilai Tugas Anda:"))
uts = float(input("Masukan Nilai Uas Anda\t:"))
uas = float(input("Masukan Nilai Uas Anda\t:"))

nilaiAkhir = (tugas*0.2) + (uts*0.4) + (uas*0.4)


print("===============HASILNYA===============")
print("Nama\t\t:",nama)
print("Nim\t\t:",nim)
print("Mata Kuliah\t:",matkul)
print("Semester\t:",semester)
print("Tugas\t\t:",tugas)
print("UTS\t\t:",uts)
print("UAS\t\t:",uas)
print(f"Nilai Akhir\t: {nilaiAkhir:.2f}")
print("===========MENENTUKAN NILAI===========")

if nilaiAkhir >=90:
    print("Grade : A")
elif nilaiAkhir >=80:
    print("Grade : B")
elif nilaiAkhir >=75:
    print("Grade : C")
elif nilaiAkhir >=50:
    print("Grade : D")
else:
    print("Grade : E")

print("=========MENENTUKAN KELULUSAN=========")

if nilaiAkhir >=70:
    print("Selamat Anda Lulus")
else:
    print("Anda Tidak Lulus")







