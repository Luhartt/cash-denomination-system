from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import platform

class Utils:
    
     def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        if platform.system() == "Windows":
            root.tk.call("tk", "scaling", 1.0)
        elif platform.system() == "Darwin":
                 root.tk.call("tk", "scaling", 1.2)


        # center window
        width = 950
        height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int((screen_width/2) - (width/2))
        center_y = int((screen_height/2) - (height/2))
        self.root.geometry(f'{width}x{height}+{center_x}+{center_y}')
        self.root.resizable(False, False)

     def setup_background(self):
        """Setup the background image"""
        try:
            background_image = Image.open("pictures/Background.png")  # Make sure this path is correct
            background_image = background_image.resize((950, 600), Image.Resampling.LANCZOS)
            self.background_image = ImageTk.PhotoImage(background_image)  # Keep the reference
            background_label = tk.Label(self.root, image=self.background_image)
            background_label.place(relwidth=1, relheight=1)  # Ensure the background label fills the entire window
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.root.configure(bg='#f0f0f0')  # Fallback background color
            
     def setup_fonts(self):
            self.font_small = ("Asap Condensed", 15)
            self.font_medium = ("Asap Condensed", 20)
            self.font_medium_big = ("Asap Condensed", 23)
            self.font_big = ("Asap Condensed", 25)
            self.font_small_bold = ("Asap Condensed", 17, "bold")
            self.font_medium_bold = ("Asap Condensed", 20, "bold")
            self.font_medium_big_bold = ("Asap Condensed", 23, "bold")
            self.font_big_bold = ("Asap Condensed", 25, "bold")
            self.font_large_bold = ("Asap Condensed", 30, "bold")
            self.font_small_italic = ("Asap Condensed", 10, "italic")
            
