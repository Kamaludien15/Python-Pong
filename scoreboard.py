from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 225)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score\n{self.left_score} - {self.right_score}", align=ALIGNMENT, font=FONT)

    def right_point(self):
        self.right_score += 1
        self.clear()
        self.update()

    def left_point(self):
        self.left_score +=1
        self.clear()
        self.update()