import pygame
# from pygame.sprite import Group
import sys
import time, math
import ball

from settings import Settings




def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.display)
    surface1 = pygame.Surface(ai_settings.resolution)
    pygame.display.set_caption("Dynamics simulation")
    # font = pygame.font.Font(None, 36)
    # text = font.render("Now create your world", 1, (10, 10, 10))
    # textpos = text.get_rect(centerx=screen.get_width()/2)
    g =  [0, 5000] # 加速度
    # clock = pygame.time.Clock()
    t1 = time.time() # 
    t2 = t1
    ball0 = ball.Ball(400, [600, -1500], [300, 900], [0, 0, 255])
    ball1 = ball.Ball(40, [-1000, 0], [600, 300], [0, 255, 0])
    ball2 = ball.Ball(40, [1500, -2500], [900, 600], [255, 0, 0])
    balls = [ball0, ball1, ball2]
    while True:
        # clock.tick(30)
        # supervise keyboard and mouse item
        # print(t2,velocity)
        # tic = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        t2 = time.time()
        dt = t2 - t1
        surface1.fill(ai_settings.bg_color) # fill color

        ## update states of balls in dt.
        ball2.update(surface1, g, dt)
        ball1.update(surface1, g, dt)
        ball0.update(surface1, g, dt)
        t1 = t2 
        # print(pygame.TIMER_RESOLUTION)

        
        ## update draw of balls
        for eachBall in balls:
            location = [int(eachBall.location[0]), int(eachBall.location[1])]
            pygame.draw.circle(surface1, eachBall.color, location, eachBall.radius)
        
        pygame.transform.scale(surface1, ai_settings.display, screen)

        pygame.display.flip()
        # toc = time.time() 
        # print((t2 - t1), toc - tic)


if __name__ == '__main__':
    run_game()