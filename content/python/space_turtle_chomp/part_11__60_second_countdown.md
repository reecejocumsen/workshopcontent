+++
title = "60 second, countdown!"
date = 2021-02-04T20:22:00+08:00
weight = 110
chapter = true
pre = "<b>11. </b>"
+++

### Part 11

# 60 second, countdown!

You have most of your Space Turtle Chomp game developed now, however at the
 moment it can go on forever, like most games what you can do is set a time
 limit for the game duration, again this is simple to do.

Step 1.  Move to the top of your code and import the time function with the
 other imports:

```python
import time
```

Step 2.  Move down to the just below the \# Set speed variable section and add:

```python
# Set game time limit for 1 minute (60 seconds)
timeout = time.time() + 10*6
```

{{% notice note %}}
note we set our game timeout to 6 lots of 10 second for a 1 minute game we
 could set it to 5 for 30 seconds or 5\*5 for 25 seconds
{{% /notice %}}

Step 3.  Move to the top of the while true section and add the following:

```python
    gametime = 0
    if gametime == 6 or time.time() > timeout:
        break
    gametime = gametime - 1
```

{{% notice note %}}
you set a variable called gametime and set it to 0, the if statement then runs
 the loop until gametime = 6
{{% /notice %}}

Step 4.  Save your game as kbgame11 and run your Module

You should now have 60 seconds to chomp more space cabbages than your computer
 opponent before the game ends. The last thing you can do
 for your game as part of this tutorial is have the game display who wins at
 the end of 60 seconds.

Step 5.  Move to the very end of your code and add the following if
 statement and argument. This time the text is not indented until after the if
 statement:

```python
if (int(score) > int(competitor_score)):
    interface_pen.setposition(0, 0)
    interface_pen.color("yellow")
    interface_pen.write("Game Over: You WIN", False, align="center", font=("Arial", 28, "normal"))
else:
    interface_pen.setposition(0, 0)
    interface_pen.color("yellow")
    interface_pen.write("Game Over: You LOSE", False, align="center", font=("Arial", 28, "normal"))
```

The if statement compares your score \(player\) against the opponent score
 \(competitor\) and if your score is higher it prints the You Win message and if it
 is lower it prints the You Lose message.

If you run your code now, the game will quit before you can actually read the message. Let’s add a delay so we can see the message.

```python
delay = input("Press Enter to finish.")
```

That is the end of today’s tutorial, if you got through all of it in 1 day well
 done that is an awesome effort but it doesn’t matter if you didn’t as the
 tutorial is online and you can still access it from home. Don't forget to join
 our [She Codes online community](https://join.slack.com/t/shecodesaus/shared_invite/zt-9jktxnlx-Rur3NGFSBFJ7LRwq7AV~ig) to keep in touch with your mentors and ask for help.

If you enjoyed this and wanted to continue practising,
 other things you might want to try is

* Making multiple opponents using the List \[\] function like you did for food
* Setting a start option at the beginning of the game
* Setting a play again option at the end
* Setting up a easy, medium and hard option for the game

There are lots of tutorials and help out on the internet.
 It is also a great idea to try the other game options from Christian Thompson
 at his [site](http://christianthompson.com).

Your code should look like this: Mac/Linux [kbgame11.py](/python_game/src/kbgame11.py), Windows [kbgame11.py](/python_game/src/kbgame11_win.py)

**Congratulations Module 11 Completed**
