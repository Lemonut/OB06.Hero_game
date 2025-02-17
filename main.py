class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден! {self.player.name} победил!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} побежден! {self.computer.name} победил!")
                break

            # Вывод текущего состояния
            print(f"{self.player.name}: {self.player.health} здоровья, {self.computer.name}: {self.computer.health} здоровья\n")


# Запуск игры
if __name__ == "__main__":
    game = Game("Игрок")
    game.start()