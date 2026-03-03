# stats.py
# Функции для статистических вычислений

def average(numbers):
    """Среднее значение списка чисел"""
    if not numbers:  # Если список пустой
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Медиана списка чисел"""
    if not numbers:
        return 0

    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    index = n // 2

    if n % 2 != 0:
        return sorted_nums[index]
    else:
        return (sorted_nums[index - 1] + sorted_nums[index])/2





def mode(numbers):
    """Мода (самое частое значение)"""
    # TODO: верни самое часто встречающееся число
    if not numbers:
        return None
    mode = max(set(numbers), key=lambda x: numbers.count(x))
    return (f"Мода (самое частое значение) - {mode}")

# Константа
STATS_VERSION = "1.0"






def mode(numbers):
    """Мода (самое частое значение)"""
    if not numbers:
        return None

    # Создаем словарь для подсчета частот
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    # Находим максимальную частоту
    max_freq = max(frequency.values())

    # Находим все числа с максимальной частотой (может быть несколько мод)
    modes = [num for num, freq in frequency.items() if freq == max_freq]

    # Возвращаем одну моду или список, если их несколько
    return modes[0] if len(modes) == 1 else modes


# Примеры использования
if __name__ == "__main__":
    # Тест median
    test1 = [1, 2, 3, 4, 5]
    test2 = [1, 2, 3, 4, 5, 6]
    test3 = [5, 2, 8, 1, 9]

    print(f"Медиана {test1}: {median(test1)}")  # 3
    print(f"Медиана {test2}: {median(test2)}")  # 3.5
    print(f"Медиана {test3}: {median(test3)}")  # 5

    # Тест mode
    test4 = [1, 2, 2, 3, 3, 3, 4]
    test5 = [1, 1, 2, 2, 3, 3]  # Несколько мод

    print(f"Мода {test4}: {mode(test4)}")  # 3
    print(f"Мода {test5}: {mode(test5)}")  # [1, 2, 3]