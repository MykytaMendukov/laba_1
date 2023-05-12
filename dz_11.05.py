class Clothing:
    def __init__(self, material, name, price, size):
        self.material = material
        self.name = name
        self.price = price
        self.size = size

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def get_items(self):
        return self.inventory

    def search_items(self, keyword):
        matching_items = []
        for item in self.inventory:
            if keyword.lower() in item.name.lower():
                matching_items.append(item)
        return matching_items


item1 = Clothing("cotton", "T-shirt", 20, "M")
item2 = Clothing("wool", "Sweater", 50, "L")
item3 = Clothing("denim", "Jeans", 40, "S")

store = Store("Fashion Shop", "123 Main Street")

store.add_item(item1)
store.add_item(item2)
store.add_item(item3)

