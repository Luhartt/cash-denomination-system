from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Utils import Utils
from Utils import SquareFrame
from ReplenishCashInventory import ReplenishCashInventory

class ErrorWindow(Utils):
    
    
    def __init__(self, root, home, window_before=NONE, shortfall = 0):
        self.root = root
        self.window_before = window_before 
        self.home = home

        super().__init__(root, "Check Inventory") 
        super().setup_background()
        super().setup_fonts()

        self.setup_frame()
        self.setup_heading()
        self.setup_labels(shortfall)
        self.setup_buttons()
    
    def setup_frame(self):
        self.error_frame = tk.Frame(self.root, bg="white", height=450, width=450)
        self.error_frame.place(relx=0.5, rely=0.5, anchor="center")
        
    def setup_heading(self):
        heading = tk.Label(self.error_frame, 
                           text="CASHIER TRANSACTION\nSHORTFALL DETECTED", 
                           bg="#bd0404",  
                           fg="white", 
                           height=3,
                           padx=50, 
                           font=self.font_medium_big_bold)
        heading.place(rely=0.2, relx=0.5, anchor="center")
    def setup_labels(self, amount):
        label = tk.Label(self.error_frame, 
                           text=f"Warning Unable to provide full change\nShortfall : ₱ {amount}.", 
                           bg="white",  
                           fg="#3f2622", 
                           height=3,
                           padx=50, 
                           font=self.font_medium_big_bold)
        label.place(rely=0.5, relx=0.5, anchor="center")

    def setup_buttons(self):
        buttons_frame = tk.Frame(self.error_frame, bg="white", width=300, height=100)
        buttons_frame.place(relx=0.5, rely=0.8, anchor="center")
        button_return = tk.Button(buttons_frame, 
                                  text= 
                                  "< Return", 
                                  bg="#f6f1ee", 
                                  fg="#3f2622", 
                                  width=22, 
                                  height=1,
                                  font = self.font_medium_bold,
                                  relief="flat",
                                  command=self.on_return)
        button_return.place(x=0, y=0, anchor="nw")
        button_replenish = tk.Button(buttons_frame, 
                                  text= 
                                  "Replenish Inventory", 
                                  bg="#f6f1ee", 
                                  fg="#3f2622", 
                                  width=22, 
                                  height=1, 
                                  font = self.font_medium_bold,
                                  relief="flat",
                                  command=self.on_replenish)
        button_replenish.place(x=0, y=100, anchor="sw")
        button_discard = tk.Button(buttons_frame, 
                                  text= 
                                  "Discard\nTransaction", 
                                  bg="#f6f1ee", 
                                  fg="#3f2622", 
                                  width=9, 
                                  pady=15,
                                  font = self.font_medium_bold,
                                  relief="flat",
                                  command=self.on_discard)
        button_discard.place(x=300, y=100, anchor="se")
    def on_return(self):
        self.root.destroy()
        if self.window_before:
            self.window_before.deiconify()
    def on_replenish(self):
        self.root.withdraw()
        replenish_inventory_window = tk.Toplevel(self.root)
        ReplenishCashInventory(replenish_inventory_window, self.window_before)
        replenish_inventory_window.protocol("WM_DELETE_WINDOW",  lambda: self.on_close_window(replenish_inventory_window))

    def on_discard(self):
        self.root.destroy()
        if self.home:
            self.home.deiconify()
        