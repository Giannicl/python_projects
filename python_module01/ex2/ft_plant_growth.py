class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = int(height)
        self.age = int(age)

    def grow(self, days: int, amount: int):
        self.height += amount
        self.age += days

    def getinfo(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    rose = Plant("Rose", 25, 30)
    for i in range(1, 7 + 1):
        rose.grow(1, 5)
        print(f"=== Day {i} ===")
        rose.getinfo()


if __name__ == "__main__":
    main()
