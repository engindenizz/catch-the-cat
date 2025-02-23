import random
import turtle
import pygame


class Game:
    def __init__(self):
        # Game Variables
        self.score_count = 0
        self.timer_count = 20
        self.count = 0
        self.time = 400
        pygame.mixer.init()
        self.win_sound = pygame.mixer.Sound("assets/sounds/win.wav")
        self.lose_sound = pygame.mixer.Sound("assets/sounds/lose.wav")
        self.meow_sound = pygame.mixer.Sound("assets/sounds/meow.wav")

        # Screen Setup

        self.screen = turtle.Screen()
        self.screen.title("Catch the Cat")
        self.screen.bgcolor("orange")
        self.screen.setup(width=800, height=800)

        # Cat(Turtle) Object
        self.cat = turtle.Turtle()
        self.screen.addshape("assets/images/cat.gif")
        self.cat.shape("assets/images/cat.gif")
        self.cat.penup()

        # Timer Display
        self.timer = turtle.Turtle()
        self.timer.hideturtle()
        self.timer.penup()
        self.timer.goto(0, 350)
        self.timer.write(
            "You have left: " + str(self.timer_count),
            align="center",
            font=("Courier", 16, "bold"),
        )

        # Score Display
        self.score = turtle.Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(0, 300)
        self.score.color("blue")
        self.score.write(
            "Score: " + str(self.score_count),
            align="center",
            font=("Courier", 22, "bold"),
        )

        self.again_button = turtle.Turtle()
        self.again_button.showturtle()
        self.again_button.penup()
        self.screen.addshape("assets/images/start.gif")
        self.again_button.shape("assets/images/start.gif")
        self.again_button.goto(-180, -200)

        self.exit_button = turtle.Turtle()
        self.exit_button.showturtle()
        self.exit_button.penup()
        self.screen.addshape("assets/images/exit.gif")
        self.exit_button.shape("assets/images/exit.gif")
        self.exit_button.goto(180, -200)

        self.restart_button = turtle.Turtle()
        self.restart_button.hideturtle()
        self.restart_button.penup()
        self.screen.addshape("assets/images/restart.gif")
        self.restart_button.shape("assets/images/restart.gif")
        self.restart_button.goto(-180, -200)

        self.screen.listen()
        self.cat.onclick(self.update_score)
        self.screen.listen()
        self.again_button.onclick(self.start_game)
        self.screen.listen()
        self.exit_button.onclick(self.exit_game)
        self.screen.listen()
        self.restart_button.onclick(self.restart_game)

    def start_game(self, x, y):
        self.again_button.hideturtle()
        self.exit_button.hideturtle()
        self.move()

    def restart_game(self, x, y):
        self.score_count = 0
        self.count = 0
        self.time = 400
        self.timer.clear()
        self.score.clear()
        self.score.color("blue")
        self.score.write(
            "Score: " + str(self.score_count),
            align="center",
            font=("Courier", 22, "bold"),
        )
        self.cat.showturtle()
        self.restart_button.hideturtle()
        self.exit_button.hideturtle()
        self.move()

    def exit_game(self, x, y):
        turtle.bye()

    def update_score(self, x, y):
        self.score_count += 1
        self.score.clear()
        self.score.color("blue")
        self.score.write(
            "Score: " + str(self.score_count),
            align="center",
            font=("Courier", 22, "bold"),
        )
        self.meow_sound.play()

    def random_place(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.cat.goto(random_x, random_y)

    def move(self):
        self.random_place()
        self.check_timer()

    def check_timer(self):
        self.timer_count = max(0, 20 - self.count)
        self.count += 1
        if self.count < 20:
            self.screen.ontimer(self.move, self.time)
            self.timer.color("black")
            self.timer.clear()
            self.timer.write(
                "You have left: " + str(self.timer_count),
                align="center",
                font=("Courier", 16, "bold"),
            )
        else:
            self.end_game()

    def end_game(self):
        self.cat.hideturtle()
        self.restart_button.showturtle()
        self.exit_button.showturtle()
        message = ""
        color = ""
        sound = None

        if self.score_count >= 10:
            message = "Your score is " + str(self.score_count) + " You Win ! 🎉"
            color = "green"
            sound = self.win_sound
        else:
            message = "Your score is " + str(self.score_count) + " You Suck 😿😿 "
            color = "red"
            sound = self.lose_sound

        self.score.clear()
        self.score.color(color)
        self.score.write(message, align="center", font=("Courier", 22, "bold"))

        self.timer.clear()
        self.timer.color(color)
        self.timer.write("Game Over 😿 ", align="center", font=("Courier", 21, "bold"))

        sound.play()

    def run(self):
        self.screen.mainloop()


game = Game()
game.run()
