from Utils import Functions
from Controller.Dashboard import managerController
from Utils import Database
class ItemRegisterModel:
    def __init__(self,data:list=None,user_id=None,status=None):
        #item name,quantity,price,supplier,expiry date, category, flooring, ceiling, stock_level
        self.status = status
        self.user_id = user_id
        if data is not None:
            self.item_name = data[0]
            self.quantity = data[1]
            self.unit = data[2]
            self.supplier = data[3]
            self.expiry_date = data[4]
            self.category = data[5]
            self.flooring = data[6]
            self.ceiling = data[7]
            self.item_id = data[8]
            self.stock_level = self.checkStockLevel()
        

    def set_item_id(self):
        return Functions.generate_unique_id("Item")
    
    def checkInput(self):
        #check error if error return ValueError else return 0
        if not self.item_name:
            return ValueError("Item name cannot be empty")
        if not self.quantity:
            return ValueError("Quantity cannot be empty")
        if not self.supplier:
            return ValueError("Supplier cannot be empty")
        if not self.expiry_date:
            return ValueError("Expiry date cannot be empty")
        if self.category == "Select Category" and self.status == "Raw item":
            return ValueError("Category cannot be empty")
        if self.category == "Select Menu Type" and self.status == "Supply Item":
            return ValueError("Menu Type cannot be empty")
        if not self.stock_level:
            return ValueError("Stock level cannot be empty")
        if not self.flooring:
            return ValueError("Flooring cannot be empty")
        if not self.ceiling:
            return ValueError("Ceiling cannot be empty")
        return 0

    def registerItemData(self):
        #register item to data base
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                if self.status == "Supply Item":
                    sql = """INSERT INTO Supply (supply_id, user_id, product_name, quantity, unit, supplier, exp_date, menu_type, flooring, ceiling, stock_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(sql, (
                        self.item_id,
                        self.user_id,
                        self.item_name,
                        self.quantity,
                        self.unit,
                        self.supplier,
                        self.expiry_date,
                        self.category,
                        self.flooring,
                        self.ceiling,
                        self.stock_level
                    ))
                if self.status == "Raw Item":
                    sql = """INSERT INTO Items (item_id, user_id, item_name, quantity, unit, supplier, exp_date, category, flooring, ceiling, stock_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(sql, (
                        self.item_id,
                        self.user_id,
                        self.item_name,
                        self.quantity,
                        self.unit,
                        self.supplier,
                        self.expiry_date,
                        self.category,
                        self.flooring,
                        self.ceiling,
                        self.stock_level
                    ))
            connection.commit()
            connection.close()
        return 0

    def checkStockLevel(self):
        if self.quantity > self.flooring and self.quantity < self.ceiling:
            return "Average"
        if self.quantity <= self.flooring:
            return "Danger"
        if self.quantity >= self.ceiling:
            return "Maximum"
        
    def subtract_stock(self,ingredient_total:dict):
        #suctract all total quantities from items table that have the same name as the ingredient
        #return error if total quantity of ingredient needed > stock level
        #subtract the quantity from the quantity in the items database
        #update the stock level
        #return 0 to go back to productRegisterController
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                for ingredient_name, required_quantity in ingredient_total.items():
                    # Retrieve the current stock level
                    cursor.execute("SELECT quantity FROM Items WHERE item_name = %s", (ingredient_name,))
                    result = cursor.fetchone()
                    if result is None:
                        return f"Error: Ingredient {ingredient_name} not found in stock."
                    current_stock = float(result['quantity'])
                    
                    # Check if sufficient stock is available
                    if required_quantity > current_stock:
                        return f"Error: Not enough stock for {ingredient_name}. Required: {required_quantity}, Available: {current_stock_level}"
                    
                    # Subtract the required quantity from the stock level
                    new_stock = current_stock - required_quantity
                    
                    # Update the stock level in the database
                    cursor.execute("UPDATE Items SET quantity = %s WHERE item_name = %s", (new_stock, ingredient_name))
                    connection.commit()
                    
        return 0  # Indicate success
    
    def update_item_in_database(self, item_id, new_quantity):
        with Database.get_db_connection() as connection:
            with connection.cursor() as cursor:
                update_query = "UPDATE your_table_name SET quantity = ? WHERE id = ?"
                cursor.execute(update_query, (new_quantity, item_id))
                self.db_connection.commit()
            cursor.close()
        return 0  # Indicate success
