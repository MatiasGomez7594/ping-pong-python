import pygame, sys, random
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
size = (800,500)

player_width = 15
player_height = 90


screen = pygame.display.set_mode(size)


clock = pygame.time.Clock()

#coordenadas player1 y player2
player1_x = 50
player1_y = 300-45
player1_speed_y = 0

player2_x = 750
player2_y = 300-45
player2_speed_y = 0
game_over = False

#coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed_y = -3
            if event.key == pygame.K_s:
                player1_speed_y = 3                
            if event.key == pygame.K_UP:
                    player2_speed_y = -3
            if event.key == pygame.K_DOWN:
                    player2_speed_y = 3
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_speed_y = 0
            if event.key == pygame.K_s:
                player1_speed_y = 0      
    
            if event.key == pygame.K_UP:
                player2_speed_y = 0
            if event.key == pygame.K_DOWN:
                player2_speed_y = 0
    #para que la pelota revote arriba y abajo
    if pelota_y > 500 or pelota_y < 10:
        pelota_speed_y *= -1
    #revisa si la pelota sale por los costados
    if pelota_x > 800 or pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        #si sale de la pantalla, invierte la direccion
        pelota_speed_x *= -1
        pelota_speed_y *= -1

        
    #para que se muevan los objetos
    player1_y += player1_speed_y
    player2_y += player2_speed_y
    #movimiento de la pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y
    
            
    screen.fill(BLACK)
    #aca creo las paletas y la pelota
    player1 = pygame.draw.rect(screen,RED,(player1_x,player1_y,player_width,player_height))
    player2 = pygame.draw.rect(screen,RED,(player2_x,player2_y,player_width,player_height))
    pelota = pygame.draw.circle(screen,WHITE,(pelota_x,pelota_y),10)

    #colisiones
    if pelota.colliderect(player1) or pelota.colliderect(player2):
        pelota_speed_x *=-1
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    
