import turtle

# Global variable to store character choice
character = ""

def getPosition(x, y):
    global character  # Important to modify the global variable
    if -300 < x < -100:
        character = "assasin"
    elif -100 < x < 100:
        character = "witch"
    else:
        character = "warrior"
    
    # Clear screen and move to level1
    turtle.clearscreen()
    import level1
    level1.start_game(character)

def hero_run():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.bgpic("assets/hero/background.png")
    screen.onclick(getPosition)