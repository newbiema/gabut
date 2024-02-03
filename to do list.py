from rich.console import Console
from rich.table import Table

data_task = []

# Menambah data
def tambah_data():
    kegiatan = input('Masukkan task: ')
    data_task.append(kegiatan)
    print("Task berhasil dimasukkan")

# Menampilkan data
def tampilkan_data():
    console = Console()
    table = Table(title="Daftar Task")
    table.add_column("No.")
    table.add_column("Task")
    
    for idx, kegiatan in enumerate(data_task, start=1):
        table.add_row(str(idx), kegiatan)

    console.print(table)

# Mengupdate data
def update_data():
    tampilkan_data()
    try:
        index = int(input("Masukkan nomor task yang akan diupdate: "))
        if 1 <= index <= len(data_task):
            updated_task = input("Masukkan task yang baru: ")
            data_task[index - 1] = updated_task
            print("Data berhasil diupdate.")
        else:
            print("Nomor task tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor task yang ingin diupdate.")

# Menghapus data
def hapus_data():
    tampilkan_data()
    try:
        index = int(input("Masukkan nomor task yang akan dihapus: "))
        if 1 <= index <= len(data_task):
            removed_task = data_task.pop(index - 1)
            print(f"Task '{removed_task}' berhasil dihapus.")
        else:
            print("Nomor task tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor task yang ingin dihapus.")

# Membuat objek Rich untuk menu
console = Console()
menu_table = Table(title="Menu")
menu_table.add_column("Key")
menu_table.add_column("Action")

# Menggunakan add_row dengan string bukan list
menu_table.add_row("v", "View a Task")
menu_table.add_row("c", "Create a task")
menu_table.add_row("u", "Update a task")
menu_table.add_row("d", "Delete a task")
menu_table.add_row("q", "Quit")

console.print("Selamat Datang di Task Manager!")
console.print(menu_table)

while True:
    action = input("Action? (Tekan 'q' untuk keluar): ")
    
    if action == "c":
        tambah_data()
    elif action == "v":
        tampilkan_data()
    elif action == "u":
        update_data()
    elif action == "d":
        hapus_data()
    elif action == "q":
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Inputan action tidak ada. Mohon masukkan Sesuai Key yang ada.")
