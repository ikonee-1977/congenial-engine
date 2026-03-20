salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0      # нач подушк
monthly_spend = spend  # Расход мес

for month in range(months):
    if month > 0:
        monthly_spend *= (1 + increase)   #  со второго месяца
    deficit = monthly_spend - salary       # дефицит
    if deficit > 0:
        money_capital += deficit           # суммa
money_capital = round(money_capital)

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")