import random
import numpy


def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")


def show():
    print()
    print("    ", end="|")
    for i in range(len(field)):
        print(f" {i + 1} ", end="|")

    print("")
    print("-----" * n)

    for i, row in enumerate(field):
        print(f"  {i + 1} | {' | '.join(row)} | ")
        print("-----" * n)
    print()


def chek_win(z):
    for i, r in enumerate(field):
        if r == [z for _ in range(n)]:
            return True

    arr = numpy.array(field)
    arr_transpose = arr.transpose()
    a = arr_transpose.tolist()

    for i, r in enumerate(a):
        if r == [z for _ in range(n)]:
            return True

    cnt1 = 0
    cnt2 = 0
    for i in range(len(field)):
        for j in range(len(field[i])):
            if i == j and field[i][j] == z:
                cnt1 += 1
            if (len(field[i]) - i - 1) == j and field[i][j] == z:
                cnt2 += 1

    if cnt1 == n or cnt2 == n:
        return True

    return False


def enter_coord(num):
    if num == 1:
        y = input("введи координату X: ")
        x = input("введи координату Y: ")

        if y.isdigit() and y.isdigit():

            y = int(y)
            x = int(x)
            y -= 1
            x -= 1
            if all([0 <= x < n, 0 <= y < n]):

                if field[x][y] != "O" and field[x][y] != "X":
                    field[x][y] = "X"
                else:
                    print("поле уже занято.")
                    enter_coord(1)

            else:
                print("неверные данные, введите еще раз.")
                enter_coord(1)

        else:
            print("введено не число.")
            enter_coord(1)

    if num == 2:
        print("ходит компьютер.")
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        if field[x][y] != "O" and field[x][y] != "X":
            field[x][y] = "O"
        else:
            enter_coord(2)


def size():
    num = input("введи размер поля: ")
    if num.isdigit():
        num = int(num)
    else:
        print("введи число.")
        return size()
    if num < 3:
        print("выбори размер от 3х.")
        return size()

    print(type(num))
    return num


def chek_end_game():
    array = numpy.array(field)
    if " " not in array:
        print("Ничья. \nКонец игры.")
        return True
    return False


greet()
n = size()
field = [[" "] * n for i in range(n)]
human = 1
ai = 2
show()

while True:

    enter_coord(human)
    show()

    if chek_win("X"):
        print("Победил человек. \nКонец игры.")
        break

    if chek_end_game():
        break

    enter_coord(ai)
    show()

    if chek_end_game():
        break

    if chek_win("O"):
        print("Победил компьютер. \nКонец игры.")
        break
