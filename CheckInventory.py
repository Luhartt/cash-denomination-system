from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class CashInventory:
    def __init__(self, root, remaining):
        self.root = root
        self.root.title("Change Inventory")
        self.root.geometry("950x600")
        
        # Initialize fonts
        self.setup_fonts()
        
        # Setup main components
        self.setup_background()
        self.setup_check_inventory_label()
        self.setup_history_frame()
        self.setup_cash_inventory_frame()
        self.setup_cash_drawer_items()
        self.setup_cash_drawer_heading()
        self.setup_total_cash()
        self.setup_return_button()
        
        # Populate initial data
        self.populate_history()
        self.remaining = remaining

    def setup_fonts(self):
        self.font_small = ("Asap Condensed", 10)
        self.font_medium = ("Asap Condensed", 15)
        self.font_big = ("Asap Condensed", 20)
        self.font_small_bold = ("Asap Condensed", 12, "bold")
        self.font_medium_bold = ("Asap Condensed", 15, "bold")
        self.font_big_bold = ("Asap Condensed", 20, "bold")
        self.font_large_bold = ("Asap Condensed", 25, "bold")
        self.font_small_italic = ("Asap Condensed", 10, "italic")
    
    def setup_background(self):
        try:
            background_image = Image.open("pictures/Background.png")
            background_image = background_image.resize((950, 600), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(background_image)  # Keep reference
            background_label = tk.Label(self.root, image=self.bg_image)
            background_label.place(relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading background image: {e}")
            # Fallback background color
            self.root.configure(bg='#f0f0f0')
    def setup_check_inventory_label(self):
        #check inventory label
        check_inventory_image = Image.open("pictures/CheckInventory.png")
        check_inventory_image = check_inventory_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.check_intentory_image = ImageTk.PhotoImage(check_inventory_image)
        self.check_inventory_label = tk.Label(self.root, 
                                        text="       Check Inventory",
                                        image=self.check_intentory_image, 
                                        font=self.font_small_bold, 
                                        bg="white",
                                        compound="left",
                                        fg="#3f2622",
                                        padx=5,
                                        pady=5
                                        )
        self.check_inventory_label.place(rely=0, relx=0.80)
    
    def setup_history_frame(self):
        # Main history frame
        self.history_frame = tk.Frame(self.root, bg="white", height=380, width=200)
        self.history_frame.place(relx=0.36, rely=0.1, anchor="ne")
        self.history_frame.pack_propagate(False)
        
        # Canvas and scrollbar setup
        self.history_canvas = tk.Canvas(self.history_frame, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.history_frame, orient="vertical", 
                               command=self.history_canvas.yview)
        
        # Content frame
        self.history_content = tk.Frame(self.history_canvas, bg="white")
        
        # Configure canvas
        self.history_canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas_frame = self.history_canvas.create_window(
            (0, 0), window=self.history_content, anchor="nw")
        
        # Pack elements
        scrollbar.pack(side="right", fill="y")
        self.history_canvas.pack(side="left", fill="both", expand=True)
        
        # Bind events
        self.history_content.bind("<Configure>", self.on_frame_configure)
        self.history_canvas.bind("<Configure>", self.on_canvas_configure)
        
        # History heading
        tk.Label(self.history_content, text="HISTORY", 
                font=self.font_medium, bg="white").pack(pady=10)
    
    def setup_cash_inventory_frame(self):
        self.cash_inventory_frame = tk.Frame(self.root, bg="white", 
                                           height=450, width=450)
        self.cash_inventory_frame.place(relx=0.40, rely=0.1, anchor="nw")
        
        self.cash_inventory_contents = tk.Frame(self.cash_inventory_frame, bg="white", width=450, height=280)
        self.cash_inventory_contents.place(relx = 0.5, rely = 0.5, anchor="center")
        
    def setup_cash_drawer_heading(self):
        cash_drawer_heading = tk.Label(self.cash_inventory_frame, 
                                       bg="white",
                                       fg="#3f2622", 
                                       text="CASH DRAWER INVENTORY",
                                       font=self.font_big_bold
                                    )    
        cash_drawer_heading.place(relx=0.5, y = 10, anchor="n")
        
    def setup_total_cash(self):
        amount = 1000.32
        total_cash = tk.Label(self.cash_inventory_frame, 
                                       bg="white",
                                       fg="#3f2622", 
                                       text=f"P {amount}",
                                       font=self.font_large_bold
                                    )    
        total_cash.place(relx=0.5,rely=0.85, anchor="n")
        
    def create_cash_drawer_inventory_item(self, rw, col, type, amount):
        cash_inventory_item_frame = tk.Frame(self.cash_inventory_contents, bg="white")
        cash_inventory_item_frame.grid(row = rw, column=col, padx=25, pady=10)
        cash_inventory_type = tk.Label(cash_inventory_item_frame, 
                                       text=f"{type}  X  ", 
                                       fg="#3f2622",
                                       bg="white",
                                       width=8,
                                       anchor="w", 
                                       font=self.font_big_bold
                                      )
        cash_inventory_amount = tk.Label(cash_inventory_item_frame, 
                                       text=f"{amount}", 
                                       fg="#3f2622",
                                       bg="#f6f1ee",
                                       width=5,
                                       anchor="w", 
                                       font=self.font_big_bold
                                      )

        cash_inventory_type.grid(column=0, row=0)
        cash_inventory_amount.grid(column=1, row=0)
        
    def setup_cash_drawer_items(self):
        column = 2
        row = 5
        for col in range(column):
            for rw in range(row):
                self.create_cash_drawer_inventory_item(rw, col, "1000", "2")
                
    def setup_return_button(self):
        return_button = tk.Button(
            self.root,
            text="< Return",
            height=1,
            width=21,
            font=self.font_medium_bold,
            bg="#f6f1ee",
            relief="flat",
            fg="#3f2622",
            command=self.on_return
        )
        return_button.place(relx=0.36, y=463, anchor="ne")
                
    
    def create_history_label(self, date, amount):
        label = tk.Label(
            self.history_content,
            text=f"{date}             {amount}",
            font=self.font_small,
            bg="white"
        )
        label.pack(pady=10)
    
    def populate_history(self):
        # Add sample history entries
        for _ in range(50):
            self.create_history_label("January 20, 2025", "+600")
            
    def on_frame_configure(self, event=None):
        """Reset the scroll region to encompass the inner frame"""
        self.history_canvas.configure(scrollregion=self.history_canvas.bbox("all"))
    
    def on_canvas_configure(self, event):
        """Update the width of the canvas window to fit the frame"""
        width = event.width
        self.history_canvas.itemconfig(self.canvas_frame, width=width)
    
    def on_return(self):
        """Handle return button click"""
        # Add your return logic here
        print("Return button clicked")

if __name__ == "__main__":
    remaining = {
        1000: 10,
        500: 15,
        200: 23,
        100: 30,
        50: 52,
        20: 56,
        10: 100,
        5: 140,
        1: 200,
        0.25: 5,
        0.10: 3,
        0.5: 1 
    }
    root = tk.Tk()
    app = CashInventory(root, remaining)
    root.mainloop()