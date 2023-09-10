from turtle import Turtle

FONT = ("Courier", 20, "normal")
COLORS = ["dim gray", "lime green", "medium blue", "orange red", "red", "black"]


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=260)
        self.color(COLORS[self.level - 1])
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color(COLORS[self.level - 1])
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        self.color(COLORS[self.level - 1])

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", align="center", font=FONT)
