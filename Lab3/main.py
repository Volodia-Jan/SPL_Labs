import pyfiglet


def main():
    user_input = input("Введіть слово або фразу: ")
    ascii_art = pyfiglet.figlet_format(user_input)
    print(ascii_art)


if __name__ == '__main__':
    main()
