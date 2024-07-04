from Utils import Database
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
from Utils import CustomCalendar
class ReportModel:
    def fetch_items_database(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Items")
                data = cursor.fetchall()
                cursor.close()
        return data
    
    def display_items_stock_level(self):
        data = self.fetch_items_database()
        
        # Assuming 'data' is already defined and contains the dataset
        stock_info = {}
        for row in data:
            total_items, category, stock_level, ceiling, flooring = row['quantity'], row['category'], row['stock_level'], row['ceiling'], row['flooring']
            if category not in stock_info:
                stock_info[category] = {'total_quantity': 0, 'average': 0, 'minimum': 0, 'maximum': 0}
        
            stock_info[category]['total_quantity'] += total_items
        
            # Calculate stock level categories based on a formula
            if total_items > ceiling:
                stock_info[category]['maximum'] += total_items
            elif total_items < flooring:
                stock_info[category]['minimum'] += total_items
            else:  # Between flooring and ceiling
                stock_info[category]['average'] += total_items
        
        # Plotting
        categories = list(stock_info.keys())
        total_quantities = [info['total_quantity'] for info in stock_info.values()]
        average = [info['average'] for info in stock_info.values()]
        minimum = [info['minimum'] for info in stock_info.values()]
        maximum = [info['maximum'] for info in stock_info.values()]
        
        x = np.arange(len(categories))  # the label locations
        width = 0.35  # the width of the bars
        
        fig, ax1= plt.subplots(figsize=(8.5,5.5))
        
        # Bar chart for total quantities
        rects = ax1.bar(x, total_quantities, width, label='Total Quantity', color='grey')
        ax2 = ax1.twinx()   # instantiate a second axes that shares the same x-axis
        # Improved Lines for stock levels with increased visibility
        ax2.plot(x, average, label='Average Stock Level', color='green', marker='o', linewidth=2, linestyle='--')
        ax2.plot(x, minimum, label='Minimum Stock Level', color='blue', marker='s', linewidth=2, linestyle='-.')
        ax2.plot(x, maximum, label='Maximum Stock Level', color='red', marker='^', linewidth=2, linestyle=':')

        # Annotations for maximum points as an example
        for i, txt in enumerate(maximum):
            ax2.annotate(txt, (x[i], maximum[i]), textcoords="offset points", xytext=(0,10), ha='center')

        # Adjusting legend to improve clarity
        ax1.legend(loc='upper left', title='Quantities')
        ax2.legend(loc='upper right', title='Stock Levels')
        
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax1.set_ylabel('Total Quantity', fontsize=14)
        ax2.set_ylabel('Stock Level Quantity', fontsize=14)
        ax1.set_title('Stock Levels by Category', fontsize=16)
        ax1.set_xticks(x)
        ax1.set_xticklabels(categories, rotation=45, fontsize=7)
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        return fig
    
    def fetch_sales_report(self, date):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Use the date parameter in the WHERE clause to filter sales for the specific date
                query = "SELECT * FROM Sales WHERE sold_on = %s"
                cursor.execute(query, (date))
                data = cursor.fetchall()
                cursor.close()
        return data

    
    def display_sales_report(self,date):
        data = self.fetch_sales_report(date)  # Fetch sales for the specific date
        print(f'Sales data for {date} model: {data}')
        product_names = [row['product_name'] for row in data]
        sales_quantities = [row['total'] for row in data]
        quantities_sold = [row['amount'] for row in data]
    
        fig, ax1 = plt.subplots(figsize=(10,5))
    
        color = 'tab:blue'
        ax1.set_xlabel('Product Name')
        ax1.set_ylabel('Total Revenue', color=color)
        ax1.bar(product_names, sales_quantities, color='skyblue', label='Total Revenue')
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.set_xticks(range(len(product_names)))  # Set x-ticks positions
        ax1.set_xticklabels(product_names, rotation=45, ha="right")  # Set x-tick labels with rotation
    
        ax2 = ax1.twinx()
        color = 'tab:red'
        ax2.set_ylabel('Quantity Sold', color=color)
        ax2.plot(product_names, quantities_sold, color=color, label='Quantity Sold', marker='o', linestyle='--')
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.yaxis.set_major_locator(MaxNLocator(integer=True))

        return fig
    # def display_sales_report(self, date):
    #     # Fetch sales data for the given date
    #     sales_data = self.fetch_sales_report(date)  # Hypothetical method to fetch data
    #     print(f'Sales data for {date}: {sales_data}')
    #     if not sales_data:
    #         print("No sales data found for the given date.")
    #         return

    #     # Process data for plotting
    #     dates = [data['date'] for data in sales_data]
    #     sales = [data['sales'] for data in sales_data]

    #     # Plotting
    #     plt.figure(figsize=(10, 6))
    #     plt.plot(dates, sales, marker='o', linestyle='-', color='b')
    #     plt.title('Sales Report')
    #     plt.xlabel('Date')
    #     plt.ylabel('Sales')
    #     plt.grid(True)
    #     plt.xticks(rotation=45)
    #     plt.tight_layout()

    #     # Check if there's data to plot
    #     if dates and sales:
    #         plt.show()
    #     else:
    #         print("No data to plot.")