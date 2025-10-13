def sum_of_even_numbers():
    sum_even = 0

    for x in range(1, 101):
        if x % 2 == 0:
            sum_even += x
    print(f"Сумма всех чётных чисел: {sum_even}")


def squares_of_odd_numbers():
    squares = []

    for z in range(1, 11):
        if z % 2 != 0:
            squares.append(z ** 2)
    print(f"Список нечётных чисел от 1 до 10: {squares}")


def entering_numbers():
    count = 1

    while True:
        number = int(input("Введите число (отрицательное число — чтобы выйти): "))

        if number >= 0:
            print(f"Вы ввели число: {number}")
            count += 1
        else:
            print(f"Вы ввели отрицательное число. Программа завершена. Количество введённых чисел: {count}")
            break


sum_of_even_numbers()
squares_of_odd_numbers()
entering_numbers()
