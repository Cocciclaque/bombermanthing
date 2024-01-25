import tkinter as tk




def on_button_click():
    user_Name = entryName.get()
    print("You entered:", user_Name)

# Create the main window
root = tk.Tk()
root.title("Menu")
root.geometry("400x200")
# Create and pack widgets
name = tk.Label(root, text="Enter Name of Player:")
name.pack(pady=10)

entryName = tk.Entry(root, width=30)
entryName.pack(pady=10)

ip = tk.Label(root, text="Enter IP adress:")
ip.pack(pady=10)

entryIp = tk.Entry(root, width=30)
entryIp.pack(pady=10)

button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

# Run the main loop
root.mainloop()