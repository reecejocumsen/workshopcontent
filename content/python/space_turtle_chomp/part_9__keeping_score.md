+++
title = "Keeping score"
date = 2021-02-04T20:02:00+08:00
weight = 90
chapter = true
pre = "<b>9. </b>"
+++

### Part 9

# Keeping score

To make this more like a game you can add a score for each time your turtle
 chomps on a cabbage. To do this you create a new score variable.

Step 1.  Move to after the \#Create player turtle section of your code and
 type the following:

```python
# Create variable score
score = 0
```

Step 2.  Move to the bottom of your while True loop at the end of your
 \# Collision checking section and type:

```python
         score +=1
```

\*note: this will calculate a score but you can’t see it on the screen

Step 3.  Now we add the score to the screen by re-using the my_pen turtle and
 using it to write the score, you can do this by typing the following under the
 score +=1 text in the \# Collision checking section:

```python
    # Draw the score on the screen
    my_pen.penup()
    my_pen.hideturtle()
    my_pen.setposition(-290, 310)
    score_string ="Score: %s" % score
    my_pen.write(score_string, False, align='left', font=('Arial', 14, 'normal'))
```

So you have created a string that displays the score in the top left hand
 corner of your screen

Step 4.  Save your game as kbgame9 and run your module

What you should now see is that your score is in the top left hand corner of
 the screen but the number \(1, 2, 3, 4 etc.\) are writing on top of each other.
 You can fix this by deleting the previous score before writing the new score.

Step 5.  Add the undo option to the top of the \#Draw the score on the screen
 section:

```python
    my_pen.undo()
```

Step 6.  Save and Run your module

Your code should look like this: Mac/Linux [kbgame9.py](/python_game/src/kbgame9.py), Windows [kbgame9.py](/python_game/src/kbgame9_win.py)

**Congratulations Module 9 Completed**
