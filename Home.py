from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Utils import Utils

class MainMenuApp(Utils):
    def __init__(self, root, values):
        self.root = root
        super().__init__(root, "Main Menu") 


        
        # Initialize font
        self.font = ("Poppins", 12, "bold")
        
        self.photos = []        
        # Setup UI components
        self.load_button_images()
        self.create_buttons()
        
    def resize_image(self, path, width, height):
        """Resize an image from path to specified dimensions"""
        try:
            img = Image.open(path)
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image {path}: {e}")
            return None
                    
    def load_button_images(self):
        """Load and store button images"""
        image_paths = [
            "pictures/CheckInventory.png",
            "pictures/ProcessPayment.png",
            "pictures/Exit.png"
        ]
        
        for path in image_paths:
            photo = self.resize_image(path, 100, 100)
            if photo:
                self.photos.append(photo)
            else:
                print(f"Failed to load image: {path}")
                
    def on_enter(self, button):
        """Mouse enter event handler"""
        button.config(bg="#614d4a", fg="#bcaba4")
        
    def on_leave(self, button):
        """Mouse leave event handler"""
        button.config(bg="white")
        
    def create_button(self, text, image, relx, command=None):
        """Create a button with specified parameters"""
        button = tk.Button(
            self.root,
            text=text,
            image=image,
            compound="top",
            padx=40,
            pady=15,
            fg="#4d342f",
            bg="white",
            borderwidth=0,
            relief="flat",
            font=self.font,
            command=command
        )
        
        # Bind hover events
        button.bind("<Enter>", lambda e: self.on_enter(button))
        button.bind("<Leave>", lambda e: self.on_leave(button))
        
        # Place the button
        button.place(relx=relx, rely=0.5, anchor="center")
        
        return button
        
    def create_buttons(self):
        """Create all main menu buttons"""
        if len(self.photos) >= 3:
            # Process Payment Button
            self.process_payment = self.create_button(
                "Process\nPayment",
                self.photos[1],
                0.3,
                self.on_process_payment
            )
            
            # Check Inventory Button
            self.check_inventory = self.create_button(
                "Check\nInventory",
                self.photos[0],
                0.5,
                self.on_check_inventory
            )
            
            # Exit Button
            self.exit_button = self.create_button(
                "Exit\n",
                self.photos[2],
                0.7,
                self.root.quit
            )
            
    def on_process_payment(self):
        """Handle process payment button click"""
        print("Process Payment clicked")
        # Add your process payment logic here
        
    def on_check_inventory(self):
        """Handle check inventory button click"""
        print("Check Inventory clicked")
        # Add your inventory check logic here

def main():
    root = tk.Tk()
    app = MainMenuApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()