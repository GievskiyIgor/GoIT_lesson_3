# Урок третий

# 1 задание
# ***
# 2 задание
# def invite_to_event(username):
    
#     if not username == ' ':
#         print(f"Dear {username}, we have the honour to invite you to our event")

# def pool_username ():
    
#     return ('Игорь', 'Максим', 'Руслан', 'Богдан', ' ')

# # username = input('Введите имя: ')

# for pool in pool_username():
#     # if not username == '' or not username == None:
#     invite_to_event(pool)
# ***

# 3 задание
# Необходимо написать функцию, которая будет рассчитывать сумму за пользование услугами такси. 
# Сумма состоит из базового тарифа 40 грн и 10 грн за каждый километр поездки. Напишите функцию, принимающую один параметр – расстояние поездки в километрах. 
# Функция должна возвращать сумму оплаты за услуги такси действительным числом. 
# Также функция должна изменять глобальную переменную счетчик total_tripпосле каждого вызова и увеличивать ее на единицу.

# base_rate = 40
# price_per_km = 10
# total_trip = 0


# def trip_price(path):
    
#     global total_trip
    
#     summm_oplat = int(base_rate + price_per_km*path)
    
#     total_trip  += 1
#     return summm_oplat
    
# path = float(input('Ввведите расстояние поездки в километрах: '))

# print(trip_price(path))
# ***
# 4 задание
# Необходимо реализовать функцию расчета цены товара со скидкой discount_price. 
# Функция принимает цену priceи скидку discount– это мелкое число от 0 до 1. 
# Здесь и дальше мы под скидкой будем понимать коэффициент, определяющий размер от цены. И на этот размер мы снижаем итоговую цена продукта. 
# Логику функции нужно прописать во внутренней функции apply_discount, используя объявление конфигурацией price как nonlocal .


# def discount_price(price, discount):
    
#     def apply_discount():
#         nonlocal price
#         price = price - price*discount
#     apply_discount()
    
#     return price

# от Владимира
# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         f = (price * discount)
#         price = price - f
#     apply_discount()
#     return price
# ***

# 5 задание
# Напишем функцию, возвращающую полное имя пользователя. 
# В базе данных преимущественно хранят имя пользователя first_name, его фамилию last_name и отчество, или, как принято в западных странах, 
# в# торое имя — middle_name. Причем middle_nameэто необязательная переменная, она может быть, а может и не передаваться при вызове функции. 
# Наша функция будет возвращать строку с полным именем 'first_name middle_name last_name', если же переменная middle_nameотсутствует, то возвращаемая 
# строка должна быть 'first_name last_name'.

# def get_fullname(first_name, last_name, middle_name = None):
    
#     if middle_name != None:
#         return first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         return first_name + ' ' + last_name
        

# first_name = input('Input first_name: ')
# last_name = input('Input last_name: ')
# middle_name = input('Input middle_name: ')

# print(get_fullname(first_name, last_name, middle_name))
# ***

# 6 задание
# Создайте функцию format_stringформатирования строки. В функцию мы передаем строку stringи lengthдлину новой строки. Функция возвращает новую строку по следующему алгоритму:

# Если длина исходной строки больше или равна length, мы возвращаем ее в том же виде
# Если она меньше length, мы добавляем впереди строки пробелы в количестве(length - len(string)) // 2.
# Тесты на правильность работы функции выполняются для следующих наборов аргументов:

# string = 'aaaaaaaaaaaaaaaaac', length = 12
# length = 15
# string = 'abaa'


# def format_string(string, length):
          
#     if len(string) == length:
#         return string
#     else:
#         probel = (length - len(string)) // 2
#         return ' '*probel + string


# print(format_string(string, length))
# ***
# 7 задание
# Наступне завдання буде суто теоретичним, і ми потренуємося працювати з довільною кількістю аргументів.

# Створіть дві функції:

# перша first буде мати першим параметром змінну size, а також вона може приймати будь-яку кількість позиційних аргументів. Функція повинна повернути суму size c загальною кількістю переданих до неї позиційних аргументів.
# друга функція second так само матиме першим параметром size і прийматиме довільну кількість ключових аргументів, і також має повернути суму size з кількістю переданих у функцію ключових аргументів.
# Тестові виклики функцій для правильності роботи будуть наступними:

