from tkinter import *


def pr1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type} ')

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, open):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.location = location
            self.open = open

        def describe_rest(self):
            print(f'Расположение ретсорана: {self.location}, часы работы ресторана {self.open}')

        class Eskimo_pie:
            def __init__(self, name, flavors):
                self.name = name
                self.flavors = flavors

        class Sherbet:
            def __init__(self, name, flavors):
                self.name = name
                self.flavors = flavors

        class Frooty_ice:
            def __init__(self, name, flavors):
                self.name = name
                self.flavors = flavors

        def add_flavors(self):
            f.append(input('Какие вкусы вы хотите добавить? '))

        def del_flavors(self):
            f.remove(input('Какие вкусы вы хотите убрать? '))

        def vflavors(self):
            print('Список сортов мороженного: ', f)

        def check(self):
            if str(input('Наличие какого вкуса хотите узнать? ')) in f:
                print('Такой вкус есть')
            else:
                print('Такого вкуса нет')

    f = ['Шоколадный', 'Ванильный', 'Фисташковый']

    r = IceCreamStand('FROOTISH', 'Корейская', f, 'ул. Виноградная 54А ', '10:00 - 22:00')

    r.describe_restaurant()
    r.describe_rest()
    r.add_flavors()
    r.del_flavors()
    r.check()


def pr2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, flavors, location, open):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.flavors = flavors
            self.location = location
            self.open = open

        def describe_rest(self):
            print(
                f'Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type}\nРасположение ретсорана: {self.location}, часы работы ресторана {self.open} ')

        def flavors(self):
            print('Вкусы мороженного:', f)

    f = ['Шоколадный', 'Ванильный', 'Фисташковый', 'Клубчный']

    r = Restaurant('FROOTY&CREAM', 'Норвежская', f, 'ул. Виноградная 54А ', '9:00 - 20:00')
    r.describe_rest()

    i = Tk()
    i['bg'] = 'dark cyan'
    i.title('Вкусы мороженного')
    i.geometry('300x250')
    frame = Frame(i, bg='white smoke', bd=5)
    frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
    title = Label(i, text='Виды мороженного:', bg='white smoke', font=30)
    title.place(relx=0.15, rely=-0.25, relwidth=0.7, relheight=0.7)
    title.pack

    ch = 0.1
    for k in f:
        e = k
        ch += 0.12
        m = Label(i, text=e, bg='white smoke', font=25)
        m.place(relx=0.15, rely=ch, relwidth=0.7, relheight=0.1)
        m.pack
    i.mainloop()


pr1()
pr2()
