import pygame
import sys
import time, math
from utils import generateRandomBalls, detectAllImpactAndUpdate, createLocationTable
from settings import Settings
from gui import gui

def run_game(g, ballNum):
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.display)
    surface1 = pygame.Surface(ai_settings.resolution)
    pygame.display.set_caption("Dynamics simulation")
    # rect = Rectangle(ai_settings,screen)
    # pygame.draw.rect(screen, (0,0,255), (100, 200, 100, 100))
    # font = pygame.font.Font(None, 36)
    # text = font.render("Now create your world", 1, (10, 10, 10))
    # textpos = text.get_rect(centerx=screen.get_width()/2)
    # g =  [0, 0] # 加速度
    updateTime = 0.02
    # clock = pygame.time.Clock()
    t1 = time.time() # 
    t2 = t1
    # ball0 = ball.Ball(40, [-100, 0], [600, 600], [0, 255, 0])
    # ball1 = ball.Ball(40, [ 100, 0], [300, 640], [0, 0, 255])
    # balls = [ball0, ball1]

    balls = generateRandomBalls(ballNum, -100, 100, 30, ai_settings.resolution)
    k = 50
    LocationTable = createLocationTable(balls, ai_settings.resolution, k)
    
    while True:
        # clock.tick(30)
        # tic = time.time() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        t2 = time.time()       
        surface1.fill(ai_settings.bg_color) # fill color

        while t2 - t1 > updateTime:
            # tt1 = time.time()
            # tt2 = time.time()

            ## update states of balls in dt.

            ## first update impacts
            detectAllImpactAndUpdate(balls, ai_settings.resolution, k, LocationTable, updateTime)
            for eachBall in balls:
                if eachBall.isImpact == 0:
                    eachBall.update(surface1, g, updateTime)

            ## update balls without impact.
            LocationTable = createLocationTable(balls, ai_settings.resolution, k)

            t1 += updateTime

        ## update draw of balls on the surface. 
        for eachBall in balls:
            location = [int(eachBall.location[0]), int(eachBall.location[1])]
            pygame.draw.circle(surface1, eachBall.color, location, eachBall.radius)
        
        pygame.transform.scale(surface1, ai_settings.display, screen)
        pygame.display.flip()
        # toc = time.time() 
        # print((t2 - t1), toc - tic)



if __name__ == '__main__':
    # g =  [0, 0] # 加速度
    g, ballNum, _, _ = gui()
    run_game(g, ballNum)