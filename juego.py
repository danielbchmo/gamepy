#JUST ADD YOUR IMG FOLDER

import pygame
import sys
import random

#Start pygame
pygame.init()

#Configure screen
width, height = 700, 775
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AILOFIU ❤️")

#IMG 
player_image = pygame.image.load("img/marce.png")
player_image = pygame.transform.scale(player_image, (60,60))

bullet_image = pygame.image.load("img/heart.png")
bullet_image = pygame.transform.scale(bullet_image, (50,50))

enemy_image = pygame.image.load("img/brandon.jpeg")
enemy_image = pygame.transform.scale(enemy_image, (60,60))

background_image = pygame.image.load("img/clouds.jpeg")
background_image = pygame.transform.scale(background_image, (width, height))

# player
player_rect = player_image.get_rect()
player_rect.topleft = (width // 2 - player_rect.width // 2, height - player_rect.height - 10)
player_speed = 15

#bullet
bullet_rect = bullet_image.get_rect()
bullet_speed = 10
bullets = []

#Enemy
enemy_rect = enemy_image.get_rect()
enemy_speed = 5
enemies = []

# clock
clock = pygame.time.Clock()

#pressed keys
keys_pressed = {'left': False, 'right': False}

#Main loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    #Player movements
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        keys_pressed['left'] = True
      elif event.key == pygame.K_RIGHT:
        keys_pressed['right'] = True
      elif event.key == pygame.K_SPACE:
        bullet_rect = bullet_image.get_rect()
        bullet = {
          'rect': pygame.Rect(
            player_rect.x +
            player_rect.width//2 -
            bullet_rect.width//2,
            player_rect.y,
            bullet_rect.width,
            bullet_rect.height
          ),
          'image': bullet_image
        }
        bullets.append(bullet)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        keys_pressed['left'] = False
      elif event.key == pygame.K_RIGHT:
        keys_pressed['right'] = False

  #Update player position
  if keys_pressed['left'] and player_rect.left > 0:
    player_rect.x -= player_speed
  if keys_pressed['right'] and player_rect.right < width:
    player_rect.x += player_speed

  #Update bullets position
  for bullet in bullets:
    bullet['rect'].y -= bullet_speed

  #Aleatory enemies
  if random.randint(0,100) < 5:
    enemy_rect = enemy_image.get_rect()
    enemy_rect.x = random.randint(0,width - enemy_rect.width)
    enemies.append(enemy_rect.copy())

  #Update enemies position
  for enemy in enemies:
    enemy.y += enemy_speed

  # Crash between bullets and enemies
  for bullet in bullets:
    for enemy in enemies:
      if enemy.colliderect(bullet['rect']):
        bullets.remove(bullet)
        enemies.remove(enemy)

  #Crash between player and enemies
  for enemy in enemies:
    if player_rect.colliderect(enemy):
      pygame.quit()
      sys.exit()

  #Clear screen with the background
  screen.blit(background_image,(0,0))

  #Print player
  screen.blit(player_image, player_rect)

  #Print bullets
  for bullet in bullets:
    screen.blit(bullet['image'],bullet['rect'].topleft)

  #Print enemies
  for enemy in enemies:
    screen.blit(enemy_image, enemy)

  #Upload screen
  pygame.display.flip()

  #FPS limits
  clock.tick(30)
