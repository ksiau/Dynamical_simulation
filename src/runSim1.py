import pygame
# from pygame.sprite import Group
import sys
import time, math
import ball
from utils import generateRandomBalls, detectAllImpactAndUpdate, createLocationTable
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
    # clock = pygame.time.Clock()
    t1 = time.time() # 
    t2 = t1
    # ball0 = ball.Ball(100, [00, 00], [1800, ai_settings.resolution[1] - 100], [0, 0, 255])
    g =  [1000, 000] # 加速度
    ball1 = ball.Ball(100, [000, 600], [ai_settings.resolution[0] - 300, 100], [0, 255, 255])
    g =  [-1000, 000] # 加速度
    ball1 = ball.Ball(100, [000, 600], [300, 100], [0, 255, 255])
    g =  [000, 1000] # 加速度
    ball1 = ball.Ball(100, [-600, 000], [2300, ai_settings.resolution[1] - 300], [0, 255, 255])
    # ball1 = ball.Ball(40, [-1000, 0], [600, 300], [0, 255, 0]
    # ball2 = ball.Ball(40, [1500, -2500], [900, 600], [255, 0, 0])
    balls = [ball1]
    updateTime = 0.001
    k = 1
    LocationTable = createLocationTable(balls, ai_settings.resolution, k)
    f = 0.1
    fr = 0.05
    e = 0.9
    while True:
        # print(t2,velocity)
        # tic = time.time()
        # print(ball0.velocity, ball0.state.bits)
        # print(ball1.velocity, ball1.state.bits)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        surface1.fill(ai_settings.bg_color) # fill color
        t2 = time.time()

        while t2 - t1 > updateTime:
            detectAllImpactAndUpdate(balls, ai_settings.resolution, k, LocationTable, updateTime, g, e=e, f=f)
            # print(1, ball0.location, ball0.velocity, ball0.isImpact, ball0.state.bits)
            # print(ball1.angVelocity, ball1.radian)
            for eachBall in balls:
                if eachBall.isImpact == 0:
                    eachBall.update(surface1, g, updateTime, f=f, fr=fr, e=e)
                eachBall.updateRadian(updateTime)

            # print(2, ball0.location, ball0.velocity, ball0.isImpact, ball0.state.bits)
            LocationTable = createLocationTable(balls, ai_settings.resolution, k)
            t1 += updateTime
            


        ## update states of balls in dt. ball0.velocity,
        # ball2.update(surface1, g, dt, f=0.1, e=0.9)
        # ball1.update(surface1, g, dt, f=0.1, e=0.9)
        # print(pygame.TIMER_RESOLUTION)

        
        ## update draw of balls
        for eachBall in balls:
            eachBall.draw(surface1)
            # location = [int(eachBall.location[0]), int(eachBall.location[1])]
            # pygame.draw.circle(surface1, eachBall.color, location, eachBall.radius)
        
        pygame.transform.scale(surface1, ai_settings.display, screen)
        pygame.display.flip()
        # toc = time.time() 
        # print((t2 - t1), toc - tic)


if __name__ == '__main__':
    run_game()