from import_this import RACE_DATA # Импортируем данные о гонке из файла import_this.py

if __name__ == '__main__':
    top_racers = sorted(RACE_DATA.values(), key=lambda x: x['FinishedTimeSeconds'])[:3]  # Сортируем гонщиков по времени финиша и выбираем первых трех 

    for i, racer in enumerate(top_racers, 1): ## Перебираем трех лучших гонщиков и выводим информацию о них
        time_seconds = racer['FinishedTimeSeconds']
        time_hours = time_seconds // 3600
        time_minutes = (time_seconds % 3600) // 60
        time_seconds = time_seconds % 60
        time_formatted = f"{time_hours:02d}:{time_minutes:02d}:{time_seconds:02d}"

        if i == 1:
            print(f"Выиграл - {racer['RacerName']}! Поздравляем!") # Выводим информацию о победителе с поздравлениями

            print("_" * len(f"Выиграл - {racer['RacerName']}! Поздравляем!")) # Подчеркиваем длинной линией имя победителя

       # Выводим информацию о гонщиках и их местах     
        print(f"Гонщик на {i} месте:")
        print(f"\tИмя: {racer['RacerName']}")
        print(f"\tКоманда: {racer['RacerTeam']}")
        print(f"\tВремя: {time_formatted}\n")