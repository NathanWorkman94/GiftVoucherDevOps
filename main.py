import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from gv_designer import process_voucher
import os

# Get the input details and call the voucher creation function
def create_voucher():
    order_number = entry_order.get().strip()
    reference_number = entry_reference.get().strip()
    pin = entry_pin.get().strip()
    value = entry_value.get().strip()
    website = store_var.get().strip()
    message = entry_message_var.get().strip()
    save_directory = save_dir_var.get().strip()

    if not order_number:
        messagebox.showerror("Error", "Order Number is required.")
        return

    if not reference_number:
        messagebox.showerror("Error", "Reference Number is required.")
        return

    if not pin:
        messagebox.showerror("Error", "Pin is required.")
        return

    if not value:
        messagebox.showerror("Error", "Value is required.")
        return

    if not website:
        messagebox.showerror("Error", "Store is required.")
        return

    if not save_directory:
        save_directory = os.path.join(os.path.expanduser('~'), 'Downloads') # Default to Downloads folder

    if len(message) > 40:
        messagebox.showerror("Error", "Message is too long. Please limit it to 40 characters.")
        return

    try:
        value = float(value)
    except ValueError:
        messagebox.showerror("Error", "Value must be a number.")
        return

    # Create the voucher
    process_voucher(order_number, reference_number, pin, value, website, message, save_directory)
    
    # Inform the user that the voucher has been created and will appear in the selected folder
    messagebox.showinfo("Success", f"Voucher created successfully!\n\nThe voucher will appear in your selected folder ({save_directory}).")
    
    # Clear all the input fields for the next entry
    entry_order.delete(0, tk.END)
    entry_reference.delete(0, tk.END)
    entry_pin.delete(0, tk.END)
    entry_value.delete(0, tk.END)
    entry_store.set('Mannys')
    entry_message_var.set("")
    save_dir_var.set("")

    # Set focus back to the first text box
    entry_order.focus_set()

# Function to browse and select a directory
def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        save_dir_var.set(directory)

# Function to exit the application
def exit_application():
    root.destroy()

# Function to limit the message length and update character count
def limit_message_length(*args):
    current_length = len(entry_message_var.get())
    if current_length > 40:
        entry_message_var.set(entry_message_var.get()[:40])
    char_count_label.config(text=f"{min(current_length, 40)}/40")

# Set up the main window
root = tk.Tk()
root.title("Gift Voucher Creator")
root.configure(bg='#f0f0f0')

# Create and apply styles
style = ttk.Style()
style.theme_use('clam')

# Frame style
style.configure('Custom.TFrame', background='#f0f0f0')

# Label style
style.configure('Custom.TLabel', background='#f0f0f0')

# Button style
style.configure('Custom.TButton', background='#d6e0f5', foreground='black', font=('Helvetica', 10, 'bold'))

# Create a frame for the input fields
frame = ttk.Frame(root, padding="10", style='Custom.TFrame')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
frame.configure(relief="solid", borderwidth=1)

# Create input fields with labels aligned to the left
labels = ["Order Number:", "Reference Number:", "Pin:", "Value:", "Store:", "Message:", "Save Directory:"]
entries = []

for i, label_text in enumerate(labels):
    label = ttk.Label(frame, text=label_text, anchor="w", style='Custom.TLabel')
    label.grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)

    if label_text == "Store:":
        store_var = tk.StringVar(value='Mannys')
        entry = ttk.Combobox(frame, textvariable=store_var)
        entry['values'] = ('Store DJ', 'Mannys')
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        entries.append(entry)
    elif label_text == "Save Directory:":
        save_dir_var = tk.StringVar()
        entry = ttk.Entry(frame, textvariable=save_dir_var)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        browse_button = ttk.Button(frame, text="Browse", command=browse_directory)
        browse_button.grid(row=i, column=2, padx=5, pady=5)
        entries.append(entry)
    elif label_text == "Message:":
        entry_message_var = tk.StringVar()
        entry_message_var.trace('w', limit_message_length)
        entry = ttk.Entry(frame, textvariable=entry_message_var)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        entries.append(entry)
    else:
        entry = ttk.Entry(frame)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        entries.append(entry)

entry_order, entry_reference, entry_pin, entry_value, entry_store, entry_message, entry_save_dir = entries

# Message label to inform about character limit and show character count
char_limit_message = tk.Label(frame, text="(Max 40 characters)", bg='#f0f0f0', fg='grey')
char_limit_message.grid(row=5, column=2, sticky=tk.W, padx=5, pady=5)

char_count_label = tk.Label(frame, text="0/40", bg='#f0f0f0', fg='grey')
char_count_label.grid(row=5, column=3, sticky=tk.W, padx=5, pady=5)

# Default save location message
default_message = tk.Label(root, text="If no location is selected, the file will be saved to your Downloads folder.", bg='#f0f0f0', fg='black')
default_message.grid(row=1, column=0, pady=(0, 10))

# Create buttons
button_frame = ttk.Frame(root, style='Custom.TFrame')
button_frame.grid(row=2, column=0, pady=10, padx=10)

# Note: Swapped positions of the buttons
exit_button = ttk.Button(button_frame, text="Exit", command=exit_application, style='Custom.TButton')
exit_button.grid(row=0, column=0, padx=5, pady=5)

create_button = ttk.Button(button_frame, text="Create Voucher", command=create_voucher, style='Custom.TButton')
create_button.grid(row=0, column=1, padx=5, pady=5)

# Configure grid to make entries expand to fill available space
for i in range(len(labels)):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Set the focus to the first text box when the GUI pops up
entry_order.focus_set()

root.mainloop()
