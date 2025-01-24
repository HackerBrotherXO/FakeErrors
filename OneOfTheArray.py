import ctypes
import random

error_messages = [
    "Error: Unable to connect to the server.",
    "Error: File not found.",
    "Error: Access denied.",
    "Error: Invalid data format.",
    "Error: The operation cannot be performed.",
    "Error: The system is overloaded.",
    "Error: Timeout exceeded.",
    "Error: The dependency cannot be found.",
    "Error: Network problems.",
    "Error: Operation cancelled."
]

def show_error():
    error_message = random.choice(error_messages)
    ctypes.windll.user32.MessageBoxW(0, error_message, "Error", 0x10)

if __name__ == "__main__":
    show_error()
