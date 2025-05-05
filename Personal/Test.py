import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PADDLE_COLOR = (50, 50, 50)

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, brick_type="normal"):
        super().__init__()
        self.brick_type = brick_type
        if brick_type == "normal":
            self.image = pygame.Surface((75, 30))
            self.image.fill((200, 50, 50))
        else:
            self.image = pygame.Surface((75, 30))
            self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))

class Paddle(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        super().__init__()
        self.normal_length = 100
        self.long_length = 150
        self.tiny_length = 50
        self.current_length = self.normal_length
        self.image = pygame.Surface((self.current_length, 20))
        self.image.fill(PADDLE_COLOR)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT-30))
        self.speed = 8
        self.shooting = False
        self.powerup_status = None
        self.powerup_start_time = 0
        self.bullets = pygame.sprite.Group()  # Group to manage bullets
        self.all_sprites = all_sprites  # Reference to the all_sprites group

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

        # Check if power-up duration has expired
        if self.powerup_status and pygame.time.get_ticks() - self.powerup_start_time >= 5000:  # 5000ms = 5s
            self.reset_paddle()

        # Update bullets
        self.bullets.update()

        # Draw guns on the paddle if shooting power-up is active
        if self.shooting:
            self.draw_guns()

    def draw_guns(self):
        # Draw two small rectangles (guns) on the paddle
        gun_width = 5
        gun_height = 10
        left_gun_rect = pygame.Rect(self.rect.left + 10, self.rect.top - gun_height, gun_width, gun_height)
        right_gun_rect = pygame.Rect(self.rect.right - 15, self.rect.top - gun_height, gun_width, gun_height)
        pygame.draw.rect(self.image, (0, 0, 0), left_gun_rect)
        pygame.draw.rect(self.image, (0, 0, 0), right_gun_rect)

    def shoot(self):
        if self.shooting:
            # Create bullets at both gun positions
            left_bullet = Bullet(self.rect.left + 10, self.rect.top)
            right_bullet = Bullet(self.rect.right - 10, self.rect.top)
            self.bullets.add(left_bullet, right_bullet)
            self.all_sprites.add(left_bullet, right_bullet)  # Add bullets to all_sprites

    def activate_powerup(self, power_type):
        # Only activate if no power-up is currently active
        if self.powerup_status is None:
            self.powerup_status = power_type
            self.powerup_start_time = pygame.time.get_ticks()

            if power_type == "long":
                self.current_length = self.long_length
            elif power_type == "tiny":
                self.current_length = self.tiny_length
            elif power_type == "shooting":
                self.shooting = True

            self.image = pygame.Surface((self.current_length, 20))
            self.image.fill(PADDLE_COLOR)

    def reset_paddle(self):
        self.current_length = self.normal_length
        self.image = pygame.Surface((self.current_length, 20))
        self.image.fill(PADDLE_COLOR)
        self.shooting = False
        self.powerup_status = None

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed = 5  # Overall speed of the ball
        self.angle = 45  # Initial angle in degrees (e.g., 45 degrees)
        self.dx = self.speed * math.cos(math.radians(self.angle))  # X component
        self.dy = -self.speed * math.sin(math.radians(self.angle))  # Y component (negative because y increases downward)

    def update(self):
        # Update position using dx and dy
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Wall collisions
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx *= -1  # Reverse horizontal direction
        if self.rect.top <= 0:
            self.dy *= -1  # Reverse vertical direction

    def collide_with_brick(self, brick):
        # Calculate overlap on each side
        overlap_left = self.rect.right - brick.rect.left
        overlap_right = brick.rect.right - self.rect.left
        overlap_top = self.rect.bottom - brick.rect.top
        overlap_bottom = brick.rect.bottom - self.rect.top

        # Find the smallest overlap to determine the collision side
        min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

        # Adjust ball direction based on collision side
        if min_overlap == overlap_left:
            self.rect.right = brick.rect.left  # Move ball outside the brick
            self.dx *= -1  # Reverse horizontal direction
        elif min_overlap == overlap_right:
            self.rect.left = brick.rect.right  # Move ball outside the brick
            self.dx *= -1  # Reverse horizontal direction
        elif min_overlap == overlap_top:
            self.rect.bottom = brick.rect.top  # Move ball outside the brick
            self.dy *= -1  # Reverse vertical direction
        elif min_overlap == overlap_bottom:
            self.rect.top = brick.rect.bottom  # Move ball outside the brick
            self.dy *= -1  # Reverse vertical direction

    def set_angle(self, angle):
        """Set the ball's movement angle in degrees."""
        self.angle = angle
        self.dx = self.speed * math.cos(math.radians(self.angle))
        self.dy = -self.speed * math.sin(math.radians(self.angle))  # Negative because y increases downward

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))  # Small bullet size
        self.image.fill((255, 255, 0))  # Yellow color
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10  # Move upward

    def update(self):
        self.rect.y += self.speed  # Move the bullet upward
        if self.rect.bottom < 0:  # Remove bullet if it goes off-screen
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, power_type):
        super().__init__()
        self.power_type = power_type
        self.image = pygame.Surface((15, 15))
        self.image.fill(power_type)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

