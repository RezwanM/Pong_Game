# Code borrowed from: https://www.youtube.com/watch?v=XGf2GcyHPhc
import turtle

# Set the turtle screen parameters
# Note: Turtle screen has coordinates, with the center being at (0,0)
wn = turtle.Screen()
wn.title("Pong by Rezwan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A - Left Paddle
paddle_a = turtle.Turtle()  # Make a Turtle object for Paddle A
paddle_a.speed(0)  # Set the speed of the animation to highest
paddle_a.shape("square")  # This creates a 20x20 px square
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Multiply width px by 5, length px by 1
paddle_a.penup()  # So that the Turtle doesn't draw a line when moving (its default behavior)
paddle_a.goto(-350, 0)  # Initial coordinates

# Paddle B - Right Paddle
paddle_b = turtle.Turtle()  # Make a Turtle object for Paddle A
paddle_b.speed(0)  # Set the speed of the animation to highest
paddle_b.shape("square")  # This creates a 20x20 px square
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # This converts our square to a rectangle
paddle_b.penup()  # So that the Turtle doesn't draw a line when moving (its default behavior)
paddle_b.goto(350, 0)  # Initial coordinates

# Ball
ball = turtle.Turtle()  # Make a Turtle object for Paddle A
ball.speed(0)  # Set the speed of the animation to highest
ball.shape("square")  # This creates a 20x20 px square
ball.color("white")
ball.penup()  # So that the Turtle doesn't draw a line when moving (its default behavior)
ball.goto(0, 0)  # Initial coordinates
ball.dx = 0.2  # delta x, defines by how many pixels the ball moves in the x-axis
ball.dy = 0.2  # delta y, defines by how many pixels the ball moves in the y-axis

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)  # Position of the score board
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()  # We need to know the current y-coordinate first
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()  # We need to know the current y-coordinate first
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()  # We need to know the current y-coordinate first
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()  # We need to know the current y-coordinate first
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()  # This "listens" for a keyboard input
wn.onkeypress(paddle_a_up, "w")  # When user presses w, call paddle_a_up()
wn.onkeypress(paddle_a_down, "s")  # When user presses s, call paddle_a_down()
wn.onkeypress(paddle_b_up, "Up")  # When user presses Up, call paddle_b_up()
wn.onkeypress(paddle_b_down, "Down")  # When user presses Down, call paddle_b_down()


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top border
    if ball.ycor() > 290:  # Since height of screen is 600 px (300 above origin of screen)
        ball.sety(290)  # Also, height of ball is 20 px (10 px above origin of ball)
        ball.dy *= -1  # This reverses the direction of y-axis movement
    
    # Bottom border
    if ball.ycor() < -290:  # Since height of screen is 600 px (300 below origin of screen)
        ball.sety(-290)  # Also, height of ball is 20 px (10 px below origin of ball)
        ball.dy *= -1  # This reverses the direction of y-axis movement
    
    # Right border
    if ball.xcor() > 390:  # If ball goes past Paddle B
        ball.goto(0, 0)  # Bring ball back to center
        ball.dx *= -1  # Reverse the direction of the x-axis movement
        score_a += 1  # Player A gets a score 
        pen.clear()  # Or else digit gets written over previous digit
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    # Left border
    if ball.xcor() < -390:  # If ball goes past Paddle A
        ball.goto(0, 0)  # Bring ball back to center
        ball.dx *= -1  # Reverse the direction of the x-axis movement
        score_b += 1  # Player B gets a score
        pen.clear()  # Or else digit gets written over previous digit
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    # We need to compare the current coordinates of the ball with the coordinates of the paddle
    # For Paddle B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    # For Paddle A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1