import tkinter as tk
from tkinter import messagebox, filedialog

# Function to reverse characters
def reverse_characters(text):
    return text[::-1]

# Function to reverse word order
def reverse_words(text):
    return ' '.join(text.split()[::-1])

# Function to save text to file
def save_to_file(text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text)
        messagebox.showinfo("Success", "Text saved successfully!")

# Function to process user input
def process_text():
    user_input = entry.get().strip()
    if not user_input:
        messagebox.showerror("Error", "Please enter text!")
        return
    
    choice = option.get()
    if choice == "Character Reversal":
        result = reverse_characters(user_input)
    elif choice == "Word Reversal":
        result = reverse_words(user_input)
    
    output_label.config(text=f"Result: {result}", fg="white", bg="#4CAF50")
    save_button.config(state=tk.NORMAL, command=lambda: save_to_file(result))

# GUI Setup
root = tk.Tk()
root.title("Text Reverser")
root.geometry("400x300")
root.configure(bg="#2C3E50")

# Header Label
header = tk.Label(root, text="Text Reverser", font=("Arial", 16, "bold"), fg="white", bg="#2980B9", pady=10)
header.pack(fill=tk.X)

# Input Field
tk.Label(root, text="Enter Text:", font=("Arial", 12), fg="white", bg="#2C3E50").pack(pady=5)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

# Radio Buttons for Reversal Option
option = tk.StringVar(value="Character Reversal")

frame = tk.Frame(root, bg="#2C3E50")
frame.pack(pady=5)

radio_style = {
    "font": ("Arial", 10),
    "bg": "#34495E",
    "fg": "white",
    "selectcolor": "#E74C3C"  # This highlights selected radio buttons in red
}

char_reverse = tk.Radiobutton(frame, text="Reverse Characters", variable=option, value="Character Reversal", **radio_style)
word_reverse = tk.Radiobutton(frame, text="Reverse Words", variable=option, value="Word Reversal", **radio_style)

char_reverse.pack(side=tk.LEFT, padx=10)
word_reverse.pack(side=tk.LEFT, padx=10)

# Reverse Button
reverse_button = tk.Button(root, text="Reverse", command=process_text, font=("Arial", 12), bg="#E74C3C", fg="white", padx=10, pady=5)
reverse_button.pack(pady=5)

# Output Label
output_label = tk.Label(root, text="Result:", font=("Arial", 12), fg="black", bg="white", width=50, pady=5)
output_label.pack(pady=5)

# Save Button (Initially Disabled)
save_button = tk.Button(root, text="Save to File", state=tk.DISABLED, font=("Arial", 12), bg="#F1C40F", fg="black", padx=10, pady=5)
save_button.pack(pady=5)

# Run Tkinter Mainloop
root.mainloop()
