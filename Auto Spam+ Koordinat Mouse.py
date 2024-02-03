import pyautogui
import time

#buat ngeliat koordinat
def posisimouse():
    print('Arahkan Cursor ke posisi yang ingin di spam (Misalnya Whatapps di kolom titik pesan)')
    time.sleep(8)
    while True:
        x, y = pyautogui.position()
        print(f"Titik Koordinat: X={x} , Y={y}")
        break
    
#buat spam
def spam():
    
    kata=input("Masukkan Kata: ")
    berapa=int(input("Berapa kali: "))
    x=int(input('Masukkan Koordinat x: '))
    y=int(input('Masukkan Koordinat y: '))
    time.sleep(2)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    for i in range(berapa):
        pyautogui.write(kata)
        time.sleep(0.1)
        pyautogui.press("Enter")
    

#tutorial penggunaan
def tutor():
    print('1.Pilih menu melihat titik koordinat,dan langsung arahkan cursor ke tempat')
    print('  yang diinginkan (Misalnya kolom pesan wa) secara cepat')
    time.sleep(5)
    print('2.Setelah itu akan muncul titik koordinat x dan y contoh (x = 1090,y = 900 ) ')
    time.sleep(5)
    print('3.Pilih menu spam di menu pilihan dan ikuti inputan yang disuruh')
    time.sleep(5)
    print('4.Nah nanti ada inputan x dan y,Masukkan sesuai titik koordinat yang sudah muncul')
    time.sleep(5)
    print('                  !!!!SELAMAT MENCOBA !!!!                    ')
    time.sleep(5)
    print('\n')

#daftar menu
def menu():
    while True:
        print('\n')
        print('=========================================')
        print('=======  RANDOM PROJEK by Evan v1.2  =======')
        print('=========================================')
        print('\n')
        print('Selamat Datang di Random Projek Pilihan')
        print('1.Melihat titik Koordinat Mouse')
        print('2.Spam')
        print('3.Tutorial Penggunaan fitur spam')
        pilihan=input('Masukkan pilihan: ')
        print('\n')
        if pilihan == "1":
            posisimouse()
        elif pilihan == '2':
            spam()
        elif pilihan == '3':
            tutor()
        else:
            break
    
        


menu()

