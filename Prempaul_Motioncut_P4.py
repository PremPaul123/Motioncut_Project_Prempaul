import random
import tkinter as tk
from tkinter import messagebox, scrolledtext, Canvas
from PIL import Image, ImageTk

# Load images for graphical representation
coin_images = {"Heads": None, "Tails": None}

def load_images():
    global coin_images
    coin_images["Heads"] = ImageTk.PhotoImage(Image.open(r"C:\Motioncut_Internship\Heads.jpg").resize((100, 100)))
    coin_images["Tails"] = ImageTk.PhotoImage(Image.open(r"C:\Motioncut_Internship\Tails.jpg").resize((100, 100)))

# Function to simulate a single coin toss
def flip_coin():
    return random.choice(["Heads", "Tails"])

# Function to handle multiple coin tosses based on user input
def simulate_tosses():
    try:
        num_flips = int(entry.get())  # Get the number of flips from user input
        if num_flips <= 0:
            messagebox.showerror("Input Error", "Please enter a positive number.")
            return
        
        results = {"Heads": 0, "Tails": 0}  # Dictionary to track results
        history_text.config(state=tk.NORMAL)
        history_text.delete(1.0, tk.END)  # Reset history display
        
        for i in range(1, num_flips + 1):
            result = flip_coin()  # Perform a coin flip
            results[result] += 1  # Update the count of heads or tails
            history_text.insert(tk.END, f"{i}. {result}\n")  # Store result with numbering
            update_coin_display(result)
        
        total = num_flips  # Total flips performed
        heads_percentage = (results["Heads"] / total) * 100  # Calculate percentage of heads
        tails_percentage = (results["Tails"] / total) * 100  # Calculate percentage of tails
        
        # Display final results in percentage
        result_text.set(f"Heads: {results['Heads']} ({heads_percentage:.2f}%)\n"
                        f"Tails: {results['Tails']} ({tails_percentage:.2f}%)")
        history_text.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Please enter a valid number.")

# Function to reset user input and displayed results
def reset():
    entry.delete(0, tk.END)  # Clear entry field
    result_text.set("")  # Reset result display
    history_text.config(state=tk.NORMAL)
    history_text.delete(1.0, tk.END)  # Clear history
    history_text.config(state=tk.DISABLED)
    coin_canvas.delete("all")  # Clear coin image

# Function to exit the application
def exit_app():
    root.quit()  # Properly exits the application

# Function to update the graphical representation of the coin toss
def update_coin_display(result):
    coin_canvas.delete("all")
    coin_canvas.create_image(50, 50, image=coin_images[result])

# GUI Setup
root = tk.Tk()
root.title("Virtual Coin Toss")  # Window title
root.geometry("500x600")  # Increased window size
root.configure(bg="#dfe6e9")  # Background color

load_images()  # Load coin images

# Create a frame to hold UI elements
frame = tk.Frame(root, bg="#2d3436", padx=10, pady=10)
frame.pack(pady=20)

# Label for user input
tk.Label(frame, text="Enter number of flips:", font=("Arial", 12, "bold"), bg="#2d3436", fg="white").pack(pady=5)
entry = tk.Entry(frame, font=("Arial", 12), width=10)  # Input field for number of flips
entry.pack(pady=5)

# Button to start coin toss simulation
tk.Button(frame, text="Toss Coins", command=simulate_tosses, font=("Arial", 12, "bold"), bg="#00cec9", fg="white").pack(pady=5)

# Label for results
tk.Label(frame, text="Results:", font=("Arial", 12, "bold"), bg="#2d3436", fg="white").pack(pady=5)
result_text = tk.StringVar()
tk.Label(frame, textvariable=result_text, font=("Arial", 12, "bold"), bg="#2d3436", fg="#fdcb6e").pack(pady=5)

# Canvas for graphical coin display
coin_canvas = Canvas(frame, width=100, height=100, bg="#2d3436", highlightthickness=0)
coin_canvas.pack(pady=10)

# ScrolledText widget to display toss history
history_text = scrolledtext.ScrolledText(frame, font=("Arial", 10), bg="#2d3436", fg="#fab1a0", height=10, width=30, wrap=tk.WORD)
history_text.pack(pady=5)
history_text.config(state=tk.DISABLED)

# Reset button
tk.Button(frame, text="Reset", command=reset, font=("Arial", 12, "bold"), bg="#e17055", fg="white").pack(pady=5)
# Exit button
tk.Button(frame, text="Exit", command=exit_app, font=("Arial", 12, "bold"), bg="#d63031", fg="white").pack(pady=5)

root.mainloop()