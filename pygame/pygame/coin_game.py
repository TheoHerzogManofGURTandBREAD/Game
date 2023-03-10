WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
fox = Actor("fox")
fox.pos = 100, 100

Squid = Actor('character-1')
coin = Actor("coin")
coin.pos = 200, 200
def update():
    Squid.left= Squid.left + 2
    if Squid.left > WIDTH:
        Squid.right= 0
def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

from random import randint
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        fox.x = fox.x - 5
    elif keyboard.right:
        fox.x = fox.x + 5
    elif keyboard.up:
        fox.y = fox.y - 5
    elif keyboard.down:
       fox.y = fox.y + 5
    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()
        sounds.fart.play()


clock.schedule(time_up, 25.0)
place_coin()


