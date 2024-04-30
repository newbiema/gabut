import os
import replicate
import time
## token api
api_token = "r8_I54Bc8aVCetwI1djbVVMOrePx5rM5EO37VvAj"

if api_token is None:
    raise ValueError("Token API Replicate tidak ditemukan. Pastikan Anda telah mengatur variabel lingkungan REPLICATE_API_TOKEN dengan token yang sesuai.")

# Buat instance klien Replicate dengan token API
client = replicate.Client(api_token=api_token)

#membuat permintaan
import replicate
#input dulu bang
input = {
    "image": open(r"D:\KENANGAN\Foto SMA\tes.jpg", "rb"), #masukkan sesuai path file kalian
    "style": "Video game",
    "prompt": "pixelated glitchart of close-up of (subject),ps2 ps1 playstation psx gamecube game radioactive dreams screencapture,bryce3d",
    "instant_id_strength": 0.8
}

output = replicate.run(
    "fofr/face-to-many:35cea9c3164d9fb7fbd48b51503eabdb39c9d04fdaef9a68f368bed8087ec5f9",
    input=input
)
print(output)

time.sleep (10)
    
