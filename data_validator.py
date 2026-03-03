def validate_email(email):
    """
        Проверяет, является ли строка валидным email

        Примеры:
        "user@example.com" -> True
        "user.name@domain.co.uk" -> True
        "invalid-email" -> False
        "user@domain" -> False
        """
    # 1. Проверяем, что это вообще строка и в ней есть ровно одна собачка
    if not isinstance(email, str) or email.count('@') != 1:
        return False

        # 2. Разделяем на имя пользователя и домен
    user_part, domain_part = email.split('@')

    if '..' in user_part:
        return False

        # 3. Проверяем, что обе части не пустые
    if not user_part or not domain_part:
        return False

        # 4. В домене должна быть хотя бы одна точка
    if '.' not in domain_part:
        return False

        # 5. Проверяем, что точка в домене не в самом начале и не в самом конце
        # (например, чтобы не прошло "user@.com" или "user@domain.")
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False

    domain_segments = domain_part.split('.')
    top_level_domain = domain_segments[-1]  # Это будет 'ru', 'com' и т.д.

    if len(top_level_domain) < 2:
        return False

    return True

#     # Проверки:
# print(validate_email("user@example.com"))  # True
# print(validate_email("user.name@domain.co.uk"))  # True
# print(validate_email("invalid-email"))  # False
# print(validate_email("user@domain"))  # False
# print(validate_email("@domain.com"))  # False


def validate_phone(phone):
    """
    Проверяет, является ли строка валидным номером телефона

    Допустимые форматы:
    "+7 (999) 123-45-67"
    "89991234567"
    "+79991234567"
    "8 (999) 123-45-67"
    """
    if not isinstance(phone, str):
        return False

    cleaned_phone = phone.replace(' ','').replace('-','').replace(')','').replace('(','')
    check_digits = cleaned_phone
    if cleaned_phone.startswith('+'):
        check_digits = cleaned_phone[1:]


    if not check_digits.isdigit():
        return False

    length = len(cleaned_phone)

    if cleaned_phone.startswith('+7') and length == 12:
        return True
    if cleaned_phone.startswith('8') and length == 11:
        return True
    return False

# print(validate_phone("+7 (999) 123-45-67")) # True
# print(validate_phone("89991234567"))         # True
# print(validate_phone("+79991234567"))        # True
# print(validate_phone("8 (999) 123-45-67"))   # True
# print(validate_phone("12345"))



def validate_number(value, min_value=None, max_value=None):
    """
    Проверяет, находится ли число в заданном диапазоне

    Примеры:
    validate_number(5, min_value=0, max_value=10) -> True
    validate_number(15, min_value=0, max_value=10) -> False
    validate_number(5, min_value=0) -> True (только нижняя граница)
    validate_number(5, max_value=10) -> True (только верхняя граница)
    """
    # Проверяем, что value - число
    if not isinstance(value, (int, float)):
        return False

        # Проверяем, что границы (если заданы) - тоже числа
    if min_value is not None and not isinstance(min_value, (int, float)):
        return False
    if max_value is not None and not isinstance(max_value, (int, float)):
        return False



    if min_value is not None and value < min_value:
        return False

    # 2. Проверяем верхнюю границу (если она задана)
    if max_value is not None and value > max_value:
        return False

    # 3. Если проверки выше не сработали, число в диапазоне
    return True

# print(validate_number(5, min_value=0, max_value=10))
# print(validate_number(15, min_value=0, max_value=10))
# print(validate_number(5, min_value=0))
# print(validate_number(5, max_value=10))
