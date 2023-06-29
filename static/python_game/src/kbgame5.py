# Turtle Graphics Game
import math
import random
import turtle

# Set up screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor("Navy")

# Draw border
my_pen = turtle.Turtle()
my_pen.color("white")
my_pen.penup()
my_pen.setposition(-300, -300)
my_pen.pendown()
my_pen.pensize(3)
for side in range(4):
    my_pen.forward(600)
    my_pen.left(90)
my_pen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color("darkorange")
player.shape("turtle")
player.penup()
player.speed(0)

# create food
food = turtle.Turtle()
food.color("lightgreen")
food.shape("circle")
food.penup()
food.speed(0)
food.setposition(random.randint(-290, 290), random.randint(-290, 290))

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


def is_collision(t1, t2):
    d = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    if d < 20:
        return True
    else:
        return False


# Set keyboard bindings
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")

while True:
    player.forward(speed)

    # Boundary Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
    # Boundary Checking x coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

    # Collision checking
    if is_collision(player, food):
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))


delay = input("Press Enter to finish.")
