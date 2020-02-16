import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Every time the ball moves, it moves by 2px
ball.dx = 0.1
ball.dy = -0.1

# Scoring Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 24, "normal"))


# Paddle A Functions
def paddle_a_up():
    # ycor = Turtle module that returns "y" coordinate
    y = paddle_a.ycor()
    # y can be moved up by 20px at a time
    y += 20
    # after y moves, reset the y value
    paddle_a.sety(y)


def paddle_a_down():
    # ycor = Turtle module that returns "y" coordinate
    y = paddle_a.ycor()
    # y can be moved down by 20px at a time
    y -= 20
    # after y moves, reset the y value
    paddle_a.sety(y)


# Paddle B Functions
def paddle_b_up():
    # ycor = Turtle module that returns "y" coordinate
    y = paddle_b.ycor()
    # y can be moved up by 20px at a time
    y += 20
    # after y moves, reset the y value
    paddle_b.sety(y)


def paddle_b_down():
    # ycor = Turtle module that returns "y" coordinate
    y = paddle_b.ycor()
    # y can be moved down by 20px at a time
    y -= 20
    # after y moves, reset the y value
    paddle_b.sety(y)


# Keyboard binding
# Tells the window to listen for keyboard input
wn.listen()

# Runs paddle_a_up when the key "w" is pressed
wn.onkeypress(paddle_a_up, "w")
# Runs paddle_a_down when the key "s" is pressed
wn.onkeypress(paddle_a_down, "s")

# Runs paddle_b_up when the "Up" arrow is pressed
wn.onkeypress(paddle_b_up, "Up")
# Runs paddle_a_down when the "Down" arrow is pressed
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()

#   Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking top y axis
    if ball.ycor() > 290:
       ball.sety(290)
       # Reset the Balls direction
       ball.dy *= -1

    # Border Checking bottom y axis
    if ball.ycor() < -280:
       ball.sety(-280)
       # Reset the Balls direction
       ball.dy *= -1

    # Reset ball if scored on Right goal
    if ball.xcor() > 450:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Reset ball if scored on Left goal
    if ball.xcor() < -450:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

#     Paddle and Ball Collisions
#     Paddle B Collisions:
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

#     Paddle A Collisions:
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() > paddle_a.ycor() + -50 and ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

