import pygame
from pygame.sprite import Group
import sys
import time

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from circle import Circle
from rectangle import Rectangle
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Dynamics simulation")
    # rect = Rectangle(ai_settings,screen)
    # pygame.draw.rect(screen, (0,0,255), (100, 200, 100, 100))
    font = pygame.font.Font(None, 36)
    text = font.render("Now create your world", 1, (10, 10, 10))
    textpos = text.get_rect(centerx=screen.get_width()/2)
    g = 300 # 加速度
    clock = pygame.time.Clock()
    circlePosY = 60
    t1 = time.time() # 
    t2 = t1
    velocity = 0

    while True:
        # clock.tick(30)
        # supervise keyboard and mouse item
        # print(t2,velocity)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color) # fill color
        if circlePosY > ai_settings.screen_height:
            velocity = -velocity

        circlePosY = round(circlePosY + (t2 - t1) * velocity)
        pygame.draw.circle(screen, (0, 0, 255), [60, circlePosY], 10)
        t1 = t2 
        t2 = time.time()
        velocity = velocity + g * (t2 - t1)

        # screen.blit(text, textpos) 
        # rect.blitme()
        # visualiaze the window
        pygame.display.flip()
    

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