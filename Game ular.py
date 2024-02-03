import turtle
import time
import random

delay = 0.1

# Skor
score = 0
high_score = 0

# Membuat jendela
wn = turtle.Screen()
wn.title("Game Ular")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Mematikan pembaruan otomatis

# Kepala ular
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Makanan ular
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Teks skor
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Skor: 0  Skor Tertinggi: 0", align="center", font=("Courier", 24, "normal"))


# Fungsi gerakan
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Fungsi tabrakan
def check_collision():
    # Tabrakan dengan batas layar
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        return True

    # Tabrakan dengan tubuh ular
    for segment in segments[1:]:
        if segment.distance(head) < 20:
            return True

    return False


# Game over
def game_over():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Stop"

    # Menghilangkan segment tubuh
    for segment in segments:
        segment.goto(1000, 1000)

    # Menghapus segment dari list
    segments.clear()

    # Reset skor
    global score, high_score
    score = 0
    score_pen.clear()
    score_pen.write("Skor: {}  Skor Tertinggi: {}".format(score, high_score), align="center",
                    font=("Courier", 24, "normal"))


# Perbarui skor tertinggi
def update_high_score():
    global high_score
    if score > high_score:
        high_score = score


# Main game loop
while True:
    wn.update()

    # Cek tabrakan dengan makanan
    if head.distance(food) < 20:
        # Pindahkan makanan ke posisi acak
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Tambahkan segment tubuh
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Perbarui skor
        score += 1
        update_high_score()
        score_pen.clear()
        score_pen.write("Skor: {}  Skor Tertinggi: {}".format(score, high_score), align="center",
                        font=("Courier", 24, "normal"))

    # Gerakkan segment terakhir ke segment sebelumnya
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Gerakkan segment 0 (kepala) ke posisi baru
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Gerakkan kepala
    move()

    # Cek tabrakan dengan tubuh ular atau batas layar
    if check_collision():
        game_over()

    time.sleep(delay)
