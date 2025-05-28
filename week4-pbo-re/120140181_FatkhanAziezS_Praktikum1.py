import random

# Inisialisasi papan
def init_board():
    return [['?' for _ in range(3)] for _ in range(3)]

# Tempatkan bom secara acak
def place_bomb():
    return random.randint(0, 2), random.randint(0, 2)

# Tampilkan papan ke layar
def print_board(board):
    print("\n" + "="*40)
    for row in board:
        print(' '.join(row))
    print("="*40)

def main():
    board = init_board()
    bomb_row, bomb_col = place_bomb()
    revealed_count = 0
    total_safe_cells = 9 - 1

    while True:
        print_board(board)

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            # Validasi input
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Input di luar batas! Masukkan angka antara 0 dan 2.")
                continue

            if board[row][col] != '?':
                print("Kotak ini sudah dibuka. Pilih kotak lain.")
                continue

            if row == bomb_row and col == bomb_col:
                board[row][col] = 'X'
                print_board(board)
                print("Boom! Kamu kalah!")
                break
            else:
                board[row][col] = '0'
                revealed_count += 1

                if revealed_count == total_safe_cells:
                    print_board(board)
                    print("Selamat! Kamu menang!")
                    break

        except ValueError:
            print("Input tidak valid. Masukkan angka antara 0 dan 2.")

if __name__ == "__main__":
    main()
