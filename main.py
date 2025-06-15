from vector2d import Vector2D

if __name__ == "__main__":
    print("--- Демонстрація Vector2D з арифметичними операціями ---")
    vec1 = Vector2D(3, 4)
    vec2 = Vector2D(1, 2)
    print(f"Вектор 1: {vec1}")
    print(f"Вектор 2: {vec2}")

    sum_v = vec1 + vec2
    print(f"Сума: {sum_v}")

    diff_v = vec1 - vec2
    print(f"Різниця: {diff_v}")

    scaled_v = vec1 * 2
    print(f"Масштабований (вектор * скаляр): {scaled_v}")

    rscaled_v = 3 * vec2
    print(f"Масштабований (скаляр * вектор): {rscaled_v}")

    try:
        vec1 + "abc"
    except TypeError as e:
        print(f"Очікувана помилка додавання: {e}")