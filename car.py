from turtle import Turtle


class Car(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.color(color)
        self.penup()
        self.speed(0)
        self.goto(position)
        self.shape("square")
        self.shapesize(1, 2, 1)

    def move(self, distance):
        x_position = self.xcor() - distance
        y_position = self.ycor()
        self.goto(x_position, y_position)
