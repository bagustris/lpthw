#Biseksi mencari akar

x = float(raw_input('masukkan angka: '))  #pengguna meng-input-kan angka yang akarnya akan dicari
epsilon = 0.01  #nilai eror yang diinginkan
banyaktebakan = 0  #inisialisasi banyaknya tebakan
atas = x #batas atas dari rentang
bawah = 0.0 #batas bawah dari rentang
akar = (atas + bawah)/2.0  #nilai tengah dari rentang atau nilai akar kuadrat
while abs(akar**2 - x) >= epsilon:  #lakukan algoritma biseksi selama eror lebih besar atau sama dengan nilai epsilon
    print ('bawah = ' + str(bawah) + ' atas = ' + str(atas) + ' akar = ' + str(akar))
    banyaktebakan += 1  #pengitunga jumlah tebakan yang dilakukan
    if akar**2 > x:  #pengujian untuk memilih rentang
        atas = akar
    else:
        bawah = akar
    akar = (bawah + atas)/2.0  #nilai akar kuadrat
print ('banyak tebakan = ' + str(banyaktebakan))
print (str(akar) + ' mendekati akar dari ' + str(x))
