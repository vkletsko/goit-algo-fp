import turtle


def tree(branch_len, t, level):

    if level > 0:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len * 0.75, t, level - 1)
        t.left(40)
        tree(branch_len * 0.75, t, level - 1)
        t.right(20)
        t.backward(branch_len)


def main():
    level = int(input("Вкачіть рівень рекурсії: "))

    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")

    tree(75, t, level)

    turtle.mainloop()


if __name__ == "__main__":
    main()
