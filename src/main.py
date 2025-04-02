from pygame import QUIT, Clock, display, event, init, quit

WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 600
FPS = 60
is_running = True

init()

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Simple Pygame 3D Projection")

clock = Clock()
while is_running:
    # set the frame rate
    clock.tick(FPS)
    # clear the screen
    screen.fill(WHITE)

    # handle GUI events
    for e in event.get():
        if e.type == QUIT:
            is_running = False

    # update the full display Surface to the screen
    display.flip()


quit()
