import turtle
import random
import time

words_list1 = ["lantern", "driftwood", "puzzle", "mountain", "spark", 
              "whisper", "notebook", "mirage", "velvet", "eclipse"]

def start_game(character):
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.bgpic("assets/level1/background.png")

    # Setup all turtles
    display = turtle.Turtle()
    display.hideturtle()
    display.penup()
    display.goto(0, 50)

    hint_turtle = turtle.Turtle()
    hint_turtle.hideturtle()
    hint_turtle.penup()
    hint_turtle.goto(0, 150)

    player = turtle.Turtle()
    player.hideturtle()
    player.penup()
    player.goto(-250, -200)
    player.showturtle()

    player_atk = turtle.Turtle()
    player_atk.hideturtle()
    player_atk.penup()
    player_atk.goto(player.pos())
    
    turtle.addshape("assets/weapon/heart.gif")
    player_heart1=turtle.Turtle()
    player_heart1.hideturtle()
    player_heart1.penup()
    player_heart1.goto(-250, 250)
    player_heart1.shape("assets/weapon/heart.gif")
    player_heart1.showturtle()

    player_heart2=turtle.Turtle()
    player_heart2.hideturtle()
    player_heart2.penup()
    player_heart2.goto(-230, 250)
    player_heart2.shape("assets/weapon/heart.gif")
    player_heart2.showturtle()
    
    player_heart3=turtle.Turtle()
    player_heart3.hideturtle()
    player_heart3.penup()
    player_heart3.goto(-210, 250)
    player_heart3.shape("assets/weapon/heart.gif")
    player_heart3.showturtle()

    demon_heart1=turtle.Turtle()
    demon_heart1.hideturtle()
    demon_heart1.penup()
    demon_heart1.goto(250, 250)
    demon_heart1.shape("assets/weapon/heart.gif")
    demon_heart1.showturtle()

    demon_heart2=turtle.Turtle()
    demon_heart2.hideturtle()
    demon_heart2.penup()
    demon_heart2.goto(230, 250)
    demon_heart2.shape("assets/weapon/heart.gif")
    demon_heart2.showturtle()
    
    demon_heart3=turtle.Turtle()
    demon_heart3.hideturtle()
    demon_heart3.penup()
    demon_heart3.goto(210, 250)
    demon_heart3.shape("assets/weapon/heart.gif")
    demon_heart3.showturtle()

    # Set character image
    if character == "assasin":
        turtle.addshape("assets/hero/assasin/still.gif")
        turtle.addshape("assets/weapon/shuriken.gif")
        player.shape("assets/hero/assasin/still.gif")
        player_atk.shape("assets/weapon/shuriken.gif")
    elif character == "witch":
        turtle.addshape("assets/hero/witch/still.gif")
        turtle.addshape("assets/weapon/fireball.gif")
        player.shape("assets/hero/witch/still.gif")
        player_atk.shape("assets/weapon/fireball.gif")
    else:
        turtle.addshape("assets/hero/warrior/still.gif")
        turtle.addshape("assets/weapon/sword.gif")
        player.shape("assets/hero/warrior/still.gif")
        player_atk.shape("assets/weapon/sword.gif")


    demon = turtle.Turtle()
    demon.hideturtle()
    demon.penup()
    demon.goto(150, -150)
    demon.showturtle()
    turtle.addshape(r"assets/level1/monster.gif")
    demon.shape(r"assets/level1/monster.gif")

    demon_atk=turtle.Turtle()
    demon_atk.hideturtle()
    demon_atk.penup()
    demon_atk.goto(demon.pos())
    turtle.addshape(r"assets/level1/monster_atk.gif")
    demon_atk.shape(r"assets/level1/monster_atk.gif")


    def converge(word):
        return word[::-1]

    def turtle_input(window_title, prompt):
        val = screen.textinput(window_title, prompt)
        if val is None:
            return 'quit'
        return val.lower()

    def start_game():
        player_life = 3
        demon_life = 3
        while player_life > 0 and demon_life > 0:
            word = random.choice(words_list1)
            encrypted_word = converge(word)  # Reverse the word
            hint_turtle.clear()
            hint_turtle.write(encrypted_word, align="center", font=("Arial", 20, "bold"))
            
            player_answer = turtle_input("Guess the Word", "Enter the correct word:")
            
            if player_answer == word:
                # Attack animation (optional)
                display.write("Correct!", align="center", font=("Arial", 20, "bold"))
                player_atk.showturtle()
                player_atk.goto(demon.pos())
                player_atk.hideturtle()
                demon_life -= 1  # Decrease demon's life
                if demon_life==2:
                    demon_heart3.hideturtle()
                elif demon_life==1:
                    demon_heart2.hideturtle()
                else:
                    demon_heart1.hideturtle()
                time.sleep(1)
                player_atk.goto(player.pos())
                display.clear()
            else:
                # Incorrect answer logic (player loses life)
                player_life -= 1
                display.write("Wrong!", align="center", font=("Arial", 20, "bold"))
                demon_atk.showturtle()
                demon_atk.goto(player.pos())
                demon_atk.hideturtle()
                if player_life==2:
                    player_heart3.hideturtle()
                elif player_life==1:
                    player_heart2.hideturtle()
                else:
                    player_heart1.hideturtle()
                time.sleep(1)
                display.clear()
        if(demon_life==0):
            demon.hideturtle()
            player.goto(300,-200)
            turtle.clearscreen()
            import level2
            level2.start_game(character)

        elif player_life==0:
            display.write("Game over, please refresh to play again", align="center", font=("Arial", 20, "bold"))

    start_game()
    turtle.done()  # Keep window open