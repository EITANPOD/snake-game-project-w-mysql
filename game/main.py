from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import requests

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

game_is_on = False
snake = None
food = None
scoreboard = None

def start_game():
    global game_is_on, snake, food, scoreboard
    start_button.clear()
    start_button.hideturtle()
    
    if not snake:
        snake = Snake()
        food = Food()
        scoreboard = Scoreboard()
    else:
        snake.reset()
        food.refresh()
        scoreboard.reset()
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    
    game_is_on = True
    play_game()

def play_game():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > screen.window_width() / 2 - 20 or snake.head.xcor() < -screen.window_width() / 2 + 20 or \
           snake.head.ycor() > screen.window_height() / 2 - 20 or snake.head.ycor() < -screen.window_height() / 2 + 20:
            game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_over()

def send_score_to_server(player_name, score):
    try:
        response = requests.post('http://localhost:5000/score', 
                                 json={'player_name': player_name, 'score': score})
        if response.status_code == 201:
            print("Score submitted successfully")
        else:
            print(f"Failed to submit score. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error connecting to server: {e}")

def game_over():
    global game_is_on
    game_is_on = False
    scoreboard.game_over()
    
    # Get player name and send score to server
    player_name = screen.textinput("Game Over", "Enter your name:")
    if player_name:
        send_score_to_server(player_name, scoreboard.score)
    
    screen.ontimer(reset_game, 2000)


def reset_game():
    scoreboard.clear_game_over()  # New method to clear game over message
    start_button.clear()
    start_button.goto(0, 0)
    start_button.write("Press SPACE to Start", align="center", font=("Courier", 24, "normal"))
    screen.listen()
    screen.onkey(start_game, "space")
    screen.update()

# Create start button
start_button = Turtle()
start_button.color("white")
start_button.hideturtle()
start_button.penup()
start_button.goto(0, 0)
start_button.write("Press SPACE to Start", align="center", font=("Courier", 24, "normal"))

# Set up key listener for starting the game
screen.listen()
screen.onkey(start_game, "space")

# Main game loop
screen.mainloop()