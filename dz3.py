n = input("Введите целое число N: ")

try:
    n = int(n)
    
    squared_list = []

    for x in range(-n, n + 1):
        squared_list.append(x ** 2)

    print(squared_list)

except ValueError:
    print("Ошибка: Введите целое число.")