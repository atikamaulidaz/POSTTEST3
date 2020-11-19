#program penjualan takoyaki

nama = input("nama pembeli: ")

print ("menu takoyaki: ")

def pilihan(i):
    menu = {
        1 : "===takoyaki varian 1 Rp. 2000/pcs===",
        2 : "===takoyaki varian 2 Rp. 2500/pcs==="
    }
    return menu.get(i)

print ("1. takoyaki varian 1")
print ("2. takoyaki varian 2")

pesanan = int(input("mau pesan takoyaki varian berapa? "))
menu = pilihan(pesanan)
print (menu)
jumlah_takoyaki = int(input("pesan berapa? "))

if pesanan == 1:
    if jumlah_takoyaki < 10:
        bayar = jumlah_takoyaki * 2000
        print("anda harus membayar:", bayar)
    elif 10 <= jumlah_takoyaki <= 45:
        total = jumlah_takoyaki * 2000
        diskon = total * (10/100)
        total_setelahDiskon = total - diskon
        print("karena kamu beli >=10 kamu dapat diskon 10%")
        print("total harga sebelum diskon: ", total)
        print("total harga setelah diskon: ", total_setelahDiskon)
        print("jadi kamu harus membayar Rp.", total_setelahDiskon)
    else:
        print("maaf kami hanya memiliki stok 45 pcs")

else:
    if jumlah_takoyaki < 10:
        bayar = jumlah_takoyaki * 2500
        print("anda harus membayar:", bayar)
    elif 8 <= jumlah_takoyaki <= 40:
        total = jumlah_takoyaki * 2500
        diskon = total * (8/100)
        total_setelahDiskon = total - diskon
        print("karena kamu beli >=8 kamu dapat diskon 8%")
        print("total harga sebelum diskon: ", total)
        print ("total harga setelah diskon: ", total_setelahDiskon)
        print("jadi kamu harus membayar Rp.", total_setelahDiskon)
    else:
        print("maaf kami hanya memiliki stok 40 pcs")
