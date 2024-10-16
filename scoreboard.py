from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_score()

    def update_score(self):
        """
        Clears the score then put a 'new' score
        """
        self.clear()
        self.write(f"Level:{self.level}", align= "left", font=FONT)

    def increase_level(self):
        """
        increase the level of the score with each win
        """
        self.level += 1
        self.update_score()

    def game_over(self):
        """
        message when a game is over
        """
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)