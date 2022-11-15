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
    print("    | 1 | 2 | 3 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i + 1} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def chek_win(z):

    for i, r in enumerate(field):
        if r == [z for _ in range(n)]:
            return True
        for j, f, v in zip(field[0], field[1], field[2]):
            if j == z and f == z and v == z:
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


def enter_coord():
    global x
    global y

    y = int(input("введи координату X: "))-1
    x = int(input("введи координату Y: "))-1

    # if y.isdigit() and y.isdigit():
    #     x = int(x)
    #     y = int(y)
    # else:
    #     print("введены не цифры")
    #     enter_coord()

    if all([0 <= x <= n, 0 <= y <= n, field[x][y] != "O", field[x][y] != "X"]):
        field[x][y] = "X"
    else:
        print("введи верные координаты")
        enter_coord()


def ai_enter_coord():
    global x
    global y
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if all([0 <= x <= 3, 0 <= y <= 3, field[x][y] != "O", field[x][y] != "X"]):
        field[x][y] = "O"
    else:
        ai_enter_coord()


greet()
n = 3
field = [[" "] * n for i in range(n)]
show()

x = 0
y = 0

while True:

    enter_coord()
    show()
    if chek_win("X"):
        print("Победил человек. \nКонец игры.")
        break

    arr = numpy.array(field)
    if " " not in arr:
        print("Ничья. \nКонец игры.")
        break

    print("ходит компьютер.")
    ai_enter_coord()

    show()

    if chek_win("O"):
        print("Победил компьютер. \nКонец игры.")
        break
