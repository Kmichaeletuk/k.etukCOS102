import tkinter as tk
from tkinter import ttk

class CafeMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PAU Cafeteria Menu")
        
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
        
        self.customer_name_label = tk.Label(root, text="Customer Name:")
        self.customer_name_label.grid(row=0, column=0)
        self.customer_name_entry = tk.Entry(root)
        self.customer_name_entry.grid(row=0, column=1)
        
        self.menu_label = tk.Label(root, text="Menu:")
        self.menu_label.grid(row=1, column=0)
        self.menu_options = tk.StringVar(root)
        self.menu_options.set("Select Menu")
        self.menu_dropdown = tk.OptionMenu(root, self.menu_options, *self.menu.keys(), command=self.update_items)
        self.menu_dropdown.grid(row=1, column=1)
        
        self.item_label = tk.Label(root, text="Item:")
        self.item_label.grid(row=2, column=0)
        self.item_options = tk.StringVar(root)
        self.item_options.set("Select Item")
        self.item_dropdown = tk.OptionMenu(root, self.item_options, "")
        self.item_dropdown.grid(row=2, column=1)
        
        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.grid(row=3, column=0)
        self.quantity_spinbox = tk.Spinbox(root, from_=1, to=10)
        self.quantity_spinbox.grid(row=3, column=1)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.calculate_total)
        self.submit_button.grid(row=4, columnspan=2)
        
    def update_items(self, *args):
        menu_choice = self.menu_options.get()
        items = list(self.menu[menu_choice].keys())
        self.item_options.set(items[0])
        self.item_dropdown['menu'].delete(0, 'end')
        for item in items:
            self.item_dropdown['menu'].add_command(label=item, command=tk._setit(self.item_options, item))
        
    def calculate_total(self):
        menu_choice = self.menu_options.get()
        item_choice = self.item_options.get()
        quantity = int(self.quantity_spinbox.get())
        price = self.menu[menu_choice][item_choice] * quantity
        total_price = price
        
        if total_price < 1000:
            discount = 0
        elif total_price < 2500:
            discount = 0.1
        elif total_price < 5000:
            discount = 0.15
        else:
            discount = 0.25
        
        total_price = total_price - (total_price * discount)
        
        total_window = tk.Toplevel(self.root)
        total_window.title("Total Charges")
        
        tk.Label(total_window, text=f"Customer Name: {self.customer_name_entry.get()}").pack()
        tk.Label(total_window, text=f"Item: {item_choice}").pack()
        tk.Label(total_window, text=f"Quantity: {quantity}").pack()
        tk.Label(total_window, text=f"Price: ₦{price}").pack()
        tk.Label(total_window, text=f"Discount: {discount*100}%").pack()
        tk.Label(total_window, text=f"Total Charges: ₦{total_price}").pack()

root = tk.Tk()
app = CafeMenuApp(root)
root.mainloop()


