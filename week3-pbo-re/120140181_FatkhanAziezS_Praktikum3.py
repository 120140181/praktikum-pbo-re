from abc import ABC, abstractmethod

# Abstraksi
class Animal(ABC):
    def __init__(self, name, age):
        if not name or not isinstance(age, int) or age < 0:
            raise ValueError("Nama harus diisi dan usia harus berupa angka >= 0.")
        self.__name = name
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

    def get_info(self):
        return f"{self.__name} ({self.__age} tahun)"

# Inheritance dan Polimorfisme
class Dog(Animal):
    def make_sound(self):
        return "Guk guk!"

class Cat(Animal):
    def make_sound(self):
        return "Meong!"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

# Manajemen Kebun Binatang
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Hanya objek bertipe Animal yang bisa ditambahkan.")
        self.animals.append(animal)
        print(f"{animal.get_info()} berhasil ditambahkan ke kebun binatang.")

    def show_animals(self):
        if not self.animals:
            print("Tidak ada hewan di kebun binatang.")
        else:
            print("\nDaftar Hewan:")
            for animal in self.animals:
                print(f"- {animal.get_info()} bersuara: {animal.make_sound()}")

# Program utama
def main():
    kebun = Zoo()

    while True:
        print("\nMenu:")
        print("1. Tambah Hewan")
        print("2. Tampilkan Hewan")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")
        try:
            if pilihan == '1':
                jenis = input("Jenis hewan (Dog/Cat/Elephant): ").strip().lower()
                nama = input("Nama hewan: ").strip()
                usia = int(input("Usia hewan: "))

                if jenis == "dog":
                    hewan = Dog(nama, usia)
                elif jenis == "cat":
                    hewan = Cat(nama, usia)
                elif jenis == "elephant":
                    hewan = Elephant(nama, usia)
                else:
                    raise ValueError("Jenis hewan tidak dikenal.")

                kebun.add_animal(hewan)

            elif pilihan == '2':
                kebun.show_animals()

            elif pilihan == '3':
                print("Keluar dari program.")
                break

            else:
                print("Pilihan tidak valid. Masukkan angka 1-3.")

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Terjadi error: {e}")

if __name__ == "__main__":
    main()
