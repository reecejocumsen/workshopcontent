# Turtle Graphics Game
import math
import os
import random
import time
import turtle

# Set up screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("kbgame-bg.gif")
wn.tracer(3)

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

# Create competition turtle
comp = turtle.Turtle()
comp.color("red")
comp.shape("turtle")
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Create competition pen
my_pen_2 = turtle.Turtle()
my_pen_2.color("red")
my_pen_2.hideturtle()

# Create player and competitor score
score = 0
comp_score = 0

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

# Set game time limit for 1 minute (60 seconds)
timeout = time.time() + 10 * 6

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
    gametime = 0
    if gametime == 6 or time.time() > timeout:
        break
    gametime = gametime - 1

    player.forward(speed)
    comp.forward(12)

    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        os.system("afplay bounce.mp3&")

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        os.system("afplay bounce.mp3&")

    # Boundary Comp Checking x coordinate
    if comp.xcor() > 280 or comp.xcor() < -280:
        comp.right(random.randint(30, 155))
        os.system("afplay bounce.mp3&")

    # Boundary Comp Checking y coordinate
    if comp.ycor() > 280 or comp.ycor() < -280:
        comp.right(random.randint(30, 155))
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

        # Player Collision checking
        if is_collision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            os.system("afplay chomp.mp3&")
            score += 1
            # Draw the score on the screen
            my_pen.undo()
            my_pen.penup()
            my_pen.hideturtle()
            my_pen.setposition(-290, 310)
            score_string = "Score: %s" % score
            my_pen.write(
                score_string, False, align="left", font=("Arial", 14, "normal")
            )

        # Comp Collision checking
        if is_collision(comp, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            os.system("afplay chomp.mp3&")
            comp_score += 1
            # Draw the Comp score on the screen
            my_pen_2.undo()
            my_pen_2.penup()
            my_pen_2.hideturtle()
            my_pen_2.setposition(200, 310)
            score_string = "Score: %s" % comp_score
            my_pen_2.write(
                score_string, False, align="left", font=("Arial", 14, "normal")
            )

if int(score) > int(comp_score):
    my_pen.setposition(0, 0)
    my_pen.color("yellow")
    my_pen.write(
        "Game Over: You WIN", False, align="center", font=("Arial", 28, "normal")
    )
else:
    my_pen.setposition(0, 0)
    my_pen.color("yellow")
    my_pen.write(
        "Game Over: You LOOSE", False, align="center", font=("Arial", 28, "normal")
    )

# delay = input("Press Enter to finish.")
