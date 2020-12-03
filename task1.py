a = 512
b = "Привет"
c = 162.3
print(f"Тип переменной 'a': {type(a)}")
print(f"Тип переменной 'b': {type(b)}")
print(f"Тип переменной 'c': {type(c)}")


name = str(input("Введите ваше имя: "))
print(f"Здравствуйте, {name}")

age = int(input("Введите ваш возраст: "))
if age % 10 < 4 and age % 10 >1:
    print(f"Вам {age} года")
elif age % 10 > 3:
    print(f"Вам {age} лет")
else:
    print(f"Вам {age} год")

