# ใช้คำสั่ง pip install pygame เพื่อติดตั้งไลบรารี pygame ก่อนรันโค้ดนี้

import pygame
import sys

# เริ่มต้น pygame
pygame.init()

# ขนาดหน้าจอ
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter - ดอกจัน")

# สี
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# กำหนด clock
clock = pygame.time.Clock()

# ยานอวกาศ
ship_width, ship_height = 40, 20
ship_x = WIDTH // 2
ship_y = HEIGHT - 50
ship_speed = 5

# กระสุน
bullets = []
bullet_speed = 7
font = pygame.font.SysFont("Arial", 20)

# loop เกม
running = True
while running:
    clock.tick(30)  # FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # กดปุ่ม
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_x > 0:
        ship_x -= ship_speed
    if keys[pygame.K_RIGHT] and ship_x < WIDTH - ship_width:
        ship_x += ship_speed
    if keys[pygame.K_SPACE]:
        # เพิ่มกระสุนใหม่
        bullets.append([ship_x + ship_width//2, ship_y])
    
    # อัพเดทกระสุน
    for bullet in bullets:
        bullet[1] -= bullet_speed
    
    # ลบกระสุนที่ออกนอกจอ
    bullets = [b for b in bullets if b[1] > 0]
    
    # วาดหน้าจอ
    screen.fill(BLACK)
    
    # วาดยาน
    pygame.draw.rect(screen, WHITE, (ship_x, ship_y, ship_width, ship_height))
    
    # วาดกระสุนเป็นดอกจัน
    for bullet in bullets:
        text = font.render("*", True, WHITE)
        screen.blit(text, (bullet[0], bullet[1]))
    
    pygame.display.flip()

pygame.quit()
sys.exit()

