import ctypes
import random
import multiprocessing

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

def show_error(offset_x, offset_y):
    error_message = random.choice(error_messages)
    ctypes.windll.user32.MessageBoxW(0, error_message, "Error", 0x10)
    
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    
    ctypes.windll.user32.SetWindowPos(hwnd, 0, offset_x, offset_y, 0, 0, 0x0001)

def main():
    offset_x = 100 # X
    offset_y = 100 # Y

    max_windows = 5 # String to indicate the number of windows

    processes = []
    for i in range(max_windows):
        p = multiprocessing.Process(target=show_error, args=(offset_x, offset_y))
        p.start()
        processes.append(p)
        
        offset_x += 30
        offset_y += 30

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
