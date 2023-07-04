# Turtle Graphics Game
import math
import random
import turtle

# Set up screen
turtle.setup(650, 650)
window = turtle.Screen()
window.bgcolor("Navy")

# Draw border
interface_pen = turtle.Turtle()
interface_pen.color("white")
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

# create food
food = turtle.Turtle()
food.color("lightgreen")
food.shape("circle")
food.penup()
food.speed(0)
food.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Set speed variable
speed = 1


# Define functions
def turn_left():
    player.left(30)


def turn_right():
    player.right(30)


def increase_speed():
    global speed
    speed += 1


def is_collision(turtle_1, turtle_2):
    distance = math.sqrt(
        math.pow(turtle_1.xcor() - turtle_2.xcor(), 2) + math.pow(turtle_1.ycor() - turtle_2.ycor(), 2)
    )
    if distance < 20:
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
    # Boundary Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

    # Boundary Food Checking x coordinate
    if food.xcor() > 290 or food.xcor() < -290:
        food.right(180)

    # Boundary Food Checking y coordinate
    if food.ycor() > 290 or food.ycor() < -290:
        food.right(180)

    # Move goal around
    food.forward(3)

    # Collision checking
    if is_collision(player, food):
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))
        food.right(random.randint(0, 360))

delay = input("Press Enter to finish.")
