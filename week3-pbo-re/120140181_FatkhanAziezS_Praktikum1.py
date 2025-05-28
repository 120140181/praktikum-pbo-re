import math

while True:
    try:
        user_input = input("Masukkan angka: ")
        number = float(user_input)

        if number < 0:
            raise ValueError("Input tidak valid. Harap masukkan angka yang positif.")
        elif number == 0:
            raise ZeroDivisionError("Error: Akar kuadrat dari nol tidak diperbolehkan.")

        hasil = math.sqrt(number)
        print(f"Akar kuadrat dari {int(number)} adalah {hasil}")
        break  # keluar dari loop jika berhasil
    except ValueError as ve:
        print(ve)
    except ZeroDivisionError as ze:
        print(ze)
    except:
        print("Input tidak valid. Harap masukkan angka yang valid.")
