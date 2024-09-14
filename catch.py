import turtle
import rand

screen = turtle.Screen()
game_over = False
score = 0
win_score = 3
FONT = ('Arial', 30, 'normal')
screen.bgcolor("light blue")
screen.title("Catch the Turtle")

turtle_list = []

# Countdown turtle
count_down_turtle = turtle.Turtle()

# Score turtle
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("dark blue")
score_turtle.penup()

top_height = screen.window_height() / 2
y = top_height * 0.9
score_turtle.setposition(0, y)
score_turtle.write(arg="Score: 0", move=False, align="center", font=("Arial", 16, "normal"))

grid_size = 10

# Turtle oluşturma fonksiyonu
def make_turtle(x, y):
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("purple")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

    def handle_click(x, y):
        global score, game_over
        if not game_over:
            score += 1
            score_turtle.clear()
            score_turtle.write("Score: {}".format(score), move=False, align="center", font=FONT)
            print(f"Tıklanan koordinatlar: {x}, {y}")
            if score >= win_score:
                game_over = True
                count_down_turtle.clear()
                hide_turtles()
                count_down_turtle.write("Kazandınız!", align='center', font=FONT)

    t.onclick(handle_click)

# Koordinatlar
x_coordinates = [-5, -3, -1, 1, 3, 5]
y_coordinates = [5, 3, 1, -1, -3, -5]

# Kaplumbağaları oluşturma fonksiyonu
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

# Tüm kaplumbağaları gizleme
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

# Rastgele kaplumbağa gösterme
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)  # 500 ms sonra rastgele turtle göster

# Geri sayım fonksiyonu
def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, y - 30)
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write("Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        if score >= win_score:
            count_down_turtle.clear()
            hide_turtles()
            count_down_turtle.write("Kazandınız!", align='center', font=FONT)
        else:
            game_over = True
            count_down_turtle.clear()
            hide_turtles()
            count_down_turtle.write("Game Over!", align='center', font=FONT)

# Oyunu başlatma fonksiyonu
def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 1000)

start_game_up()
turtle.mainloop()
