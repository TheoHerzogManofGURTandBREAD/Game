Squid = Actor('character-1')
Squid.pos = 100, 50

WIDTH = 500
HEIGHT = 300

def draw():
    screen.fill((169,0,0))
    Squid.draw()

def update():
    Squid.left= Squid.left + 2
    if Squid.left > WIDTH:
        Squid.right= 0
