print(""" 
=================================
| MENENTUKAN KELIPATAN 3 DAN 5 |
=================================
""")

bilangan = int((input("Masukan bilangan :")))

if bilangan % 3 == 0 and bilangan % 5 == 0:
    print("Kelipatan 3 dan 5")
elif bilangan % 3 == 0:
    print("Kelipatan 3")
elif bilangan % 5 == 0:
    print("Kelipatan 5")
else:
    print("Bukan Kelipatan 3 dan 5")
