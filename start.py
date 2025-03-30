import turtle

def close_and_open(x, y):
    # Clear current screen
    turtle.clearscreen()
    # Import and run hero selection
    import hero
    hero.hero_run()

def start_run():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.bgpic("assets/start/start.png")
    screen.onclick(close_and_open)