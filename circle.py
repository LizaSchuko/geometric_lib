
import math


def _validate_radius(r):
    '''
    Проверяет корректность радиуса.
    '''
    if isinstance(r, bool) or not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом (int или float)")

    if isinstance(r, float) and not math.isfinite(r):
        raise ValueError("Радиус должен быть конечным числом")

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
