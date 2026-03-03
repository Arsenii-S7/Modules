# calculator.py

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление с проверкой"""
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

# Константы
PI = 3.14159
VERSION = "1.0.0"

# Вспомогательная функция (не экспортируется по умолчанию)
def _private_helper():
    return "Внутренняя функция"


if __name__ == "__main__":
    print("Этот код выполнится только при ПРЯМОМ запуске calculator.py")
    print("При импорте в другой файл — НЕ выполнится")
