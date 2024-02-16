#soal 2.3
gajiPerJam = float(input("Berapa gaji perjam yang anda inginkan :"))
jmlhJam = float(input("jumlah jam yang akan anda ambil dalam seminggu :"))
#nonpajak
nonpjk = gajiPerJam * jmlhJam * 5
#pajak
pjk = nonpjk * 0.14
bersih = nonpjk - pjk
#baju
bj = bersih * 0.1
#tulis
tulis = bersih * 0.01
#total buku, aksesoris dan alat tulis
bukTul = bj + tulis
#sisa uang untuk sedekah
sedekah = (bersih - bukTul) * 0.25
#loop pembagian sedekah
bagi = sedekah
while bagi % 1000 == 0 and bagi >= 1000 or bagi % 1000 != 0 and bagi >=1000:
    bagi -= 1000
     
yatim = (sedekah - bagi) *0.3
dhuafa = (sedekah - bagi) *0.7

print("1. Pendapatan Budi sebelum membayar pajak Rp.{}".format(round(nonpjk)))
print("2. Pendapatan Budi setelah membayar pajak Rp.{}".format(round(bersih)))
print("3. yang digunakan untuk memebeli baju dan aksesoris Rp.{}".format(round(bj)))
print("4. Yang digunakan untuk beli alat tulis Rp.{}".format(round(tulis)))
print("5. Yang digunakan untuk bersedekah Rp.{}".format(round(sedekah)))
print("6. Yang dibagikan ke anak yatim Rp.{}".format(round(round(yatim))))
print("7. Yang dibagikan ke kaum dhuafa Rp.{}".format(round(dhuafa)))