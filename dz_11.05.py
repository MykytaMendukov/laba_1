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
        print(f'{item.name} був доданий до {self.name}')

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f'{item.name} був видалений з {self.name}')
        else:
            print(f'{item.name} не був знайдений у {self.name}')

    def get_items(self):
        return self.inventory

    def search_items(self, search):
        self.search = search
        for item in self.inventory:
            if search.lower() in item.name.lower():
                print(f"\nІнформація про шуканий продукт за ключовим словом - '{search}':")
                print(f'Name: {item.name}, Material: {item.material}, Size: {item.size}, Price: {item.price}')
    def __str__(self):
        return f'Store Name: {self.name}, Address: {self.address}'


item1 = Clothing('cotton', 'T-shirt', 100, 'M')
item2 = Clothing('wool', 'Sweater', 150, 'XL')
item3 = Clothing('denim', 'Jeans', 120, 'S')
item4 = Clothing('leather', 'Jacket', 200, 'L')

store = Store('Fashion Store', 'Soborna 25a')

print(store) #виведання назви магазину

store.inventory = [item1, item2, item3, item4]

print('\nПочатковий список товарів: ')
for item in store.inventory:
    print(f'Name: {item.name}, Material: {item.material}, Size: {item.size}, Price: {item.price}')

print()

item5 = Clothing('wool', 'Cap', 130, 'XS')
store.add_item(item5)  #додавання елемента одягу

store.remove_item(item2)  #видалення елемента одягу

store.search_items('ans')   #пошук одягу за ключовим словом


print('\nСписок товарв після редагування: ')
for item in store.get_items():
    print(f'Name: {item.name}, Material: {item.material}, Size: {item.size}, Price: {item.price}')

class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.cart = []
    def add_to_cart(self, purchase):
        self.cart.append(purchase)
        print(f'{purchase.name} був доданий до кошика {self.name}')
    def remove_from_cart(self, purchase):
        if purchase in self.cart:
            self.cart.remove(purchase)
            print(f'{purchase.name} був видалений з кошика {self.name}')
        else:
            print(f'{purchase.name} не був знайдений у кошику {self.name}')
    def view_cart(self):
        for purchase in self.cart:
            print(
                f'Name: {purchase.name}, Material: {purchase.material}, Size: {purchase.size}, Price: {purchase.price}')
    def checkout(self):
        bill = 0
        for purchase in self.cart:
            bill += purchase.price
        print(f'До сплати {bill} грн')
        if bill > self.budget:
            print(f'Недостатньо коштів, для покупки поповніть разхунок на {bill - self.budget} грн')
        else:
            print(f'Оплата пройшла успішно.\nЧек:')
            for purchase in self.cart:
                print(f'{purchase.name} - {purchase.price} грн')
            print(f'На рахунку залишається {self.budget - bill} грн')
    def __str__(self):
        return f'{self.name} - Бютжет: {self.budget}'

cost1 = Customer('Oleg', 2030)
cost2 = Customer('Vika', 1500)
cost3 = Customer('Dmytro', 200)

cost1.cart = [item1, item5]   #додавання товір до кошику клієнтів
cost2.cart = [item3, item4]
cost3.cart = [item1]

cost_l = []  #створюємо базу з клієнтами
cost_l.append(cost1)
cost_l.append(cost2)
cost_l.append(cost3)

for cost in cost_l:    #виведення початкових кошиків
    print(f'\n{cost}\nКошик клієнта {cost.name}:')
    cost.view_cart()

print()
cost1.add_to_cart(item3) #додавання до кошика
cost3.add_to_cart(item4)
cost2.remove_from_cart(item3) #видалення елементу з кошика

for cost in cost_l:   #виведення оновлених кошиків
    print(f'\n{cost}\nКошик клієнта {cost.name}:')
    cost.view_cart()

for cost in cost_l:
    print(f'\nКлієнт- {cost.name}')
    cost.checkout()  #виведення платежів клієнтів