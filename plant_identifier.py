import tkinter as tk
from tkinter import filedialog
import pprint
from pprint import pprint
import requests
import json

#this quoted out portion needs reformatted to reflect Tkinter protocol
"""    
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
BUTTON_WIDTH = 110
BUTTON_HEIGHT = 20
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)


def main():
    draw_button()
    canvas.clear()
    load_image()
    submit_api()
    canvas.clear()
    return_results()
"""
#User submits a photo by clicking a button and uploading a photo
#Draw button with text
#Stil needs file handling operation implemented
def draw_button():
    #this portion needs to be reformatted to align with Tkinter protocol
    """
    Start_X = (CANVAS_WIDTH/2)-(BUTTON_WIDTH/2)
    Start_Y = (CANVAS_HEIGHT/2) - (BUTTON_HEIGHT/2)
    COLOR = "white"
    OUTLINE = "black"
    canvas.create_rectangle(Start_X, Start_Y, Start_X + BUTTON_WIDTH, Start_Y + BUTTON_HEIGHT, COLOR, OUTLINE )
    canvas.create_text(CANVAS_WIDTH/2, (CANVAS_HEIGHT/2), "UPLOAD A PLANT", anchor = "center")
#Waits for user to click on the button    
    canvas.wait_for_click()
    """
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

def load_image(file_path):
    #Max POST (total size of photos sent) size: 52428800 bytes
    image = file_path
    canvas.create_image_with_size(
    (CANVAS_WIDTH/2 - 200),
    (0),
    400,
    400,
    image
)   
    Start_X = (CANVAS_WIDTH/2)-(BUTTON_WIDTH/2)
    Start_Y = CANVAS_HEIGHT*.8
    COLOR = "white"
    OUTLINE = "black"
    canvas.create_rectangle(Start_X, Start_Y, Start_X + BUTTON_WIDTH, Start_Y + BUTTON_HEIGHT, COLOR, OUTLINE )
    canvas.create_text(Start_X+5, (Start_Y+BUTTON_HEIGHT*.25), "CLICK TO SUBMIT")
    canvas.wait_for_click()
    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
    
        if Start_X <= x <= (Start_X + BUTTON_WIDTH) and Start_Y <= y <= (Start_Y + BUTTON_HEIGHT):
            break
        else:
            canvas.clear()
            load_image()



def submit_api(file_path):
#submits user photo to the Plantnet API
#NEEDS UI loading screen
    API_KEY = "2b108OvWhxjjceSLhrfgWXn0He"	# Your API_KEY here
    PROJECT = "all"; # try specific floras: "weurope", "canada"…
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

    image_path_1 = "/Users/majid/Downloads/vaccinium-boreale-le-ahaines-a.jpg"
    image_data_1 = open(image_path_1, 'rb')

    #image_path_2 = "../data/image_2.jpeg"
    #image_data_2 = open(image_path_2, 'rb')

    data = { 'organs': ['flower', 'leaf'] }

    files = [
    ('images', (image_path_1, image_data_1)),
    #('images', (image_path_2, image_data_2))
    ]

    req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    prepared = req.prepare()

    s = requests.Session()
    response = s.send(prepared)
    json_result = json.loads(response.text)

    pprint(response.status_code)
    pprint(json_result)

"""    image = "/Users/majid/Downloads/vaccinium-boreale-le-ahaines-a.jpg"
    API_KEY = "2b108OvWhxjjceSLhrfgWXn0He"
    API_BASE_URL = https://my-api.plantnet.org/v2/identify/all
    
    params = {   
        "project": "all",
        "images": [image],
        #Available Organs values : leaf, flower, fruit, bark, auto
        "organs": ["auto"],
        "api-key": API_KEY
    }
    response = requests.get(API_BASE_URL, params)
    return response.json()
"""

def return_results(json_result):
    #Display original image submissions along with the API result with a link to plant dicitonary page
    
    canvas.create_text((CANVAS_WIDTH*.25), (CANVAS_HEIGHT*.103), "Your plant is vaccinium-boreale")
    canvas.create_text((CANVAS_WIDTH*.25), (CANVAS_HEIGHT*.133), "Here is a link to more information")
    canvas.create_text((CANVAS_WIDTH*.25), (CANVAS_HEIGHT*.163), "https://en.wikipedia.org/wiki/Vaccinium_formosum")
    canvas.create_image_with_size((CANVAS_WIDTH/2) - 150, (CANVAS_HEIGHT*.35), 300, 300, 'vaccinium-boreale-le-ahaines-a.jpg'
 )
    Start_X = (CANVAS_WIDTH/2)-(BUTTON_WIDTH/2 + 25)
    Start_Y = (CANVAS_HEIGHT/2) - (BUTTON_HEIGHT/2 + 115 )
    COLOR = "white"
    OUTLINE = "black"
    canvas.create_rectangle(Start_X, Start_Y, Start_X + BUTTON_WIDTH + 50, Start_Y + BUTTON_HEIGHT, COLOR, OUTLINE)
    canvas.create_text(CANVAS_WIDTH/2, (CANVAS_HEIGHT/2) - 114, "UPLOAD ANOTHER PLANT", anchor = "center")
    canvas.wait_for_click()
    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        if Start_X <= x <= (Start_X + BUTTON_WIDTH) and Start_Y <= y <= (Start_Y + BUTTON_HEIGHT):
            canvas.clear()
            main()
        else:
            canvas.clear()
            return_results()

#prints the plant name, and a link to the wikipedia page for that plant
if __name__ == '__main__':
    main()