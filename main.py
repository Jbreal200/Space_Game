import pygame
import math
import random
from pygame import mixer
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Gravity Simulation")

font = pygame.font.Font(None, 50)
label_font = pygame.font.Font(None, 20)

PLANET_MASS = 200
OBJECT_MASS = 5
G = 5
FPS = 60
PLANET_SIZE = 50
OBJECT_SIZE = 8
VELOCITY_SCALE = 100

mixer.init()
mixer.music.load('Music.wav')
mixer.music.play()

LABEL_COLOR = (0, 255, 0)

current_trail_color = (0, 0, 255)
alternate_trail_color = (0, 255, 0)
use_alternate_color = False
color_change_interval = 10 
TRAIL_LENGTH = 1
DISPLAY_DURATION = 2


BG = pygame.transform.scale(pygame.image.load("Background.jpg"), (WIDTH, HEIGHT))
PLANET =  pygame.transform.scale(pygame.image.load("Earth.png"), (PLANET_SIZE * 2, PLANET_SIZE* 2))

WHITE = (255, 255, 255)
RED  = (255, 0, 0)
BLUE = (0, 0, 255)

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y =y
        self.mass = mass

    def draw(self):
        win.blit(PLANET, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))

class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass, label, image_path, scale_factor):
        self.x = x
        self.y =y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass
        self.label = label
        self.trail = []
        self.creation_time = pygame.time.get_ticks()
        original_image = pygame.image.load(image_path)

        self.show_label = False
        self.label_display_time = 0

        self.trail_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


        self.image = pygame.transform.scale(original_image, (int(original_image.get_width() * scale_factor),int(original_image.get_height() * scale_factor)))
    
    def move(self, planet = None):
        distance = math.sqrt((self.x - planet.x)**2 + (self.y - planet.y)**2)
        force = (G * self.mass * planet.mass) / distance **2 
        acceleration = force / self.mass
        angle = math.atan2(planet.y - self.y, planet.x - self.x)
        acceleration_x = acceleration * math.cos(angle)
        acceleration_y = acceleration * math.sin(angle)

        self.vel_x += acceleration_x
        self.vel_y += acceleration_y

        self.x += self.vel_x
        self.y += self.vel_y
        self.trail.append((int(self.x), int(self.y)))
        #print(acceleration)


    def draw(self, font):
        image_rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        win.blit(self.image, image_rect)

        if self.show_label:
            label_surface = label_font.render("IN ORBIT", True, LABEL_COLOR)
            label_rect = label_surface.get_rect(center=(self.x, self.y + 15))
            win.blit(label_surface, label_rect)

        for i in range(len(self.trail) - 1):
            pygame.draw.line(win, self.trail_color, self.trail[i], self.trail[i + 1], 2)

def create_ship(location, mouse):
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VELOCITY_SCALE
    vel_y = (m_y - t_y) / VELOCITY_SCALE
    obj = Spacecraft(t_x, t_y, vel_x, vel_y, OBJECT_MASS,"Object","rocket.png",0.01)
    return obj


def printing():
    print("One of your objects is in orbit")

def main():

    

    #global current_trail_color, use_alternate_color, orbit_trail_color
    running = True
    clock = pygame.time.Clock()
    frame_counter = 0


    planet = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS)
    objects = []
    temp_obj_pos = None

    display_timer = 0

    while running:
        clock.tick(FPS)


        mouse_pos = pygame.mouse.get_pos()
        frame_counter += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None
                    print("Object has enetred the zone")
                else:
                    temp_obj_pos = mouse_pos
            



        win.blit(BG, (0,0))

        if temp_obj_pos:
            pygame.draw.line(win, WHITE, temp_obj_pos, mouse_pos,2)
            pygame.draw.circle(win, RED, temp_obj_pos, OBJECT_SIZE)

        for obj in objects[:]:
            obj.draw(font)
            obj.move(planet)
            off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT
            on_screen= obj.x > 0 or obj.x < WIDTH or obj.y > 0 or obj.y < HEIGHT
            current_time = pygame.time.get_ticks()
            on_screen_duration = (current_time - obj.creation_time) // 1000


            collided = math.sqrt((obj.x - planet.x)**2 +(obj.y-planet.y)**2) <= PLANET_SIZE
            if off_screen or collided:
                    objects.remove(obj)
            if collided:
                text = font.render(f"CRASHED ", True, (255, 255, 255))
                text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
                win.blit(text, text_rect)            
            if off_screen:
                text = font.render(f"LOST IN SPACE ", True, (255, 255, 255))
                text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
                win.blit(text, text_rect)
            if on_screen_duration > 8:
                obj.show_label = True
        planet.draw()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()