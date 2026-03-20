money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0              # счётчик месяцев
current_money = money_capital  # текущий бюджет (подушка)
monthly_spend = spend          # расходы текущего месяца

while True:
    current_money += salary    # нач месяца
    if current_money >= monthly_spend:
        current_money -= monthly_spend  # расходы
        months += 1
        monthly_spend *= (1 + increase)  # увел расход
    else:
        break  # денег неет

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
