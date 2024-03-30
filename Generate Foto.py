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

while True:
    perintah = input ("Perintah : ")
    output = client.run(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt": perintah}
    )

    # Keluaran akan berisi URL ke gambar yang dihasilkan
    print(output)
    time.sleep (10)
    
