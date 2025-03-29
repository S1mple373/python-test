# Функция для проверки делимости на 2
def is_divisible_by_2(number):
    return number % 2 == 0

# Запрос числа у пользователя
num = int(input("Введите число: "))

# Проверка делимости и вывод результата
if is_divisible_by_2(num):
    print(f"{num} делится на 2.")
else:
    print(f"{num} не делится на 2.")