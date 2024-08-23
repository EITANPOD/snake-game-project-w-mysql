from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
screen = Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, screen.window_height() / 2 - 95)  # Position at the top
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def clear_game_over(self):
        self.clear()
        self.goto(0, screen.window_height() / 2 - 95)  # Reset position to top
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.clear_game_over()