class CalculationSettings:

    def __init__(self, digits_after_point=2):
        self.__digits_after_point = digits_after_point

    def settings_interface(self):
        flag = True
        while flag:
            option = int(input("Enter setting option:\n1 - change number of digits after point\n"
                               "0 - exit\n"))
            if option == 1:
                digits = int(input("Enter number of digits\n"))
                self.digits_after_point = digits
            elif option == 0:
                flag = False
            else:
                print("Invalid option entered")
                flag = False

    @property
    def digits_after_point(self):
        return self.__digits_after_point

    @digits_after_point.setter
    def digits_after_point(self, value):
        if type(value) != int:
            print("Value should be integer")
        elif value < 0:
            print("You cannot set value smaller then 0")
        else:
            self.__digits_after_point = value
