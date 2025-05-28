import random

# Daftar kata
words = [
    'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
]

# Gambar tahapan Hangman
stages = [
    """
       _______
       |     |
       |     
       |    
       |    
       |    
    _________
    """,
    """
       _______
       |     |
       |     O
       |    
       |    
       |    
    _________
    """,
    """
       _______
       |     |
       |     O
       |     |
       |    
       |    
    _________
    """,
    """
       _______
       |     |
       |     O
       |    /|
       |    
       |    
    _________
    """,
    """
       _______
       |     |
       |     O
       |    /|\\
       |    
       |    
    _________
    """,
    """
       _______
       |     |
       |     O
       |    /|\\
       |    / 
       |    
    _________
    """,
    """
       _______
       |     |
       |     O
       |    /|\\
       |    / \\
       |    
    _________
    """
]

MAX_ATTEMPTS = len(stages) - 1

def main():
    word = random.choice(words)
    guessed = ['_' for _ in word]
    used_letters = set()
    attempts = 0

    print("Selamat datang di Hangman!\n")

    while attempts < MAX_ATTEMPTS and '_' in guessed:
        print(stages[attempts])
        print("Kata: ", ' '.join(guessed))
        print("Huruf yang sudah ditebak: ", ' '.join(sorted(used_letters)))
        
        guess = input("Tebak satu huruf: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Masukkan hanya satu huruf.")
            continue
        if guess in used_letters:
            print("Kamu sudah menebak huruf itu.")
            continue

        used_letters.add(guess)

        if guess in word:
            for i, c in enumerate(word):
                if c == guess:
                    guessed[i] = c
            print("Tebakan benar!")
        else:
            print("Tebakan salah.")
            attempts += 1

    # Akhir permainan
    print(stages[attempts])
    if '_' not in guessed:
        print("Selamat! Kamu berhasil menebak katanya:", word)
    else:
        print("Game over! Kata yang benar adalah:", word)

if __name__ == "__main__":
    main()
