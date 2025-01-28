import pyautogui
from screeninfo import get_monitors
import tkinter as tk
from tkinter import messagebox

def take_screenshot():
    try:
        # Get selected monitor index from dropdown
        selected_monitor = monitor_dropdown.get()
        if not selected_monitor:
            messagebox.showerror("Error", "Please select a monitor.")
            return

        # Convert to zero-based index
        monitor_index = int(selected_monitor.split()[1]) - 1

        # Get the dimensions of the selected monitor
        monitor = monitors[monitor_index]
        x, y, width, height = monitor.x, monitor.y, monitor.width, monitor.height

        # Take the screenshot
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save(f"screenshot_monitor_{monitor_index + 1}.png")

        # Show success message
        messagebox.showinfo("Success", f"Screenshot saved for Monitor {monitor_index + 1}!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Get all active monitors
monitors = get_monitors()

# Create main window
root = tk.Tk()
root.title("Monitor Screenshot")
root.geometry("250x190")
root.resizable(False, False)
# Add label
label = tk.Label(root, text="Select a monitor to capture:", font=("Arial", 12))
label.pack(pady=10)

# Create dropdown for monitor selection
monitor_options = [f"Monitor {i + 1}" for i in range(len(monitors))]
monitor_dropdown = tk.StringVar()
dropdown = tk.OptionMenu(root, monitor_dropdown, *monitor_options)
dropdown.pack(pady=5)
def exit_program():
# Exit the application
    root.destroy()
# Add button to take screenshot
screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot, font=("Arial", 12))
screenshot_button.pack(pady=20)

# Add Exit button
exit_button = tk.Button(root, text="Exit", command=exit_program, font=("Arial", 14), width=20, bg="red", fg="white")
exit_button.pack(pady=10)

# Run the GUI loop
root.mainloop()