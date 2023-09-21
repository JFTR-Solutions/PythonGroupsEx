from colorama import init, Fore, Back, Style
import pyfiglet

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
