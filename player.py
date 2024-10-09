from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.restart()
        self.setheading(90)

    def go_up(self):
        """
        Makes the turtle move forward
        """
        self.forward(MOVE_DISTANCE)

    def restart(self):
        """
        Bring the Turtle back to the start position
        """
        self.goto(STARTING_POSITION)

    def finish_line(self):
        """
        Detect when the turtle crossed the road
        """
        if self.ycor() > 280:
            return True
        else:
            return False