print('''
        |====================================================|     
        |                   CAFE JREBET                      |
        |   Pembelian Rp.100.000 Akan Mendapatkan Diskon 10% |
        |====================================================|     
''')

makanan = []
camilan = []
minuman = []
harga_makanan = []
harga_camilan = []
harga_minuman = []
totalHarga = 0

while True:
    print("\n\t       ========== MENU MAKANAN =========")
    print("""
          
          ------------------------------------------
          | NO |    NAMA MAKANAN       |   HAGRA   | 
          ------------------------------------------
          |  1 |    BEBEK GORENG       |   25.000 |
          |  2 |    AYAM GEPREK        |   10.000 |
          |  3 |    AYAM PENYET        |   15.000 |
          |  4 |    NASI GORENG        |   15.000 |
          |  5 |    MIE GORENG         |   10.000 |
          |  6 |    AYAM BAKAR         |   25.000 |
          |  7 |    AYAM RENDANG       |   20.000 |
          |  8 |    SOTO AYAM          |   15.000 |
          |  9 |    RAWON              |   15.000 |
          | 10 |    IKAN NILA BAKAR    |   19.000 |
          ------------------------------------------
    """)
    nomer_makanan = int(input("Masukan nomer menu makanan yang anda pesan :"))

    if nomer_makanan == 1:
        makanan.append("BEBEK GORENG")
        harga_makanan.append(25000)
        totalHarga += 25000
    elif nomer_makanan == 2:
        makanan.append("AYAM GEPREK")
        harga_makanan.append(10000)
        totalHarga += 10000
    elif nomer_makanan == 3:
        makanan.append("AYAM PENYET")
        harga_makanan.append(15000)
        totalHarga += 15000
    elif nomer_makanan == 4:
        makanan.append("AYAM GORENG")
        harga_makanan.append(15000)
        totalHarga += 15000
    elif nomer_makanan == 5:
        makanan.append("MIE GORENG")
        harga_makanan.append(10000)
        totalHarga += 10000
    elif nomer_makanan == 6:
        makanan.append("AYAM BAKAR")
        harga_makanan.append(25000)
        totalHarga += 25000
    elif nomer_makanan == 7:
        makanan.append("AYAM RENDANG")
        harga_makanan.append(20000)
        totalHarga += 20000
    elif nomer_makanan == 8:
        makanan.append("SOTO AYAM")
        harga_makanan.append(15000)
        totalHarga += 15000
    elif nomer_makanan == 9:
        makanan.append("RAWON")
        harga_makanan.append(15000)
        totalHarga += 15000
    elif nomer_makanan == 10:
        makanan.append("IKAN NILA BAKAR")
        harga_makanan.append(19000)
        totalHarga += 19000
    else:
        print("Menu makanan tidak terdaftar di program ,silahkan masukan kembali!!")
        
        
    print("\n\t       ========== MENU CAMILAN =========")
    print("""
          
          ------------------------------------------
          | NO |    MENU CAMILAN       |   HAGRA   | 
          ------------------------------------------
          |  1 |    KENTANG GORENG     |   12.000 |
          |  2 |    TELUR MATA SAPI    |   14.000 |
          |  3 |    DONAT KENTANG      |   16.000 |
          |  4 |    SAYAP AYAM PEDAS   |   18.000 |
          |  5 |    SALAD BUAH         |   12.000 |
          |  6 |    ROTI MARYAM        |   14.000 |
          |  7 |    PISANG COKLAT      |    9.000 |
          |  8 |    TAHU KRISPI        |   12.000 |
          ------------------------------------------
    """)
    nomer_camilan  = int(input("Masukan nomer menu camilan yang anda pesan :"))
    
    if nomer_camilan == 1:
        camilan.append("KENTANG GORENG")
        harga_camilan.append(12000)
        totalHarga += 12000
    elif nomer_camilan == 2:
        camilan.append("TELUR MATA SAPI")
        harga_camilan.append(14000)
        totalHarga += 14000
    elif nomer_camilan == 3:
        camilan.append("DONAT KENTANG")
        harga_camilan.append(16000)
        totalHarga += 16000
    elif nomer_camilan == 4:
        camilan.append("SAYAP AYAM KENTANG")
        harga_camilan.append(18000)
        totalHarga += 18000
    elif nomer_camilan == 5:
        camilan.append("SALAD BUAH")
        harga_camilan.append(12000)
        totalHarga += 12000
    elif nomer_camilan == 6:
        camilan.append("ROTI MARYAM")
        harga_camilan.append(14000)
        totalHarga += 14000
    elif nomer_camilan == 7:
        camilan.append("PISANG COKLAT")
        harga_camilan.append(9000)
        totalHarga += 9000
    elif nomer_camilan == 8:
        camilan.append("TAHU KRISPI")
        harga_camilan.append(12000)
        totalHarga += 12000
    else:
        print("Menu Camilan tidak terdaftar di program ,silahkan masukan kembali!!")
        
        
    print("\n\t       ========== MENU MINUMAN =========")
    print("""
          
          ------------------------------------------
          | NO |    MENU CAMILAN       |   HAGRA   | 
          ------------------------------------------
          |  1 |    TEH                |   5.000   |
          |  2 |    KOPI               |   5.000   |
          |  3 |    ES JERUK           |   5.000   |
          |  4 |    ES BUAH            |   5.000   |
          |  5 |    ES DEGAN           |   5.000   |
          |  6 |    ES CAMPUR          |   10.000  | 
          |  7 |    SUSU               |    7.000  |
          ------------------------------------------
    """)
    nomer_minuman  = int(input("Masukan nomer menu minuman yang anda pesan :"))
    
    if nomer_minuman == 1:
        minuman.append("TEH")
        harga_minuman.append(5000)
        totalHarga += 5000
    elif nomer_minuman == 2:
        minuman.append("KOPI")
        harga_minuman.append(5000)
        totalHarga += 5000
    elif nomer_minuman == 3:
        minuman.append("ES JERUK")
        harga_minuman.append(5000)
        totalHarga += 5000
    elif nomer_minuman == 4:
        minuman.append("ES BUAH")
        harga_minuman.append(5000)
        totalHarga += 5000
    elif nomer_minuman == 5:
        minuman.append("ES DEGAN")
        harga_minuman.append(5000)
        totalHarga += 5000
    elif nomer_minuman == 6:
        minuman.append("ES CAMPUR")
        harga_minuman.append(10000)
        totalHarga += 10000
    elif nomer_minuman == 7:
        minuman.append("PISANG COKLAT")
        harga_minuman.append(7000)
        totalHarga += 7000
    else:
        print("Menu Camilan tidak terdaftar di program ,silahkan masukan kembali!!")


    pesan_lagi = input("Pesan lagi? (y/t) :")

    if pesan_lagi == "t":
        break




print("=============================== STRUK PEMBELIAN ===============================")
print(f"""
Makanan                     : {', '.join(makanan)}
Harga                       : Rp. {', Rp. '.join(map(str, harga_makanan))}
Makanan                     : {', '.join(camilan)}
Harga                       : Rp. {', Rp. '.join(map(str, harga_camilan))}
Makanan                     : {', '.join(minuman)}
Harga                       : Rp. {', Rp. '.join(map(str, harga_minuman))}
Jumlah total harga          : Rp. {totalHarga}
""")

bayar = int(input("MAsukan pembayaran Anda     :"))

if bayar > 100000:
    diskon = bayar * 0.1
    total  = bayar - diskon
    kembalian = bayar - total
    print(f"Kembalian Anda setelah mendapatkan diskon Rp.{kembalian} ")
elif bayar > totalHarga:
    kembalian = bayar - totalHarga
    print(f"Kembalian Anda Rp.{kembalian}")
else:
    uang_kurang = totalHarga - bayar
    print(f"Uang yang anda bayar kurang Rp.{uang_kurang} ")
    


