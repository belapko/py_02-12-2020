user_sec = int(input("Введите время в секундах, чтобы вывести его в формате чч:мм:сс "))

hour = user_sec // 3600
if hour <10:
    hour = str(0) + str(hour)
min = user_sec // 60 % 60
if min <10:
    min = str(0) + str(min)
sec = user_sec % 60
if sec <10:
    sec = str(0) + str(sec)

print(f"{user_sec} секунд в ином формате {hour}:{min}:{sec}")
