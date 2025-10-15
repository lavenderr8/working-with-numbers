def sum_of_even_numbers():
    sum_even = 0
    for x in range(1, 101):
        if x % 2 == 0:
            sum_even += x
    print(f"Сумма всех чётных чисел: {sum_even}")


def squares_of_odd_numbers():
    numbers = [1, 3, 5, 7, 9]
    squares = [n ** 2 for n in numbers]
    print(f"Список квадратов нечётных чисел от 1 до 10: {squares}")


def entering_numbers():
    count = 1
    try:
        number = int(input("Введите число (отрицательное число — чтобы выйти): "))
        while number >= 0:
            print(f"Вы ввели число: {number}")
            count += 1
            number = int(input("Введите следующее число (отрицательное число — чтобы выйти): "))
        else:
            print(f"Вы ввели отрицательное число. Программа завершена. Количество введённых чисел: {count}")
    except ValueError:
        print("Вы ввели не число, попробуйте заново.")


sum_of_even_numbers()
squares_of_odd_numbers()
entering_numbers()
