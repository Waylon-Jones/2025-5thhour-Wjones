import pygame
import sys
import random

# Settings
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Fortnite Prototype")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.health = 100

    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            self.rect.y += PLAYER_SPEED
        if keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED

        # Keep player on screen
        self.rect.clamp_ip(screen.get_rect())

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        super().__init__()
        self.image = pygame.Surface((10, 4))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction

    def update(self):
        self.rect.x += BULLET_SPEED * self.direction[0]
        self.rect.y += BULLET_SPEED * self.direction[1]
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        self.health = 50

    def update(self, player_pos):
        # Simple chasing behavior
        if self.rect.x < player_pos[0]:
            self.rect.x += ENEMY_SPEED
        if self.rect.x > player_pos[0]:
            self.rect.x -= ENEMY_SPEED
        if self.rect.y < player_pos[1]:
            self.rect.y += ENEMY_SPEED
        if self.rect.y > player_pos[1]:
            self.rect.y -= ENEMY_SPEED

def main():
    player = Player()
    player_group = pygame.sprite.Group(player)

    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # Spawn some enemies
    for _ in range(5):
        enemies.add(Enemy())

    running = True
    while running:
        clock.tick(60)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Shoot bullet toward mouse
                mx, my = pygame.mouse.get_pos()
                px, py = player.rect.center
                dx, dy = mx - px, my - py
                dist = (dx**2 + dy**2) ** 0.5
                direction = (dx/dist, dy/dist)
                bullet = Bullet(player.rect.center, direction)
                bullets.add(bullet)

        player_group.update(keys)
        bullets.update()
        enemies.update(player.rect.center)

        # Bullet hits enemy
        for bullet in bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, enemies, False)
            for enemy in hit_enemies:
                enemy.health -= 25
                bullet.kill()
                if enemy.health <= 0:
                    enemy.kill()

        # Enemy hits player
        if pygame.sprite.spritecollide(player, enemies, False):
            player.health -= 1
            if player.health <= 0:
                print("Game Over!")
                running = False

        # Drawing
        screen.fill(BLACK)
        player_group.draw(screen)
        bullets.draw(screen)
        enemies.draw(screen)

        # Draw health bar
        pygame.draw.rect(screen, RED, (10, 10, 100, 20))
        pygame.draw.rect(screen, GREEN, (10, 10, player.health, 20))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
