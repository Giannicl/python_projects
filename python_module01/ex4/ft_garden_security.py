class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = int(height)
        self._age = int(age)

    def set_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self._height = value

    def set_age(self, value):
        if value < 0:
            print("Error: negative age!")
        else:
            self._age = value

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def getinfo(self):
        print(
            f"Plant created: {self.name}\n"
            f"Height updated: {self._height}cm [OK]\n"
            f"Age updated: {self._age} days [OK]\n"
        )


def main():
    rose = Plant("Rose", 25, 30)
    print("=== Garden Security System ===")
    rose.getinfo()
    rose.set_height(-5)

    print(f"Current plant: {rose.name} ({rose._height}cm, {rose._age} days)")


if __name__ == "__main__":
    main()
