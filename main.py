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
    print(f"    | 1 | 2 | 3 | ")
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


def enter_coord2(num):

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
                    enter_coord2(1)

            else:
                print("неверные данные, введите еще раз.")
                print(x, y)
                enter_coord2(1)

        else:
            print("введено не число.")
            enter_coord2(1)

    if num == 2:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if all([0 <= x <= 3, 0 <= y <= 3, field[x][y] != "O", field[x][y] != "X"]):
            field[x][y] = "O"
        else:
            enter_coord2(2)


def enter_coord():
    global x
    global y

    y = int(input("введи координату X: ")) - 1
    x = int(input("введи координату Y: ")) - 1

    if all([0 <= x <= n, 0 <= y <= n, field[x][y] != "O", field[x][y] != "X"]):
        field[x][y] = "X"
    else:
        print("введи верные координаты.")
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

n = int(input("введи размер поля: "))
field = [[" "] * n for i in range(n)]
print(field)
show()

x = 0
y = 0

while True:

    # enter_coord()
    enter_coord2(1)
    show()
    if chek_win("X"):
        print("Победил человек. \nКонец игры.")
        break

    arr = numpy.array(field)
    if " " not in arr:
        print("Ничья. \nКонец игры.")
        break

    print("ходит компьютер.")
    enter_coord2(2)
    # ai_enter_coord()

    show()

    if chek_win("O"):
        print("Победил компьютер. \nКонец игры.")
        break