class SquareFrame:
        def __init__(self, root, heading, x, y):
            self.root = root
            self.frameX = x
            self.frameY = y
            self.font_big_bold = ("Asap Condensed", 25, "bold")
            self.font_large_bold = ("Asap Condensed", 35, "bold")
            self.font_medium_bold = ("Asap Condensed", 15, "bold")
            self.heading = heading

            self.setup_square_frame()
            self.setup_heading()


             
    
        def set_values_editable(self, values):
            self.values = values
            self.amount_vars = {}
            self.cash_total = 0
            self.cash_total_var = tk.StringVar()
            self.cash_total_var.set("P 0.00")
    
        def create_cash_components(self, callback, button):
            self.setup_editable_items()
            self.setup_dynamic_total_cash()
            self.setup_button(callback, button)


            
        def set_change_denomination(self, values):
            self.change_denomination = values
        def create_change_components(self, callback, button):
            self.setup_label_items()
            self.setup_total_change()
            self.setup_button(callback, button)


            
        def setup_square_frame(self):
            self.square_frame = tk.Frame(self.root, bg="white", 
                                            height=450, width=450)
            self.square_frame.place(relx=self.frameX, rely=self.frameY, anchor="nw")
            
            self.square_contents = tk.Frame(self.square_frame, bg="white", width=450, height=280)
            self.square_contents.place(relx = 0.5, rely = 0.5, anchor="center")
            
        def setup_heading(self):
            heading = tk.Label(self.square_frame, 
                                        bg="white",
                                        fg="#3f2622", 
                                        text= self.heading,
                                        font=self.font_large_bold
                                        )    
            heading.place(relx=0.5, y = 15, anchor="n")            
        
            """This part up to calculate_total is used for the Process Payment Main / Replenish Cash Drawer part
            """
            
            # Used to create Label and Entries for payment input 
        def create_editable_item(self, row, column, item_type):
            if not hasattr(self, 'validation_command'):
                self.validation_command = (self.root.register(self.validate_numeric), '%P')
            
            item_frame = tk.Frame(self.square_contents, bg="white")
            item_frame.grid(row=row, column=column, padx=20, pady=5)
            
            type_label = tk.Label(item_frame,
                                text=f"{item_type}  X  ",
                                fg="#3f2622",
                                bg="white",
                                width=8,
                                anchor="w",
                                font=self.font_big_bold)
            
            amount_var = tk.StringVar()
            amount_var.trace('w', self.calculate_total)  
            self.amount_vars[item_type] = amount_var  
            
            amount_entry = tk.Entry(item_frame,
                                validate='all',
                                validatecommand=self.validation_command,
                                textvariable=amount_var, 
                                fg="#3f2622",
                                bg="#f6f1ee",
                                width=5,
                                font=self.font_big_bold,
                                relief="flat")
            
            type_label.grid(column=0, row=0)
            amount_entry.grid(column=1, row=0)
            
            return type_label, amount_entry            

         # Used to create dynamic for total change
        def setup_dynamic_total_cash(self):
            # Create StringVar for total
            self.cash_total_var = tk.StringVar()
            self.cash_total_var.set("₱ 0.00")  # Set default value
            
            self.total_cash_label = tk.Label(self.square_frame,
                                    bg="white",
                                    fg="#3f2622",
                                    pady=0,
                                    height=1,
                                    textvariable=self.cash_total_var,  
                                    font=self.font_large_bold)    
            self.total_cash_label.place(relx=0.3, rely=0.87, anchor="n")

        
        # Validating input in entry
        def validate_numeric(self, value):
            """Validate that input is numeric or empty"""
            return value.isdigit() or value == ""
        
        # Setting up the label and the entries
        def setup_editable_items(self):
            column = 0
            row = 0
            counter = 0;
            for x in self.values:
                counter+=1
                if(counter == 7):
                    column += 1
                    row = 0
                    counter = 0
                self.create_editable_item(row, column, x)
                row += 1
                
        # function used in calculating total cash
        def calculate_total(self, *args):
            total = 0
            for type, var in self.amount_vars.items():
                try:
                    amount = var.get()
                    if amount:  
                        total += float(type) * float(amount)
                except ValueError:
                    pass  
            
            self.cash_total = total
            self.cash_total_var.set(f"₱ {total:.2f}")
        
        
            """This part until create setup_total_change is used for Change Denomination
            """
            # Used in creating labels (1000 x 5)
        def create_label_item(self, rw, col, type, amount):
            item_frame = tk.Frame(self.square_contents, bg="white")
            item_frame.grid(row = rw, column=col, padx=25, pady=5)
            item_type = tk.Label(item_frame, 
                                        text=f"{type}  X  ", 
                                        fg="#3f2622",
                                        bg="white",
                                        width=8,
                                        anchor="w", 
                                        font=self.font_big_bold
                                        )
            item_amount = tk.Label(item_frame, 
                                        text=f"{amount}", 
                                        fg="#3f2622",
                                        bg="#f6f1ee",
                                        width=5,
                                        anchor="w", 
                                        font=self.font_big_bold
                                        )

            item_type.grid(column=0, row=0)
            item_amount.grid(column=1, row=0)
            
            # Setting up items
        def setup_label_items(self):
            column = 0
            row = 0
            counter = 0;
            for x in self.change_denomination:
                counter+=1
                if(counter == 7):
                    column += 1
                    row = 0
                    counter = 0
                self.create_label_item(row, column, x, self.change_denomination[x])
                row += 1
                
            # calculating and setting up total change
        def setup_total_change(self):
            total = 0;
            for x in self.change_denomination:
                total+= float(x) * float(self.change_denomination[x]);
            total_cash = tk.Label(self.square_frame, 
                                        bg="white",
                                        fg="#3f2622", 
                                        text=f"P {total}",
                                        font=self.font_large_bold
                                        )    
            total_cash.place(relx=0.3, rely=0.87, anchor="n")
        
            # Proceed Button
        def setup_button(self, callback, content):
            proceed_button = tk.Button(self.square_frame, 
                                       text=content, 
                                       bg="#3f2622",
                                       fg="white",
                                       borderwidth=0,
                                       font=self.font_big_bold,
                                       relief="flat",
                                       command=callback)
            proceed_button.place(relx=0.7, rely=0.87, anchor="n")
            
            # returns total calculate change
        def get_cash_total(self):
            return self.cash_total
        def get_cash_denomination(self):
            denomination_amounts = {}
            for type, var in self.amount_vars.items():
                # var is the StringVars (what is returned in Entries)
                try:
                    amount = var.get()
                    if amount:  
                        denomination_amounts[float(type)] = amount
                    else:  
                        denomination_amounts[float(type)] = 0
                except ValueError:
                    denomination_amounts[float(type)] = 0
            return denomination_amounts