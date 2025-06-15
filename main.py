from vector2d import Vector2D

if __name__ == "__main__":
    print("--- Фінальна демонстрація класу Vector2D ---")

    print("\n1. Створення векторів та їх виведення (використовуємо __str__):")
    try:
        vec1 = Vector2D(3, 4)
        print(f"Вектор 1: {vec1}")
        vec2 = Vector2D(1.5, -2.5)
        print(f"Вектор 2: {vec2}")
        vec3 = Vector2D(0, 0)
        print(f"Вектор 3 (нульовий): {vec3}")
    except (TypeError, ValueError) as e:
        print(f"Сталася помилка при створенні вектора: {e}")

    print("\n2. Демонстрація валідації (спробуємл створити з помилковими даними):")
    try:
        invalid_vec1 = Vector2D("русоріз", 5)
        print(f"Цей рядок не повинен з'явитися: {invalid_vec1}")
    except TypeError as e:
        print(f"Очікувана помилка при створенні з невірним типом X: {e}")

    try:
        invalid_vec2 = Vector2D(10, [1, 2])
        print(f"Цей рядок також не повинен з'явитися: {invalid_vec2}")
    except TypeError as e:
        print(f"Очікувана помилка при створенні з невірним типом Y: {e}")

    print("\n3. Демонстрація перевантажених операторів:")
    v_a = Vector2D(5, 7)
    v_b = Vector2D(2, 3)
    print(f"Вектор А: {v_a}")
    print(f"Вектор Б: {v_b}")

    sum_vector = v_a + v_b
    print(f"Вектор А + Вектор Б = {sum_vector}")

    diff_vector = v_a - v_b
    print(f"Вектор А - Вектор Б = {diff_vector}")

    scaled_vector = v_a * 2.5
    print(f"Вектор А * 2.5 = {scaled_vector}")

    scaled_vector_reverse = 3 * v_b
    print(f"3 * Вектор Б = {scaled_vector_reverse}")

    print(f"Вектор А == Vector2D(5, 7): {v_a == Vector2D(5, 7)}")
    print(f"Вектор А == Вектор Б: {v_a == v_b}")
    print(f"Вектор А == 'не вектор': {v_a == 'не вектор'}")

    try:
        v_a + "якийсь текст"
    except TypeError as e:
        print(f"Очікувана помилка при додаванні вектора до тексту: {e}")

    print("\n4. Демонстрація власних методів:")
    test_vec = Vector2D(6, 8)
    print(f"Тестовий вектор: {test_vec}")

    vec_length = test_vec.length()
    vec_magnitude = test_vec.magnitude()
    print(f"Довжина тестового вектора (length()): {vec_length}")
    print(f"Модуль тестового вектора (magnitude()): {vec_magnitude}")

    normalized_vec = test_vec.normalize()
    print(f"Нормалізований тестовий вектор: {normalized_vec}")
    print(f"Довжина нормалізованого вектора: {normalized_vec.length()}")

    another_vec = Vector2D(1, 1)
    dot_prod_result = test_vec.dot_product(another_vec)
    print(f"Скалярний добуток {test_vec} та {another_vec}: {dot_prod_result}")

    zero_vec = Vector2D(0, 0)
    print(f"Довжина нульового вектора: {zero_vec.length()}")
    norm_zero_vec = zero_vec.normalize()
    print(f"Нормалізований нульовий вектор: {norm_zero_vec}")