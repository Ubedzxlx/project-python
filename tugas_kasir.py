nama_kasir = input("Masukan nama kasir\t :")

nama_barang1   = input("Masukan nama barang      :")
jumlah_barang1 = int(input("Masukan jumlah barang\t :"))
harga_barang1  = int(input("Masukan harga barang\t :"))
total_barang1  = jumlah_barang1*harga_barang1
    
nama_barang2   = input("Masukan nama barang      :")
jumlah_barang2 = int(input("Masukan jumlah barang\t :"))
harga_barang2  = int(input("Masukan harga barang\t :"))
total_barang2  = jumlah_barang2*harga_barang2
    
nama_barang3   = input("Masukan nama barang      :")
jumlah_barang3 = int(input("Masukan jumlah barang\t :"))
harga_barang3  = int(input("Masukan harga barang\t :"))
total_barang3  = jumlah_barang3*harga_barang3

total_belanja = total_barang1 + total_barang2 + total_barang3
total_jml_barang = jumlah_barang1 + jumlah_barang2 + jumlah_barang3

print(f"Total Belnja anda Rp.{total_belanja}")

biaya_admin   = int(input("Masukan biaya admin \t :"))
 
bayar = float(input("Masukan pembayaran anda  :"))
print("pilih metode :")
print("1. Tunai\n2. Transfer\n3. m-banking")

metode = int(input("Masukan metode pembayaran:"))

if metode == 1:
    metode_pembayaran = "Tunai"
elif metode == 2:
    metode_pembayaran = "Transfer"
elif metode == 3:
    metode_pembayaran = "M-banking"
else:
    print("Metode Pembayaran Tidak Tersedia di Program!")    
 
donasi = int(input("Donasi :"))
hemat  = int(input("Hemat  :"))

if bayar > total_belanja:
    kembalian = bayar - total_belanja
else:
    kurang = total_belanja - bayar
    
        
print("=============================== STRUK PEMBELIAN ===============================")
print('''
                               BASMALAH PAITON 1
                  Jl.Raya Paiton,desa pondok kelor,Probolinggo    
                                  083143702296
''')
print("N2006-SL2432024050773281 | 31/05/2024 | 16:54:01")
print("Kasir  :",nama_kasir)
print("........................................................................")
print(f'''
{nama_barang1}\t\t\t                        {jumlah_barang1}  {harga_barang1}  {total_barang1}
{nama_barang2}\t                        {jumlah_barang2}  {harga_barang2}   {total_barang2}
{nama_barang3}                       {jumlah_barang3}  {harga_barang3}  {total_barang3}
''')
print("........................................................................")
print(f"Total Belanja:\t\t\t                {total_jml_barang}       {total_belanja}")
print(f"adm:\t                                                   {biaya_admin}")
print(f"Total Bayar:\t                                         {total_belanja}\n")

print(f"Metode          : {metode_pembayaran}")
print(f"Bayar           : {bayar}")
print(f"Donasi          : {donasi}")
print(f"Hemat           : {hemat}")
print(f"Kembali         : {kembalian}\n")
print("Harga Sudah\ntermasuk PPN")