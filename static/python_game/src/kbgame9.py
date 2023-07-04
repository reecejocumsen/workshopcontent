# Turtle Graphics Game
import math
import os
import random
import turtle

# Set up screen
turtle.setup(650, 650)
window = turtle.Screen()
window.bgcolor("black")
window.bgpic("kbgame-bg.gif")
window.tracer(3)

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

# Create player and competitor score
score = 0

# create food
max_foods = 10
foods = []

for count in range(max_foods):
    new_food = turtle.Turtle()
    new_food.color("lightgreen")
    new_food.shape("circle")
    new_food.shapesize(0.5)
    new_food.penup()
    new_food.speed(0)
    new_food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(new_food)
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

    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        os.system("afplay bounce.mp3&")

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        os.system("afplay bounce.mp3&")

    # Move Food around
    for food in foods:
        food.forward(3)

        # Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(180)
            os.system("afplay bounce.mp3&")

        # Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() < -290:
            food.right(180)
            os.system("afplay bounce.mp3&")

        # Collision checking
        if is_collision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            os.system("afplay chomp.mp3&")
            score += 1
            # Draw the score on the screen
            interface_pen.undo()
            interface_pen.penup()
            interface_pen.hideturtle()
            interface_pen.setposition(-290, 310)
            score_string = "Score: %s" % score
            interface_pen.write(
                score_string, False, align="left", font=("Arial", 14, "normal")
            )

delay = input("Press Enter to finish.")
