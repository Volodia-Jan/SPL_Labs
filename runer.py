import unittest

from Lab4 import execute_lab4
from Lab5 import execute_lab5
from Lab7 import execute_lab7
from Lab8 import execute_lab8
from utils import UserInputHelper
from Lab1 import execute_lab1
from Lab2 import execute_lab2
from Lab3 import execute_lab3


def choose_program():
    print("Choose a program to run:")
    print("1. Lab1 - Calculator")
    print("2. Lab2 - Calculator (Class-based)")
    print("3. Lab3 - ASCII Art Generator")
    print("4. Lab4 - Custom ASCII Art Generator")
    print("5. Lab5 - 3D ASCII Generator")
    print("6. Lab6 - Unit Test")
    print("7. Lab7 - Dog API Program")
    print("8. Lab8 - Data Visualization")

    choice = UserInputHelper.get_limited_user_input('\n', ['1', '2', '3', '4', '5', '6', '7', '8'])

    if choice == "1":
        execute_lab1()
    elif choice == "2":
        execute_lab2()
    elif choice == "3":
        execute_lab3()
    elif choice == "4":
        execute_lab4()
    elif choice == "5":
        execute_lab5()
    elif choice == "6":
        unittest.main()
    elif choice == "7":
        execute_lab7()
    elif choice == "8":
        execute_lab8()


if __name__ == "__main__":
    choose_program()
