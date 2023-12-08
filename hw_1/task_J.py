def calculate_values(a, b, c, d, e, f):
    if a * d - b * c == 0:
        if (a == 0 and b == 0 and e == 0) and (c == 0 and d == 0 and f == 0):
            return [5]

        elif a == 0 and c == 0:
            if (b * f) == (e * d):
                if d == 0 and b == 0:
                    return [0]
                elif d == 0:
                    y = e / b
                    return [4, f"{y:.5f}"]
                elif b == 0:
                    y = f / d
                    return [4, f"{y:.5f}"]
                else:
                    y = e / b
                    return [4, f"{y:.5f}"]
            else:
                return [0]

        elif b == 0 and d == 0:
            if e * c == a * f:
                if a == 0 and c == 0:
                    return [0]
                elif a == 0:
                    x = f / c
                    return [3, f"{x:.5f}"]
                elif c == 0:
                    x = e / a
                    return [3, f"{x:.5f}"]
                else:
                    x = f / c
                    return [3, f"{x:.5f}"]
            else:
                return [0]

        elif a != 0:
            coefficient = c / a
            c = 0
            d -= coefficient * b
            f -= coefficient * e
            if c == 0 and d == 0 and f == 0:
                return [1, f"{-a / b:.5f}", f"{e / b:.5f}"]

        elif a == 0:
            coefficient = a / c
            a = 0
            b -= coefficient * d
            e -= coefficient * f
            if a == 0 and b == 0 and e == 0:
                return [1, f"{-c / d:.5f}", f"{f / d:.5f}"]

        return [0]

    else:
        if d != 0:
            x = (e * d - b * f) / (a * d - b * c)
            y = (f - c * x) / d
            return [2, f"{x:.5f}", f"{y:.5f}"]

        else:
            x = (f - d * e / b) / (c - d * a / b)
            y = (e - a * x) / b
            return [2, f"{x:.5f}", f"{y:.5f}"]


assert calculate_values(1, 0, 0, 1, 3, 3) == [2, "3.00000", "3.00000"]
assert calculate_values(2, 2, 3, -3, 6, -3) == [2, "1.00000", "2.00000"]
assert calculate_values(1, 1, 1, -1, 3, -1) == [2, "1.00000", "2.00000"]
assert calculate_values(1, 1, 2, 2, 1, 2) == [1, "-1.00000", "1.00000"]
assert calculate_values(1, 1, 1, 1, 1, 2) == [0]
assert calculate_values(0, 1, 0, 1, 2, 3) == [0]
assert calculate_values(0, 1, 0, 2, 2, 4) == [4, "2.00000"]
assert calculate_values(1, 0, 2, 0, 2, 4) == [3, "2.00000"]
assert calculate_values(0, 0, 0, 0, 0, 0) == [5]
assert calculate_values(0, 0, 0, 0, 1, 0) == [0]
assert calculate_values(0, 2, 0, 4, 1, 2) == [4, "0.50000"]
assert calculate_values(0, 2, 0, 4, 1, 2) == [4, "0.50000"]
assert calculate_values(0, 0, 2, 4, 0, 2) == [1, "-0.50000", "0.50000"]
assert calculate_values(2, 4, 0, 0, 2, 0) == [1, "-0.50000", "0.50000"]
assert calculate_values(2, 0, 3, 0, 2, 3) == [3, "1.00000"]
assert calculate_values(2, 2, 3, 0, 6, 3) == [2, "1.00000", "2.00000"]
assert calculate_values(1, 1, 1.5, 0, 3, 1.5) == [2, "1.00000", "2.00000"]


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())
    result = calculate_values(a, b, c, d, e, f)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
