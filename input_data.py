def input_data(xyplayer, tab):
    valid = False
    while not valid:
        player_move = input(f"{xyplayer} - choose your position: ")
        try:
            player_move = int(player_move)
        except:
            print("Incorrect input")
            continue
        if player_move >= 1 and player_move <= 9:
            if (str(tab[player_move-1]) not in "XO"):
                tab[player_move-1] = xyplayer
                valid = True
            else:
                print("This position is occupied")
        else:
            print("Incorrect input. Enter a number from 1 to 9")
