Data_Product = {
    101:"Beras Putih",	
    102:"Gula Pasir",
    103:"Gula Jawa",
    104:"Mie Instan",
    105:"Telur Ayam",
    106:"Minyak Goreng",
    107:"Susu Bubuk",
    108:"Susu Kental",
    109:"Susu UHT",
    110:"T. Terigu",
    111:"T. Maizena",
    112:"T. Tapioka",
    113:"T. Beras",
    114:"T. Ketan",
    115:"Kopi Hitam",
    116:"Kecap Manis",
    117:"Kecap Asin",
}
Daftar_Harga = {
    101: 15000,
    102: 12000,
    103: 28000,
    104: 48000,
    105: 20000,
    106: 21000,
    107: 35000,
    108: 15000,
    109: 6000,
    110: 18000,
    111: 17000,
    112: 15000,
    113: 12000,
    114: 19000,
    115: 10000,
    116: 13000,
    117: 13000,
}

dict_transaksi = {}
Daftar_Metode_Pembayaran = {
    1:"Transfer Bank",
    2:"Cash on Delivery"
}
print("================================ Daftar Produk ================================")
for i in Data_Product:
    print("Id Product : ", i,"\t Nama Product : ", 
        Data_Product[i],"\t Harga Produk : ", Daftar_Harga[i])
pilih_id = int(input("Pilih Id Product : "))
if pilih_id in Data_Product :
    Pilih_Beli = input("Pilih Barang Ini ? (Ok): ")
    if Pilih_Beli == "ok" or Pilih_Beli == "Ok" or Pilih_Beli == "OK":
        Nama_Pembeli         = input("Nama Pembeli         : ")
        Alamat_Pembeli       = input("Alamat Pembeli       : ")
        Nomor_HP             = input("Nomor HP             : ")
        Ekspedisi_Pengiriman = input("Ekspedisi Pengiriman : ")
        dict_transaksi = {
            "Nama Pembeli":Nama_Pembeli,
            "Alamat pembeli":Alamat_Pembeli,
            "Nomor HP":Nomor_HP,
            "Ekspedisi Pengiriman":Ekspedisi_Pengiriman,
        }
    if len (dict_transaksi) > 0 :
        print("================================ Metode Pembayaran ================================")
    for i in Daftar_Metode_Pembayaran:
        print("id : ", i, "\t Metode Pembayaran : ", Daftar_Metode_Pembayaran[i]) 
    Pilih_Metode = int(input("Pilih ID Metode Pembayaran : "))
    if Pilih_Metode in Daftar_Metode_Pembayaran :
        print("Nama Pembeli : ", dict_transaksi["Nama Pembeli"])
        print("Alamat pembeli : ", dict_transaksi["Alamat pembeli"])
        print("Nomor HP : ", dict_transaksi["Nomor HP"])
        print("Ekspedisi Pengiriman : ", dict_transaksi["Ekspedisi Pengiriman"])
        print("Produk : ", Data_Product[pilih_id])
        print("Harga : ", Daftar_Harga[pilih_id])
        print("Metode Pembayaran : ", Daftar_Metode_Pembayaran[Pilih_Metode])
        Pembayaran = input ("Masukkan nominal pembayaran (Uang Pas) : ")
        Konfirmasi = input("Apakah Anda yakin ingin melakukan pembayaran? (Y/N) : ")
        if Konfirmasi == "y" or Konfirmasi == "Y":
            print("Anda telah berhasil melakukan pembayaran")
        if Konfirmasi == "n" or Konfirmasi == "N":
            print("Proses transaksi gagal")
else:
    print("Id produk tidak tersedia")