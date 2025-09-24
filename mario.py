import pygame
import sys
# Initialize Pygame
pygame.init()
# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mario Game")
# Load images
mario_img = pygame.image.load('man-with-laptop-presenting-something.jpg')
bg_img = pygame.image.load('man-with-laptop-presenting-something.jpg')
# Mario class
class Mario:
   def __init__(self):
       self.image = mario_img
       self.rect = self.image.get_rect()
       self.rect.x, self.rect.y = 50, WINDOW_HEIGHT - self.rect.height - 50
       self.velocity_y = 0
   def update(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
           self.rect.x -= 5
       if keys[pygame.K_RIGHT]:
           self.rect.x += 5
       if keys[pygame.K_SPACE] and self.rect.bottom >= WINDOW_HEIGHT:
           self.velocity_y = -15
       # Gravity
       self.velocity_y += 1
       if self.velocity_y > 10:
           self.velocity_y = 10
       self.rect.y += self.velocity_y
       # Prevent Mario from falling through the floor
       if self.rect.bottom > WINDOW_HEIGHT:
           self.rect.bottom = WINDOW_HEIGHT
   def draw(self):
       screen.blit(self.image, self.rect)
# Main game loop
def main():
   clock = pygame.time.Clock()
   mario = Mario()
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
       screen.blit(bg_img, (0, 0))
       mario.update()
       mario.draw()
       pygame.display.flip()
       clock.tick(FPS)
if __name__ == "__main__":
   main()
