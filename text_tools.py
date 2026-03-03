# text_tools.py

def reverse_text(text):
    """Возвращает текст наоборот"""
    return text[::-1]

def count_words(text):
    """Считает количество слов"""
    return len(text.split())

def capitalize_all(text):
    """Каждое слово с заглавной буквы"""
    return ' '.join(word.capitalize() for word in text.split())






def is_palindrome(text):
    """Проверяет, является ли строка палиндромом"""
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

def get_most_common_char(text):
    """Находит самый частый символ в строке"""
    if not text:
        return None
    from collections import Counter
    counter = Counter(text.replace(" ", ""))
    return counter.most_common(1)[0]


# Константа
AUTHOR = "Python Student"


# Примеры использования

if __name__ == '__main__':

    print(reverse_text('Hello'))
    print(capitalize_all('i am great'))
    print(is_palindrome('радар'))
    print(is_palindrome('привет'))
    print(get_most_common_char('hhh, gr4rrr, f4r'))
