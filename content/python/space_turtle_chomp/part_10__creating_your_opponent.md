+++
title = "Creating your opponent"
date = 2021-02-04T20:09:00+08:00
weight = 100
chapter = true
pre = "<b>10. </b>"
+++

### Part 10

# Creating your opponent

In general games are more fun if you get to compete against an opponent,
 for Space Turtle Chomp this is very easy to do as we have already written
 all the code we just need to create an opponent section and cut and paste
 then modify our existing code.

Step 1.  First we need to create a new turtle object as the opponent, move to
 the end of  \#Create player turtle section and add:

```python
# Create opponent turtle
competitor = turtle.Turtle()
competitor.color('red')
competitor.shape('turtle')
competitor.penup()
competitor.setposition(random.randint(-290, 290), random.randint(-290, 290))
```

Step 2.  Save your game as kbgame10 and run your module

You now have a red opponent space turtle now, but you'll notice it doesn't move. Let’s make it move around the
 screen and add the boundary checking so it doesn’t run away.

Step 3. To move your opponent turtle add the following code to the while True
 loop under player.forward\(speed\)

```
    competitor.forward(12)
```

Step 4. Next copy the following text and paste it directly underneath. Note, the below example is in the format for Mac, if you are on Windows yours will look slightly different:

```python
    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        os.system('afplay bounce.mp3&')

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        os.system("afplay bounce.mp3&")
```

Step 5. Edit the pasted text to:

```py
    # Boundary Comp Checking x coordinate
    if competitor.xcor() > 290 or competitor.xcor() < -290:
        competitor.right(180)
        os.system('afplay bounce.mp3&')

    # Boundary Comp Checking y coordinate
    if competitor.ycor() > 290 or competitor.ycor() < -290:
        competitor.right(180)
        os.system('afplay bounce.mp3&')
```

{{% notice note %}}
you can make the competitor.forward speed faster or slower by changing the number
 within the brackets
{{% /notice %}}

Step 6.  Save and run your module

Now your opponent turtle is moving around the screen and bouncing of the walls,
 next we want to give them a score

Step 7.  Within the \# Create variable score section add:

```python
competitor_score = 0
```

Step 8. Now you create your competition score just under your \# Create
 opponent turtle section by adding:

```py
# Create competition score
competitor_interface_pen = turtle.Turtle()
competitor_interface_pen.color('red')
competitor_interface_pen.hideturtle()
```

Step 9.  Now copy the player collision checking section and paste direct below. Note: this example code is the version for Windows, if you are on a mac yours will look slightly different:

```python
    # Collision checking
    if is_collision(player, food):
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))
        food.right(random.randint(0,360))
        winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
        score +=1
        interface_pen.penup()
        interface_pen.hideturtle()
        interface_pen.setposition(-290, 305)
        score_string ="Score: %s" % score
        interface_pen.write(score_string, False, align='left', font=('Arial', 14, 'normal'))
```

Step 10.  Edit the pasted code, changing player to competitor, score to competitor_score, interface_pen to competitor_interface_pen and setting the position of the competitor score. It should look something like the below:

```python
    # Comp Collision checking
    if is_collision(competitor, food):
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))
        food.right(random.randint(0,360))
        winsound.playSound('chomp.wav', winsound.SND_ASYNC)
        competitor_score+=1
        # Draw the Comp score on the screen
        competitor_interface_pen.undo()
        competitor_interface_pen.penup()
        competitor_interface_pen.hideturtle()
        competitor_interface_pen.setposition(200, 305)
        score_string ="Score: %s" % competitor_score
        competitor_interface_pen.write(score_string, False, align='left', font=('Arial', 14, 'normal'))
```



Step 11. Save and run your module

Your code should look like this: Mac/Linux [kbgame10.py](/python_game/src/kbgame10.py), Windows [kbgame10.py](/python_game/src/kbgame10_win.py)

**Congratulations Module 10 Completed**
