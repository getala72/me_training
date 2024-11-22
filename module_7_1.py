# Задача "Учёт товаров":

# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.

# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:

# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.



# Вывод на консоль:

# Первый запуск:

# Spaghetti, 3.4, Groceries

# Potato, 50.5, Vegetables

# Spaghetti, 3.4, Groceries

# Potato, 5.5, Vegetables

# Второй запуск:

# Spaghetti, 3.4, Groceries

# Продукт Potato, 50.5, Vegetables уже есть в магазине

# Продукт Spaghetti, 3.4, Groceries уже есть в магазине

# Продукт Potato, 5.5, Vegetables уже есть в магазине

# Potato, 50.5, Vegetables

# Spaghetti, 3.4, Groceries

# Potato, 5.5, Vegetables

# Как выглядит файл после запусков (см. файл домашнего задания)


# Примечания:

# Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
# При проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
# Не забывайте закрывать файл вызывая метод close() у объектов файла.

class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_names = {product.split(', ')[0] for product in existing_products}

        new_products = []
        for product in products:
            if product.name not in existing_names:
                new_products.append(str(product))
                existing_names.add(product.name)
            else:
                print(f'Продукт {product} уже есть в магазине')

        if new_products:
            with open(self.__file_name, 'a', encoding='utf-8') as f:
                f.write('\n'.join(new_products) + '\n')

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())

           
           
                
        
    #  Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:

# Инкапсулированный атрибут __file_name = 'products.txt'.
# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
# Метод add(self, *products), который принимает неограниченное количество объектов класса Product. 
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). 
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .


