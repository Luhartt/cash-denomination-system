from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Utils import Utils
from Utils import SquareFrame
from Session import Session
class ProcessPaymentMain(Utils):
        def __init__(self, root, values):
                super().__init__(root, "Process Payment") 
                super().setup_background()
                super().setup_fonts()
                self.session = Session()
    
                self.square_frame_process_payment = SquareFrame(self.root, 
                                                                heading="PAYMENT", 
                                                                x=0.45, y=0.15,
                                                               )
                
                self.square_frame_process_payment.set_values_editable(values)
                self.square_frame_process_payment.create_cash_components(callback=self.proceed_clicked)
                
                self.setup_payment_container()
                self.setup_calculator_contents()
                self.setup_buttons()
                self.setup_instructions()
                self.total_bill = 0
                self.total_payment = 0
                self.payment_denomination = {}
        
        def proceed_clicked(self):
                self.total_bill = float(self.get_bill_total())
                self.total_payment = float(self.get_payment_total())
                change = self.total_payment-self.total_bill 
                self.payment_denomination = self.get_payment_denomination()
                
                # passes to session
                self.session.set_total_bill(self.total_bill)
                self.session.set_total_payment(self.total_payment)
                self.session.set_payment_denomination(self.payment_denomination)
                self.session.set_total_change(change)
                
                print("Proceed Clicked")
    
        
        def setup_payment_container(self):
                self.calculator_frame = tk.Frame(self.root,                                        
                                            bg="#3f2622",
                                            width=300,
                                            height=350
                                        )
                self.calculator_frame.place(rely = 0.15, relx=0.10, anchor="nw")
                calculator_heading = tk.Label(self.root, 
                                              text="TOTAL BILL",
                                              fg="#3f2622", 
                                              bg="white",
                                              padx=50,
                                              pady=5,
                                              font=self.font_big_bold
                                              )
                calculator_heading.place(rely = 0.095, relx = 0.147, anchor="nw")
        def setup_calculator_contents(self):
                if not hasattr(self, 'validation_command'):
                        self.validation_command = (self.root.register(self.validate_numeric), '%P')
                # input frame
                input_frame = tk.Frame(self.calculator_frame,
                                       bg="white",
                                       width=250,
                                       height=50)
                input_frame.place(relx=0.5, rely=0.15, anchor="center")
                # input frame label (Peso sign)
                input_frame_label = tk.Label(input_frame, text="₱", padx=5, font=self.font_big_bold, bg="white", fg="#3f2622",)
                input_frame_label.place(rely = 0.5, x=0, anchor="w")
                # input
                self.numvar = tk.StringVar()
                self.input_frame_entry=tk.Entry(input_frame, 
                                           font=self.font_big_bold, 
                                           textvariable=self.numvar,
                                           bg="white",
                                           fg="#3f2622", 
                                           width=15,
                                           validate="all",
                                           validatecommand=self.validation_command,
                                           relief="flat")
                self.input_frame_entry.place(rely = 0.5, relx=0.95, anchor="e")
                # frame for buttons
                self.button_frame = tk.Frame(self.calculator_frame, bg="#3f2622", width= 250, height = 220)
                self.button_frame.place(rely = 0.96, relx = 0.5, anchor="s")
                
        def validate_numeric(self, value):
                """Validate that the input is numeric, allows one dot (.) for decimals, or is empty."""
                if value == "":  
                        return True
                if value.count(".") > 1: 
                        return False
                if value.replace(".", "").isdigit():  
                        return True
                return False
        
        """Function for creating buttons"""
        def create_button(self, content, col, rw, callback):
                button = tk.Button(self.button_frame, text=content, 
                                   font=self.font_medium_bold, 
                                   bg="white", 
                                   fg="#3f2622", 
                                   command=callback, 
                                   width=7, 
                                   pady=0,
                                   borderwidth=1,
                                   relief="solid")
                button.grid(column=col, row=rw, padx=4, pady=4)
        # Setup Buttons
        def setup_buttons(self):
                button = [
                "1", "2", "3",
                "4", "5", "6",
                "7", "8", "9",
                "0", ".", "Clear",
                "PAY"
                ]

                for index, var in enumerate(button):
                        row = index // 3  
                        column = index % 3  
                        if var == "PAY":
                                column = 2  
                                row += 1  
                        if var == "Clear":
                                callback = lambda self = self: self.button_callback("clear", None)
                        elif var == "PAY":
                                callback = lambda self = self: self.button_callback("pay", None)
                        else:
                                callback = lambda self = self, lbl=var: self.button_callback("num", lbl)
                        self.create_button(var, column, row, callback)
                        
        def button_callback(self, type, num):
                if type == "num":
                        self.input_frame_entry.insert('end', num)   
                elif type == "clear":
                        self.input_frame_entry.delete(0, 'end')      
                elif type == "pay":
                        pass
        def setup_instructions(self):
                instructions_frame = tk.Frame(self.root, 
                                              bg="white",
                                              width=300,
                                              height=70,
                                              padx=20
                                                )
                                              
                instructions_label1 = tk.Label(instructions_frame,
                                               text = "Enter the total amount to \npay and click", 
                                               font=self.font_medium_big,  
                                               fg="#3f2622", 
                                               bg="white",
                                               anchor='w',
                                               justify='left'
                                                )
                instructions_label2 = tk.Label(instructions_frame, 
                                               text = "PAY.", 
                                               font=self.font_medium_big_bold,    
                                               bg="white",
                                               fg="#3f2622", 
                                                )
                instructions_label1.place(x=0, y=0)
                instructions_label2.place(x=140, y=48, anchor="center")
                instructions_frame.place(rely = 0.8, relx=0.1, anchor="nw")
                
        def get_bill_total(self):
                return self.input_frame_entry.get()  
        def get_payment_total(self):
                return SquareFrame.get_cash_total(self.square_frame_process_payment)
        def get_payment_denomination(self):
                return SquareFrame.get_cash_denomination(self.square_frame_process_payment)