def main():
    # Sprite groups
    all_sprites = pygame.sprite.Group()
    bricks = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    # Create paddle and ball
    paddle = Paddle(all_sprites)  # Pass all_sprites to the Paddle
    ball = Ball()
    all_sprites.add(paddle, ball)
    balls.add(ball)

    # Brick layout configuration
    row_length = 7      # Bricks per full row
    brick_amount = 37   # Total bricks to place
    brick_spacing = 5   # Space between bricks
    brick_width = 75    # Individual brick width
    brick_height = 30   # Individual brick height
    start_y = 50        # Starting Y position

    # Calculate rows needed
    full_rows = brick_amount // row_length
    remaining_bricks = brick_amount % row_length
    total_rows = full_rows + (1 if remaining_bricks else 0)

    # Create bricks with new layout
    for row in range(total_rows):
        # Determine bricks in this row
        bricks_in_row = row_length if row < full_rows else remaining_bricks
        
        # Calculate row dimensions
        row_width = (bricks_in_row * brick_width) + ((bricks_in_row - 1) * brick_spacing)
        start_x = (WIDTH - row_width) // 2  # Center the row
        
        # Create bricks for this row
        for brick_num in range(bricks_in_row):
            x = start_x + (brick_num * (brick_width + brick_spacing))
            y = start_y + (row * (brick_height + 10))  # 10px vertical spacing
            
            # Create brick (20% chance for unbreakable)
            if random.random() < 0.2:
                brick = Brick(x, y, "unbreakable")
            else:
                brick = Brick(x, y)
                
            bricks.add(brick)
            all_sprites.add(brick)

    # Count normal bricks
    normal_brick_count = sum(1 for brick in bricks if brick.brick_type == "normal")
    running = True
    game_over = False

    while running:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and paddle.shooting:  # Shoot bullets when Space is pressed
                    paddle.shoot()

        if not game_over:
            # Update objects
            paddle.update(keys)
            balls.update()
            powerups.update()

            # Ball-paddle collision
            if pygame.sprite.spritecollide(paddle, balls, False):
                # Calculate the offset from the center of the paddle
                offset = (ball.rect.centerx - paddle.rect.centerx) / (paddle.rect.width / 2)
                
                # Set the new angle based on the offset
                new_angle = 180 - offset * 60  # Adjust the angle range (e.g., 60 degrees)
                
                # Update the ball's direction
                ball.set_angle(new_angle)
                
                # Ensure the ball moves upward
                ball.dy = -abs(ball.dy)

            # Ball-brick collisions
            for brick in pygame.sprite.spritecollide(ball, bricks, False):
                if brick.brick_type == "normal":
                    brick.kill()
                    normal_brick_count -= 1
                    # 25% chance for each power-up type
                    if random.random() < 0.75:  # 75% chance to drop something
                        power_type = random.choice([RED, BLUE, GREEN])
                        powerup = PowerUp(brick.rect.centerx, brick.rect.centery, power_type)
                        powerups.add(powerup)
                        all_sprites.add(powerup)

                ball.collide_with_brick(brick)

            # Bullet-brick collisions
            for bullet in paddle.bullets:
                bricks_hit = pygame.sprite.spritecollide(bullet, bricks, False)
                for brick in bricks_hit:
                    if brick.brick_type == "normal":  # Only break normal bricks
                        brick.kill()
                        normal_brick_count -= 1
                    bullet.kill()  # Remove bullet on collision

            # Power-up collection
            for powerup in pygame.sprite.spritecollide(paddle, powerups, True):
                if paddle.powerup_status is None:  # Only activate if no power-up is active
                    if powerup.power_type == RED:
                        paddle.activate_powerup("long")
                    elif powerup.power_type == BLUE:
                        paddle.activate_powerup("tiny")
                    elif powerup.power_type == GREEN:
                        paddle.activate_powerup("shooting")

            # Win condition
            if normal_brick_count <= 0:
                game_over = True
                print("You Win!")

            # Lose condition
            if ball.rect.bottom > HEIGHT:
                game_over = True
                print("Game Over!")

        # Draw
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()