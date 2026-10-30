print("welcome to stock")

class Stock:
    def __init__(self, name=None, value=0):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} value is {self.value}"

class Inventory(Stock):
    def __init__(self):
        super().__init__()
        self.box = []

    def add_stock(self, name, value):
        self.box.append(f"item {name}, value is: {value}")

    def sale_off(self, name, value):
        found = False
        for i in range(len(self.box)):
            if f"item {name}" in self.box[i]:
                part = self.box[i].split(", value is: ")
                current_value = int(part[1])

                answer = current_value - int(value)
                self.box[i] = f"item {name}, value is: {answer}"
                return f"{name} left is: {answer}"
        return f"{name} not found"

    def full_up(self,name, add):
        found = False
        for i in range(len(self.box)):
            if f"item {name}" in self.box[i]:
                part = self.box[i].split(", value is: ")
                current_value = int(part[1])

                answer = current_value + int(add)
                self.box[i] = f"item {name}, value is: {answer}"
                return f"{name} left is: {answer}"
        return f"{name} not found"

    def show(self):
        return "\n".join(self.box)
    
    def save(self, filename):
        with open(filename, "w", encoding="utf-8")as f:
            for item in self.box:
                    f.write(item + "\n")

    def load(self, filename):
        self.box = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    self.box.append(line.rstrip("\n"))
        except FileNotFoundError:
            self.box = []

stock = Inventory()

while True:
    print("1.add item 2.sale off 3.full stock 4.show 5.save 6.load 7.exit")
    x = input("type: ")

    if x == "1":
        y = input("enter name (item)")
        x = input("enter volue")
        stock.add_stock(y, x)
        print()

    if x == "2":
        y = input("enter name (item)")
        x = input("enter how many you sale off")
        print(stock.sale_off(y, x))
        print()

    if x == "3":
        y = input("enter name(item)")
        x = input("how many you want to add")
        print(stock.full_up(y, x))
        print()

    if x == "4":
        print(stock.show())
        print()

    if x == "5":
        stock.save("stock.txt")
        print(stock.show())

    if x == "6":
        try:
            stock.load("stock.txt")
            print(stock.show())

        except FileNotFoundError:
            print("file not found")

    if x == "7":
        break
