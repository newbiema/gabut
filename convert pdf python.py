from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def convert_to_pdf(input_filenames, output_filename):
    # Membuat file PDF
    pdf = canvas.Canvas(output_filename, pagesize=letter)

    for input_filename in input_filenames:
        # Mengambil ukuran gambar dari setiap file
        img = Image.open(input_filename)
        width, height = img.size

        # Menambahkan halaman baru untuk setiap gambar
        pdf.setPageSize((width, height))
        pdf.showPage()

        # Menggambar gambar ke halaman PDF
        pdf.drawInlineImage(img, 0, 0, width, height)

    # Menyimpan file PDF
    pdf.save()

def batch_convert_to_pdf(input_directory, output_filename):
    # Mencari file dalam direktori input_directory dengan ekstensi .jpg
    input_files = [os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.lower().endswith(".jpg")]

    # Melakukan konversi ke PDF
    convert_to_pdf(input_files, output_filename)
    print(f"Berhasil mengonversi {len(input_files)} file JPG menjadi {output_filename}")

if __name__ == "__main__":
    input_directory = "D:\KENANGAN\SMA"
    output_filename = "D:\\KENANGAN\\output\\output_file.pdf"


    batch_convert_to_pdf(input_directory, output_filename)
