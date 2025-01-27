from Utils import Database
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

class ReportModel:
    def fetch_items_database(self):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
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
        
        fig, ax1= plt.subplots(figsize=(7.5,5))
        
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
        print(f'Date: {date}')
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            # Use the date parameter in the WHERE clause to filter sales for the specific date
            query = "SELECT * FROM Invoice WHERE sold_on LIKE %s"
            _date = f"%{date}%"
            cursor.execute(query, (_date,))
            data = cursor.fetchall()
            cursor.close()
        return data

    
    def display_sales_report(self, date):
        data = self.fetch_sales_report(date)  # Fetch sales for the specific date
        print(f'Sales data for {date} model: {data}')

        # Aggregate totals and amounts for each product
        aggregated_data = defaultdict(lambda: {'total': 0, 'amount': 0})
        for row in data:
            product_name = row['product_name']
            aggregated_data[product_name]['total'] += row['total']
            aggregated_data[product_name]['amount'] += row['amount']

        # Extract data for plotting
        product_names = list(aggregated_data.keys())
        sales_quantities = [info['total'] for info in aggregated_data.values()]
        quantities_sold = [info['amount'] for info in aggregated_data.values()]

        fig, ax1 = plt.subplots(figsize=(8, 5))

        color = 'tab:blue'
        ax1.set_xlabel('Product Name')
        ax1.set_ylabel('Total Price', color=color)
        ax1.bar(product_names, sales_quantities, color='skyblue', label='Total Price')
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.set_xticks(range(len(product_names)))  # Set x-ticks positions
        ax1.set_xticklabels(product_names, fontsize= 7,rotation=26, ha="right")  # Set x-tick labels with rotation

        ax2 = ax1.twinx()
        color = 'tab:red'
        ax2.set_ylabel('Total Sold', color=color)
        ax2.plot(product_names, quantities_sold, color=color, label='Total Sold', marker='o', linestyle='--')
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.yaxis.set_major_locator(MaxNLocator(integer=True))

        return fig
    

    def fetch_reorder_history(self, date):
        with Database.get_db_connection() as conn:
            cursor = conn.cursor()
            # Use the date parameter in the WHERE clause to filter supply history for the specific date
            query = "SELECT * FROM Reordered WHERE ordered_on LIKE %s"
            _date = f"%{date}%"
            cursor.execute(query, (_date,))
            data = cursor.fetchall()
            cursor.close()
        return data
    
    def display_reorder_history(self, date):
        data = self.fetch_reorder_history(date)
        print(f'Supply data for {date} model: {data}')

        # Process data for plotting
        order_dates = [row['ordered_on'].strftime('%H:%M') for row in data]
        arrival_dates = [row['arrival_date'].strftime('%H:%M') for row in data]
        quantities = [row['quantity'] for row in data]

        # Plotting
        fig, ax = plt.subplots(figsize=(8, 5))

        ax.plot(order_dates, quantities, label='Ordered Quantity', marker='o', linestyle='--', color='blue')
        ax.plot(arrival_dates, quantities, label='Arrived Quantity', marker='s', linestyle='-', color='green')

        ax.set_xlabel('Date')
        ax.set_ylabel('Quantity')
        ax.set_title(f'Supply History for {date}')
        ax.legend()

        return fig

