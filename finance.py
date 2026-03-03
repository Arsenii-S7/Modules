# 1. Расчет сложных процентов
import time


# A = P × (1 + r/n)^(n×t)
# где:
# A - будущая сумма (основная сумма + проценты)
# P - основная сумма (начальный капитал)
# r - годовая процентная ставка (в десятичной форме: 5% = 0.05)
# n - количество начислений процентов в год
# t - количество лет


def calculate_interest(principal, rate, years, compounds_per_year = 12):

    r = rate/100
    Total = principal * (1 + r/compounds_per_year)**(compounds_per_year * years)
    return f'будущая сумма (основная сумма + проценты) = {Total:.2f}'

#
# if __name__ == "__main__":
#     result = calculate_interest(10000, 5, 3)
#     print(f"10000 руб под 5% на 3 года: {result} руб")



# 2. Расчет ежемесячного платежа по кредиту (аннуитетный платеж)

# M = P × [r(1+r)^n] / [(1+r)^n - 1]
# где:
# M - ежемесячный платеж
# P - сумма кредита
# r - месячная процентная ставка (годовая ставка / 12 / 100)
# n - общее количество платежей (срок в годах × 12)


def calculate_monthly_payment(principal, annual_rate, years):
    # 1. Переводим годовую ставку в месячную десятичную дробь
    # (Например: 12% -> 0.12 / 12 = 0.01)
    r = annual_rate / 12 / 100

    # 2. Переводим срок в годах в количество месяцев
    n = years * 12
    if r == 0:
        return principal / n

    # 3. Сама формула аннуитета
    numerator = r * (1 + r) ** n
    denominator = (1 + r) ** n - 1

    monthly_payment = principal * (numerator / denominator)

    return f'{monthly_payment:.2f}'
#
# if __name__ == "__main__":
#
#     payment = calculate_monthly_payment(100000, 15, 2)
#     print(f"Ежемесячный платеж: {payment:.2f} руб.")
#     payment = calculate_monthly_payment(1500000, 12, 5)
#     print(f"Ежемесячный платеж: {payment:.2f} руб.")


# 3. Расчет покупательной способности с учетом инфляции
# FV = PV / (1 + i)^t
# где:
# FV - будущая покупательная способность
# PV - текущая сумма
# i - годовой уровень инфляции (в десятичной форме)
# t - количество лет

def calculate_purchasing_power(amount, inflation_rate, years):
    # Переводим инфляцию из процентов в десятичное число (например, 7% -> 0.07)
    i = inflation_rate / 100

    # Считаем реальную стоимость
    real_value = amount / (1 + i) ** years

    return f'Реальная стоимость после инфляции: {real_value:.2f}'

# if __name__ == "__main__":
#     print(calculate_purchasing_power(100000, 7, 5))



def test_module1():
    print('#'*50)
    print('Расчет сложных процентов')
    print()
    while True:
        try:
            principal = float(input('Основная сумма (начальный капитал): '))
            rate = int(input('Годовая процентная ставка (%): '))
            years = int(input('Kоличество лет: '))
            compounds_per_year = int(input('Количество начислений процентов в год (по умолчанию 12): '))
            break
        except ValueError:
            print('Неверный ввод данных')




    print('\n⏳ Выполняется расчет...')
    time.sleep(3)
    result = calculate_interest(principal, rate, years, compounds_per_year = 12)
    print(result)
    print('#' * 50)
    return result




def test_module2():
    print('#' * 50)
    print('Расчет ежемесячного платежа по кредиту (аннуитетный платеж)')
    print()
    while True:
        try:
            principal = float(input('основная сумма (начальный капитал): '))
            annual_rate = int(input('годовая процентная ставка (в %): '))
            years = float(input('Количество лет (срок): '))
            break
        except ValueError:
            print('Неверный ввод данных')

    print('\n⏳ Выполняется расчет...')
    time.sleep(3)
    result = calculate_monthly_payment(principal, annual_rate, years)
    print(result)
    print('#' * 50)
    return result



def test_module3():
    print('#' * 50)
    print('Расчет покупательной способности с учетом инфляции')
    print()
    while True:
        try:
            amount = float(input('Текущая сумма: '))
            inflation_rate= int(input('Уровень инфляции (в %): '))
            years = float(input('Количество лет (срок): '))
            break
        except ValueError:
            print('Неверный ввод данных')

    print('\n⏳ Выполняется расчет...')
    time.sleep(3)
    result = calculate_purchasing_power(amount, inflation_rate, years)
    print(result)
    print('#' * 50)
    return result



def All():
    print("\n" + "=" * 50)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("=" * 50)

    while True:
        print("\nВыберите расчет:")
        print("1 - Сложные проценты")
        print("2 - Ежемесячный платеж по кредиту")
        print("3 - Влияние инфляции")
        print("4 - Выход")

        choice = input("Ваш выбор (1-4): ")

        if choice == '4':
            break
        elif choice == '1':
            test_module1()
        elif choice == '2':
            test_module2()
        elif choice == '3':
            test_module3()
        else:
            print("\n❌ Неверный выбор! Пожалуйста, выберите 1-4.")
            input("Нажмите Enter, чтобы продолжить...")


