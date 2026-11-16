
import math


def _validate_radius(r):
    '''
    Проверяет корректность радиуса.

    Параметры:
        r (int | float): радиус круга.

    Исключения:
        TypeError: если передан неподдерживаемый тип.
        ValueError: если радиус отрицательный.
    '''
    if isinstance(r, bool) or not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом (int или float)")

    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")


def area(r):
    '''
    Вычисляет площадь круга.

    Параметры:
        r (int | float): неотрицательный радиус круга.

    Возвращает:
        float: площадь круга.
    '''
    _validate_radius(r)
    return math.pi * r ** 2


def perimeter(r):
    '''
    Вычисляет длину окружности.

    Параметры:
        r (int | float): неотрицательный радиус круга.

    Возвращает:
        float: длина окружности.
    '''
    _validate_radius(r)
    return 2 * math.pi * r
