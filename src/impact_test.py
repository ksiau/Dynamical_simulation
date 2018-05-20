import pygame
# from pygame.sprite import Group
import sys
import time, math
import ball

from settings import Settings
# from rectangle import Rectangle
# from game_stats import game_statsts
# from scoreboard import Scoreboard
# from button import Button
# from circle import Circle
# import game_functions as gf


def impact(ball1, ball2, dt):
    v1  = (ball1.location[0] - ball2.location[0], ball1.location[1] - ball2.location[1])
    v2 = (ball1.velocity[0] - ball2.velocity[0], ball1.velocity[1] - ball2.velocity[1])
    dis = math.sqrt(v1[0]**2 + v1[1]**2)
    velocity = math.sqrt(v2[0]**2 + v2[1]**2)
    cs = (v1[0]*v2[0] + v1[1]*v2[1])/dis/velocity
    # print(cs)
    if cs >= 0: return 0
    error = 0.0001
    # print(math.sqrt(1 - (cs + error)**2)*dis)
    if math.sqrt(1 - (cs + error)**2)*dis - ball1.radius - ball2.radius > 0: return 0
    dt1 = (dis - ball1.radius - ball2.radius)*-cs/velocity
    # print(1)
    # print(dis, cs, velocity, dt1)
    if dt1 > dt:
        return 0
    ball1.location[0] += ball1.velocity[0]*dt
    ball1.location[1] += ball1.velocity[1]*dt
    ball2.location[0] += ball2.velocity[0]*dt
    ball2.location[1] += ball2.velocity[1]*dt
    dt2 = dt - dt1
    v1  = (ball1.location[0] - ball2.location[0], ball1.location[1] - ball2.location[1])
    dis = math.sqrt(v1[0]**2 + v1[1]**2)
    # print(dis, ball1.radius + ball2.radius)
    dvscale = (v1[0]*v2[0] + v1[1]*v2[1])/dis
    dv = (-dvscale*v1[0]/dis, -dvscale*v1[1]/dis)
    ball1.velocity[0] += dv[0]
    ball1.velocity[1] += dv[1]
    ball2.velocity[0] -= dv[0]
    ball2.velocity[1] -= dv[1]
    ball1.velocity[0] += ball1.velocity[0]*dt2
    ball1.location[1] += ball1.velocity[1]*dt2
    ball2.location[0] += ball2.velocity[0]*dt2
    ball2.location[1] += ball2.velocity[1]*dt2
    # print(ball2.velocity)
    # print(v2, dvscale, dv)

    return 1







def run_game():
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
    g =  [0, 0] # 加速度
    updateTime = 0.001
    # clock = pygame.time.Clock()
    t1 = time.time() # 
    t2 = t1
    ball0 = ball.Ball(40, [-100, 0], [600, 600], [0, 255, 0])
    ball1 = ball.Ball(40, [ 100, 0], [300, 640], [0, 0, 255])
    while True:
        # clock.tick(30)
        # supervise keyboard and mouse item
        # print(t2,velocity)
        # tic = time.time() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # circlePosY = round(circlePosY + (t2 - t1) * velocity)
        t2 = time.time()       
        surface1.fill(ai_settings.bg_color) # fill color

        while t2 - t1 > updateTime:
            isImpact = impact(ball0, ball1, updateTime)
            # print(isImpact)
            if not isImpact:
                ball1.update(surface1, g, updateTime)
                ball0.update(surface1, g, updateTime)
            else:
                ball1.update(surface1, g, 0)
                ball0.update(surface1, g, 0)

            t1 += updateTime
        # velocity = velocity + g * (t2 - t1)
        # print(pygame.TIMER_RESOLUTION)

        # screen.blit(text, textpos) 
        # rect.blitme()
        # visualiaze the window
        ## resize the resolution into the window
        pygame.transform.scale(surface1, ai_settings.display, screen)
        # screen.blit(surface2, ( (screen.get_size()[0] - surface2.get_size()[0])/2,
        #                         (screen.get_size()[1] - surface2.get_size()[1])/2)) # Blit main surface on center of display
        pygame.display.flip()
        # print(g[1]*(ai_settings.resolution[1] - ball0.location[1]) + g[0]*(ai_settings.resolution[0] - ball0.location[0]) + 1/2*ball0.velocity[1]**2) 
        # toc = time.time() 
        # print((t2 - t1), toc - tic)


    #############
    # # Make the Play button.
    # play_button = Button(ai_settings, screen, "Play")
    
    # # Create an instance to store game statistics, and a scoreboard.
    # stats = GameStats(ai_settings)
    # sb = Scoreboard(ai_settings, screen, stats)
    
    
    # # Make a ship, a group of bullets, and a group of aliens.
    # ship = Ship(ai_settings, screen)
    # bullets = Group()
    # aliens = Group()
    
    # # Create the fleet of aliens.
    # gf.create_fleet(ai_settings, screen, ship, aliens)

    # # Start the main loop for the game.
    # while True:
    #     gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
    #         aliens, bullets)
        
    #     if stats.game_active:
    #         ship.update()
    #         gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
    #             bullets)
    #         gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
    #             bullets)
        
    #     gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
    #         bullets, play_button)


if __name__ == '__main__':
    run_game()