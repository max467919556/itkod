import random


class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def calculate_damage(self, incoming_damage):
        """Метод для расчета фактического урона с учетом брони."""
        effective_damage = incoming_damage - self.armor
        if effective_damage < 0:
            effective_damage = 0
        return effective_damage


class Player(Person):
    def attack(self, enemy):
        """Метод для атаки врага."""
        print(f"Игрок атакует врага на {self.damage} урона.")
        damage_to_enemy = enemy.calculate_damage(self.damage)
        enemy.health -= damage_to_enemy
        print(f"Враг получил {damage_to_enemy} урона. У врага осталось {enemy.health} здоровья.")


class Enemy(Person):
    def attack(self, player):
        """Метод для атаки игрока."""
        print(f"Враг атакует игрока на {self.damage} урона.")
        damage_to_player = player.calculate_damage(self.damage)
        player.health -= damage_to_player
        print(f"Игрок получил {damage_to_player} урона. У игрока осталось {player.health} здоровья.")


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        """Метод для начала боя между игроком и врагом."""
        while self.player.health > 0 and self.enemy.health > 0:
            # Игрок атакует первым
            self.player.attack(self.enemy)
            if self.enemy.health <= 0:
                print("Игрок победил врага!")
                break

            # Враг атакует
            self.enemy.attack(self.player)
            if self.player.health <= 0:
                print("Враг победил игрока!")
                break


# Пример использования
if __name__ == "__main__":
    player = Player(health=100, damage=20, armor=5)
    enemy = Enemy(health=80, damage=15, armor=3)

    game = Game(player, enemy)
    game.start_battle()
