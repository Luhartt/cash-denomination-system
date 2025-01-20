from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Utils import Utils
from Utils import SquareFrame

class ProcessPaymentMain(Utils):
        def __init__(self, root, values):
                super().__init__(root, "Process Payment") 
                super().setup_background()
                super().setup_fonts()
    
                self.square_frame_process_payment = SquareFrame(self.root, values, heading="PAYMENT", callback=self.proceed_clicked)
                
        
        def proceed_clicked(self):
                print(SquareFrame.getTotal(self.square_frame_process_payment))        
        
            

def main():
        
    values = [
        1000,500,200,100,50,20,
        10,5,1,0.25,0.10,0.5, 
        ]
    
    root = tk.Tk()
    app = ProcessPaymentMain(root, values)
    root.mainloop()

if __name__ == "__main__":
    main()