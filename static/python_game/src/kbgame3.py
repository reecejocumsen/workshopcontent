# Turtle Graphics Game
import turtle

# Set up screen
turtle.setup(650, 650)
window = turtle.Screen()
window.bgcolor("Navy")

# Draw border
interface_pen = turtle.Turtle()
interface_pen.penup()
interface_pen.setposition(-300, -300)
interface_pen.pendown()
interface_pen.pensize(3)
for side in range(4):
    interface_pen.forward(600)
    interface_pen.left(90)
interface_pen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color("darkorange")
player.shape("turtle")
player.penup()
player.speed(0)

# Set speed variable
speed = 1

# Define  functions


def turn_left():
    player.left(30)


def turn_right():
    player.right(30)


def increase_speed():
    global speed
    speed += 1


# Set keyboard bindings
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")

while True:
    player.forward(speed)

    # Boundary Checking x cordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
    # Boundary Checking x cordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

delay = input("Press Enter to finish.")
