import tkinter as tk
from tkinter import ttk

class CafeMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PAU Cafeteria Menu")
        
        # Define the menu items and their prices
        self.menu = {
            "RICE/PASTA": {
                "Jollof Rice": 350,
                "Coconut Fried Rice": 350,
                "Jollof Spaghetti": 350
            },
            "PROTEINS": {
                "Sweet Chili Chicken": 1100,
                "Grilled Chicken Wings": 400,
                "Fried Beef": 400,
                "Fried Fish": 400,
                "Boiled Egg": 200,
                "Sauteed Sausages": 200
            },
            "SIDE DISHES": {
                "Savoury Beans": 350,
                "Roasted Sweet Potatoes": 300,
                "Fried Plantains": 150,
                "Mixed Vegetable Salad": 150,
                "Boiled Yam": 150
            },
            "BEVERAGES": {
                "Water": 200,
                "Glass Drink (35cl)": 150,
                "PET Drink (35cl)": 300,
                "PET Drink (50cl)": 350,
                "Glass/Canned Malt": 500,
                "Fresh Yo": 600,
                "Pineapple Juice": 350,
                "Mango Juice": 350,
                "Zobo Drink": 350
            },
            "SOUPS & SWALLOWS": {
                "Eba": 100,
                "Poundo Yam": 100,
                "Semo": 100,
                "Atama Soup": 450,
                "Egusi Soup": 480
            }
        }
        
        # Create and place GUI elements
        self.customer_name_label = tk.Label(root, text="Customer Name:")
        self.customer_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.customer_name_entry = tk.Entry(root)
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        self.menu_label = tk.Label(root, text="Menu:")
        self.menu_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.menu_options = tk.StringVar(root)
        self.menu_options.set("Select Menu")
        self.menu_dropdown = tk.OptionMenu(root, self.menu_options, *self.menu.keys(), command=self.update_items)
        self.menu_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        self.item_label = tk.Label(root, text="Item:")
        self.item_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.item_options = tk.StringVar(root)
        self.item_options.set("Select Item")
        self.item_dropdown = tk.OptionMenu(root, self.item_options, "")
        self.item_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.quantity_spinbox = tk.Spinbox(root, from_=1, to=10)
        self.quantity_spinbox.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        self.add_button = tk.Button(root, text="Add to Order", command=self.add_to_order)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        
        # Initialize order list and total price
        self.order_list = []
        self.total_price = 0
        
        self.order_frame = tk.Frame(root)
        self.order_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        
        self.total_label = tk.Label(root, text="Total Charges: ₦0")
        self.total_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        
        self.submit_button = tk.Button(root, text="Submit Order", command=self.submit_order)
        self.submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        
    def update_items(self, *args):
        """Update item dropdown based on selected menu"""
        menu_choice = self.menu_options.get()
        items = list(self.menu[menu_choice].keys())
        self.item_options.set(items[0])
        self.item_dropdown['menu'].delete(0, 'end')
        for item in items:
            self.item_dropdown['menu'].add_command(label=item, command=lambda value=item: self.item_options.set(value))
        
    def add_to_order(self):
        """Add selected item to order list"""
        menu_choice = self.menu_options.get()
        item_choice = self.item_options.get()
        quantity = int(self.quantity_spinbox.get())
        price = self.menu[menu_choice][item_choice] * quantity
        
        # Add item to order list
        self.order_list.append((item_choice, quantity, price))
        
        # Update total price
        self.total_price += price
        
        # Display order in order frame
        order_text = f"{item_choice} (Quantity: {quantity}) - ₦{price}"
        tk.Label(self.order_frame, text=order_text).pack(anchor="w")
        
        # Update total price label
        self.total_label.config(text=f"Total Charges: ₦{self.total_price}")
        
    def submit_order(self):
        """Submit order and display total charges"""
        if not self.order_list:
            tk.messagebox.showinfo("Error", "Please add items to your order!")
            return
        
        # Calculate discount based on total price
        if self.total_price < 1000:
            discount = 0
        elif self.total_price < 2500:
            discount = 0.1
        elif self.total_price < 5000:
            discount = 0.15
        else:
            discount = 0.25
        
        # Apply discount
        total_price_after_discount = self.total_price - (self.total_price * discount)
        
        # Display total charges including discount
        total_window = tk.Toplevel(self.root)
        total_window.title("Total Charges")
        
        tk.Label(total_window, text=f"Customer Name: {self.customer_name_entry.get()}").pack()
        for item, quantity, price in self.order_list:
            tk.Label(total_window, text=f"{item} (Quantity: {quantity}) - ₦{price}").pack()
        tk.Label(total_window, text=f"Total Charges (before discount): ₦{self.total_price}").pack()
        tk.Label(total_window, text=f"Discount: {discount*100}%").pack()
        tk.Label(total_window, text=f"Total Charges (after discount): ₦{total_price_after_discount}").pack()

root = tk.Tk()
app = CafeMenuApp(root)
root.mainloop()


