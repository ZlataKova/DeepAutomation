first_player, second_player = input().split()

def play_game(first_player, second_player):
    if first_player == second_player:
        return "ничья"
    if (first_player == "камень" and second_player == "ножницы") or (first_player == "ножницы" and second_player== "бумага") or (first_player == "бумага" and second_player == "камень"):
        return "Первый игрок выиграл"
    else:
        return "Второй игрок выиграл"

result = play_game(first_player,second_player)
print(result)