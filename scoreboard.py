from turtle import Turtle

MOVE = False
ALIGNMENT = "center"
FONT = ('Courier', 17, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.increase_score()

    def game_over(self):
        self.goto(0, 0 )
        self.write("GAME OVER", MOVE, ALIGNMENT, FONT)

    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score}", MOVE, ALIGNMENT, FONT)
