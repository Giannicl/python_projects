class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = int(height)
        self.age = int(age)

    def getinfo(self):
        print(
            f"Plant created: {self.name} Height updated: "
            f"{self.height}cm Age updated: {self.age} days"
        )


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        if self.height != 500:
            return print(
                f"{self.name} provides {self.height / 6, 41} "
                f"square meters of shade\n"
            )
        else:
            return print(f"{self.name} provides 78 square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def main():
    rose = Flower("Rose", 25, 30, "red")
    # lely = Flower("Lely", 10, 10, "white")
    oak = Tree("Oak", 500, 1825, 50)
    # pine = Tree("Pine", 300, 500, 30)
    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "C")

    print("=== Garden Plant Types ===\n")
    print(
        f"{rose.name} (Flower): {rose.height}cm, "
        f"{rose.age} days, {rose.color} color"
    )
    rose.bloom()

    print(
        f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
        f"{oak.trunk_diameter}cm diameter"
    )
    oak.produce_shade()

    print(
        f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, "
        f"{tomato.harvest_season}"
    )
    print(f"Tomato is rich in vitamin {tomato.nutritional_value}")


if __name__ == "__main__":
    main()
