import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

# Initialize the main application window
root = tk.Tk()
root.title("Sales Invoice Generator")

# Input fields
item_name_label = ttk.Label(root, text="Item Name:")
item_name_label.grid(row=0, column=0, padx=10, pady=10)
item_name_entry = ttk.Entry(root)
item_name_entry.grid(row=0, column=1, padx=10, pady=10)

item_price_label = ttk.Label(root, text="Item Price:")
item_price_label.grid(row=1, column=0, padx=10, pady=10)
item_price_entry = ttk.Entry(root)
item_price_entry.grid(row=1, column=1, padx=10, pady=10)

item_quantity_label = ttk.Label(root, text="Item Quantity:")
item_quantity_label.grid(row=2, column=0, padx=10, pady=10)
item_quantity_entry = ttk.Entry(root)
item_quantity_entry.grid(row=2, column=1, padx=10, pady=10)

items = []

def add_item():
    try:
        item_name = item_name_entry.get()
        item_price = float(item_price_entry.get())
        item_quantity = int(item_quantity_entry.get())
        
        if item_name and item_price > 0 and item_quantity > 0:
            total = item_price * item_quantity
            items.append((item_name, item_price, item_quantity, total))
            item_name_entry.delete(0, tk.END)
            item_price_entry.delete(0, tk.END)
            item_quantity_entry.delete(0, tk.END)
            update_invoice_display()
        else:
            messagebox.showerror("Invalid Input", "Please enter valid item details.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for price and quantity.")

# Add Item Button
add_item_button = ttk.Button(root, text="Add Item", command=add_item)
add_item_button.grid(row=3, column=0, columnspan=2, pady=10)

# Treeview for displaying the invoice
invoice_tree = ttk.Treeview(root, columns=("Item", "Price", "Quantity", "Total"), show='headings')
invoice_tree.heading("Item", text="Item Name")
invoice_tree.heading("Price", text="Item Price")
invoice_tree.heading("Quantity", text="Item Quantity")
invoice_tree.heading("Total", text="Total")
invoice_tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def update_invoice_display():
    for item in invoice_tree.get_children():
        invoice_tree.delete(item)
    for item in items:
        invoice_tree.insert("", "end", values=item)

def calculate_grand_total():
    return sum(item[3] for item in items)

def   generate_invoice():
    if not items:
        messagebox.showwarning("No Items", "No items to generate invoice.")
        return

    receipt_text = "Restaurant Name\nAddress Line 1\nAddress Line 2\nPhone: 123-456-7890\n"
    receipt_text += "Date: {}\n\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    receipt_text += "Item Name\tPrice\tQuantity\tTotal\n" + "-"*40 + "\n"
    for item in items:
        receipt_text += "{}\t{}\t{}\t{}\n".format(item[0], item[1], item[2], item[3])
    receipt_text += "-"*40 + "\n"
    subtotal = calculate_grand_total()
    tax = subtotal * 0.10  # Assuming a 10% tax rate
    grand_total = subtotal + tax
    receipt_text += "Subtotal:\t{}\nTax (10%):\t{}\nGrand Total:\t{}\n".format(subtotal, tax, grand_total)
    receipt_text += "-"*40 + "\nThank you for dining with us!\n"

    with open("receipt.txt", "w") as file:
        file.write(receipt_text)

    messagebox.showinfo("Invoice Generated", "Invoice has been generated successfully!\n\n" + receipt_text)

# Generate Invoice Button
generate_invoice_button = ttk.Button(root, text="Generate Invoice", command=generate_invoice)
generate_invoice_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()