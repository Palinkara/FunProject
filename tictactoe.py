gameField = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def field():
    print(gameField[0] + " " + gameField[1] + " " + gameField[2])
    print(gameField[3] + " " + gameField[4] + " " + gameField[5])
    print(gameField[6] + " " + gameField[7] + " " + gameField[8])


def play():
    gameOn = True
    player = "X"
    field()
    while gameOn:
        print("Player " + player + "'s turn!")
        position = (input("Move:"))
        if position.isdigit() and int(position) in range(10) and int(position) > 0:
            position = int(position)
            success = playerMove(player, position)
            player = playerChange(player, success)
        else:
            print("error")
        field()
        if win():
            break


def playerMove(player, pos):
    pos = pos - 1
    if gameField[pos] == "-":
        if player == "X":
            gameField[pos] = "X"
        else:
            gameField[pos] = "0"
        return True
    else:
        print("Choose another value!")
        return False


def playerChange(player, success):
    if player == "X" and success:
        return "0"
    elif success:
        return "X"


def win():
    if gameField[0] == "X" and gameField[1] == "X" and gameField[2] == "X":
        print("X wins!")
        return True
    elif gameField[0] == "0" and gameField[1] == "0" and gameField[2] == "0":
        print("0 wins!")
    if gameField[3] == "X" and gameField[4] == "X" and gameField[5] == "X":
        print("X wins!")
        return True
    if gameField[3] == "0" and gameField[4] == "0" and gameField[5] == "0":
        print("0 wins!")
        return True
    if gameField[6] == "X" and gameField[7] == "X" and gameField[8] == "X":
        print("X wins!")
        return True
    if gameField[6] == "0" and gameField[7] == "0" and gameField[8] == "0":
        print("0 wins!")
        return True
    if gameField[0] == "X" and gameField[4] == "X" and gameField[8] == "X":
        print("X wins!")
        return True
    if gameField[0] == "0" and gameField[4] == "0" and gameField[8] == "0":
        print("0 wins!")
        return True
    if gameField[2] == "X" and gameField[4] == "X" and gameField[6] == "X":
        print("X wins!")
        return True
    if gameField[2] == "0" and gameField[4] == "0" and gameField[6] == "0":
        print("0 wins!")
        return True


def test():
    if input().isdigit():
        print("number")


play()
