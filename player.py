from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.speed(0)
        self.goto(STARTING_POSITION)
        own_screen = self.screen
        own_screen.onkey(self.turtle_forward, "Up")
        own_screen.onkey(self.turtle_backward, "Down")
        own_screen.listen()

    def turtle_forward(self):
        if self.ycor() > 280:
            return
        self.forward(MOVE_DISTANCE)

    def turtle_backward(self):
        if self.ycor() < -270:
            return
        self.backward(MOVE_DISTANCE)
