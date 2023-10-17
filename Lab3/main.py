import pyfiglet


def main():
    user_input = input("Enter a word or phrase to convert to ASCII art: ")
    print("User input:", user_input)
    font_list = pyfiglet.FigletFont.getFonts()
    print("Available fonts:")
    for font in font_list:
        print(font)

    font_choice = input("Choose a font from the list above: ")
    ascii_art = pyfiglet.figlet_format(user_input, font=font_choice)
    print(ascii_art)


if __name__ == '__main__':
    main()
