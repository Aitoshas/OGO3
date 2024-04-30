import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("The Game Tir")
icon = pygame.image.load("img/shootphoto.img.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width )
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0,255), random.randint(0,255), random.randint(0, 255))

speed = 1
direction = random.choice(['up', 'down', 'left', 'right'])
fps = 60
frame_count = 0
change_direction_freq = fps * 7
score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1
                print("Score: ", score)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if direction == 'up':
        target_y -= speed
    elif direction == 'down':
        target_y += speed
    elif direction == 'left':
        target_x -= speed
    elif direction == 'right':
        target_x += speed

    frame_count += 1
    if frame_count >= change_direction_freq:
        direction = random.choice(['up', 'down', 'left', 'right'])
        frame_count = 0

    if target_x < 0 or target_x > SCREEN_WIDTH - target_width or target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
        direction = random.choice(['up', 'down', 'left', 'right'])



    screen.blit(target_img, (target_x,target_y))
    pygame.display.update()

pygame.quit()

