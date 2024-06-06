import pgzrun

WIDTH, HEIGHT = 640, 480

circle_x, circle_y = WIDTH // 2, HEIGHT // 2
circle_radius = 50

def draw():
    global circle_radius
    screen.clear()
    for i in range (10):
        screen.draw.circle((circle_x, circle_y), circle_radius, 'blue')

        circle_radius += 5
    
pgzrun.go()