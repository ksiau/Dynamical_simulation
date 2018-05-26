import pygame
# from pygame.sprite import Group
import sys
import time, math
import ball

from settings import Settings
from gui import gui
from random import random

def generateBalls(num, maxv, minv, radius, initLocation, resolution):
    if num != len(radius):
        raise Exception('Wrong match of ball number and radius number')
    balls = []
    for i in range(num):
        while 1:
            # location = [resolution[0]*random(), resolution[1]*random()]
            # if location[0] + radius > resolution[0] or location[0] - radius < 0 \
            #     or location[1] + radius > resolution[1] or location[1] - radius < 0: continue
            # sig = 0
            # for eachBall in balls:
            #     if math.sqrt((location[0] - eachBall.location[0])**2 + (location[1] - eachBall.location[1])**2) - radius - eachBall.radius < 0: 
            #         sig = 1
            #         break
            # if sig == 1: continue
            vx = minv + (maxv - minv)*random()
            vy = minv + (maxv - minv)*random()
            balls.append(ball.Ball(radius[i], [vx, vy], initLocation[i], [255*random(), 255*random(), 255*random()]))
            break
    return balls


def run_game(g,ballNum, radius, initLocation):
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.display)
    surface1 = pygame.Surface(ai_settings.resolution)
    pygame.display.set_caption("Dynamics simulation")
    # font = pygame.font.Font(None, 36)
    # text = font.render("Now create your world", 1, (10, 10, 10))
    # textpos = text.get_rect(centerx=screen.get_width()/2)
    # g =  [0, 5000] # 加速度
    # clock = pygame.time.Clock()
    t1 = time.time() # 
    t2 = t1
    # ball0 = ball.Ball(400, [600, -1500], [300, 900], [0, 0, 255])
    # ball1 = ball.Ball(40, [-1000, 0], [600, 300], [0, 255, 0])
    # ball2 = ball.Ball(40, [1500, -2500], [900, 600], [255, 0, 0])
    balls = generateBalls(ballNum, -500, 500, radius, initLocation, ai_settings.resolution)
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
        for eachBall in balls:
            eachBall.update(surface1, g, dt)
        # ball2.update(surface1, g, dt)
        # ball1.update(surface1, g, dt)
        # ball0.update(surface1, g, dt)
        t1 = t2 
        # print(pygame.TIMER_RESOLUTION)

        # screen.blit(text, textpos) 
        # rect.blitme()
        # visualiaze the window
        ## resize the resolution into the window
        for eachBall in balls:
            location = [int(eachBall.location[0]), int(eachBall.location[1])]
            pygame.draw.circle(surface1, eachBall.color, location, eachBall.radius)
 
        pygame.transform.scale(surface1, ai_settings.display, screen)
        # screen.blit(surface2, ( (screen.get_size()[0] - surface2.get_size()[0])/2,
        #                         (screen.get_size()[1] - surface2.get_size()[1])/2)) # Blit main surface on center of display
        pygame.display.flip()
        # print(g[1]*(ai_settings.resolution[1] - ball0.location[1]) + g[0]*(ai_settings.resolution[0] - ball0.location[0]) + 1/2*ball0.velocity[1]**2) 
        # toc = time.time() 
        # print((t2 - t1), toc - tic)


if __name__ == '__main__':
    g, ballNum, radius, initLocation = gui()
    # print(g,type(g))
    run_game(g, ballNum, radius, initLocation)