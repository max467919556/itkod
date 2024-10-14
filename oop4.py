class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}, Тип: {self.toy_type}"


class ToyFactory:
    def __init__(self):
        pass

    def purchase_materials(self):
        """Метод для закупки сырья."""
        print("Закупка сырья для производства игрушек.")

    def sew_toy(self):
        """Метод для пошива игрушки."""
        print("Пошив игрушки.")

    def paint_toy(self):
        """Метод для окраски игрушки."""
        print("Окраска игрушки.")

    def create_toy(self, name, color, toy_type):
        """Метод для создания новой игрушки."""
        self.purchase_materials()
        self.sew_toy()
        self.paint_toy()

        new_toy = Toy(name, color, toy_type)
        print(f"Игрушка создана: {new_toy}")
        return new_toy


# Пример использования
if __name__ == "__main__":
    factory = ToyFactory()
    toy1 = factory.create_toy("Мягкий медведь", "коричневый", "животное")
    toy2 = factory.create_toy("Супергерой", "синий", "персонаж мультфильма")
