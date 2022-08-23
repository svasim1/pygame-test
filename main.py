#Imports
import pygame
import os

pygame.init()

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (54, 236, 189)
GRAY = (64, 64, 64)

#Images
ICON = pygame.image.load(os.path.join("Assets", "icon.png"))
COOL = pygame.image.load(os.path.join("Assets", "cool.jpg"))
CAR1_IMG = pygame.image.load(os.path.join("Assets", "car1_sprite.png"))
CAR2_IMG = pygame.image.load(os.path.join("Assets", "car2_sprite.png"))

#Characters
CHARACTER_WIDTH = 252
CHARACTER_HEIGHT = 86

#Sounds
THROTTLE = pygame.mixer.Sound(os.path.join("Assets", "throttle.wav"))

#Window
WIDTH, HEIGHT = 1280, 720
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("USSPCS: Ultimate Super Supercar Policecar Chase Simulator Game of The Year Deluxe Edition")
pygame.display.set_icon(ICON)

FPS = 60
VEL = 3

#Render
def draw_window(CAR1_RECT, CAR2_RECT, CAR1, CAR2):
    WIN.fill(GRAY)
    WIN.blit(CAR1, (CAR1_RECT.x, CAR1_RECT.y)) #Draw CAR1
    WIN.blit(CAR2, (CAR2_RECT.x, CAR2_RECT.y)) #Draw CAR2
    pygame.display.update()

#Game
def main():
    CAR1_RECT = pygame.Rect(300, 100, CHARACTER_WIDTH, CHARACTER_HEIGHT) #CAR1 Hitbox
    CAR2_RECT = pygame.Rect(300, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT) #CAR2 Hitbox
    
    CAR1 = pygame.transform.scale(CAR1_IMG, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    CAR2 = pygame.transform.scale(CAR2_IMG, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    
    CAR1_FLIP = False
    CAR2_FLIP = False
    
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get(): #Shutdown when clicking the X
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN: #Shutdown with ESC
                    
                match event.key:
                    case pygame.K_a:
                        break
                    
                    case pygame.K_ESCAPE:
                        running = False
                                
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]: #CAR1 Go left
            CAR1_RECT.x -= VEL
            if not CAR1_FLIP:
                CAR1_FLIP = True
                CAR1 = pygame.transform.flip(CAR1, True, False)

        if key_pressed[pygame.K_d]: #CAR1 Go right
            CAR1_RECT.x += VEL
            if CAR1_FLIP:
                CAR1_FLIP = False
                CAR1 = pygame.transform.flip(CAR1, True, False)

        if key_pressed[pygame.K_w]: #CAR1 Go up
            CAR1_RECT.y -= VEL
            

        if key_pressed[pygame.K_s]: #CAR1 Go down
            CAR1_RECT.y += VEL
            
        if key_pressed[pygame.K_LEFT]: #CAR2 Go left
            CAR2_RECT.x -= VEL
            if not CAR2_FLIP:
                CAR2_FLIP = True
                CAR2 = pygame.transform.flip(CAR2, True, False)

        if key_pressed[pygame.K_RIGHT]: #CAR2 Go right
            CAR2_RECT.x += VEL
            if CAR2_FLIP:
                CAR2_FLIP = False
                CAR2 = pygame.transform.flip(CAR2, True, False)

        if key_pressed[pygame.K_UP]: #CAR2 Go up
            CAR2_RECT.y -= VEL

        if key_pressed[pygame.K_DOWN]: #CAR2 Go down
            CAR2_RECT.y += VEL
        
        draw_window(CAR1_RECT, CAR2_RECT, CAR1, CAR2)
                
    pygame.quit()
    
if __name__ == "__main__":
    main()