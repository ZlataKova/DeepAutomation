input_string = input("Введите массив чисел через запятую, например, 1,2,3: ")
numbers = input_string.split(',')
numbers = [int(num) for num in numbers]
dataArray = numbers
indexes = []

for i in range(1, len(dataArray)):
    current_number = dataArray[i]
    previous_number = dataArray[i - 1]
    if  previous_number + 1 < current_number:
        indexes.append(i)

if len(indexes) == 0:
    print("Не найдено")
elif len(indexes) == 1:
    print(f"Простое число: {indexes[0]}")
else:
    print(f"Список индексов: {indexes}")