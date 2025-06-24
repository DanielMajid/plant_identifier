import tkinter as tk
from tkinter import filedialog
import pprint
from pprint import pprint
import requests
import json

    
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
BUTTON_WIDTH = 110
BUTTON_HEIGHT = 20
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)


def main():
    draw_button()

    def draw_button():
        while True:
            x = canvas.get_mouse_x()
            y = canvas.get_mouse_y()
            if Start_X <= x <= (Start_X + BUTTON_WIDTH) and Start_Y <= y <= (Start_Y + BUTTON_HEIGHT):
                root = tk.Tk()
                root.withdraw()  # Hide the root window

                file_path = filedialog.askopenfilename()
                # need to pass this result to the submit_api function >>print(file_path)
            else:
                canvas.clear()
                draw_button()


if __name__ == '__main__':
    main()