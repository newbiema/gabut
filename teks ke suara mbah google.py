import os
import subprocess
from gtts import gTTS
import time 
bahasa = "id"
skor = 0
path = "D:\Projek\Python\soal"
## Pembukaan
tts=gTTS("""Selamat Datang di game Tebak Tebakan program buatan Evan
         ,Sebelum mulai kita Absen Dulu Ya.Ada Alwi penyuka sesama jenis , Ada Anwar Ga Mandi Satu tahun ,Ada Evan sang penghuni surga""",lang=bahasa)
tts.save("pembukaan.mp3")
os.system("start pembukaan.mp3")
time.sleep(16)
subprocess.run('taskkill /f /im Microsoft.Media.Player.exe', shell=True)

## input nama dan lain lain

nama = input ("Masukkan nama anda : ")
umur = int (input ("Umur : "))
asal = input("Asal : ") 

tts = gTTS (f"""Haiiii {nama} bersiaplah untuk soal yang pertama """,lang=bahasa)
tts.save("sebut_nama.mp3")
os.system("start sebut_nama.mp3")
time.sleep(5)
subprocess.run('taskkill /f /im Microsoft.Media.Player.exe', shell=True)


tts = gTTS ("Soal Pertama 10 + 10 = ")
tts.save ("soal1.mp3")
soal1 = int( input ("1. 10 + 10 = "))
tts = gTTS ("Soal Pertama 10 + 10 = ")
if soal1 == 20:
    skor += 10
    os.chdir(path)
    os.system("start bener.mp4")
    time.sleep(4)
    subprocess.run('taskkill /f /im Microsoft.Media.Player.exe', shell=True) 
else:
    os.chdir(path)
    os.system("start tolol.mp4")
    time.sleep(7) 
    subprocess.run('taskkill /f /im Microsoft.Media.Player.exe', shell=True)
    
soal2 = input ("Siapakah nama lengkap presiden kita : ")
if soal2 == "jokowi dodo":
    skor += 10
    os.chdir(path)
    os.system("start bener.mp4")
    time.sleep(4) 
    subprocess.run('taskkill /f /im Microsoft.Media.Player.exe', shell=True)
        
else :
    os.chdir(path)
    os.system("start tolol.mp4")
    time.sleep(6)
    subprocess.run('taskkill /f /im Microsoft.Media.Player.exe', shell=True)
        
        

            
tts=gTTS(f""" Nama : {nama}
         Asal : {asal}
         Skor :  {skor}""",lang=bahasa)
tts.save("output.mp3")
os.system("start output.mp3")
time.sleep (6)
subprocess.run('taskkill /f /im Microsoft.Media.Player.exe', shell=True) ##menghentikan / teminate Microsoft.Media.Player

if nama == 'anwar':
    tts=gTTS(f""" Peringatan keras khusus kepada anwar Jangan lupa ,mandii """,lang=bahasa)
    tts.save("anwar.mp3")
    os.system("start anwar.mp3")
    time.sleep(6)
    subprocess.run('taskkill /f /im Microsoft.Media.Player.exe', shell=True)
elif nama == 'alawi':
    tts=gTTS(f""" e basong {nama} wah side mandik """,lang=bahasa)
    tts.save("alawi.mp3")
    os.system("start alawi.mp3")
    time.sleep(6)
    subprocess.run('taskkill /f /im Microsoft.Media.Player.exe', shell=True)
else:
    tts=gTTS(f""" fuck you {nama}  """,lang=bahasa)
    tts.save("fuck.mp3")
    os.system("start fuck.mp3")
    time.sleep(6)
    subprocess.run('taskkill /f /im Microsoft.Media.Player.exe', shell=True)


print('====================')
print('Nama : ',nama)
print('Umur : ',umur)
print('Asal : ',asal)
print('SKor : ',skor)
print('====================')

    
    
    
    

