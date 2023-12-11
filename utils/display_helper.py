from tabulate import tabulate


class DisplayHelper:

    def display_table(self, headers, rows):
        table = tabulate(rows, headers, tablefmt="grid")
        print(table)

    def display_list(self, color, data):
        for row in data:
            print(color + f'{str(row)}')