# first(5, "first", "second", "third")
# first(1, "Alex", "Boris")
# second(3, comment_one="first", comment_two="second", comment_third="third")
# second(10, comment_one="Alex", comment_two="Boris")

# def first(size, *second_parametr):
    
#     size += len(second_parametr)
#     return size


# def second(size, **second_parametr):
#     size += len(second_parametr)
#     return size


# size = first(5, "first", "second", "third")
# print(size)

# size = second(3, comment_one="first", comment_two="second", comment_third="third")
# print(size)
# ***
# 8 задание

# def cost_delivery(quantity, *price, discount=0):
#     two_price = 0 
#     price_one = 5
#     price_two = 2 
#     for pr in price:
#         two_price += pr*price_two
#     if discount != 0:
#         summ = (price_one*quantity + two_price)*discount
#     else:
#         summ = price_one*quantity + two_price
#     return summ


# summ = cost_delivery(2, 1, 2, 3, discount=0.5)
# print(summ)

#  вариант для программы, несогласен, так как условие задачи совсем друое. Код сверху. 
# def cost_delivery(quantity, *two_quantity, discount = 0):
    
#     summ = (5 + 2 * (quantity - 1)) * (1 - discount)
#     return summ 

# summ = cost_delivery(3, 3)
# print (summ)
# ***
# 9 задание
# ***
# 10 задание
# Ми проводимо розіграш призів серед перших 50 підписників ютуб-каналу. Ми маємо 7 призів для розіграшу. Може виникнути питання, 
# скільки різних списків переможців ми можемо отримати під час розіграшу? Для цього ми будемо використовувати формулу сполучень без повторень

# Cnk = n! / ((n - k)! · k!)

# де n — це загальна кількість людей (випадків), а k — кількість людей, які отримали призи.

# Напишіть функцію number_of_groups, яка приймає параметри n та k, і за допомогою функції factorial повертає нам скільки різних списків переможців ми можемо отримати при розіграші

# Зверніть увагу на те, які великі значення ми отримуємо для факторіала. Рекурсивні висловлювання треба завжди застосовувати з обережністю при обчисленнях, 
# щоб не отримати переповнення пам'яті.

# def factorial(n):
#      if n< 2:
#         return 1
#      else:
#         return n * factorial(n-1)

# def number_of_groups(n, k):

#     """Факториал
#     1 parametr - n! = 1 *  ... *50
#     2 parametr - (n-k)! = 1 *  ... *(50 -7)
#     3 parametr - k! = 1 *  ... * 7
    
#     Args:
#         n int: количество участников
#         k int: количество призов
    
#     Формула:
#         Cnk = n! / ((n - k)! · k!)
#         Cnk = 50!/ (50-7)! * 7!
    
#     Error - Функція number_of_groups повернула неправильний результат: 2537223575040000. Очікувалося, що number_of_groups(50, 7) == 99884400    
    
#     """
#     parametr_1 = factorial(n)
#     parametr_2 = factorial(n-k)
#     parametr_3 = factorial(k)

#     # return parametr_1  # 30414093201713378043612608166064768844377641568960512000000000000
#     # return parametr_2  # 60415263063373835637355132068513997507264512000000000
#     # return parametr_3    #  5040
#     # return parametr_2 * parametr_3  # 304492925839404131612269865625310547436613140480000000000
#     return int(parametr_1/(parametr_2 * parametr_3))
# n = int(input('Введите количество участников розыграша: '))
# k = int(input('Введите количество призов: '))

# result = number_of_groups(n, k)

# print (result)
# ***
# 11 задание
# Однією з класичних задач на розуміння рекурсії, яку часто задають на співбесідах, особливо початківцям-програмістам — це ряд Фібоначчі.

# Ряд Фібоначчі — це послідовність чисел виду: '0, 1, 1, 2, 3, 5, 8, ...' де кожне наступне число послідовності виходить додаванням двох попередніх членів ряду.

# У загальному вигляді для обчислення n-го члена ряду Фібоначчі слід обчислити вираз:

# Fn = Fn-1 + Fn-2.

# Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа послідовності доти, доки виклик не сягне членів ряду менше n = 1, на якій задана послідовність.

# summ = 0

# def fibonacci(n):

#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)


# n = int(input('Введите число Фибоначи: '))

# for n in range(n):
#     summ += fibonacci(n)

# print(summ)
# ***
