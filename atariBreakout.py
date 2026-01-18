import turtle
import time

#screen
screen=turtle.Screen()
screen.setup(600,400)
screen.bgcolor("#141B41")
#screen.tracer(0)


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


screen.mainloop()

