from Utils import Database
import matplotlib.pyplot as plt
class ReportModel:
    def fetch_items_database(self):
        with Database.get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM items")
                data = cursor.fetchall()
                cursor.close()
        return data
    
    def display_items_stock_level(self):
        data = self.fetch_items_database()
        stock_info = {}
        for row in data:
            category, stock_level, ceiling = row[1], row[2], row[3]  # Adjust indices based on your table structure
            if category not in stock_info:
                stock_info[category] = {'above_ceiling': 0, 'below_ceiling': 0, 'average': 0, 'total_items': 0, 'total_stock': 0}
            
            stock_info[category]['total_items'] += 1
            stock_info[category]['total_stock'] += stock_level

            if stock_level > ceiling:
                stock_info[category]['above_ceiling'] += 1
            elif stock_level < ceiling:
                stock_info[category]['below_ceiling'] += 1
            else:  # stock_level == ceiling
                stock_info[category]['average'] += 1

        # Plotting
        categories = list(stock_info.keys())
        above_ceiling = [info['above_ceiling'] for info in stock_info.values()]
        below_ceiling = [info['below_ceiling'] for info in stock_info.values()]
        average = [info['average'] for info in stock_info.values()]

        x = range(len(categories))  # the label locations
        width = 0.25  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x, above_ceiling, width, label='Above Ceiling')
        rects2 = ax.bar([p + width for p in x], below_ceiling, width, label='Below Ceiling')
        rects3 = ax.bar([p + width * 2 for p in x], average, width, label='Average')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Counts')
        ax.set_title('Stock levels by category')
        ax.set_xticks([p + width for p in x])
        ax.set_xticklabels(categories)
        ax.legend()

        fig.tight_layout()

        plt.show()
    
    # def fetch_sales_report(self):
    #     with Database.get_db_connection() as conn:
    #         with conn.cursor() as cursor:
    #             cursor.execute("SELECT * FROM sales")
    #             data = cursor.fetchall()
    #             cursor.close()
    #     return data

    # def display_sales_report(self):
    #     data = self.fetch_sales_report()
    #     sales_info = {}