import pygame
import assets

#general car class that will be inherited from
class Car:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.car_image = None

    #allows the image to be drawn on screen
    def draw(self, window):
        window.blit(self.car_image, (self.x, self.y))

    #makes it easier to get the width & height of the certain image being used
    def get_width(self):
        return self.car_image.get_width()

    def get_height(self):
        return self.car_image.get_height()

#player class
class Player(Car):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.car_image = assets.main_car
        self.mask = pygame.mask.from_surface(self.car_image)
        #setting the image of the car and masking to remove white space in the asset image

# enemy class that can crash with player
class Hostile(Car):

    #color coding for variety in asset image
    color_dictionary = {"red": (assets.red_car), "green": (assets.green_car), "yellow": (assets.yellow_car)}

    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.car_image = self.color_dictionary[color]
        self.mask = pygame.mask.from_surface(self.car_image)

    #enemies will continually move downwards
    def move(self, speed):
        self.y += speed

# coin class that can be picked up by player

class Coin(Car):
    color_dictionary = {"gold": (assets.gold_coin), "silver": (assets.silver_coin), "bronze": (assets.bronze_coin)}

    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.car_image = self.color_dictionary[color]
        self.mask = pygame.mask.from_surface(self.car_image)

    def move(self, speed):
        self.y += speed