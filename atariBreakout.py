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
paddle.speed(0)
paddle_width=120

#ball
ball=turtle.Turtle()



screen.mainloop()

