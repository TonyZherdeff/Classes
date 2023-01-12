class Auto:
    def __init__(self, model, engine, year, price, color):
        self.model = model
        self.engine = engine
        self.year = year
        self.price = price
        self.color = color

    def change_model(self, new_model):
        self.model = new_model

    def change_engine(self, new_engine):
        self.engine = new_engine

    def change_year(self, new_year):
        self.year = new_year

    def change_price(self, new_price):
        self.price = new_price

    def change_color(self, new_color):
        self.color = new_color

    def print_class(self):
        print(f'Модель: {self.model}\n'
              f'Объем двигателя: {self.engine} кубических дюймов\n'
              f'Год выпуска: {self.year}\n'
              f'Цена: {self.price}\n'
              f'Цвет: {self.color}')


def work_with_class():
    print("Про первом использоавнии атрибуты "
          "класса необходимо проинициализировать, "
          "введите данные ниже")
    object_name = input("Введите имя объекта (латиницей):\n")
    new_model = input("Введите модель автомобиля:\n")
    new_engine = input("Введите объем двигателя:\n")
    new_year = input("Введите год выпуска:\n")
    new_price = input("Введите цену:\n")
    new_color = input("Введите цвет:\n")
    object_name = Auto(new_model, new_engine, new_year, new_price, new_color)
    while True:
        choose_option = input("Для просмотра класса введите 'view'\n"
                              "Для редактирования введите 'edit'\n"
                              "Для выхода введите 'exit'\n")
        if choose_option.upper() == "EXIT":
            print("До свидания!")
            break
        elif choose_option.upper() == "VIEW":
            object_name.print_class()
        elif choose_option.upper() == "EDIT":
            choose_option1 = input("Для смены модели введите 'model'\n"
                                   "Для смены объема двигателя введите 'engine'\n"
                                   "Для смены года выпуска введите 'year'\n"
                                   "Для смены цены введите 'price'\n"
                                   "Для смены цвета введите 'color'\n")
            if choose_option1.upper() == "MODEL":
                new_model = input("Введите модель автомобиля:\n")
                object_name.change_model(new_model)
            elif choose_option1.upper() == "ENGINE":
                new_engine = input("Введите объем двигателя:\n")
                object_name.change_engine(new_engine)
            elif choose_option1.upper() == "YEAR":
                new_year = input("Введите год выпуска:\n")
                object_name.change_year(new_year)
            elif choose_option1.upper() == "PRICE":
                new_price = input("Введите цену:\n")
                object_name.change_price(new_price)
            elif choose_option1.upper() == "COLOR":
                new_color = input("Введите цвет:\n")
                object_name.change_color(new_color)
            else:
                print("Ввеены некорректные данные, повторите попытку")
        else:
            print("Ввеены некорректные данные, повторите попытку")


print(work_with_class())