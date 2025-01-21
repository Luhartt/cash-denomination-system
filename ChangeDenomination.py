from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Utils import Utils
from Utils import SquareFrame
from transactions import Transactions
from datetime import datetime

class ChangeDenomination(Utils):
           
    def __init__(self, root, denomination, total_bill, total_payment, main_window):
        self.root = root
        super().__init__(root, "Process Payment") 
        super().setup_background()
        super().setup_fonts()
        self.total_bill = total_bill
        self.total_payment = total_payment
        self.main_window = main_window
    
        self.square_frame_change_denomination = SquareFrame(self.root, 
                                                       heading="CHANGE DENOMINATION", 
                                                       x=0.41, y=0.15
                                                       )
        self.square_frame_change_denomination.set_change_denomination(denomination)
        self.square_frame_change_denomination.create_change_components(callback=self.finished_clicked, button = "FINISHED")
        self.setup_totals(label_text="TOTAL BILL", label_y=0.51, label_x=0.24, total_y=0.65, total_x=0.37, total_text=f"₱  {self.total_bill}")
        self.setup_totals(label_text="TOTAL PAYMENT", label_y=0.76, label_x=0.24, total_y=0.90, total_x=0.37, total_text=f"₱  {self.total_payment}")
        self.setup_process_payment_label()
        self.add_transaction(self.total_bill)
    def finished_clicked(self):
        self.root.destroy()
        if self.main_window:
                self.main_window.deiconify() 
    def add_transaction(self, total_bill):
        transaction = Transactions()
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M")
        transaction.add_transaction(formatted_time, f"+{total_bill}")
        
    def setup_totals(self, label_x, label_y, total_x, total_y, label_text, total_text):
        total = tk.Label(self.root, text=total_text, fg="white", bg="#3f2622", font=self.font_big_bold, height=2, width=20)
        total.place(relx=total_x, rely=total_y, anchor="se")
        label = tk.Label(self.root, text=label_text, fg="#3f2622", bg="white", font=self.font_large_bold, pady=5, padx=5)
        label.place(relx=label_x, rely= label_y, anchor="center")
        
    def setup_process_payment_label(self):
        #check inventory label
        process_payment_image = Image.open("pictures/ProcessPayment.png")
        process_payment_image = process_payment_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.process_payment_image = ImageTk.PhotoImage(process_payment_image)
        self.process_payment_label = tk.Label(self.root, 
                                        text="       Process Payment",
                                        image=self.process_payment_image, 
                                        font=self.font_small_bold, 
                                        bg="white",
                                        compound="left",
                                        fg="#3f2622",
                                        padx=5,
                                        pady=5
                                        )
        self.process_payment_label.place(rely=0, relx=0.80)
        
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