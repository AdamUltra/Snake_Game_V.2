from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_sq(position)

    def add_sq(self, position):
        new_sq = Turtle("square")
        new_sq.penup()
        new_sq.color("white")
        new_sq.goto(position)
        self.squares.append(new_sq)

    def extend(self):
        # Add a new square to the nake
        self.add_sq(self.squares[-1].position())

    def move(self):
        for sq_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[sq_num - 1].xcor()
            new_y = self.squares[sq_num - 1].ycor()
            self.squares[sq_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.squares[0].setheading(LEFT)

