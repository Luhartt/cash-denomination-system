from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Utils import Utils
from Utils import SquareFrame
from Session import Session

class ChangeDenomination(Utils):
           
    def __init__(self, root, denomination):
        self.root = root
        super().__init__(root, "Process Payment") 
        super().setup_background()
        super().setup_fonts()
        self.session = Session()
    
        self.square_frame_change_denomination = SquareFrame(self.root, 
                                                       heading="DENOMINATION BREAKDOWN", 
                                                       x=0.45, y=0.15,
                                                       )
        self.square_frame_change_denomination.set_change_denomination(denomination)
        self.square_frame_change_denomination.create_change_components(callback=self.proceed_clicked)
        self.setup_totals(label_text="TOTAL BILL", label_y=0.5, label_x=0.5, total_y=0.1, total_x=0.1, total_text="₱5.00")
        self.setup_totals(label_text="TOTAL PAYMENT", label_y=0.7, label_x=0.7, total_y=0.2, total_x=0.2, total_text="₱10.00")

        
    def proceed_clicked(self):
        pass
        
    def setup_totals(self, label_x, label_y, total_x, total_y, label_text, total_text):
        label = tk.Label(self.root, text=label_text, fg="white")
        label.place(relx=label_x, rely= label_y, anchor="center")
        total = tk.Label(self.root, text=total_text, fg="#4d342f", bg="white")
        total.place(relx=total_x, rely=total_y, anchor="cent")
        
        
        
def main():
    denomination = {
            1000: 10, 500: 15, 200: 23, 100: 30, 50: 52,
            20: 56, 10: 100, 5: 140, 1: 200, 0.25: 5,
            0.10: 3, 0.5: 1
    }
    root = tk.Tk()
    app = ChangeDenomination(root, denomination)
    root.mainloop()

if __name__ == "__main__":
    main()