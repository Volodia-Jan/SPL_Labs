import logging

from tabulate import tabulate


# Class that helps represent data
class DisplayHelper:

    # Display content as table
    def display_table(self, headers, rows):
        logging.info('Displays data in table')
        table = tabulate(rows, headers, tablefmt="grid")
        print(table)

    # Displays content as list
    def display_list(self, color, data):
        logging.info('Displays data in list')
        for row in data:
            print(color + f'{str(row)}')
