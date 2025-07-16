import random
import shutil
import time
import os

def matrix_effect():
    columns = shutil.get_terminal_size().columns
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*"
    try:
        while True:
            print("".join(random.choice(chars) for _ in range(columns)))
            time.sleep(0.05)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Matrix effect ended.")

if __name__ == "__main__":
    os.system('color 0A')  # green text on black background
    matrix_effect()
