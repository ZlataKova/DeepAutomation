def convert_the_time(N):
    hours = N // 3600  # Вычисляем количество часов
    minutes = (N % 3600) // 60  # Вычисляем количество минут

    # Определяем суффиксы для часов и минут
    hours_suffix = "час" if hours == 1 else "часов"
    minutes_suffix = "минута" if minutes == 1 else "минут"

    # Формируем строку ответа
    result = f"{hours} {hours_suffix} и {minutes} {minutes_suffix}"

    return result