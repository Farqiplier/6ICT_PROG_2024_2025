import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Bird settings
BIRD_WIDTH = 100
BIRD_HEIGHT = 100
GRAVITY = 1
JUMP_STRENGTH = -15

# Pillar settings
PILLAR_WIDTH = 200
PILLAR_GAP = 400
PILLAR_SPEED = 10
PILLAR_SPAWN_INTERVAL = 950  # Time in milliseconds

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Flappy Bird")

# Load and scale the bird image
bird_image_path = r"C:\Users\TAKR211206\OneDrive - MOSA-RT\2024 - 2025\Prog\6ICT_PROG_2024_2025\Personal\SANDRO.png"
bird_image = pygame.image.load(bird_image_path)
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))

# Bird class
class Bird:
    def __init__(self):
        self.x = SCREEN_WIDTH // 4
        self.y = SCREEN_HEIGHT // 2
        self.width = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.velocity = 0
        self.started = False

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height), 2)

    def update(self):
        if self.started:
            self.velocity += GRAVITY
            self.y += self.velocity

    def jump(self):
        self.velocity = JUMP_STRENGTH
        self.started = True

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# Pillar class
class Pillar:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.gap_y = random.randint(50, SCREEN_HEIGHT - 50 - PILLAR_GAP)
        self.width = PILLAR_WIDTH
        self.gap = PILLAR_GAP
        self.color = RED
        self.top_image = pygame.transform.scale(bird_image, (self.width, self.gap_y))
        self.bottom_image = pygame.transform.scale(bird_image, (self.width, SCREEN_HEIGHT - self.gap_y - self.gap))

    def draw(self):
        screen.blit(self.top_image, (self.x, 0))
        screen.blit(self.bottom_image, (self.x, self.gap_y + self.gap))
        pygame.draw.rect(screen, RED, (self.x, 0, self.width, self.gap_y), 2)
        pygame.draw.rect(screen, RED, (self.x, self.gap_y + self.gap, self.width, SCREEN_HEIGHT - self.gap_y - self.gap), 2)

    def update(self):
        self.x -= PILLAR_SPEED

    def get_rects(self):
        top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        bottom_rect = pygame.Rect(self.x, self.gap_y + self.gap, self.width, SCREEN_HEIGHT - self.gap_y - self.gap)
        return top_rect, bottom_rect

# Function to display the start screen
def start_screen():
    font = pygame.font.Font(None, 74)
    text = font.render("Start", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    button_rect = pygame.Rect(text_rect.left - 20, text_rect.top - 10, text_rect.width + 40, text_rect.height + 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, button_rect)
        screen.blit(text, text_rect)
        pygame.display.flip()

# Function to display the game over screen
def game_over_screen():
    font = pygame.font.Font(None, 74)
    retry_text = font.render("Retry", True, BLACK)
    quit_text = font.render("Quit", True, BLACK)
    retry_rect = retry_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    retry_button_rect = pygame.Rect(retry_rect.left - 20, retry_rect.top - 10, retry_rect.width + 40, retry_rect.height + 20)
    quit_button_rect = pygame.Rect(quit_rect.left - 20, quit_rect.top - 10, quit_rect.width + 40, quit_rect.height + 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button_rect.collidepoint(event.pos):
                    return True
                if quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, retry_button_rect)
        pygame.draw.rect(screen, GREEN, quit_button_rect)
        screen.blit(retry_text, retry_rect)
        screen.blit(quit_text, quit_rect)
        pygame.display.flip()

# Main game loop
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pillars = []
    game_started = False
    last_pillar_spawn_time = pygame.time.get_ticks()

    start_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                    game_started = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        bird.update()

        if game_started:
            current_time = pygame.time.get_ticks()
            if current_time - last_pillar_spawn_time > PILLAR_SPAWN_INTERVAL:
                pillars.append(Pillar())
                last_pillar_spawn_time = current_time

            # Update and draw pillars
            screen.fill(WHITE)
            for pillar in pillars:
                pillar.update()
                pillar.draw()

            # Check for collisions
            bird_rect = bird.get_rect()
            if bird.y > SCREEN_HEIGHT or bird.y < 0:
                if game_over_screen():
                    main()
                else:
                    pygame.quit()
                    sys.exit()
            for pillar in pillars:
                top_rect, bottom_rect = pillar.get_rects()
                if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                    if game_over_screen():
                        main()
                    else:
                        pygame.quit()
                        sys.exit()

            # Remove off-screen pillars
            if pillars and pillars[0].x < -PILLAR_WIDTH:
                pillars.pop(0)

        bird.draw()
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()