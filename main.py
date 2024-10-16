# Importing all classes and functions from the tkinter module, which is used for creating GUI applications
from tkinter import *
# Importing the requests module for making HTTP requests
import requests

# Function to fetch a quote from the Kanye Rest API and update the text on the canvas
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

# Creating the main window for the application
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Creating a canvas widget where the background image and quote will be displayed
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Creating a button with an image of Kanye, when clicked it triggers the get_quote function
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


# Start the Tkinter event loop, making the window appear and respond to user inputs
window.mainloop()