# Задание 1
# class Product:
#     def __init__(self, name, shop_name, price):
#         self.__name = name
#         self.__shop_name = shop_name
#         self.__price = price
#
#
#     def get_name(self):
#         return self.__name
#
#     def get_shop_name(self):
#         return self.__shop_name
#
#     def get_price(self):
#         return self.__price
#
#     def __add__(self, other):
#         if isinstance(other, Product):
#             return int(self.get_price()) + int(other.get_price())
#
#
# class Stash:
#
#     def __init__(self):
#         self.__products = []
#
#     def append_products(self, product):
#         self.__products.append(product)
#
#     def get_products(self):
#         return self.__products
#
#     def get_by_index(self):
#         while True:
#             length = len(self.get_products()) - 1
#             index = None
#             try:
#                 index = int(input(f'Введите индекс от 0 до {length}'))
#             except ValueError as err:
#                 error_logged = str(err).split("'")[1]
#                 print(f"Данное значение {error_logged} не является int\n"
#                       f"пожалуйста укажите int ")
#             if index in range(0, length + 1):
#                 object = self.get_products()[index]
#                 return f'Наименование товара: {object.get_name()}\n' \
#                        f'Приобрести товар можно в магазине: {object.get_shop_name()}\n' \
#                        f'Цена товара: {object.get_price()}\n'
#             else:
#                 pass
#
#     def get_by_name(self, name):
#         for item in self.get_products():
#             if item.get_name() == name:
#                 return f'Наименование товара: {item.get_name()}\n' \
#                        f'Приобрести товар можно в магазине: {item.get_shop_name()}\n' \
#                        f'Цена товара: {item.get_price()}\n'
#
#     def sort_by_name(self):
#         self.__products.sort(key=lambda product: product.get_name())
#         return [product.get_name() for product in self.__products]
#
#     def sort_by_store(self):
#         self.__products.sort(key=lambda product: product.get_shop_name())
#         return [product.get_shop_name() for product in self.__products]
#
#     # Сортировка товаров по цене
#     def sort_by_price(self):
#         self.__products.sort(key=lambda product: product.get_price())
#         return [product.get_price() for product in self.__products]
#
#
# product1 = Product('Кола', 'Пятерочка', '200')
# product2 = Product('Фанта', 'Магнит', '180')
# stash = Stash()
# stash.append_products(product1)
# stash.append_products(product2)
# print(product1 + product2)
# print(stash.get_by_index())
# print(stash.get_by_name("Кола"))
# print(stash.sort_by_price())



# Задание 2

# class ElephantBee:
#
#     def __init__(self, bee: int, elephant: int):
#         self.bee = bee
#         self.elephant = elephant
#
#     def fly(self):
#         if self.bee >= self.elephant:
#             return True
#         else:
#             return False
#
#     def trumpet(self):
#         if self.elephant >= self.bee:
#             return "tu-tu-doo-doo"
#         else:
#             return "wzzzz"
#
#     def eat(self, meal: str, value: int):
#         if meal == 'grass':
#             self.elephant += value
#             if self.elephant > 100:
#                 self.elephant = 100
#             self.bee -= value
#             if self.bee <= 0:
#                 self.bee = 0
#
#         elif meal == 'nectar':
#             self.bee += value
#             if self.bee > 100:
#                 self.bee = 100
#             self.elephant -= value
#             if self.elephant <= 0:
#                 self.elephant = 0
#
# elephant_bee = ElephantBee(12, 10)
# print(elephant_bee.bee)
# print(elephant_bee.elephant)
# print(elephant_bee.fly())
# print(elephant_bee.trumpet())
# print(elephant_bee.eat('grass', 100))
# print(elephant_bee.bee)
# print(elephant_bee.elephant)

# Задание 3
class Bus:

    def __init__(self, speed: float,
                 seats: int,
                 max_speed: float,
                 passengers: list):
        self.speed = speed
        self.seats = seats
        self.max_speed = max_speed
        self.passengers = passengers
        self.empty_seats_flag = False
        self.dict_of_passengers = None

    def empty_seats(self):
        if self.seats > len(self.passengers):
            self.empty_seats_flag = True
        else:
            self.empty_seats_flag = False

    def make_dict_of_passengers(self):
        self.dict_of_passengers = dict()
        for key in range(1, self.seats + 1):
            self.dict_of_passengers[key] = None
        counter = 1
        for passenger in self.passengers:
            self.dict_of_passengers[counter] = passenger
            counter += 1

    def go_faster(self, correction: float):
        if self.speed + correction > self.max_speed:
            self.speed = self.max_speed
            print(f'This bus cant go faster than {self.max_speed}!')
        else:
            self.speed += correction

    def go_slower(self, correction: float):
        if self.speed - correction < 0:
            self.speed = 0
            print('The bus already stopped')
        else:
            self.speed -= correction

    def get_on_board(self, list_of_names):
        len_pass = len(self.passengers)
        if len_pass + len(list_of_names) <= self.seats:
            for passenger in list_of_names:
                self.passengers.append(passenger)
                self.dict_of_passengers[len_pass + 1] = passenger
                len_pass += 1
        else:
            print(f'К сожалению доступно только {self.seats} мест в автобусе')

    def get_off_board(self, list_of_names):
        for name in list_of_names:
            for item, num in zip(self.passengers, range(0, len(self.passengers))):
                if name == item:
                    del self.passengers[num]
                    self.make_dict_of_passengers()

    def __add__(self, other: str):
        other_list = [other]
        return self.get_on_board(other_list)

    def __sub__(self, other: str):
        other_list = [other]
        return self.get_off_board(other_list)

    def __contains__(self, item):
        for name in self.passengers:
            if item == name:
                return True
        return False


school_bus = Bus(40, 8, 120, ['Jhon', 'Harry', 'Rose', 'Peter', 'Samantha'])
school_bus.make_dict_of_passengers()
print(school_bus.empty_seats_flag)
print(school_bus.dict_of_passengers)
school_bus.go_slower(12)
print(school_bus.speed)
school_bus.get_on_board(['Chubrick'])
print(school_bus.passengers)
print(school_bus - 'Jhon')
print(school_bus.passengers)
print('Rose' in school_bus)
print(school_bus.dict_of_passengers)














