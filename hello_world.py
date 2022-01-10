from types import MethodWrapperType

# message = "hello, PYTHON world!"
# print(message.upper())

# message = "hello, python CRASH course world!"
# print(message.lower())

# first_name = "    dmitrii"
# last_name = "smirnov    "
# full_name = f"{first_name} {last_name}"
# full_name = full_name.strip()
# hello = f"Hello, {full_name.title()}!\n\tYou are in the Python world."

# print(hello)

# message = "One of Python's strengths is its diverse community."
# print(message)

# number_1, number_2, number_3 = 15, 25, 40
# print(number_1 + number_2 + number_3)

# figure_skaters = ['камила валиева', 'Александра Трусова', 'Анна Щербакова', 'Елизавета Туктамышева']
# print(f"Первое место заняла {figure_skaters[-4].title()}")
# print(f"Второе место заняла {figure_skaters[-3]}")
#print(f"Третье место заняла {figure_skaters[-2]}")
# print(f"Четвертое место заняла {figure_skaters[-1]}")

# fruits = ['яблоко', 'апельсин', 'мандарин', 'грейпфрут']
# print(fruits)

# fruits[0] = 'груша'
# print(fruits)

# print(fruits[-1])
# fruits[-1] = 'хурма'
# print(fruits[-1])

# print(fruits)
# print(fruits[-1])
# fruits.append('гранат')
# print(fruits)
# print(fruits[-1])

# fruits.insert(1, 'лайм')
# print(fruits)

# del fruits[0]
# print(fruits)

# popped_fruits = fruits.pop()
# print(fruits)
# print(popped_fruits)

purchases = ['Квартира', 'Машина', 'Денежные средства на счетах']
print(purchases)

purchases_flat = f"В первую очередь мне нужна собственная {purchases[0].lower()} в Москве"
print(purchases_flat)

purchases_car = f"Во вторую очередь мне нужна собственная {purchases[1].lower()} комфорт-класса"
print(purchases_car)

purchases_money = f"В третью очередь мне нужны {purchases[2].lower()} в достаточном количестве для комфортной жизни"
print(purchases_money)

# purchases_popped = purchases.pop(0)
# print(purchases)
# print(purchases_popped)

# purchases.pop(0)
print(purchases)

purchases.remove('Денежные средства на счетах')
print(purchases)




