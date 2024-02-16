#soal 2.1
#menghitung body mass index/bmi
#rumusnya = berat badan / tinggi badan^2
berat = (int(input("silahkan masukkan berat badan anda(dalam satuan KiloGram) :")))
tinggi = (float(input("silahkan masukkan tinggi badan anda(dalam satuan Meter) :")))
bmi = (berat / (tinggi*tinggi))
print("jadi Body Mass Index(BMI) anda adalah =", round(bmi),"KG/M^2")
