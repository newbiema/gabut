from datetime import datetime

def header():
    while True:
        print('==============================================')
        print('== Selamat datang di program mencari zodiak ==')
        print('==============================================\n')
        print('\tMENU')
        print('\n')
        print('1. Mulai')
        print('2. Exit')
        pilih = input('Masukkan pilihan: ')
        print('\n')
        if pilih == '1':
            nama=input('Nama: ')
            umur=input('Umur: ')
            day = int(input("Tanggal lahir Anda: "))
            month = int(input("Bulan lahir Anda: "))
            tahun=int(input('Tahun lahir Anda: '))
            print('\n')
            zodiac_sign = get_zodiac_sign(day, month)
            print('========================================')
            print(' Nama: ',nama,'')
            print(' Umur: ',umur)
            print(' Kelahiran: ',day,month,tahun,'')
            print(f" Zodiak Anda adalah {zodiac_sign}.")
            print('========================================\n')
        elif pilih == '2':
            break
        else:
            print('Pilihan tidak valid.')

def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"

header()
