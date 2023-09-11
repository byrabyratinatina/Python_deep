# Треугольник существует только тогда,
# когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
import logg_triangle


def triangle(a: int, b: int, c: int):
    if 1_000_000_000 < a or a <= 0 or \
            1_000_000_000 < b or b <= 0 or \
            1_000_000_000 < c or c <= 0:
        text = 'Вы ввели недопустимые значения попробуйте снова!'
        logg_triangle.log_warning_triangle(text)
        return text

    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        text = 'стороны треугольника должны быть типа int..'
        logg_triangle.log_warning_triangle(text)
        return text

    if a < b + c and b < a + c and c < a + b:
        if a == b and a == c:
            text = 'Треугольник  является равносторонним!'
            logg_triangle.log_info_triangle(text)
            return text
        elif a == b or a == c or a == c:
            text = 'Треугольник является равнобедренним!'
            logg_triangle.log_info_triangle(text)
            return text
        else:
            text = 'Треугольник является разносторонним!'
            logg_triangle.log_info_triangle(text)
            return text
    else:
        text = 'Такого треугольника не существует!'
        logg_triangle.log_warning_triangle(text)
        return text
    