import pygame
import os

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

#loading images
red_car = pygame.image.load(os.path.join("assets", "red_car.png"))
green_car = pygame.image.load(os.path.join("assets", "green_car.png"))
yellow_car = pygame.image.load(os.path.join("assets", "yellow_car.png"))

gold_coin = pygame.transform.scale(pygame.image.load(os.path.join("assets", "gold_coin.png")), (32, 32))
silver_coin = pygame.transform.scale(pygame.image.load(os.path.join("assets", "silver_coin.png")), (32, 32))
bronze_coin = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bronze_coin.png")), (32, 32))

main_car = pygame.transform.scale(pygame.image.load(os.path.join("assets", "racer.png")), (48, 96))

background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "road.png")), (700, 800))

#loading sound effects
coin_pickup = pygame.mixer.Sound(os.path.join("assets", "smw_coin.wav"))
coin_pickup.set_volume(0.5)

car_crash = pygame.mixer.Sound(os.path.join("assets", "carcrash.wav"))
car_crash.set_volume(0.5)

game_music = pygame.mixer.Sound(os.path.join("assets", "ikenaiborderline8bit.mp3"))
game_music.set_volume(0.1)

win_music = pygame.mixer.Sound(os.path.join("assets", "win_music.wav"))
win_music.set_volume(0.1)
