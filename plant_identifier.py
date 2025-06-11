from graphics import Canvas
    
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
BUTTON_WIDTH = 110
BUTTON_HEIGHT = 20
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)


def main():
    draw_button()
    canvas.clear()
    load_image()
    canvas.clear()
    return_results()

#User submits a photo by clicking a button and uploading a photo
#Draw button with text
def draw_button():
    Start_X = (CANVAS_WIDTH/2)-(BUTTON_WIDTH/2)
    Start_Y = (CANVAS_HEIGHT/2) - (BUTTON_HEIGHT/2)
    COLOR = "white"
    OUTLINE = "black"
    canvas.create_rectangle(Start_X, Start_Y, Start_X + BUTTON_WIDTH, Start_Y + BUTTON_HEIGHT, COLOR, OUTLINE )
    canvas.create_text(CANVAS_WIDTH/2, (CANVAS_HEIGHT/2), "UPLOAD A PLANT", anchor = "center")
#Waits for user to click on the button    
    canvas.wait_for_click()
    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        if Start_X <= x <= (Start_X + BUTTON_WIDTH) and Start_Y <= y <= (Start_Y + BUTTON_HEIGHT):
            break
        else:
            canvas.clear()
            draw_button()

def load_image():
    canvas.create_image_with_size(
    (CANVAS_WIDTH/2 - 200),
    (0),
    400,
    400,
    'vaccinium-boreale-le-ahaines-a.jpg'
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

def return_results():
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