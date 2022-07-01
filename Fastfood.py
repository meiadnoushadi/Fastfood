import enum
from abc import ABC, abstractclassmethod
# ----------------------------------------------------------------------------------


class Delivery(enum.Enum):
    bike = 10000
    engine = 15000
    drone = 50000


# ----------------------------------------------------------------------------------


class Item(ABC):
    def __init__(self, weight, priceDaily) -> None:
        self.weight = weight
        self.priceDaily = priceDaily

    @abstractclassmethod
    def calculate_expense(self):
        pass
# ----------------------------------------------------------------------------------


class Cheese(Item):
    def __init__(self, weight, priceDaily):
        if weight > 100:
            weight = 100
        Item.__init__(self, weight, priceDaily)

    def calculate_expense(self):
        return self.weight*self.priceDaily
# ----------------------------------------------------------------------------------


class Meat(Item):
    def __init__(self, weight, priceDaily):
        Item.__init__(self, weight, priceDaily)

    def calculate_expense(self):
        return self.weight*self.priceDaily
# ----------------------------------------------------------------------------------


class Ham(Meat):
    def __init__(self, weight, priceDaily, smoky):
        Item.__init__(self, weight, priceDaily)
        self.smoky = smoky

    def calculate_expense(self):
        if not self.smoky:
            return self.weight*self.priceDaily
        return self.weight*self.priceDaily+6000
# ----------------------------------------------------------------------------------


class RedMeat(Meat):
    def __init__(self, weight, priceDaily):
        Item.__init__(self, weight, priceDaily)

# ----------------------------------------------------------------------------------


class Chicken(Meat):
    def __init__(self, weight, priceDaily):
        Item.__init__(self, weight, priceDaily)

# ----------------------------------------------------------------------------------


class Vegetable(Item):
    def __init__(self, weight, priceDaily):
        Item.__init__(self, weight, priceDaily)

    @abstractclassmethod
    def calculate_expense(self):
        pass
# ----------------------------------------------------------------------------------


class Tomato(Vegetable):
    def __init__(self, weight, priceDaily):
        Item.__init__(self, weight, priceDaily)

    def calculate_expense(self):
        return self.weight*self.priceDaily
# ----------------------------------------------------------------------------------


class Mushroom(Vegetable):
    def __init__(self, weight, priceDaily, canned):
        Item.__init__(self, weight, priceDaily)
        self.canned = canned

    def calculate_expense(self):
        if not self.canned:
            return self.weight*(self.priceDaily+20000)
        return self.weight*self.priceDaily
# ----------------------------------------------------------------------------------


class PizzaSize(enum.Enum):
    mini = 1
    midium = 2
    big = 4

# ----------------------------------------------------------------------------------


class OrderItem(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def calculate_expense(self):
        pass
# ----------------------------------------------------------------------------------


class Pizza(OrderItem):
    def __init__(self, name, size) -> None:
        self.name = name
        self.__basicPrice = 10000
        self.size = size
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def calculate_expense(self):
        sum = self.__basicPrice
        for item in self.items:
            sum += item.calculate_expense()
        return sum*self.size

# ----------------------------------------------------------------------------------


class Drink(OrderItem):
    def __init__(self, name, weight, carbonated) -> None:
        self.name = name
        self.weight = weight
        self.carbonated = carbonated

    def calculate_expense(self):
        if not self.carbonated:
            return self.weight*20
        return self.weight*20 + 5000

# ----------------------------------------------------------------------------------


class Order:
    def __init__(self, deliveryType):
        self.deliveryType = deliveryType
        self.orderItemList = []

    def add_order_item(self, object):
        self.orderItemList.append(object)

    def all_calculate_expense(self):
        sum = self.deliveryType
        for item in self.orderItemList:
            sum += item.calculate_expense()
        return sum

    def __str__(self) -> str:
        temp = f"Delivery : {str(self.deliveryType)}\n"
        for item in self.orderItemList:
            temp += f"{item.name} : {str(item.calculate_expense())}\n"
        return temp

# ------------------------------
pizza1 = Pizza("mini pizza Meat", PizzaSize.mini.value)
pizza1.add_items(Tomato(0.1, 12000))
pizza1.add_items(Chicken(0.150, 56000))
pizza1.add_items(RedMeat(0.08, 210000))
pizza1.add_items(Cheese(0.05, 320000))
# ------------------------------
pizza2 = Pizza("big pizza Meat", PizzaSize.big.value)
pizza2.add_items(Tomato(0.1, 12000))
pizza2.add_items(Chicken(0.150, 56000))
pizza2.add_items(RedMeat(0.08, 210000))
pizza2.add_items(Cheese(0.05, 320000))
# ------------------------------
d1 = Drink("pepsi ", 300, True)
# ------------------------------
d2 = Drink("pepsi ", 200, False)
# ------------------------------

o1 = Order(Delivery.drone.value)
o1.add_order_item(pizza1)
o1.add_order_item(pizza2)
o1.add_order_item(d2)
o1.add_order_item(d1)

print(o1, end="totall price: ")
print(o1.all_calculate_expense(), end="  toman")

# print(pizza1.calculate_expense())
# print(pizza2.calculate_expense())
# print(d1.calculate_expense())
# print(d2.calculate_expense())
# print(Delivery.drone.value)