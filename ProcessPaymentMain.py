from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Utils import Utils
from Utils import SquareFrame
from ChangeDenomination import ChangeDenomination
class ProcessPaymentMain(Utils):
        def __init__(self, root, values, main_window):
                super().__init__(root, "Process Payment") 
                super().setup_background()
                super().setup_fonts()
                self.square_frame_process_payment = SquareFrame(self.root, 
                                                                heading="PAYMENT", 
                                                                x=0.45, y=0.15,
                                                               )
                
                self.square_frame_process_payment.set_values_editable(values)
                self.square_frame_process_payment.create_cash_components(callback=self.proceed_clicked, button="PROCEED")
                
                self.setup_payment_container()
                self.setup_calculator_contents()
                self.setup_buttons()
                self.setup_instructions()
                self.total_bill = 0
                self.total_payment = 0
                self.payment_denomination = {}
                self.setup_process_payment_label()
                self.main_window = main_window
        
        def proceed_clicked(self):
                self.total_bill = float(self.get_bill_total())
                self.total_payment = float(self.get_payment_total())
                change = self.total_payment-self.total_bill 
                self.payment_denomination = self.get_payment_denomination()
                      
                # next window if conditions are met
                
                if (self.give_change(change) and change > 0):
                        self.root.withdraw()
                        change_denomination_window = tk.Toplevel(self.root)
                        ChangeDenomination(change_denomination_window, 
                                           self.change_denomination, 
                                           self.total_bill, 
                                           self.total_payment, 
                                           self.main_window)
                        change_denomination_window.protocol("WM_DELETE_WINDOW",  lambda: self.on_close_window(change_denomination_window))  

        def give_change(self, change):
                self.bills_and_coins = {
                "1000": 10,
                "500": 10,
                "200": 10,
                "100": 10,
                "50": 10,
                "20": 10,
                "10": 10,
                "5": 10,
                "1": 10,
                "0.25": 10, 
                "0.10": 10, 
                "0.05": 10, 
                }
                change_in_cents = int(change * 100)
                denominations = [
                (100000, "1000"), (50000, "500"), (20000, "200"),
                (10000, "100"), (5000, "50"), (2000, "20"),
                (1000, "10"), (500, "5"), (100, "1"),
                (25, "0.25"), (10, "0.10"), (5, "0.05")  
                ]
                self.change_denomination = {denomination: 0 for type, denomination in denominations}
                
                print("\nGiving change:")
                insufficient_change = False

                for value_in_cents, denomination in denominations:
                        if change_in_cents <= 0:
                                break

                        quantity_needed = change_in_cents // value_in_cents
                        available_quantity = self.bills_and_coins[denomination]

                        if quantity_needed > 0:
                                quantity_to_give = min(quantity_needed, available_quantity)
                                if quantity_to_give > 0:
                                        self.bills_and_coins[denomination] -= quantity_to_give
                                        change_in_cents -= quantity_to_give * value_in_cents
                                        print(f"{denomination} peso(s): {quantity_to_give}")
                                        self.change_denomination[denomination] = quantity_to_give
                if change_in_cents > 0:
                        shortfall = change_in_cents / 100
                        print(f"Warning: Unable to provide full change. Shortfall: {shortfall:.2f} pesos.")
                        return False

                print("Change given successfully.")
                return denomination

                
        def on_close_window(self, child_window):
                child_window.destroy()
                self.root.deiconify() 
                
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




