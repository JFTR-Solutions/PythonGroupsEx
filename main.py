from colorama import init, Fore, Back, Style
import pyfiglet
import pygame
import random


# Initialize colorama
init(autoreset=True)

def main():
    print(Fore.RED + 'This is a red text!')
    print(Back.GREEN + 'This has a green background!')
    print(Fore.BLUE + Back.YELLOW + 'Blue text on yellow background!')
    print(Style.BRIGHT + 'This is bright text!')
    print(Style.DIM + 'This is dim text!')

    # You can also reset to default using
    print(Style.RESET_ALL + 'Back to default.')

if __name__ == '__main__':
  main()

# Create a Figlet font object
font = pyfiglet.Figlet()

# Text to convert to ASCII art
text = "Hello, ASCII Art!"

# Generate the ASCII art
ascii_art = font.renderText(text)

# Print the result
print(ascii_art)



# Initialize pygame
# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 320, 240
CELL_SIZE = 10

# Directions
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = RIGHT

    def move(self):
        head = self.body[0]
        new_head = ((head[0] + self.direction[0]) % (WIDTH // CELL_SIZE), 
                    (head[1] + self.direction[1]) % (HEIGHT // CELL_SIZE))
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        head = self.body[0]
        new_head = ((head[0] + self.direction[0]) % (WIDTH // CELL_SIZE), 
                    (head[1] + self.direction[1]) % (HEIGHT // CELL_SIZE))
        self.body = [new_head] + self.body

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def change_direction(self, new_direction):
        if (new_direction[0], new_direction[1]) != (-self.direction[0], -self.direction[1]):
            self.direction = new_direction

def snakeGame():
    snake = Snake()
    food = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)
                elif event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)

        snake.move()

        # Check collision with food
        if snake.body[0] == food:
            snake.grow()
            food = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))

        # Check collision with self
        if snake.collides_with_self():
            snake = Snake()  # Reset game

        # Drawing
        win.fill(WHITE)
        
        for segment in snake.body:
            pygame.draw.rect(win, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        pygame.draw.rect(win, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


snakeGame()