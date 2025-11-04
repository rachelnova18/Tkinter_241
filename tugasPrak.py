import tkinter as tk
import tkinter.messagebox as msg

# Fungsi untuk tombol hasil prediksi
def hasil_prediksi():
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")

# Membuat jendela utama
top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("400x550")
top.configure(bg="LightGreen")    # atur warna latar belakang

# Label judul aplikasi
def buat_label_judul():
    label_judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16), bg="LightGreen")
    label_judul.pack(pady=10)
buat_label_judul()

# Input nilai mata pelajaran
labels = ["Matematika", "Fisika", "Kimia", "Biologi", "Bahasa Indonesia", "Bahasa Inggris", "Sejarah", "Geografi", "Ekonomi", "Sosiologi"]
entries = []    
for label in labels:
    frame = tk.Frame(top, bg="LightGreen")
    frame.pack(pady=2)
    lbl = tk.Label(frame, text=label + ":", width=20, anchor='w', bg="LightGreen")
    lbl.pack(side=tk.LEFT)
    entry = tk.Entry(frame, bd=5)
    entry.pack(side=tk.RIGHT)
    entries.append(entry)

# Tombol hasil prediksi
tombol_hasil = tk.Button(top, text="Hasil Prediksi", command=hasil_prediksi)
tombol_hasil.pack(pady=20)  

# Label luaran hasil prediksi
label_hasil = tk.Label(top, text="Hasil Prediksi Akan Ditampilkan Di Sini", font=("Arial", 12), bg="LightGreen")
label_hasil.pack(pady=10)

top.mainloop()