# Keylogger with Tkinter GUI

This project is a basic keylogger that logs keystrokes to a file. It also includes a simple `Tkinter` GUI where users can input text, which is logged in the same file. The keylogger runs globally once activated, capturing all key presses outside the input field.

> **Disclaimer:** This project is for educational purposes only. Always ensure you have permission before using keyloggers in any environment.


## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [How It Works](#how-it-works)
- [File Structure](#file-structure)
- [Customization](#customization)
- [Ethical Considerations](#ethical-considerations)


## Features

- **Text Input Logging**: Allows users to input text in a field and log it to a file by clicking a button.
- **Global Keylogger**: Captures and logs all keystrokes outside the input field.
- **Interactive GUI**: Built using `Tkinter` for ease of use.
- **Styled Buttons**: Includes hover effects, custom colors, and a focus effect on the input field.

## Prerequisites

- Python 3.x
- `pynput` library (to capture global keystrokes)
- `Tkinter` (comes pre-installed with Python)

## Installation

1. Clone this repository or download the project files to your local machine.
2. Install the `pynput` library if you don't have it already:
```bash
   pip install pynput
 ```
3. Save the project files to your preferred directory.


## Running the Project

1. Open a terminal and navigate to your project directory.
2. Run the Python script:
```bash
python keyLogger.py
```
3. A Tkinter window will appear, allowing you to:
- Log text entered in the input field by clicking the Log Text button.
- Start a global keylogger that captures all keystrokes by clicking the Start Keylogger button.

## How It Works

- Log Text Button: Type text into the input field, and click the "Log Text" button. The text will be logged to the file captured_text.txt. After logging, the input field is cleared.

- Start Keylogger Button: Clicking this button starts a background keylogger that captures all key presses globally (outside the input field) and logs them to the same file (captured_text.txt).

## File Structure

```bash
|-- keyLogger.py        # Main Python script for the keylogger
|-- captured_text.txt          # File where keystrokes are logged
```

## Customization

- You can change the file path to log keystrokes by modifying the log_file variable in the keyLogger.py script.
- You can customize the appearance of the buttons and input field (e.g., colors, fonts) by modifying the Tkinter widget attributes.

## Ethical Considerations

- *Important:* Keylogging software should only be used for ethical and legal purposes, such as testing in a personal environment with proper permissions. Unauthorized keylogging may result in legal consequences.
