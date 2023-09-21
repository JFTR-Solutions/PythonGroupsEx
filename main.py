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
pygame.init()

# Set up display
WIDTH, HEIGHT = 300, 200
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot Machine")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Symbols represented as colors
symbols = [RED, GREEN, BLUE, YELLOW]

def spin_slot_machine():
    return [random.choice(symbols) for _ in range(3)]

def game():
    run = True
    spin_result = [WHITE, WHITE, WHITE]
    
    while run:
        win.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                spin_result = spin_slot_machine()

        for i, color in enumerate(spin_result):
            pygame.draw.circle(win, color, (i * 100 + 50, HEIGHT // 2), 40)

        pygame.display.flip()

    pygame.quit()

game()