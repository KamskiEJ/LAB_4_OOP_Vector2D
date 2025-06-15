from vector2d import Vector2D

if __name__ == "__main__":
    print("--- Демонстрація початкової версії Vector2D ---")
    try:
        v1 = Vector2D(1, 2)
        print(f"Створено вектор: {v1}")
        v2 = Vector2D(0.5, -1.5)
        print(f"Створено інший вектор: {v2}")
    except TypeError as e:
        print(f"Помилка при створенні вектора: {e}")

    try:
        invalid_v = Vector2D("a", 2)
    except TypeError as e:
        print(f"Очікувана помилка при валідації: {e}")