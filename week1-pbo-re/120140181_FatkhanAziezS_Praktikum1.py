import random

class Robot:
    def __init__(self, name, hp, attack, defense, accuracy):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.accuracy = accuracy  # nilai antara 0 - 100

    def attack_enemy(self, enemy):
        hit_chance = random.randint(1, 100)
        if hit_chance <= self.accuracy:
            damage = max(0, self.attack - enemy.defense)
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dan memberi {damage} damage!")
        else:
            print(f"------------ {self.name} gagal menyerang ------------------")

    def is_alive(self):
        return self.hp > 0

    def display_status(self):
        print(f"{self.name} [{self.hp}][{self.defense}]")


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def play(self):
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\nRound-{self.round} {'='*50}")
            self.robot1.display_status()
            self.robot2.display_status()

            for robot, enemy in [(self.robot1, self.robot2), (self.robot2, self.robot1)]:
                if not enemy.is_alive():
                    break

                print("\n1. Attack   2. Defense   3. Giveup")
                choice = input(f"{robot.name}, pilih aksi: ")

                if choice == '1':
                    robot.attack_enemy(enemy)
                elif choice == '2':
                    robot.defense += 1
                    print(f"{robot.name} meningkatkan pertahanannya!")
                elif choice == '3':
                    print(f"{robot.name} menyerah!")
                    robot.hp = 0
                    break
                else:
                    print("Pilihan tidak valid!")

            self.round += 1

        self.declare_winner()

    def declare_winner(self):
        if self.robot1.is_alive():
            print(f"\n{self.robot1.name} menang!")
        elif self.robot2.is_alive():
            print(f"\n{self.robot2.name} menang!")
        else:
            print("\nKeduanya KO! Tidak ada pemenang.")


# ======== MAIN ===========
if __name__ == "__main__":
    # Inisialisasi robot
    r1 = Robot("Atreus", hp=500, attack=100, defense=10, accuracy=90)
    r2 = Robot("Daedalus", hp=750, attack=120, defense=8, accuracy=75)

    game = Game(r1, r2)
    game.play()
