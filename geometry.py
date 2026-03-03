# geometry.py
# Функции для геометрических вычислений

def circle_area(radius):
    """Площадь круга: π × r²"""
    S = PI * (radius ** 2)
    return (f'Площадь круга = {S}')

def rectangle_area(width, height):
    """Площадь прямоугольника"""
    S = width * height
    return (f'Площадь прямоугольника = {S}')

def triangle_area(base, height):
    """Площадь треугольника"""
    S = (base * height)/2
    return (f'Площадь треугольника = {S}')


# Константы
PI = 3.141592653589793