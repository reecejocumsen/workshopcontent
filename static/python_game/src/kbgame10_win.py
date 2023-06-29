# Turtle Graphics Game
import math
import random
import turtle
import winsound

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

# Create player and competition score
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
    comp.forward(12)

    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Boundary Comp Checking x coordinate
    if comp.xcor() > 290 or comp.xcor() < -290:
        comp.right(random.randint(10, 170))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Boundary Comp Checking y coordinate
    if comp.ycor() > 290 or comp.ycor() < -290:
        comp.right(random.randint(10, 170))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Move Food around
    for food in foods:
        food.forward(3)

        # Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(180)
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() < -290:
            food.right(180)
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # Player Collision checking
        if is_collision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            winsound.PlaySound("chomp.wav", winsound.SND_ASYNC)
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
            winsound.PlaySound("chomp.wav", winsound.SND_ASYNC)
            comp_score += 1
            # Draw the Comp score on the screen
            my_pen_2.undo()
            my_pen_2.penup()
            my_pen_2.hideturtle()
            my_pen_2.setposition(200, 305)
            score_string = "Score: %s" % comp_score
            my_pen_2.write(
                score_string, False, align="left", font=("Arial", 14, "normal")
            )

delay = input("Press Enter to finish.")
