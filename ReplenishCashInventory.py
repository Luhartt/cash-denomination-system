from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Utils import Utils
from Utils import SquareFrame
from session import Session

class ReplenishCashInventory(Utils):
    def __init__(self, root, window_before):
        self.root = root
        self.window_before = window_before 

        super().__init__(root, "Check Inventory") 
        super().setup_background()
        super().setup_fonts()
        self.session = Session()
        self.current_value_map = self.session.get_coins_and_bills()
        self.square_frame_replenish_inventory = SquareFrame(self.root, 
                                                            heading="REPLENISH INVENTORY", 
                                                            x=0.36, y=0.15,)
        self.square_frame_replenish_inventory.set_values_editable(self.session.get_coins_and_bills())
        self.square_frame_replenish_inventory.create_cash_components(callback=self.proceed_clicked, button="PROCEED")
    
        self.setup_current_values()
        self.setup_return_button()
        self.setup_current_value_items()
        self.cash_add_denomination = {}

    def proceed_clicked(self):
        self.cash_add_denomination = self.get_cash_denomination()
        
        if not self.cash_add_denomination:
            return
            
        for denomination in self.cash_add_denomination:
            if self.cash_add_denomination[denomination] == 0:
                continue
                
            denomination_str = str(int(denomination)) if denomination >= 1 else str(denomination)
            denomination_str += "0" if denomination_str == "0.1" else ""
                    
            self.session.add_coins_and_bills(
                type=denomination_str, 
                to_add=self.cash_add_denomination[denomination]
            )
            
        for widget in self.values_frame.winfo_children():
            widget.destroy
        self.setup_current_value_items()
        self.cash_add_denomination = {}
            
    def setup_current_values(self):
        self.current_values = tk.Frame(self.root, bg = "#bcaba4", height=390, width=160)
        self.current_values.place(rely=0.15, relx=0.32, anchor="ne")
        self.current_values.grid_propagate(False)
        self.values_frame = tk.Frame(self.current_values, bg = "#bcaba4", height=320, width=130)
        self.values_frame.place(relx= 0.5, rely=0.13, anchor="n")
        self.inventory_label = tk.Label(self.current_values, text="CASH DRAWER\nINVENTORY", 
                                        fg ="#3f2622", 
                                        bg="#bcaba4", 
                                        font=self.font_small_bold)
        self.inventory_label.place(relx=0.5, rely=0.07, anchor="center")
    
    def create_current_value_item(self, type, amount, rw):
        value_item = tk.Label(self.values_frame, 
                              text=f"{type}     X     {amount}", 
                              font=self.font_small_bold, 
                              fg="#3f2622", 
                              bg="#bcaba4"
                            )   
        value_item.grid(column=0, row=rw)
        
    def setup_current_value_items(self):
        row = 0
        for x in self.current_value_map:
            self.create_current_value_item(type=x, amount=self.current_value_map[x], rw=row )
            row+=1
    def get_cash_denomination(self):
        return SquareFrame.get_cash_denomination(self.square_frame_replenish_inventory)
    def get_cash_total(self):
        return SquareFrame.get_cash_total(self.square_frame_replenish_inventory)


    def setup_return_button(self):
        return_button = tk.Button(
            self.root,
            text="<  Return",
            height=1,
            width=17,
            font=self.font_medium_bold,
            bg="#f6f1ee",
            relief="flat",
            fg="#3f2622",
            command=self.on_return
        )
        return_button.place(relx=0.32, rely=0.82, anchor="ne")
        
    def on_return(self):
            """Handle return button click"""
            self.root.destroy()
            if self.window_before:
                self.window_before.deiconify() 
                
def main():
    root = tk.Tk()
    app = ReplenishCashInventory(root)
    root.mainloop()

if __name__ == "__main__":
    main()