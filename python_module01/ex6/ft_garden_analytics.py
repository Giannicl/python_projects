class GardenManager:
    garden_networks = {}
    total_gardens = 0

    @staticmethod
    def height_validation(height):
        if height > 0:
            return True
        else:
            return False

    @classmethod
    def create_garden_network(cls, network_name):
        cls.garden_networks[network_name] = {}

    @classmethod
    def add_member(cls, network_name, member, score):
        cls.garden_networks[network_name][member] = int(score)
        GardenManager.total_gardens += 1

    class GardenStats:
        plants_added = 0
        total_growth = 0
        regular = 0
        flowering = 0
        prize_flowers = 0

        @classmethod
        def add_plant(cls, name, garden):
            cls.plants_added += 1
            return print(f"Added {name} to {garden}'s garden")

        @classmethod
        def add_regular(cls):
            cls.regular += 1

        @classmethod
        def add_flowering(cls):
            cls.flowering += 1

        @classmethod
        def add_prize_flowers(cls):
            cls.prize_flowers += 1

        @classmethod
        def growing(cls):
            cls.total_growth += 1


class Plant:
    def __init__(self, name, height, garden):
        self.name = name
        self.height = int(height)
        GardenManager.GardenStats.add_plant(name, garden)
        if self.__class__ == Plant:
            GardenManager.GardenStats.add_regular()
        self.growth = 0

    def grow(self, amount):
        self.height += amount
        self.growth = amount
        GardenManager.GardenStats.growing()
        return self.growth

    def getinfo(self):
        print(
            f"Plant created: {self.name} Height updated: "
            f"{self.height}cm Age updated: {self.age} days"
        )


class FloweringPlant(Plant):
    def __init__(self, name, height, garden, color):
        super().__init__(name, height, garden)
        self.color = color
        if self.__class__ == FloweringPlant:
            GardenManager.GardenStats.add_flowering()


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, garden, color):
        super().__init__(name, height, garden, color)
        GardenManager.GardenStats.add_prize_flowers()

    def give_points(self, points):
        self._points = points


def main():
    print("=== Garden Management System Demo ===\n")
    oak_tree = Plant("Oak Tree", 100, "Alice")
    rose = FloweringPlant("Rose", 25, "Alice", "red")
    sunflower = PrizeFlower("Sunflower", 50, "Alice", "yellow")

    print("\nAlice is helping all plants grow...")
    print(f"{oak_tree.name} grew {oak_tree.grow(1)}cm")
    print(f"{rose.name} grew {rose.grow(1)}cm")
    print(f"{sunflower.name} grew {sunflower.grow(1)}cm")

    print("\n=== Alice's Garden Report ===")
    print("Plants in garden:")
    print(f"- {oak_tree.name}: {oak_tree.height}cm")
    print(f"- {rose.name}: {rose.height}cm, {rose.color} flowers (blooming)")
    sunflower.give_points(10)
    print(
        f"- {sunflower.name}: {sunflower.height}cm {sunflower.color} "
        f"flowers (blooming), Prize points: {sunflower._points}"
    )
    print(
        f"\nPlants added: {GardenManager.GardenStats.plants_added}, "
        f"Total growth: {GardenManager.GardenStats.total_growth} "
    )
    print(
        f"Plants types: {GardenManager.GardenStats.regular} regular, "
        f"{GardenManager.GardenStats.flowering} flowering, "
        f"{GardenManager.GardenStats.prize_flowers} prize flowers"
    )
    GardenManager.create_garden_network("Community")
    GardenManager.add_member("Community", "Alice", 218)
    GardenManager.add_member("Community", "Bob", 92)
    print(f"\nHeight validation test: {GardenManager.height_validation(100)}")
    print(
        f"Garden scores - Alice: "
        f"{GardenManager.garden_networks["Community"]["Alice"]}, "
        f"Bob: {GardenManager.garden_networks["Community"]["Bob"]}"
    )
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
