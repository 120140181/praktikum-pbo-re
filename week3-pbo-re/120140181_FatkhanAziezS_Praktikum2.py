tugas = []

while True:
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")
    
    try:
        pilihan = int(input("Masukkan pilihan (1/2/3/4): "))

        if pilihan == 1:
            item = input("Masukkan tugas yang ingin ditambahkan: ").strip()
            if not item:
                raise ValueError("Tugas tidak boleh kosong.")
            tugas.append(item)
            print("Tugas berhasil ditambahkan!")

        elif pilihan == 2:
            if not tugas:
                raise IndexError("Daftar tugas kosong, tidak bisa menghapus.")
            try:
                idx = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                if idx < 1 or idx > len(tugas):
                    raise IndexError(f"Tugas dengan nomor {idx} tidak ditemukan.")
                removed = tugas.pop(idx - 1)
                print(f"Tugas '{removed}' berhasil dihapus.")
            except ValueError:
                print("Input harus berupa angka.")

        elif pilihan == 3:
            if not tugas:
                print("Daftar tugas kosong.")
            else:
                print("Daftar Tugas:")
                for i, t in enumerate(tugas, 1):
                    print(f"{i}. {t}")

        elif pilihan == 4:
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka antara 1 hingga 4.")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
    except Exception as e:
        print(f"Error: {e}")
