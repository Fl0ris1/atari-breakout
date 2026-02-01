import turtle
import time

#screen
screen=turtle.Screen()
screen.setup(600,400)
screen.bgcolor("#141B41")
screen.tracer(0)


#paddle
paddle=turtle.Turtle()
paddle.shape("square")
paddle.color("#306BAC")
paddle.penup()
paddle.goto(0,-180)
paddle.turtlesize(stretch_wid=1, stretch_len=4, outline=1)
paddle.speed(0)
paddle_width=120

#ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("#FFFFFF")
ball.penup()
ball.goto(0,-50)
ball.dx=2
ball.dy=-2

#bricks
bricks=[]
colors=["red","#ff5400","yellow","green","purple"]

for row in range(5):
    for col in range(-250,300,80):
        brick=turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.penup()
        brick.goto(col,150-(row*30))
        brick.speed(0)
        bricks.append(brick)

#score
score=0
scoreDis=turtle.Turtle()
scoreDis.color("white")
scoreDis.penup()
scoreDis.goto(0,170)
scoreDis.write(f"Score: {score}",align="center",font=("Arial",18,"bold"))
scoreDis.hideturtle()


#paddle movement
def moveLeft():
    x=paddle.xcor()
    if x-paddle_width//2>-450:
        paddle.setx(x-50)

def moveRight():
    x=paddle.xcor()
    if x+paddle_width//2<450:
        paddle.setx(x+50)

screen.listen()
screen.onkey(moveLeft,"a")
screen.onkey(moveRight,"d")

gameStart=False

def startGame(x,y):
    global gameStart
    gameStart=True
    
screen.onclick(startGame)

#game loop

while True:
    screen.update()
    time.sleep(0.01)
    if not gameStart:
        continue
    

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #check colision with walls
    if ball.xcor()>290 or ball.xcor()<-290:
        ball.dx*=-1

    if ball.ycor()>190:
        ball.dy*=-1

    if ball.ycor()<-190:
        ball.dy*=-1
        ball.goto(0,-50)
        gameStart=False
        score=0
        scoreDis.clear()
        scoreDis.write(f"Score: {score}",align="center",font=("Arial",18,"bold"))    

    #collision between ball and paddle
    if (ball.ycor()>-180 and ball.ycor()<-170) and (paddle.xcor()-paddle_width//2<ball.xcor()<paddle.xcor()+paddle_width//2):
        ball.dy*=-1

    #collision between ball and bricks
    for brick in bricks:
        if abs(ball.xcor()-brick.xcor())<40 and abs(ball.ycor()-brick.ycor())<15:
            score+=10
            ball.dy*=-1
            brick.hideturtle()
            bricks.remove(brick)
            scoreDis.clear()
            scoreDis.write(f"Score: {score}",align="center",font=("Arial",18,"bold"))
    #winning condition
    if len(bricks)==0:
        print("You Win")
        break


screen.mainloop()

