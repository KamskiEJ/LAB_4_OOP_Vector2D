class Vector2D:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)):
            raise TypeError("Координата X має бути числом (ціле абож дробове).")

        if not isinstance(y,(int, float)):
            raise TypeError("Координата Y має бути числом (ціле абож дробове).")

        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return f"Вектор2Д: ({self._x}, {self._y})"

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Можна додавати тільки об'єкти Vector2D.")

        new_x = self._x + other._x
        new_y = self._y + other._y
        return Vector2D(new_x, new_y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Можна віднімати тільки об'єкти Vector2D.")

        new_x = self._x - other._x
        new_y = self._y - other._y
        return Vector2D(new_x, new_y)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Можна множити вектор тільки на число (скаляр).")

        new_x = self._x * scalar
        new_y = self._y * scalar
        return Vector2D(new_x, new_y)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)






