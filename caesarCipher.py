import tkinter as tk
from tkinter import ttk, messagebox

# Fungsi enkripsi
def enkripsi(plain_text, shift):
    chipher_text = ""
    for char in plain_text:
        if char.isupper():  # Huruf besar
            chipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():  # Huruf kecil
            chipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            chipher_text += char
    return chipher_text

# Fungsi deskripsi
def deskripsi(chipher_text, shift):
    plain_text = ""
    for char in chipher_text:
        if char.isupper():  # Huruf besar
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():  # Huruf kecil
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

# Fungsi untuk tombol enkripsi
def enkripsi_text():
    try:
        plain_text = entry_plain_text.get()
        shift = int(entry_shift.get())
        if not (1 <= shift <= 25):
            raise ValueError("Pergeseran harus antara 1 dan 25")
        chipher_text = enkripsi(plain_text, shift)
        entry_chipher_text.delete(0, tk.END)
        entry_chipher_text.insert(tk.END, chipher_text)
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai pergeseran yang valid (1-25)")

# Fungsi untuk tombol deskripsi
def deskripsi_text():
    try:
        chipher_text = entry_chipher_text.get()
        shift = int(entry_shift.get())
        if not (1 <= shift <= 25):
            raise ValueError("Pergeseran harus antara 1 dan 25")
        plain_text = deskripsi(chipher_text, shift)
        entry_plain_text.delete(0, tk.END)
        entry_plain_text.insert(tk.END, plain_text)
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai pergeseran yang valid (1-25)")

# Setup UI dengan Tkinter
root = tk.Tk()
root.title("Program Enkripsi dan Deskripsi Text")
root.geometry("600x500")
root.configure(bg="#f0f8ff")  # Background utama lebih terang

# Gaya global untuk widget
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f0f8ff", foreground="#333")
style.configure("TButton", font=("Arial", 10, "bold"), foreground="#fff", background="#4CAF50")  # Hijau lebih menarik
style.configure("TEntry", font=("Arial", 12), padding=5)

# Frame utama
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Judul aplikasi
title_label = ttk.Label(main_frame, text="Program Enkripsi dan Deskripsi Text", font=("Arial", 23, "bold"), foreground="#007acc")
title_label.pack(pady=10)

# Frame untuk Text Asli (Plaintext)
frame_plain_text = ttk.Frame(main_frame, padding="10", relief=tk.RAISED, borderwidth=2)
frame_plain_text.pack(pady=10, fill=tk.X)
label_plain_text = ttk.Label(frame_plain_text, text="Masukkan Text Asli (Plaintext):")
label_plain_text.pack(pady=5)
entry_plain_text = ttk.Entry(frame_plain_text, width=60)
entry_plain_text.pack(pady=5)

# Frame untuk Shift
frame_shift = ttk.Frame(main_frame, padding="10", relief=tk.RAISED, borderwidth=2)
frame_shift.pack(pady=10, fill=tk.X)
label_shift = ttk.Label(frame_shift, text="Masukkan Nilai Pergeseran (1-25):")
label_shift.pack(pady=5)
entry_shift = ttk.Entry(frame_shift, width=60)
entry_shift.pack(pady=5)

# Frame untuk Chiper Text
frame_chipher_text = ttk.Frame(main_frame, padding="10", relief=tk.RAISED, borderwidth=2)
frame_chipher_text.pack(pady=10, fill=tk.X)
label_chipher_text = ttk.Label(frame_chipher_text, text="Hasil Enkripsi (Chipher Text):")
label_chipher_text.pack(pady=5)
entry_chipher_text = ttk.Entry(frame_chipher_text, width=60)
entry_chipher_text.pack(pady=5)

# Tombol Enkripsi dan Deskripsi
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

button_encrypt = ttk.Button(button_frame, text="Enkripsi", command=enkripsi_text)
button_encrypt.pack(side=tk.LEFT, padx=10)

button_decrypt = ttk.Button(button_frame, text="Deskripsi", command=deskripsi_text)
button_decrypt.pack(side=tk.LEFT, padx=10)

# Footer
footer_label = ttk.Label(root, text="Dibuat oleh Zakiul Fata & GPT", font=("Arial", 10), foreground="#555")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Main Loop
root.mainloop()
