revenue = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))

if revenue < costs:
    print("Издержки вашей фирмы больше прибыли!")
else:
    profit = revenue - costs
    print(f"Ваша фирма работает на прибыль! Ваша прибыль составляет {profit:.1f}")
    print(f"Рентабельность равна {(profit / revenue):.3f}")
    emp_num = int(input("Введите количество сотрудников фирмы"))
    print(f"Прибыль фирмы в расчёте на одного сотрудника составляет: {profit // emp_num}")

