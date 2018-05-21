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
        ball2.update(surface1, g, dt)
        ball1.update(surface1, g, dt)
        ball0.update(surface1, g, dt)
        t1 = t2 
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