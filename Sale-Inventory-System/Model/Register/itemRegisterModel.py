from Utils import Functions
from Controller.Dashboard import managerController
from Utils import Database
from icecream import ic
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
        if not self.quantity or self.quantity <=0:
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

    def registerItemData(self) -> int:
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            if self.status == "Supply Item":
                sql = """INSERT INTO Supply (supply_id, user_id, item_name, quantity, unit, supplier, exp_date, menu_type, flooring, ceiling, stock_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
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

    def updateItemData(self):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            if self.status == "Supply Item":
                sql = """UPDATE Supply SET 
                        user_id = %s, 
                        item_name = %s, 
                        quantity = %s, 
                        unit = %s, 
                        supplier = %s, 
                        exp_date = %s, 
                        menu_type = %s, 
                        flooring = %s, 
                        ceiling = %s, 
                        stock_level = %s
                        WHERE supply_id = %s;"""
                cursor.execute(sql, (
                    self.user_id,
                    self.item_name,
                    self.quantity,
                    self.unit,
                    self.supplier,
                    self.expiry_date,
                    self.category,
                    self.flooring,
                    self.ceiling,
                    self.stock_level,
                    self.item_id,
                ))
            if self.status == "Raw Item":
                sql = """UPDATE Items SET 
                        user_id = %s, 
                        item_name = %s, 
                        quantity = %s, 
                        unit = %s, 
                        supplier = %s, 
                        exp_date = %s, 
                        category = %s, 
                        flooring = %s, 
                        ceiling = %s, 
                        stock_level = %s
                        WHERE item_id = %s;"""
                cursor.execute(sql, (
                    self.user_id,
                    self.item_name,
                    self.quantity,
                    self.unit,
                    self.supplier,
                    self.expiry_date,
                    self.category,
                    self.flooring,
                    self.ceiling,
                    self.stock_level,
                    self.item_id,
                ))
        connection.commit()
        connection.close()
        return 0

    def checkStockLevel(self):
        if self.quantity >= self.flooring and self.quantity < self.ceiling:
            return "Average"
        if self.quantity <= self.flooring:
            return "Danger"
        if self.quantity >= self.ceiling:
            return "Maximum"
        
    def subtract_item_stock(self, ingredient_total: dict):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            try:
                connection.autocommit = False
                for ingredient_name, required_quantity in ingredient_total.items():
                    cursor.execute("SELECT item_id, quantity FROM Items WHERE item_name = %s AND quantity > 0 ORDER BY exp_date ASC", (ingredient_name,))
                    items = cursor.fetchall()
                    
                    remaining_quantity = abs(required_quantity)
                    for item in items:
                        item_id, item_quantity = item['item_id'], item['quantity']
                        
                        if required_quantity > 0:  # Product/Supply created, subtract items
                            if item_quantity >= remaining_quantity:
                                new_quantity = item_quantity - remaining_quantity
                                cursor.execute("UPDATE Items SET quantity = %s WHERE item_id = %s", (new_quantity, item_id))
                                remaining_quantity = 0
                            else:
                                remaining_quantity -= item_quantity
                                cursor.execute("UPDATE Items SET quantity = %s WHERE item_id = %s", (0, item_id))
                        else:  # Product/Supply removed, add items back
                            new_quantity = item_quantity + remaining_quantity
                            cursor.execute("UPDATE Items SET quantity = %s WHERE item_id = %s", (new_quantity, item_id))
                            remaining_quantity = 0
                        
                        if remaining_quantity == 0:
                            break
                    
                    if remaining_quantity > 0 and required_quantity > 0:
                        return ValueError(f"Not enough stock for {ingredient_name}.")
                connection.commit()
            except Exception as e:
                connection.rollback()
                raise e
            finally:
                connection.autocommit = True
        return 0

    
    
    def subtract_item_stock(self, ingredient_total: dict):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            try:
                connection.autocommit = False
                for ingredient_name, required_quantity in ingredient_total.items():
                    if required_quantity == 0:
                        print(f"Skipping {ingredient_name} as required quantity is 0")
                        continue

                    cursor.execute("SELECT item_id, quantity FROM Items WHERE item_name = %s AND quantity > 0 ORDER BY exp_date ASC", (ingredient_name,))
                    items = cursor.fetchall()
                    
                    remaining_quantity = abs(required_quantity)
                    for item in items:
                        item_id, item_quantity = item['item_id'], item['quantity']
                        
                        if required_quantity > 0:  # Product/Supply created, subtract items
                            if item_quantity >= remaining_quantity:
                                new_quantity = item_quantity - remaining_quantity
                                cursor.execute("UPDATE Items SET quantity = %s WHERE item_id = %s", (new_quantity, item_id))
                                print(f"Subtracted {remaining_quantity} from item {item_id}")
                                remaining_quantity = 0
                            else:
                                remaining_quantity -= item_quantity
                                cursor.execute("UPDATE Items SET quantity = %s WHERE item_id = %s", (0, item_id))
                                print(f"Subtracted {item_quantity} from item {item_id}")
                        else:  # Product/Supply removed, add items back
                            new_quantity = item_quantity + remaining_quantity
                            cursor.execute("UPDATE Items SET quantity = %s WHERE item_id = %s", (new_quantity, item_id))
                            print(f"Added {remaining_quantity} back to item {item_id}")
                            remaining_quantity = 0
                        
                        if remaining_quantity == 0:
                            break
                    
                    if remaining_quantity > 0 and required_quantity > 0:
                        raise ValueError(f"Not enough stock for {ingredient_name}. Short by {remaining_quantity}")
                
                connection.commit()
            except Exception as e:
                connection.rollback()
                print(f"An error occurred: {e}")
                raise e
            finally:
                connection.autocommit = True
        return 0

        # def subtract_item_stock(self, ingredient_total: dict):
    #     with Database.get_db_connection() as connection:
    #         with connection.cursor() as cursor:
    #             try:
    #                 # Start transaction
    #                 connection.autocommit = False
    #                 for ingredient_name, required_quantity in ingredient_total.items():
    #                     remaining_quantity = required_quantity
    #                     cursor.execute("SELECT item_id, quantity FROM Items WHERE item_name = %s AND quantity > 0 ORDER BY exp_date ASC", (ingredient_name,))
    #                     items = cursor.fetchall()
    #                     for item in items:
    #                         item_id, item_quantity = item['item_id'], item['quantity']
    #                         if item_quantity >= remaining_quantity:
    #                             new_quantity = item_quantity - remaining_quantity
    #                             cursor.execute("UPDATE Items SET quantity = %s WHERE item_id = %s", (new_quantity, item_id))
    #                             remaining_quantity = 0
    #                         else:
    #                             remaining_quantity -= item_quantity
    #                             item_quantity = 0
    #                             cursor.execute("UPDATE Items SET quantity = %s WHERE item_id = %s", (item_quantity, item_id,))
    #                         if remaining_quantity <= 0:
    #                             break
    #                     if remaining_quantity > 0:
    #                         raise ValueError(f"Not enough stock for {ingredient_name}.")
    #                 connection.commit()
    #             except Exception as e:
    #                 connection.rollback()
    #                 raise e
    #             finally:
    #                 connection.autocommit = True
    #     return 0

    # def subtract_supply_stock(self, supply_total: list):
    #     with Database.get_db_connection() as connection:
    #         with connection.cursor() as cursor:
    #             try:
    #                 # Start transaction
    #                 print("debug 3")
    #                 ic(supply_total)
    #                 connection.autocommit = False
    #                 supply_id, supply_name, required_quantity = supply_total
    #                 remaining_quantity = required_quantity
    #                 cursor.execute("SELECT supply_id, quantity FROM Supply WHERE item_name = %s AND quantity > 0 ORDER BY exp_date ASC", (supply_name,))
    #                 items = cursor.fetchall()
    #                 for item in items:
    #                     supply_id, supply_quantity = item['supply_id'], item['quantity']
    #                     if supply_quantity >= remaining_quantity:
    #                         new_quantity = supply_quantity - remaining_quantity
    #                         cursor.execute("UPDATE Supply SET quantity = %s WHERE supply_id = %s", (new_quantity, supply_id))
    #                         remaining_quantity = 0
    #                     else:
    #                         remaining_quantity -= item_quantity
    #                         item_quantity = 0
    #                         cursor.execute("UPDATE Supply SET quantity = %s WHERE supply_id = %s", (item_quantity, supply_id,))
    #                     if remaining_quantity <= 0:
    #                         print("debug 4")
    #                         ic(remaining_quantity)
    #                         break
    #                 print("debug 5")
    #                 ic(remaining_quantity)
    #                 if remaining_quantity > 0:
    #                     raise ValueError(f"Not enough stock for {supply_name}.")
    #                 connection.commit()
    #             except Exception as e:
    #                 connection.rollback()
    #                 raise e
    #             finally:
    #                 connection.autocommit = True
    #     return 0



    
    def update_item_in_database(self, item_id, new_quantity):
        with Database.get_db_connection() as connection:
            cursor = conn.cursor()
            update_query = "UPDATE your_table_name SET quantity = ? WHERE id = ?"
            cursor.execute(update_query, (new_quantity, item_id))
            self.db_connection.commit()
        cursor.close()
        return 0
