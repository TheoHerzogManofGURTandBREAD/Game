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
def on_mouse_down(pos):
    if Squid.collidepoint(pos):
        print("Yuhhhhh")
    if Squid.collidepoint(pos):
        set_Squid_hurt()
    else:
        print("You missed me!")
    if Squid.collidepoint(pos):
        sounds.eep.play()





def set_Squid_hurt():
    Squid.image = 'character-2'
    clock.schedule_unique(set_Squid_normal, 1.0)


def set_Squid_normal():
    Squid.image = 'character-1'
