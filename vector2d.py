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





