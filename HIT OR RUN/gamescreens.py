import pygame
import time
import assets

#setting screen variables

width,height = 700,800
window = pygame.display.set_mode((width, height))
click = False
FPS = 60
clock = pygame.time.Clock()

#function for drawing text
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("verdana", size)
    text_surface = font.render(text, True, (255,255,255))
    text_rectangle = text_surface.get_rect()
    text_rectangle.midtop = (x,y)
    surface.blit(text_surface, text_rectangle)

#game over/main menu function
def game_over():
    window.blit(assets.background, (0, 0))
    draw_text(window, "HIT OR RUN", 64, width/2, height/4)
    draw_text(window, "WASD to move!", 24, width / 2, height / 2)
    draw_text(window, "Press any key to begin", 24, width / 2, height * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        assets.game_music.stop()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
                assets.game_music.play(-1,0,0)

#win screen that shows up after passing a certain amount of levels
def win_screen():
    assets.game_music.stop()
    assets.win_music.play()
    draw_text(window, "YOU HAVE SUCCESFULLY ESCAPED!", 32, width / 2, height / 2 -50)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
