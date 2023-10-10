from calculator import ModernCalculator


def main():
    valid_operators = ['+', '-', '*', '/', '^', '%', 'sqrt']
    calc = ModernCalculator(valid_operators)
    calc.do_operation()


if __name__ == '__main__':
    main()
