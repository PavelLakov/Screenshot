# Monitor Screenshot Tool

This is a simple Python application with a graphical user interface (GUI) built using `tkinter`. The program allows users to select a monitor from a dropdown list and take a screenshot of the selected monitor. An "Exit" button is also provided to close the application.

## Features
- Lists all active monitors connected to the system.
- Allows users to select a monitor to capture using a dropdown menu.
- Saves a screenshot of the selected monitor.
- Fixed window size to prevent resizing.
- Includes an "Exit" button to close the application.

## Requirements
- Python 3.x
- Libraries:
  - `pyautogui`
  - `screeninfo`
  - `tkinter` (built into Python)

## Installation
1. Clone this repository or download the source code.
2. Install the required Python libraries if not already installed:
   ```bash
   pip install pyautogui screeninfo
   ```

## How to Use
1. Run the script:
   ```bash
   GUI-format.py
   ```
2. A GUI window will open.
3. Select the monitor you want to capture from the dropdown menu.
4. Click the **Take Screenshot** button to capture the selected monitor. The screenshot will be saved as `screenshot_monitor_<number>.png` in the same directory as the script.
5. To exit the application, click the **Exit** button.

## Example Output
If you select "Monitor 1" and click "Take Screenshot," the application will save a screenshot named `screenshot_monitor_1.png` in the current directory.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
