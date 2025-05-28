# Input tinggi segitiga
height = int(input("Masukkan tinggi segitiga: "))

print(f"Height: {height}")
for i in range(1, height + 1):
    print("*" * (2 * i - 1))