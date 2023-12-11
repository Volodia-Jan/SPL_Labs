import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


class MonthlyFinancialAnalyzer:
    def __init__(self, csv_file_path):
        self.df = pd.read_csv(csv_file_path)

    def explore_monthly_financial_data(self):
        min_values = self.df.min()
        max_values = self.df.max()

        print("Minimum values:")
        print(min_values)

        print("\nMaximum values:")
        print(max_values)

    def plot_total_income_distribution(self):
        total_income_distribution = self.df
        total_income_distribution.plot(kind='pie', y='Total_Income', autopct='%1.1f%%',
                                       title='Total Income Distribution')
        plt.show()

    def plot_expenses_distribution(self):
        expenses_distribution = self.df
        expenses_distribution.plot(kind='bar', x='Month', y='Expenses',
                                   xlabel='Month', ylabel='Expenses (Dollars)', title='Monthly Expenses Distribution')
        plt.show()

    def plot_profit_distribution(self):
        profit_distribution = self.df
        profit_distribution.plot(kind='bar', x='Month', y='Profit',
                                 xlabel='Month', ylabel='Profit (Dollars)', title='Monthly Profit Distribution')
        plt.show()

    def show_all_monthly_plots(self):
        # Matplotlib Subplots
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))

        # Pie chart - Total Income Distribution
        self.plot_total_income_distribution_subplot(axes[0, 0])

        # Bar chart - Expenses Distribution
        self.plot_expenses_distribution_subplot(axes[0, 1])

        # Bar chart - Profit Distribution
        self.plot_profit_distribution_subplot(axes[1, 0])

        # Remove empty subplot
        plt.delaxes(axes[1, 1])

        # Adjust subplot spacing
        plt.subplots_adjust(wspace=0.5, hspace=0.5)

        # Save plots in PNG
        plt.savefig('files/monthly_plot.png')

        # Plotly Bar chart
        self.plot_expenses_distribution_plotly()

        plt.show()

    def plot_total_income_distribution_subplot(self, ax):
        total_income_distribution = self.df
        ax.pie(total_income_distribution['Total_Income'], autopct='%1.1f%%',
               labels=total_income_distribution['Month'], startangle=90)
        ax.set_title('Total Income Distribution')

    def plot_expenses_distribution_subplot(self, ax):
        expenses_distribution = self.df
        ax.bar(expenses_distribution['Month'], expenses_distribution['Expenses'])
        ax.set_xlabel('Month')
        ax.set_ylabel('Expenses (Dollars)')
        ax.set_title('Monthly Expenses Distribution')

    def plot_profit_distribution_subplot(self, ax):
        profit_distribution = self.df
        ax.bar(profit_distribution['Month'], profit_distribution['Profit'])
        ax.set_xlabel('Month')
        ax.set_ylabel('Profit (Dollars)')
        ax.set_title('Monthly Profit Distribution')

    def plot_expenses_distribution_plotly(self):
        fig = px.bar(self.df, x='Month', y='Expenses', title='Monthly Expenses Distribution')
        fig.write_html('files/monthly_plot.png')
