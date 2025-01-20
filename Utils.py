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
        self.root.geometry("950x600")
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
        def __init__(self, root, values, heading, callback, x, y, editable):
             self.values = values
             self.root = root
             self.frameX = x
             self.frameY = y
             self.editable = editable
             self.font_big_bold = ("Asap Condensed", 25, "bold")
             self.font_large_bold = ("Asap Condensed", 35, "bold")
             self.font_medium_bold = ("Asap Condensed", 15, "bold")
             self.heading = heading
             self.amount_vars = {}
             self.total = 0
             self.total_var = tk.StringVar()
             self.total_var.set("P 0.00")
             self.callback=callback
             self.setup_square_frame()
             self.setup_heading()

             
             if(editable):
              self.setup_editable_items()
              self.setup_editable_total()
              self.setup_proceed_button_editable()

             
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

        def setup_editable_total(self):
            # Create StringVar for total
            self.total_var = tk.StringVar()
            self.total_var.set("₱ 0.00")  # Set default value
            
            self.total_cash = tk.Label(self.square_frame,
                                    bg="white",
                                    fg="#3f2622",
                                    pady=0,
                                    height=1,
                                    textvariable=self.total_var,  
                                    font=self.font_large_bold)    
            self.total_cash.place(relx=0.3, rely=0.87, anchor="n")

        def calculate_total(self, *args):
            total = 0
            for value, var in self.amount_vars.items():
                try:
                    amount = var.get()
                    if amount:  
                        total += float(value) * float(amount)
                except ValueError:
                    pass  
            
            self.total = total
            self.total_var.set(f"₱ {total:.2f}")

        def validate_numeric(self, value):
            """Validate that input is numeric or empty"""
            return value.isdigit() or value == ""
        
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
        def setup_proceed_button_editable(self):
            proceed_button = tk.Button(self.square_frame, 
                                       text="PROCEED", 
                                       bg="#3f2622",
                                       fg="white",
                                       borderwidth=0,
                                       font=self.font_big_bold,
                                       relief="flat",
                                       command=self.callback)
            proceed_button.place(relx=0.7, rely=0.87, anchor="n")
            
        def getTotal(self):
            return self.total