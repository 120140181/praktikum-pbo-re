import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Penyimpanan akun sementara (dalam dictionary)
akun = {}

# Fungsi untuk register
def register():
    username = reg_username.get()
    password = reg_password.get()

    if username in akun:
        messagebox.showerror("Gagal", "Username sudah terdaftar!")
    elif username == "" or password == "":
        messagebox.showerror("Gagal", "Username dan password tidak boleh kosong!")
    else:
        akun[username] = password
        messagebox.showinfo("Sukses", "Registrasi berhasil!")

# Fungsi untuk login
def login():
    username = login_username.get()
    password = login_password.get()

    if akun.get(username) == password:
        messagebox.showinfo("Sukses", f"Selamat datang, {username}!")
    else:
        messagebox.showerror("Gagal", "Username atau password salah!")

# Buat window utama
root = tk.Tk()
root.title("Login - Register")
root.geometry("300x300")

# Tab Control
tab_control = ttk.Notebook(root)

# Tab Register
tab_register = ttk.Frame(tab_control)
tab_control.add(tab_register, text='Register')

ttk.Label(tab_register, text="Username:").pack(pady=5)
reg_username = ttk.Entry(tab_register)
reg_username.pack(pady=5)

ttk.Label(tab_register, text="Password:").pack(pady=5)
reg_password = ttk.Entry(tab_register, show="*")
reg_password.pack(pady=5)

ttk.Button(tab_register, text="Daftar", command=register).pack(pady=10)

# Tab Login
tab_login = ttk.Frame(tab_control)
tab_control.add(tab_login, text='Login')

ttk.Label(tab_login, text="Username:").pack(pady=5)
login_username = ttk.Entry(tab_login)
login_username.pack(pady=5)

ttk.Label(tab_login, text="Password:").pack(pady=5)
login_password = ttk.Entry(tab_login, show="*")
login_password.pack(pady=5)

ttk.Button(tab_login, text="Masuk", command=login).pack(pady=10)

tab_control.pack(expand=1, fill="both")

# Jalankan aplikasi
root.mainloop()
