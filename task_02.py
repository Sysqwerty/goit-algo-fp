import turtle

DEFAULT_RECURSION_LEVEL = 5


def draw_pifagor_tree(branch_length, _turtle, angle, recursion_level):
    if recursion_level == 0:
        return
    else:
        _turtle.forward(branch_length)
        _turtle.left(angle)
        draw_pifagor_tree(0.7 * branch_length, _turtle, angle, recursion_level - 1)
        _turtle.right(2 * angle)
        draw_pifagor_tree(0.7 * branch_length, _turtle, angle, recursion_level - 1)
        _turtle.left(angle)
        _turtle.backward(branch_length)


def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Getting window size
    window_height = screen.window_height()

    my_turtle = turtle.Turtle()
    my_turtle.speed(10)
    my_turtle.color("green")

    # Start position of the turtle
    my_turtle.penup()
    my_turtle.goto(0, -window_height / 5 + 20)
    my_turtle.pendown()

    try:
        recursion_level = int(turtle.textinput(
            "Recursion level", "Enter recursion level (default = 5):"))
    except:
        recursion_level = DEFAULT_RECURSION_LEVEL
        print("Selected default recursion level = 5")

    # Turn the turtle
    my_turtle.left(90)

    draw_pifagor_tree(100, my_turtle, 40, recursion_level)

    screen.mainloop()


if __name__ == "__main__":
    main()
