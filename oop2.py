class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехал(а) на скорости {self.speed} км/ч.")

    def stop(self):
        print(f"{self.name} остановился(ась).")

    def turn(self, direction):
        print(f"{self.name} повернул(а) {direction}.")

class TownCar(Car):
    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

# Пример использования
if __name__ == "__main__":
    town_car = TownCar(60, "синий", "Городской автомобиль")
    sport_car = SportCar(120, "красный", "Спортивный автомобиль")
    work_car = WorkCar(70, "зеленый", "Рабочий автомобиль")
    police_car = PoliceCar(100, "черный", "Полицейский автомобиль")

    town_car.go()
    sport_car.turn("налево")
    work_car.stop()
    police_car.go()
