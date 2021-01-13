import pygame
import os
import time
import random
import assets
import classes
import gamescreens

#setting up pygamae window and variables
pygame.init()
pygame.font.init()
pygame.display.set_caption("HIT OR RUN")
width,height = 700,800
window = pygame.display.set_mode((width, height))
click = False
FPS = 60
clock = pygame.time.Clock()

def game():

    run = True
    lost = True

    # function for detecting collision between overlapping objects
    def collide(object1, object2):
        offset_x = object2.x - object1.x
        offset_y = object2.y - object1.y
        return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None

    # game variables that need to be reset each playthrough
    while run:
        clock.tick(FPS)
        if lost:
            gamescreens.game_over()
            lost = False
            level = 1
            score = 0
            coinscore = 0
            player = classes.Player(350, 650)
            hostiles = []
            coins = []
            enemy_per_wave = 8
            coin_per_wave = 6
            minimum_coins = 8


        def draw_stats():
            # setting background and fonts
            window.blit(assets.background, (0, 0))
            main_font = pygame.font.SysFont("verdana", 25, 1)
            lost_font = pygame.font.SysFont("verdana", 45, 1)

            # displaying score and level on screen
            score_text = main_font.render(f"Cars dodged: {score}", 1, (255, 255, 255))
            level_text = main_font.render(f"Level: {level}", 1, (255, 255, 255))
            coin_text = main_font.render(f"Coins: {coinscore}", 1, (255, 255, 255))
            window.blit(score_text, (10, 10))
            window.blit(coin_text, (10, 50))
            window.blit(level_text, (width - level_text.get_width() - 10, 10))

            #drawing ALL images
            for enemy in hostiles:
                enemy.draw(window)
                for coin in coins:
                    coin.draw(window)
                    if collide(coin,enemy):
                        coins.remove(coin)
                    #checks if coin is colliding with enemy, remove if true

            player.draw(window)

            #updating lost screen if game is lost
            if lost:
                lost_text = lost_font.render("You have crashed!", 1, (255, 255, 255))
                window.blit(lost_text, (175, 325))

            pygame.display.update()

        draw_stats()

        #spawning enemies in waves
        spawnxaxis = [120, 265, 395, 545]

        if len(hostiles) == 0:

            for i in range(enemy_per_wave):
                enemy = classes.Hostile(random.choice(spawnxaxis),random.randrange(-8000*level/5,-100), random.choice(["red", "green", "yellow"]))
                    #spawns enemies in a randomized set x axis and spawns them in a randomized y axis away from each other
                hostiles.append(enemy)


        if len(coins) == 0:
            for i in range(coin_per_wave):
                coin = classes.Coin(random.choice(spawnxaxis),random.randrange(-10000*level/5,-100), random.choice(["bronze", "silver", "gold"]))
                coins.append(coin)

        #puts a minimum amount of coins needed to collect to advance to the next level
        if coinscore >= minimum_coins:
            level += 1
            minimum_coins += 8
            enemy_per_wave += 6
            coin_per_wave += 4

        #showing win scresen when passing level 10
        if level == 11:
            gamescreens.win_screen()

        #closing the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # setting keyboard movement controls
        player_speed = 8
        other_speed = 7
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x + player_speed > 15:
            player.x -= player_speed
        if keys[pygame.K_d] and player.x + player_speed + player.get_width() < width:
            player.x += player_speed
        if keys[pygame.K_w] and player.y - player_speed > 0:
            player.y -= player_speed
        if keys[pygame.K_s] and player.y + player_speed + player.get_height() < height:
            player.y += player_speed

        #enemy movement
        for enemy in hostiles[:]:
            enemy.move(other_speed)
            if enemy.y + enemy.get_height() > height + 125:
                score += 1
                hostiles.remove(enemy)
            #collision with enemies causes the game to lose
            if collide(enemy, player):
                assets.car_crash.play()
                lost = True
                hostiles.remove(enemy)

        for coin in coins[:]:
            coin.move(other_speed)
            if coin.y + coin.get_height() > height + 50:
                coins.remove(coin)
            #picking up coins add to your coin score
            if collide(coin, player):
                coins.remove(coin)
                coinscore += 1
                assets.coin_pickup.play()




game()
