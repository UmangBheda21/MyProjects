import tkinter as tk

def convert_miles_to_km():
    # Get the input value from the entry widget
    miles = entry.get()
    try:
        # Convert the input value to float
        miles = float(miles)
        # Perform the conversion (1 mile = 1.60934 kilometers)
        km = miles * 1.60934
        # Update the result label with the converted value
        result_label.config(text=f"{km:.2f} Kilometers")
    except ValueError:
        # Handle invalid input
        result_label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Mile to Kilometers Converter")

# Create an entry widget for input
entry = tk.Entry(root, width=10)
entry.pack(pady=10)

# Create a button that calls the conversion function
convert_button = tk.Button(root, text="Convert", command=convert_miles_to_km)
convert_button.pack(pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="0 Kilometers")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
