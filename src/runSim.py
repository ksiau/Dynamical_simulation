import pygame
# from pygame.sprite import Group
import sys
import time, math

from settings import Settings
# from rectangle import Rectangle
# from game_stats import game_statsts
# from scoreboard import Scoreboard
# from button import Button
# from circle import Circle
# import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.display)
    surface1 = pygame.Surface(ai_settings.resolution)
    surface2 = pygame.Surface(ai_settings.display)
    pygame.display.set_caption("Dynamics simulation")
    # rect = Rectangle(ai_settings,screen)
    # pygame.draw.rect(screen, (0,0,255), (100, 200, 100, 100))
    # font = pygame.font.Font(None, 36)
    # text = font.render("Now create your world", 1, (10, 10, 10))
    # textpos = text.get_rect(centerx=screen.get_width()/2)
    g = 3000 # 加速度
    # clock = pygame.time.Clock()
    circlePosY = 300
    t1 = time.time() # 
    t2 = t1
    velocity = 0
    radius = 40
    while True:
        # clock.tick(30)
        # supervise keyboard and mouse item
        # print(t2,velocity)
        # tic = time.time() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # circlePosY = round(circlePosY + (t2 - t1) * velocity)
        dt = t2 - t1
        ## rebound
        if circlePosY + radius > ai_settings.resolution[1]:
            ds1 = ai_settings.resolution[1] - circlePosY- radius
            dt1 = math.sqrt((velocity/g)**2 + 2*ds1/g) - velocity/g 
            velocity = -(velocity + g*dt1)
            circlePosY = ai_settings.resolution[1] - radius
            dt -= dt1


        circlePosY = circlePosY + velocity*dt + 1/2*g*dt**2
        velocity = velocity + g * dt
        surface1.fill(ai_settings.bg_color) # fill color
        pygame.draw.circle(surface1, (0, 0, 255), [300, round(circlePosY)], radius)
        t1 = t2 
        t2 = time.time()
        # velocity = velocity + g * (t2 - t1)
        # print(pygame.TIMER_RESOLUTION)

        # screen.blit(text, textpos) 
        # rect.blitme()
        # visualiaze the window
        ## resize the resolution into the window
        pygame.transform.scale(surface1, ai_settings.display, surface2)
        screen.blit(surface2, ( (screen.get_size()[0] - surface2.get_size()[0])/2,
                                (screen.get_size()[1] - surface2.get_size()[1])/2)) # Blit main surface on center of display
        pygame.display.flip()
        print(g*(ai_settings.resolution[1] - circlePosY) + 1/2*velocity**2) 
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