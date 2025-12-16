class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = int(height)
        self.age = int(age)

    def grow(self, days: int, amount: int):
        self.height += amount
        self.age += days

    def getinfo(self):
        print(f"{self.name} ({self.height}cm, {self.age} days)")


def main():
    yiannis = Plant("Yiannis", 25, 30)
    marco = Plant("Marco", 30, 11)
    robin = Plant("Robin", 50, 3)
    koodal = Plant("koodal", 20, 40)
    ama = Plant("Ama", 15, 100)

    list = [yiannis, marco, robin, koodal, ama]
    print("=== Plant Factory Output ===")
    total = 0
    for i in list:
        total += 1
        print("Created: ", end=" ")
        i.getinfo()
    print(f"Total plants created: {total}")


if __name__ == "__main__":
    main()
