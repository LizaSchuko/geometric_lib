import math

def _validate_side(a):
    '''
    Проверяет корректность стороны квадрата.
    '''
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом (int или float)")

    if isinstance(a, float) and not math.isfinite(a):
        raise ValueError("Сторона должна быть конечным числом")

    if a < 0:
        raise ValueError("Сторона не может быть отрицательной")


def area(a):
    '''
    Вычисляет площадь квадрата.

    Параметры:
        a (int | float): неотрицательная длина стороны.

    Возвращает:
        int | float: площадь квадрата.
    '''
    _validate_side(a)
    return a ** 2


def perimeter(a):
    '''
    Вычисляет периметр квадрата.

    Параметры:
        a (int | float): неотрицательная длина стороны.

    Возвращает:
        int | float: периметр квадрата.
    '''
    _validate_side(a)
    return 4 * a
