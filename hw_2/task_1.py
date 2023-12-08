s = input()
list_numbers = list(map(int, s.split()))


def f():
    if len(list_numbers) <= 1:
        return "YES"
    for i in range(len(list_numbers) - 1):
        if list_numbers[i] >= list_numbers[i + 1]:
            return "NO"
    return "YES"

print(f())
