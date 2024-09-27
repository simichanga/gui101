import customtkinter as ctk

# Set appearance mode (Options: "System" (default), "Dark", "Light")
ctk.set_appearance_mode("Dark")
# Set default color theme (Options: "blue" (default), "green", "dark-blue")
ctk.set_default_color_theme("blue")

# Create the main application window
app = ctk.CTk()

# Set the window title and size
app.title("Modern GUI Example")
app.geometry("400x300")

# Create a frame inside the window
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Create a label inside the frame
label = ctk.CTkLabel(master=frame, text="Welcome to the Modern GUI", font=("Arial", 18))
label.pack(pady=12, padx=10)

# Create an entry box (for user input)
entry = ctk.CTkEntry(master=frame, placeholder_text="Enter something")
entry.pack(pady=12, padx=10)

# Create a button inside the frame
button = ctk.CTkButton(master=frame, text="Submit", command=lambda: print(entry.get()))
button.pack(pady=12, padx=10)

# Run the application
app.mainloop()
