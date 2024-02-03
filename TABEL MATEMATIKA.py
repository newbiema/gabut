#PERKALIAN
def perkalian():
    a=int(input("Masukkan Perkalian Berapa: "))
    print("Perkalian ",a)
    for i in range(1,11):
        hasil = (i * a) 
        print(f"{i} * {a} = ",hasil)
        
def operasi_perkalian():
    angka1=int(input("Angka pertama = "))
    angka2=int(input("Angka kedua = "))
    hasil=(angka1*angka2)
    print(f"{angka1} * {angka2} = ",hasil)



#PEMBAGIAN   
def pembagian():
    a=int(input("Masukkan Tabel pembagian Berapa: "))
    print("Tabel Pembagian ",a)
    for i in range(1,11):
        hasil = (i / a) 
        print(f"{i} / {a} = ",(hasil))
        
def operasi_pembagian():
    angka1=int(input("Angka pertama = "))
    angka2=int(input("Angka kedua = "))
    hasil=(angka1+angka2)
    print(f"{angka1} + {angka2} = ",float(hasil))


#PENJUMLAHAN   
def penjumlahan():
    a=int(input("Masukkan Tabel penjumlahan Berapa: "))
    print("Tabel Penjumlahan ",a)
    for i in range(1,11):
        hasil = (i + a) 
        print(f"{i} + {a} = ",hasil)
        
def operasi_penjumlahan():
    angka1=int(input("Angka pertama = "))
    angka2=int(input("Angka kedua = "))
    hasil=(angka1+angka2)
    print(f"{angka1} + {angka2} = ",hasil)


#PENGURANGAN
def pengurangan():
    a=int(input("Masukkan Tabel pembagian Berapa: "))
    print("Tabel Pengurangan ",a)
    for i in range(1,11):
        hasil = (i - a) 
        print(f"{i} - {a} = ",hasil)
        
def operasi_pengurangan():
    angka1=int(input("Angka pertama = "))
    angka2=int(input("Angka kedua = "))
    hasil=(angka1-angka2)
    print(f"{angka1} - {angka2} = ",hasil)
    
    

while True:
    print("""Selamat Datang di Program Operasi Matematika
         pilihan: 
         1.Operasi Perkalian
         2.Operasi Pembagian
         3.Operasi Penjumlahan
         4.Operasi Pengurangan""")
    pil =int( input("Masukkan Pilihan: "))
    
    # Memilih dulu bang
    if pil == 1:
        while True :
            print("""Mode Perkalian : 
                    1.Tabel Perkalian
                    2.Operasi Perkalian
                    3.Exit""")
            mode_perkalian= int( input("Pilih : "))
            if mode_perkalian == 1:
                perkalian()
                break
            elif mode_perkalian == 2 :
                operasi_perkalian() 
                break
            elif mode_perkalian == 3:
                break
            else:
                print("Inputan salah!!,pilih '1', '2',dan'3'")

    elif pil == 2:
        while True :
            print(""" Mode Pembagian :
                  1.Tabel Pembagian
                  2.Operasi Pembagian""")
            mode_pembagian = int(input("pilih"))
            if mode_pembagian == 1:
                pembagian()
                break
            elif mode_pembagian == 2:
                operasi_pembagian()
                break
    elif pil == 3:
        while True :
            print("""Mode Penjumlahan : 
                    1.Tabel Penjumlahan
                    2.Operasi Penjumlahan
                    3.Exit""")
            mode_penjumlahan= int( input("Pilih : "))
            if mode_penjumlahan == 1:
                penjumlahan()
                break
            elif mode_penjumlahan == 2 :
                operasi_penjumlahan() 
                break
            elif mode_penjumlahan == 3:
                break
            else:
                print("Inputan salah!!,pilih '1', '2',dan'3'")
    
    elif pil == 4:
        while True :
            print("""Mode Pengurangan : 
                    1.Tabel Pengurangan
                    2.Operasi Pengurangan
                    3.Exit""")
            mode_pengurangan = int( input("Pilih : "))
            if mode_pengurangan  == 1:
                pengurangan()
                break
            elif mode_pengurangan  == 2 :
                operasi_pengurangan() 
                break
            elif mode_pengurangan  == 3:
                break
            else:
                print("Inputan salah!!,pilih '1', '2',dan'3'")
                
    else:
        print("PILIHANNYA GA ADA TOLOL")   